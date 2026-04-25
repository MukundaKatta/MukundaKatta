from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
README_FILE = ROOT / "README.md"

GH_USER = "MukundaKatta"
NPM_USER = "mukundakatta"

# Mirrors the PyPI table in README.md. PyPI's user page sits behind a JS
# challenge, so we verify each package via the JSON API instead of scraping.
PYPI_PACKAGES = [
    "claude-skill-check",
    "mcp-config-check",
    "claude-hooks-check",
    "claude-commands-check",
    "llm-usage-report",
    "codex-skill-kit",
    "ai-eval-forge",
    "agent-run-diff",
]

GH_TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")


def gh_graphql(query: str) -> dict:
    if not GH_TOKEN:
        sys.exit("GH_TOKEN or GITHUB_TOKEN required")
    req = Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query}).encode(),
        headers={
            "Authorization": f"bearer {GH_TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "MukundaKatta-profile-refresh",
        },
    )
    with urlopen(req, timeout=30) as response:  # noqa: S310 - GitHub API
        payload = json.loads(response.read().decode("utf-8"))
    if "errors" in payload:
        sys.exit(f"GraphQL errors: {payload['errors']}")
    return payload["data"]


def fetch_repo_counts() -> dict[str, int]:
    query = (
        "{\n"
        f'  user(login: "{GH_USER}") {{\n'
        "    total: repositories(ownerAffiliations: OWNER, privacy: PUBLIC) { totalCount }\n"
        "    forks: repositories(ownerAffiliations: OWNER, privacy: PUBLIC, isFork: true) { totalCount }\n"
        "    archived: repositories(ownerAffiliations: OWNER, privacy: PUBLIC, isArchived: true) { totalCount }\n"
        "    originals: repositories(ownerAffiliations: OWNER, privacy: PUBLIC, isFork: false) { totalCount }\n"
        "  }\n"
        f'  activeOriginals: search(query: "user:{GH_USER} is:public archived:false fork:false", type: REPOSITORY) {{ repositoryCount }}\n'
        f'  upstreamPRs: search(query: "is:pr is:merged author:{GH_USER} -user:{GH_USER}", type: ISSUE) {{ issueCount }}\n'
        "}"
    )
    data = gh_graphql(query)
    user = data["user"]
    return {
        "public_repos": user["total"]["totalCount"],
        "forks": user["forks"]["totalCount"],
        "archived": user["archived"]["totalCount"],
        "originals": user["originals"]["totalCount"],
        "active_originals": data["activeOriginals"]["repositoryCount"],
        "upstream_prs": data["upstreamPRs"]["issueCount"],
    }


def fetch_total_stars() -> int:
    # shields.io has no documented endpoint for total stars across all of a
    # user's repos, so we paginate the owner's public repos and sum
    # stargazerCount ourselves. The README badge is rewritten in main() to a
    # static `/badge/STARS-{N}-color` URL using this value.
    cursor: str | None = None
    total = 0
    while True:
        after = f', after: "{cursor}"' if cursor else ""
        query = (
            "{\n"
            f'  user(login: "{GH_USER}") {{\n'
            f"    repositories(ownerAffiliations: OWNER, privacy: PUBLIC, first: 100{after}) {{\n"
            "      pageInfo { hasNextPage endCursor }\n"
            "      nodes { stargazerCount }\n"
            "    }\n"
            "  }\n"
            "}"
        )
        data = gh_graphql(query)
        repos = data["user"]["repositories"]
        total += sum(node["stargazerCount"] for node in repos["nodes"])
        if not repos["pageInfo"]["hasNextPage"]:
            break
        cursor = repos["pageInfo"]["endCursor"]
    return total


def fetch_npm_count() -> int:
    url = f"https://registry.npmjs.org/-/v1/search?text=maintainer:{NPM_USER}&size=250"
    with urlopen(url, timeout=30) as response:  # noqa: S310
        return int(json.loads(response.read().decode("utf-8")).get("total", 0))


def fetch_pypi_count() -> int:
    found = 0
    for name in PYPI_PACKAGES:
        try:
            with urlopen(f"https://pypi.org/pypi/{name}/json", timeout=30) as response:  # noqa: S310
                response.read()
            found += 1
        except HTTPError as err:
            if err.code != 404:
                raise
        except URLError:
            return 0
    return found


def replace_after_label(text: str, label: str, value: int) -> tuple[str, bool]:
    pattern = re.compile(
        r"(<sub>" + re.escape(label) + r"</sub><br/>\s*<strong>)(\d+)(</strong>)"
    )
    new_text, count = pattern.subn(
        lambda m: f"{m.group(1)}{value}{m.group(3)}", text, count=1
    )
    return new_text, count > 0


STARS_BADGE_PATTERN = re.compile(
    r"(\!\[GitHub Stars\]\()https://img\.shields\.io/[^)]+(\))"
)


def replace_stars_badge(text: str, total_stars: int) -> tuple[str, bool]:
    replacement = (
        rf"\1https://img.shields.io/badge/STARS-{total_stars}-D4A853"
        r"?style=for-the-badge&logo=github&labelColor=1a1a1a\2"
    )
    new_text, count = STARS_BADGE_PATTERN.subn(replacement, text, count=1)
    return new_text, count > 0


def main() -> None:
    repos = fetch_repo_counts()
    packages = fetch_npm_count() + fetch_pypi_count()
    total_stars = fetch_total_stars()

    updates = [
        ("PUBLIC REPOS", repos["public_repos"]),
        ("ORIGINALS", repos["originals"]),
        ("ACTIVE PROJECTS", repos["active_originals"]),
        ("FORKS", repos["forks"]),
        ("ARCHIVED", repos["archived"]),
        ("UPSTREAM", repos["upstream_prs"]),
        ("PACKAGES", packages),
        ("ORIGINAL WORK", repos["originals"]),
    ]

    text = README_FILE.read_text(encoding="utf-8")
    missing: list[str] = []
    for label, value in updates:
        text, ok = replace_after_label(text, label, value)
        if not ok:
            missing.append(label)
    text, stars_ok = replace_stars_badge(text, total_stars)
    if not stars_ok:
        missing.append("GitHub Stars badge")
    if missing:
        sys.exit(f"Could not locate stat labels in README: {', '.join(missing)}")

    README_FILE.write_text(text, encoding="utf-8")
    print(json.dumps({**dict(updates), "STARS": total_stars}, indent=2))


if __name__ == "__main__":
    main()
