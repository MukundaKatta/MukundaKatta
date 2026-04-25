from __future__ import annotations

import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
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


def gh_graphql(query: str, token: str | None = None) -> dict:
    auth = token or GH_TOKEN
    if not auth:
        sys.exit("GH_TOKEN or GITHUB_TOKEN required")
    req = Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query}).encode(),
        headers={
            "Authorization": f"bearer {auth}",
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
    # Total stars the user has given (own self-stars + external stars), which
    # is what shows on the Stars tab of the profile. Private self-stars are
    # only visible when authenticated as the user — set STARS_TOKEN in repo
    # secrets to a PAT with `read:user` scope to include those. Without it
    # the workflow falls back to the publicly-visible count, which understates
    # by the number of private repos the user has starred.
    query = (
        "{\n"
        f'  user(login: "{GH_USER}") {{\n'
        "    starredRepositories { totalCount }\n"
        "  }\n"
        "}"
    )
    data = gh_graphql(query, token=os.environ.get("STARS_TOKEN"))
    return data["user"]["starredRepositories"]["totalCount"]


def fetch_npm_packages() -> list[str]:
    url = f"https://registry.npmjs.org/-/v1/search?text=maintainer:{NPM_USER}&size=250"
    with urlopen(url, timeout=30) as response:  # noqa: S310
        data = json.loads(response.read().decode("utf-8"))
    return [obj["package"]["name"] for obj in data.get("objects", [])]


def fetch_npm_count() -> int:
    return len(fetch_npm_packages())


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


def _fetch_npm_release(name: str) -> tuple[str, str, str] | None:
    try:
        with urlopen(f"https://registry.npmjs.org/{name}", timeout=15) as response:  # noqa: S310
            data = json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError):
        return None
    latest = data.get("dist-tags", {}).get("latest")
    if not latest:
        return None
    timestamp = data.get("time", {}).get(latest) or data.get("time", {}).get("modified")
    if not timestamp:
        return None
    return (timestamp, name, latest)


def _fetch_pypi_release(name: str) -> tuple[str, str, str] | None:
    try:
        with urlopen(f"https://pypi.org/pypi/{name}/json", timeout=15) as response:  # noqa: S310
            data = json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError):
        return None
    version = data.get("info", {}).get("version")
    if not version:
        return None
    releases = data.get("releases", {}).get(version, [])
    if not releases:
        return None
    upload_times = [entry.get("upload_time_iso_8601") for entry in releases if entry.get("upload_time_iso_8601")]
    if not upload_times:
        return None
    return (max(upload_times), name, version)


def fetch_recent_releases(limit: int = 3) -> list[dict]:
    npm_packages = fetch_npm_packages()
    releases: list[tuple[str, str, str, str]] = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        for result in pool.map(_fetch_npm_release, npm_packages):
            if result:
                releases.append((*result, "npm"))
        for result in pool.map(_fetch_pypi_release, PYPI_PACKAGES):
            if result:
                releases.append((*result, "pypi"))
    releases.sort(reverse=True)
    output = []
    for timestamp, name, version, registry in releases[:limit]:
        date = timestamp[:10]
        if registry == "npm":
            url = f"https://www.npmjs.com/package/{name}"
            display = f"`{name}`"
        else:
            url = f"https://pypi.org/project/{name}/"
            display = f"`{name}`"
        output.append({"date": date, "name": name, "version": version, "registry": registry, "url": url, "display": display})
    return output


def fetch_recent_prs(limit: int = 5) -> list[dict]:
    # Surface the user's most prestigious upstream contributions. We pull a
    # generous window of recent external merged PRs, then rank by repo stars
    # (with merge date as tiebreaker) so well-known projects like openai,
    # anthropics, microsoft, langgenius/dify float to the top instead of
    # whatever PR happened to merge most recently.
    pool_size = max(limit * 6, 30)
    query = (
        "{\n"
        f'  search(query: "is:pr is:merged author:{GH_USER} -user:{GH_USER} sort:updated-desc", type: ISSUE, first: {pool_size}) {{\n'
        "    nodes {\n"
        "      ... on PullRequest {\n"
        "        title\n"
        "        url\n"
        "        mergedAt\n"
        "        repository { nameWithOwner stargazerCount }\n"
        "      }\n"
        "    }\n"
        "  }\n"
        "}"
    )
    data = gh_graphql(query)
    pulls: list[dict] = []
    for node in data["search"]["nodes"]:
        if not node:
            continue
        repo = node["repository"]
        merged = node.get("mergedAt") or ""
        pulls.append(
            {
                "stars": repo["stargazerCount"],
                "merged": merged,
                "date": merged[:10],
                "repo": repo["nameWithOwner"],
                "url": node["url"],
                "title": node["title"],
                "number": node["url"].rsplit("/", 1)[-1],
            }
        )
    pulls.sort(key=lambda p: (p["stars"], p["merged"]), reverse=True)
    return pulls[:limit]


def render_recently_shipped(releases: list[dict], prs: list[dict]) -> str:
    lines = [
        "<!-- recently-shipped:start -->",
        "",
        f"_Last refreshed {datetime.now(timezone.utc).strftime('%Y-%m-%d')} from npm, PyPI, and the GitHub API._",
        "",
        "**Latest releases**",
        "",
    ]
    if releases:
        for r in releases:
            registry_tag = "npm" if r["registry"] == "npm" else "PyPI"
            lines.append(f"- `{r['date']}` · [{r['display']}]({r['url']}) `v{r['version']}` · {registry_tag}")
    else:
        lines.append("- _no releases discovered_")
    lines.extend(["", "**Recently merged PRs**", ""])
    if prs:
        for p in prs:
            lines.append(f"- `{p['date']}` · [{p['repo']} #{p['number']}]({p['url']}) — {p['title']}")
    else:
        lines.append("- _no merged PRs discovered_")
    lines.extend(["", "<!-- recently-shipped:end -->"])
    return "\n".join(lines)


def replace_recently_shipped(text: str, replacement: str) -> tuple[str, bool]:
    pattern = re.compile(
        r"<!-- recently-shipped:start -->.*?<!-- recently-shipped:end -->",
        re.DOTALL,
    )
    new_text, count = pattern.subn(replacement, text, count=1)
    return new_text, count > 0


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
    releases = fetch_recent_releases(limit=3)
    prs = fetch_recent_prs(limit=5)

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
    text, shipped_ok = replace_recently_shipped(text, render_recently_shipped(releases, prs))
    if not shipped_ok:
        missing.append("recently-shipped section")
    if missing:
        sys.exit(f"Could not locate sections in README: {', '.join(missing)}")

    README_FILE.write_text(text, encoding="utf-8")
    summary = {
        **dict(updates),
        "STARS": total_stars,
        "RECENT_RELEASES": len(releases),
        "RECENT_PRS": len(prs),
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
