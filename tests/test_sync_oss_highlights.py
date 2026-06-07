"""Tests for the pure (non-network) helpers in scripts/sync_oss_highlights.py."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

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


def test_render_highlights_format() -> None:
    out = so.render_highlights(_sample_highlights())
    lines = out.splitlines()
    assert lines[0] == so.START_MARKER
    assert so.END_MARKER in lines
    assert "- [openai/openai-python #123]" in out
    assert "— Fix a bug" in out
    assert "- [anthropics/anthropic-sdk-python #45]" in out


def test_render_highlights_empty() -> None:
    out = so.render_highlights([])
    assert so.START_MARKER in out
    assert so.END_MARKER in out


def test_replace_section_replaces_between_markers() -> None:
    readme = (
        "before text\n\n"
        f"{so.START_MARKER}\nold content\n{so.END_MARKER}\n\n"
        "after text\n"
    )
    replacement = so.render_highlights(_sample_highlights())
    out = so.replace_section(readme, replacement)
    assert "old content" not in out
    assert "openai/openai-python #123" in out
    assert out.startswith("before text")
    assert out.rstrip().endswith("after text")
    # Markers must survive so the next sync can find them again.
    assert out.count(so.START_MARKER) == 1
    assert out.count(so.END_MARKER) == 1


def test_replace_section_preserves_trailing_content() -> None:
    readme = f"{so.START_MARKER}\nx\n{so.END_MARKER}\n\n## Next section\nbody\n"
    out = so.replace_section(readme, so.render_highlights([]))
    assert "## Next section" in out
    assert "body" in out


def test_replace_section_missing_marker_raises() -> None:
    with pytest.raises(ValueError):
        so.replace_section("no markers here", so.render_highlights([]))
