from __future__ import annotations

import json
import os
from pathlib import Path
from urllib.request import urlopen


ROOT = Path(__file__).resolve().parents[1]
README_FILE = ROOT / "README.md"
START_MARKER = "<!-- oss-highlights:start -->"
END_MARKER = "<!-- oss-highlights:end -->"
DEFAULT_SOURCE = "https://raw.githubusercontent.com/MukundaKatta/oss-contributions/main/highlights.json"


REQUIRED_FIELDS = ("repo", "pr", "url", "title")


def fetch_highlights(source: str) -> list[dict]:
    """Fetch and validate the ``highlights`` list from a JSON source.

    The source is a curated file in another repo, so a typo there (a missing
    ``highlights`` key, or the wrong top-level type) should fail loudly with an
    actionable message instead of surfacing a bare ``KeyError``/``TypeError``
    inside the unattended workflow that pushes to ``main``.
    """
    with urlopen(source, timeout=30) as response:  # noqa: S310 - controlled raw GitHub source for repo automation
        payload = json.loads(response.read().decode("utf-8"))
    if not isinstance(payload, dict) or "highlights" not in payload:
        raise ValueError(
            f"highlights source {source!r} must be a JSON object with a "
            "'highlights' key"
        )
    highlights = payload["highlights"]
    if not isinstance(highlights, list):
        raise ValueError(
            f"'highlights' in {source!r} must be a list, got "
            f"{type(highlights).__name__}"
        )
    return highlights


def render_highlights(highlights: list[dict]) -> str:
    lines = [START_MARKER]
    for item in highlights:
        missing = [field for field in REQUIRED_FIELDS if field not in item]
        if missing:
            raise ValueError(
                f"highlight entry {item!r} is missing required field(s): "
                f"{', '.join(missing)}"
            )
        label = f"{item['repo']} #{item['pr']}"
        lines.append(f"- [{label}]({item['url']}) — {item['title']}")
    lines.extend([END_MARKER, ""])
    return "\n".join(lines)


def replace_section(readme_text: str, replacement: str) -> str:
    """Swap the content between the OSS-highlights markers.

    Raises ``ValueError`` with a clear message if either marker is missing so a
    structurally broken README fails the workflow rather than silently writing
    nothing.
    """
    if START_MARKER not in readme_text or END_MARKER not in readme_text:
        raise ValueError(
            f"README is missing the {START_MARKER!r}/{END_MARKER!r} marker pair"
        )
    start = readme_text.index(START_MARKER)
    end = readme_text.index(END_MARKER) + len(END_MARKER)
    return (
        readme_text[:start].rstrip() + "\n" + replacement.rstrip() + readme_text[end:]
    )


def main() -> None:
    readme = README_FILE.read_text()
    source = os.environ.get("OSS_HIGHLIGHTS_SOURCE", DEFAULT_SOURCE)
    replacement = render_highlights(fetch_highlights(source))
    README_FILE.write_text(replace_section(readme, replacement))


if __name__ == "__main__":
    main()
