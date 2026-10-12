"""Tests for the pure (non-network) helpers in scripts/refresh_stats.py.

These cover the README text-transformation and formatting logic that runs
unattended in CI and pushes to main, so a silent regression here would
corrupt the rendered profile. Runs on the standard-library ``unittest``
framework (no third-party deps):

    python3 -m unittest discover -s tests
"""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import refresh_stats as rs  # noqa: E402


class HumanFormatTests(unittest.TestCase):
    def test_human(self) -> None:
        cases = [
            (0, "0"),
            (999, "999"),
            (1_000, "1.0k"),
            (1_500, "1.5k"),
            (23_400, "23.4k"),
            (1_000_000, "1.0M"),
            (2_500_000, "2.5M"),
        ]
        for value, expected in cases:
            with self.subTest(value=value):
                self.assertEqual(rs._human(value), expected)


class ReplaceAfterLabelTests(unittest.TestCase):
    def test_plain(self) -> None:
        text = "<sub>FORKS</sub><br/>\n<strong>12</strong>"
        out, ok = rs.replace_after_label(text, "FORKS", 15)
        self.assertTrue(ok)
        self.assertEqual(out, "<sub>FORKS</sub><br/>\n<strong>15</strong>")

    def test_preserves_plus_suffix(self) -> None:
        text = "<sub>PACKAGES</sub><br/>\n        <strong>200+</strong>"
        out, ok = rs.replace_after_label(text, "PACKAGES", 250)
        self.assertTrue(ok)
        self.assertIn("<strong>250+</strong>", out)

    def test_missing_label(self) -> None:
        out, ok = rs.replace_after_label("nothing here", "FORKS", 5)
        self.assertFalse(ok)
        self.assertEqual(out, "nothing here")

    def test_only_first_occurrence(self) -> None:
        text = (
            "<sub>FORKS</sub><br/>\n<strong>1</strong>"
            " ... "
            "<sub>FORKS</sub><br/>\n<strong>1</strong>"
        )
        out, _ = rs.replace_after_label(text, "FORKS", 9)
        self.assertEqual(out.count("<strong>9</strong>"), 1)
        self.assertEqual(out.count("<strong>1</strong>"), 1)


class ReplaceMarkerTests(unittest.TestCase):
    def test_replaces_all_occurrences(self) -> None:
        text = (
            "a <!-- npm-count -->5<!-- /npm-count --> "
            "b <!-- npm-count -->old<!-- /npm-count -->"
        )
        out, ok = rs.replace_marker(text, "npm-count", 9)
        self.assertTrue(ok)
        self.assertEqual(
            out,
            (
                "a <!-- npm-count -->9<!-- /npm-count --> "
                "b <!-- npm-count -->9<!-- /npm-count -->"
            ),
        )

    def test_accepts_non_int_values(self) -> None:
        text = "<!-- ext-refresh-date -->2020-01-01<!-- /ext-refresh-date -->"
        out, ok = rs.replace_marker(text, "ext-refresh-date", "2026-06-07")
        self.assertTrue(ok)
        self.assertIn("2026-06-07", out)

    def test_missing(self) -> None:
        out, ok = rs.replace_marker("plain text", "npm-count", 3)
        self.assertFalse(ok)
        self.assertEqual(out, "plain text")


class ReplaceStarsBadgeTests(unittest.TestCase):
    def test_replace(self) -> None:
        text = (
            "![GitHub Stars](https://img.shields.io/badge/STARS-100-D4A853"
            "?style=for-the-badge&logo=github&labelColor=1a1a1a)"
        )
        out, ok = rs.replace_stars_badge(text, 250)
        self.assertTrue(ok)
        self.assertIn("STARS-250-D4A853", out)
        self.assertNotIn("STARS-100", out)

    def test_missing(self) -> None:
        out, ok = rs.replace_stars_badge("no badge", 250)
        self.assertFalse(ok)
        self.assertEqual(out, "no badge")


class CountHelperTests(unittest.TestCase):
    def test_count_section_entries_stops_at_divider(self) -> None:
        md = (
            "### Hackathon Submissions\n\n"
            "| [Project A](url) | desc |\n"
            "| [Project B](url) | desc |\n"
            "not a row\n"
            "---\n"
            "| [Project C](url) | other section |\n"
        )
        self.assertEqual(
            rs.count_section_entries(md, r"^### Hackathon Submissions", "| ["), 2
        )

    def test_count_section_entries_missing_header(self) -> None:
        self.assertEqual(rs.count_section_entries("nope", r"^### Missing", "| ["), 0)

    def test_count_distinct_bolded_filters_numeric_and_dedupes(self) -> None:
        md = (
            "### Hackathon Submissions\n"
            "**Event One** and **Event Two** and **53.19** and **Event One**\n"
            "---\n"
        )
        self.assertEqual(
            rs.count_distinct_bolded(md, r"^### Hackathon Submissions"), 2
        )

    def test_count_badge_images(self) -> None:
        md = (
            "### Certifications\n"
            "![AWS](https://x/a.svg)\n"
            "some prose\n"
            "![GCP](https://x/b.svg)\n"
            "---\n"
            "![Other](https://x/c.svg)\n"
        )
        self.assertEqual(rs.count_badge_images(md, r"^### Certifications"), 2)


class WriteShieldEndpointTests(unittest.TestCase):
    def test_write_shield_endpoint(self) -> None:
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "nested" / "badge.json"
            rs.write_shield_endpoint("downloads/mo", 23_400, "D4A853", out)
            payload = json.loads(out.read_text(encoding="utf-8"))
            self.assertEqual(payload["schemaVersion"], 1)
            self.assertEqual(payload["label"], "downloads/mo")
            self.assertEqual(payload["message"], "23.4k")
            self.assertEqual(payload["color"], "D4A853")


class RecentlyShippedTests(unittest.TestCase):
    def test_render_with_data(self) -> None:
        releases = [
            {
                "date": "2026-06-01",
                "name": "pkg",
                "version": "1.2.3",
                "registry": "pypi",
                "url": "https://pypi.org/project/pkg/",
                "display": "`pkg`",
            }
        ]
        prs = [
            {
                "date": "2026-05-30",
                "repo": "openai/openai-python",
                "number": "42",
                "url": "https://github.com/openai/openai-python/pull/42",
                "title": "Fix a bug",
            }
        ]
        out = rs.render_recently_shipped(releases, prs)
        self.assertTrue(out.startswith("<!-- recently-shipped:start -->"))
        self.assertTrue(out.endswith("<!-- recently-shipped:end -->"))
        self.assertIn("v1.2.3", out)
        self.assertIn("PyPI", out)
        self.assertIn("openai/openai-python #42", out)

    def test_render_empty(self) -> None:
        out = rs.render_recently_shipped([], [])
        self.assertIn("_no releases discovered_", out)
        self.assertIn("_no merged PRs discovered_", out)

    def test_replace_roundtrip(self) -> None:
        text = (
            "intro\n"
            "<!-- recently-shipped:start -->\nOLD\n<!-- recently-shipped:end -->\n"
            "outro\n"
        )
        new = rs.render_recently_shipped([], [])
        out, ok = rs.replace_recently_shipped(text, new)
        self.assertTrue(ok)
        self.assertNotIn("OLD", out)
        self.assertTrue(out.startswith("intro"))
        self.assertTrue(out.rstrip().endswith("outro"))

    def test_replace_missing_section(self) -> None:
        out, ok = rs.replace_recently_shipped("no markers", "x")
        self.assertFalse(ok)
        self.assertEqual(out, "no markers")


if __name__ == "__main__":
    unittest.main()
