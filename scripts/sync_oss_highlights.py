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


def fetch_highlights(source: str) -> list[dict]:
    with urlopen(source) as response:  # noqa: S310 - controlled raw GitHub source for repo automation
        payload = json.loads(response.read().decode("utf-8"))
    return payload["highlights"]


def render_highlights(highlights: list[dict]) -> str:
    lines = ["### Recent OSS Highlights", "", START_MARKER]
    for item in highlights:
        label = f"{item['repo']} #{item['pr']}"
        lines.append(f"- [{label}]({item['url']}) — {item['title']}")
    lines.extend([END_MARKER, ""])
    return "\n".join(lines)


def replace_section(readme_text: str, replacement: str) -> str:
    start = readme_text.index(START_MARKER)
    end = readme_text.index(END_MARKER) + len(END_MARKER)
    return readme_text[:start].rstrip() + "\n" + replacement.rstrip() + readme_text[end:]


def main() -> None:
    readme = README_FILE.read_text()
    source = os.environ.get("OSS_HIGHLIGHTS_SOURCE", DEFAULT_SOURCE)
    replacement = render_highlights(fetch_highlights(source))
    README_FILE.write_text(replace_section(readme, replacement))


if __name__ == "__main__":
    main()
