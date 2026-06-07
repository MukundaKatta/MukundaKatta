"""Tests for the pure (non-network) helpers in scripts/refresh_stats.py.

These cover the README text-transformation and formatting logic that runs
unattended in CI and pushes to main, so a silent regression here would
corrupt the rendered profile.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import refresh_stats as rs  # noqa: E402


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (0, "0"),
        (999, "999"),
        (1_000, "1.0k"),
        (1_500, "1.5k"),
        (23_400, "23.4k"),
        (999_999, "1000.0k"),
        (1_000_000, "1.0M"),
        (2_500_000, "2.5M"),
    ],
)
def test_human(value: int, expected: str) -> None:
    assert rs._human(value) == expected


def test_replace_after_label_plain() -> None:
    text = "<sub>FORKS</sub><br/>\n<strong>12</strong>"
    out, ok = rs.replace_after_label(text, "FORKS", 15)
    assert ok is True
    assert out == "<sub>FORKS</sub><br/>\n<strong>15</strong>"


def test_replace_after_label_preserves_plus_suffix() -> None:
    text = "<sub>PACKAGES</sub><br/>\n        <strong>200+</strong>"
    out, ok = rs.replace_after_label(text, "PACKAGES", 250)
    assert ok is True
    assert "<strong>250+</strong>" in out


def test_replace_after_label_missing_label() -> None:
    out, ok = rs.replace_after_label("nothing here", "FORKS", 5)
    assert ok is False
    assert out == "nothing here"


def test_replace_after_label_only_first_occurrence() -> None:
    text = (
        "<sub>FORKS</sub><br/>\n<strong>1</strong>"
        " ... "
        "<sub>FORKS</sub><br/>\n<strong>1</strong>"
    )
    out, _ = rs.replace_after_label(text, "FORKS", 9)
    assert out.count("<strong>9</strong>") == 1
    assert out.count("<strong>1</strong>") == 1


def test_replace_marker_replaces_all_occurrences() -> None:
    text = (
        "a <!-- npm-count -->5<!-- /npm-count --> "
        "b <!-- npm-count -->old<!-- /npm-count -->"
    )
    out, ok = rs.replace_marker(text, "npm-count", 9)
    assert ok is True
    assert out == (
        "a <!-- npm-count -->9<!-- /npm-count --> "
        "b <!-- npm-count -->9<!-- /npm-count -->"
    )


def test_replace_marker_accepts_non_int_values() -> None:
    text = "<!-- ext-refresh-date -->2020-01-01<!-- /ext-refresh-date -->"
    out, ok = rs.replace_marker(text, "ext-refresh-date", "2026-06-07")
    assert ok is True
    assert "2026-06-07" in out


def test_replace_marker_missing() -> None:
    out, ok = rs.replace_marker("plain text", "npm-count", 3)
    assert ok is False
    assert out == "plain text"


def test_replace_stars_badge() -> None:
    text = (
        "![GitHub Stars](https://img.shields.io/badge/STARS-100-D4A853"
        "?style=for-the-badge&logo=github&labelColor=1a1a1a)"
    )
    out, ok = rs.replace_stars_badge(text, 250)
    assert ok is True
    assert "STARS-250-D4A853" in out
    assert "STARS-100" not in out


def test_replace_stars_badge_missing() -> None:
    out, ok = rs.replace_stars_badge("no badge", 250)
    assert ok is False
    assert out == "no badge"


def test_count_section_entries_stops_at_divider() -> None:
    md = (
        "### Hackathon Submissions\n\n"
        "| [Project A](url) | desc |\n"
        "| [Project B](url) | desc |\n"
        "not a row\n"
        "---\n"
        "| [Project C](url) | other section |\n"
    )
    assert rs.count_section_entries(md, r"^### Hackathon Submissions", "| [") == 2


def test_count_section_entries_missing_header() -> None:
    assert rs.count_section_entries("nope", r"^### Missing", "| [") == 0


def test_count_distinct_bolded_filters_numeric_and_dedupes() -> None:
    md = (
        "### Hackathon Submissions\n"
        "**Event One** and **Event Two** and **53.19** and **Event One**\n"
        "---\n"
    )
    assert rs.count_distinct_bolded(md, r"^### Hackathon Submissions") == 2


def test_count_badge_images() -> None:
    md = (
        "### Certifications\n"
        "![AWS](https://x/a.svg)\n"
        "some prose\n"
        "![GCP](https://x/b.svg)\n"
        "---\n"
        "![Other](https://x/c.svg)\n"
    )
    assert rs.count_badge_images(md, r"^### Certifications") == 2


def test_write_shield_endpoint(tmp_path: Path) -> None:
    import json

    out = tmp_path / "nested" / "badge.json"
    rs.write_shield_endpoint("downloads/mo", 23_400, "D4A853", out)
    payload = json.loads(out.read_text(encoding="utf-8"))
    assert payload["schemaVersion"] == 1
    assert payload["label"] == "downloads/mo"
    assert payload["message"] == "23.4k"
    assert payload["color"] == "D4A853"


def test_render_recently_shipped_with_data() -> None:
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
    assert out.startswith("<!-- recently-shipped:start -->")
    assert out.endswith("<!-- recently-shipped:end -->")
    assert "v1.2.3" in out
    assert "PyPI" in out
    assert "openai/openai-python #42" in out


def test_render_recently_shipped_empty() -> None:
    out = rs.render_recently_shipped([], [])
    assert "_no releases discovered_" in out
    assert "_no merged PRs discovered_" in out


def test_replace_recently_shipped_roundtrip() -> None:
    text = (
        "intro\n"
        "<!-- recently-shipped:start -->\nOLD\n<!-- recently-shipped:end -->\n"
        "outro\n"
    )
    new = rs.render_recently_shipped([], [])
    out, ok = rs.replace_recently_shipped(text, new)
    assert ok is True
    assert "OLD" not in out
    assert out.startswith("intro")
    assert out.rstrip().endswith("outro")


def test_replace_recently_shipped_missing_section() -> None:
    out, ok = rs.replace_recently_shipped("no markers", "x")
    assert ok is False
    assert out == "no markers"
