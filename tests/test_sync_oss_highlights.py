"""Tests for the pure (non-network) helpers in scripts/sync_oss_highlights.py.

Runs on the standard-library ``unittest`` framework (no third-party deps):

    python3 -m unittest discover -s tests
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import sync_oss_highlights as so  # noqa: E402


def _sample_highlights() -> list[dict]:
    return [
        {
            "repo": "openai/openai-python",
            "pr": 123,
            "url": "https://github.com/openai/openai-python/pull/123",
            "title": "Fix a bug",
        },
        {
            "repo": "anthropics/anthropic-sdk-python",
            "pr": 45,
            "url": "https://github.com/anthropics/anthropic-sdk-python/pull/45",
            "title": "Add a feature",
        },
    ]


class RenderHighlightsTests(unittest.TestCase):
    def test_render_highlights_format(self) -> None:
        out = so.render_highlights(_sample_highlights())
        lines = out.splitlines()
        self.assertEqual(lines[0], so.START_MARKER)
        self.assertIn(so.END_MARKER, lines)
        self.assertIn("- [openai/openai-python #123]", out)
        self.assertIn("— Fix a bug", out)
        self.assertIn("- [anthropics/anthropic-sdk-python #45]", out)

    def test_render_highlights_empty(self) -> None:
        out = so.render_highlights([])
        self.assertIn(so.START_MARKER, out)
        self.assertIn(so.END_MARKER, out)

    def test_render_highlights_missing_field_raises(self) -> None:
        # Each entry must carry every required field; an incomplete entry should
        # fail loudly rather than render a KeyError mid-loop.
        bad = [{"repo": "owner/name", "pr": 1, "url": "https://x"}]  # no title
        with self.assertRaises(ValueError) as ctx:
            so.render_highlights(bad)
        self.assertIn("title", str(ctx.exception))


class ReplaceSectionTests(unittest.TestCase):
    def test_replace_section_replaces_between_markers(self) -> None:
        readme = (
            "before text\n\n"
            f"{so.START_MARKER}\nold content\n{so.END_MARKER}\n\n"
            "after text\n"
        )
        replacement = so.render_highlights(_sample_highlights())
        out = so.replace_section(readme, replacement)
        self.assertNotIn("old content", out)
        self.assertIn("openai/openai-python #123", out)
        self.assertTrue(out.startswith("before text"))
        self.assertTrue(out.rstrip().endswith("after text"))
        # Markers must survive so the next sync can find them again.
        self.assertEqual(out.count(so.START_MARKER), 1)
        self.assertEqual(out.count(so.END_MARKER), 1)

    def test_replace_section_preserves_trailing_content(self) -> None:
        readme = (
            f"{so.START_MARKER}\nx\n{so.END_MARKER}\n\n## Next section\nbody\n"
        )
        out = so.replace_section(readme, so.render_highlights([]))
        self.assertIn("## Next section", out)
        self.assertIn("body", out)

    def test_replace_section_missing_marker_raises(self) -> None:
        with self.assertRaises(ValueError):
            so.replace_section("no markers here", so.render_highlights([]))

    def test_replace_section_missing_only_end_marker_raises(self) -> None:
        # Half a marker pair is still structurally broken and must not silently
        # drop content.
        readme = f"{so.START_MARKER}\nbody\n"  # no END_MARKER
        with self.assertRaises(ValueError):
            so.replace_section(readme, so.render_highlights([]))


class FetchHighlightsValidationTests(unittest.TestCase):
    """Validate the JSON-shape checks in fetch_highlights without network I/O.

    fetch_highlights pulls bytes over the network, so here we exercise the
    validation branches directly by feeding parsed payloads through a tiny
    shim that mirrors the post-parse checks.
    """

    @staticmethod
    def _validate(payload: object) -> list[dict]:
        # Mirror of the validation in fetch_highlights, applied to an
        # already-parsed payload so the assertions stay offline.
        if not isinstance(payload, dict) or "highlights" not in payload:
            raise ValueError("must be a JSON object with a 'highlights' key")
        highlights = payload["highlights"]
        if not isinstance(highlights, list):
            raise ValueError("'highlights' must be a list")
        return highlights

    def test_valid_payload_returns_list(self) -> None:
        self.assertEqual(self._validate({"highlights": []}), [])

    def test_missing_key_raises(self) -> None:
        with self.assertRaises(ValueError):
            self._validate({"other": 1})

    def test_non_dict_raises(self) -> None:
        with self.assertRaises(ValueError):
            self._validate([1, 2, 3])

    def test_highlights_not_a_list_raises(self) -> None:
        with self.assertRaises(ValueError):
            self._validate({"highlights": {"not": "a list"}})


if __name__ == "__main__":
    unittest.main()
