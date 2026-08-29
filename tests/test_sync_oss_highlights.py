"""Tests for the pure (non-network) helpers in scripts/sync_oss_highlights.py.

Written against the standard-library ``unittest`` framework so the suite runs
with ``python -m unittest discover -s tests`` and needs no third-party
dependencies.
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
    def test_format(self) -> None:
        out = so.render_highlights(_sample_highlights())
        lines = out.splitlines()
        self.assertEqual(lines[0], so.START_MARKER)
        self.assertIn(so.END_MARKER, lines)
        self.assertIn("- [openai/openai-python #123]", out)
        self.assertIn("— Fix a bug", out)
        self.assertIn("- [anthropics/anthropic-sdk-python #45]", out)

    def test_one_bullet_per_highlight(self) -> None:
        out = so.render_highlights(_sample_highlights())
        bullet_lines = [ln for ln in out.splitlines() if ln.startswith("- [")]
        self.assertEqual(len(bullet_lines), 2)

    def test_empty(self) -> None:
        out = so.render_highlights([])
        self.assertIn(so.START_MARKER, out)
        self.assertIn(so.END_MARKER, out)


class ReplaceSectionTests(unittest.TestCase):
    def test_replaces_between_markers(self) -> None:
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

    def test_preserves_trailing_content(self) -> None:
        readme = f"{so.START_MARKER}\nx\n{so.END_MARKER}\n\n## Next section\nbody\n"
        out = so.replace_section(readme, so.render_highlights([]))
        self.assertIn("## Next section", out)
        self.assertIn("body", out)

    def test_missing_marker_raises(self) -> None:
        with self.assertRaises(ValueError):
            so.replace_section("no markers here", so.render_highlights([]))


if __name__ == "__main__":
    unittest.main()
