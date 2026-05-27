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
HF_USER = "mukunda1729"
MCP_REGISTRY = "https://registry.modelcontextprotocol.io/v0/servers"

# Mirrors the PyPI table in README.md. PyPI's user page sits behind a JS
# challenge, so we verify each package via the JSON API instead of scraping.
PYPI_PACKAGES = [
    # Featured (linked at the top of the README PyPI table).
    "claude-skill-check",
    "mcp-config-check",
    "claude-hooks-check",
    "claude-commands-check",
    "llm-usage-report",
    "codex-skill-kit",
    "ai-eval-forge",
    "agent-run-diff",
    "mk-agentkit",
    # Streaming + agent reliability stack (Python ports of the npm quintet).
    "agentfit-py",
    "agentguard-firewall",
    "agentsnap-py",
    "agentvet-py",
    "agentcast-py",
    "partial-json-stream",
    # Prompt + output safety.
    "prompt-injection-shield-py",
    "llm-output-sanitizer-py",
    "system-prompt-leak-scan",
    # RAG + retrieval.
    "embedding-dedupe",
    "rag-quality-kit",
    "rag-staleness-auditor-py",
    # Cost, caching, evals.
    "llm-cost-guard-py",
    "semantic-cache-key",
    "eval-flake-detector",
    # Verification + grounding.
    "hallucination-risk-meter",
    "citation-integrity-check",
    "vector-poison-score",
    # Agent infrastructure + meta.
    "agent-loop-breaker-py",
    "agent-regression-lens-py",
    "agent-trajectory-replay-py",
    "context-forge-py",
    "context-window-packer-py",
    "context-drift-detector-py",
    # Tools / safety / privacy.
    "tool-call-contracts-py",
    "tool-permission-gate-py",
    "tool-result-taint-py",
    "pii-sentry-py",
    # Niche linters + extras.
    "designlint-py",
    "skillint-py",
    "mcpcheck-py",
    "kavach-py",
    # Evals + cost + routing.
    "eval-dataset-smith-py",
    "model-router-policy-py",
    "model-fallback-planner-py",
    "llm-trace-sampler-py",
    "llm-response-schema-lite-py",
    # Safety + supply chain.
    "ai-supply-chain-manifest-py",
    "consent-redaction-log-py",
    "retrieval-acl-filter-py",
    "prompt-token-trim-py",
    "prompt-version-diff-py",
    "jailbreak-corpus-mini-py",
    "openai-responses-testkit",
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


def _npm_downloads_last_month(name: str) -> int:
    from urllib.parse import quote

    enc = quote(name, safe="")
    try:
        with urlopen(
            f"https://api.npmjs.org/downloads/point/last-month/{enc}", timeout=15
        ) as response:  # noqa: S310
            return int(json.loads(response.read().decode("utf-8")).get("downloads", 0) or 0)
    except (HTTPError, URLError):
        return 0


def _pypi_downloads_last_month(name: str) -> int:
    try:
        with urlopen(
            f"https://pypistats.org/api/packages/{name}/recent", timeout=15
        ) as response:  # noqa: S310
            data = json.loads(response.read().decode("utf-8"))
        return int((data.get("data") or {}).get("last_month", 0) or 0)
    except HTTPError as err:
        if err.code == 404:
            return 0
        return 0
    except URLError:
        return 0


def fetch_crates_packages() -> list[str]:
    """List crates owned by ``GH_USER`` on crates.io.

    Resolves username → user_id, then pages through their owned crates.
    """
    try:
        with urlopen(
            f"https://crates.io/api/v1/users/{GH_USER}", timeout=15
        ) as response:  # noqa: S310
            user = json.loads(response.read().decode("utf-8")).get("user") or {}
    except (HTTPError, URLError):
        return []
    user_id = user.get("id")
    if not user_id:
        return []
    crates: list[str] = []
    page = 1
    while True:
        url = (
            f"https://crates.io/api/v1/crates?user_id={user_id}"
            f"&per_page=100&page={page}"
        )
        try:
            with urlopen(url, timeout=30) as response:  # noqa: S310
                data = json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError):
            break
        items = data.get("crates", [])
        if not items:
            break
        crates.extend(c["name"] for c in items if c.get("name"))
        if len(items) < 100:
            break
        page += 1
    return crates


def fetch_hf_count(kind: str) -> int:
    """Count HuggingFace items (`spaces`, `datasets`, or `models`) owned by HF_USER."""
    try:
        with urlopen(
            f"https://huggingface.co/api/{kind}?author={HF_USER}&limit=200",
            timeout=30,
        ) as response:  # noqa: S310
            data = json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError):
        return 0
    return len(data) if isinstance(data, list) else 0


def fetch_repo_directory_count(repo: str, path: str) -> int:
    """Count entries inside a directory of a repo. Used to size meta-repos like
    ``mcp-stack/packages`` and ``rust-llm-stack/crates`` so the now: prose
    self-updates as the stack grows."""
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    req = Request(url, headers={
        "Authorization": f"bearer {GH_TOKEN}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "MukundaKatta-profile-refresh",
    })
    try:
        with urlopen(req, timeout=15) as response:  # noqa: S310
            entries = json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError):
        return 0
    if not isinstance(entries, list):
        return 0
    return sum(1 for e in entries if e.get("type") in {"dir", "file"})


def count_section_entries(text: str, header_pattern: str, row_prefix: str) -> int:
    """Count table rows under a section header, stopping at the next ``---``."""
    section = re.search(
        rf"{header_pattern}.*?(?:\n---\n|\Z)", text, flags=re.DOTALL | re.MULTILINE,
    )
    if not section:
        return 0
    return sum(
        1 for line in section.group(0).splitlines() if line.startswith(row_prefix)
    )


def count_distinct_bolded(text: str, header_pattern: str) -> int:
    """Count distinct ``**Bold Name**`` markers under a section header. Filters
    out numeric-only bolds (scores like ``**53.19**``) so only event-style names
    are counted."""
    section = re.search(
        rf"{header_pattern}.*?(?:\n---\n|\Z)", text, flags=re.DOTALL | re.MULTILINE,
    )
    if not section:
        return 0
    bolds = re.findall(r"\*\*([A-Z][^*]+)\*\*", section.group(0))
    return len({b.strip() for b in bolds})


def count_badge_images(text: str, header_pattern: str) -> int:
    """Count ``![alt](badge-url)`` images under a section header."""
    section = re.search(
        rf"{header_pattern}.*?(?:\n---\n|\Z)", text, flags=re.DOTALL | re.MULTILINE,
    )
    if not section:
        return 0
    return len(re.findall(r"^!\[", section.group(0), flags=re.MULTILINE))


def fetch_external_pr_stats() -> dict[str, int]:
    """Counts of PRs authored upstream (excluding own repos) by state, plus
    unique-repo counts for merged and total. Uses the GitHub search API for
    state aggregates and paginates merged/total repo URLs for distinct counts."""

    def total_count(query: str) -> int:
        data = gh_graphql(
            "{ search(query: " + json.dumps(query) + ', type: ISSUE) { issueCount } }'
        )
        return data["search"]["issueCount"]

    base = f"is:pr author:{GH_USER} -user:{GH_USER}"
    merged_total = total_count(f"{base} is:merged")
    open_total = total_count(f"{base} is:open")
    closed_total = total_count(f"{base} is:closed is:unmerged")
    total = total_count(base)

    def distinct_repos(query: str) -> int:
        # The search REST API caps at 1000 results across pagination — fine for
        # our scale today (964 total). Each item carries a repository_url we
        # can dedupe on.
        seen: set[str] = set()
        page = 1
        while True:
            url = (
                "https://api.github.com/search/issues"
                f"?q={query.replace(' ', '+')}&per_page=100&page={page}"
            )
            req = Request(url, headers={
                "Authorization": f"bearer {GH_TOKEN}",
                "Accept": "application/vnd.github+json",
                "User-Agent": "MukundaKatta-profile-refresh",
            })
            try:
                with urlopen(req, timeout=30) as response:  # noqa: S310
                    data = json.loads(response.read().decode("utf-8"))
            except (HTTPError, URLError):
                break
            items = data.get("items", [])
            if not items:
                break
            for item in items:
                if (u := item.get("repository_url")):
                    seen.add(u)
            if len(items) < 100:
                break
            page += 1
            if page > 10:  # 1000-item cap
                break
        return len(seen)

    return {
        "merged": merged_total,
        "open": open_total,
        "closed": closed_total,
        "total": total,
        "unique_repos": distinct_repos(base),
        "merged_repos": distinct_repos(f"{base} is:merged"),
    }


def fetch_mcp_registry_count() -> int:
    """Count MCP servers in the official registry under ``io.github.<GH_USER>``."""
    prefix = f"io.github.{GH_USER}".lower()
    seen: set[str] = set()
    cursor = ""
    for _ in range(20):  # safety cap on pagination
        url = f"{MCP_REGISTRY}?search={GH_USER}&limit=100"
        if cursor:
            url += f"&cursor={cursor}"
        try:
            with urlopen(url, timeout=30) as response:  # noqa: S310
                data = json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError):
            break
        # Entries wrap their payload under "server": {"name": "io.github.<user>/..."}
        for entry in data.get("servers", []):
            srv = entry.get("server") if isinstance(entry, dict) else None
            name = ((srv or entry).get("name") or "").lower()
            if name.startswith(prefix):
                seen.add(name)
        cursor = (data.get("metadata") or {}).get("next_cursor") or ""
        if not cursor:
            break
    return len(seen)


def _crates_downloads_last_month(name: str) -> int:
    """Sum the last 30 days of downloads for one crate.

    crates.io returns per-version daily counts plus an ``extra_downloads``
    bucket for downloads that don't pin a specific version; both contribute
    to the human-visible total.
    """
    from datetime import timedelta
    from urllib.parse import quote

    enc = quote(name, safe="")
    try:
        with urlopen(
            f"https://crates.io/api/v1/crates/{enc}/downloads", timeout=15
        ) as response:  # noqa: S310
            data = json.loads(response.read().decode("utf-8"))
    except (HTTPError, URLError):
        return 0
    cutoff = (datetime.now(timezone.utc) - timedelta(days=30)).date().isoformat()
    total = 0
    for item in data.get("version_downloads", []) or []:
        if (item.get("date") or "") >= cutoff:
            total += int(item.get("downloads", 0) or 0)
    for item in (data.get("meta") or {}).get("extra_downloads", []) or []:
        if (item.get("date") or "") >= cutoff:
            total += int(item.get("downloads", 0) or 0)
    return total


def fetch_total_downloads() -> dict[str, int]:
    """Sum last-month downloads across npm, PyPI, and crates.io.

    npm has tight per-IP rate limits on /downloads, so we throttle with a small
    pool. PyPI's pypistats.org and crates.io's API are more generous but still
    benefit from a pool.
    """
    npm_packages = fetch_npm_packages()
    crates_packages = fetch_crates_packages()
    with ThreadPoolExecutor(max_workers=4) as pool:
        npm_total = sum(pool.map(_npm_downloads_last_month, npm_packages))
    with ThreadPoolExecutor(max_workers=8) as pool:
        pypi_total = sum(pool.map(_pypi_downloads_last_month, PYPI_PACKAGES))
    with ThreadPoolExecutor(max_workers=4) as pool:
        crates_total = sum(pool.map(_crates_downloads_last_month, crates_packages))
    return {
        "npm": npm_total,
        "pypi": pypi_total,
        "crates": crates_total,
        "combined": npm_total + pypi_total + crates_total,
    }


def _human(n: int) -> str:
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}k"
    return str(n)


def write_shield_endpoint(label: str, value: int, color: str, path: Path) -> None:
    """Write a shields.io 'endpoint' JSON file the README badge can point at."""
    payload = {
        "schemaVersion": 1,
        "label": label,
        "message": _human(value),
        "color": color,
        "labelColor": "1a1a1a",
        "style": "for-the-badge",
        "namedLogo": "data",
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload) + "\n", encoding="utf-8")


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
    # Preserve an optional trailing "+" if the README uses it as an approximation marker
    # (e.g. "<strong>200+</strong>"); the new value keeps the same suffix.
    pattern = re.compile(
        r"(<sub>" + re.escape(label) + r"</sub><br/>\s*<strong>)(\d+)(\+?)(</strong>)"
    )
    new_text, count = pattern.subn(
        lambda m: f"{m.group(1)}{value}{m.group(3)}{m.group(4)}", text, count=1
    )
    return new_text, count > 0


def replace_marker(text: str, marker: str, value: object) -> tuple[str, bool]:
    """Replace the body between ``<!-- {marker} -->`` ... ``<!-- /{marker} -->``.

    Lets the prose between the markers stay editorial (units, asides, " + "
    separators) while the value itself self-updates each refresh. Accepts any
    stringifiable value (ints for counts, ISO dates, etc.) and replaces every
    occurrence so the same metric can appear in more than one section without
    falling out of sync.
    """
    pattern = re.compile(
        r"(<!-- " + re.escape(marker) + r" -->).*?(<!-- /" + re.escape(marker) + r" -->)",
        re.DOTALL,
    )
    new_text, count = pattern.subn(
        lambda m: f"{m.group(1)}{value}{m.group(2)}", text
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
    npm = fetch_npm_count()
    pypi = fetch_pypi_count()
    crates = len(fetch_crates_packages())
    mcp_registry = fetch_mcp_registry_count()
    hf_spaces = fetch_hf_count("spaces")
    hf_datasets = fetch_hf_count("datasets")
    hf_models = fetch_hf_count("models")
    external = fetch_external_pr_stats()
    mcp_stack = fetch_repo_directory_count(f"{GH_USER}/mcp-stack", "packages")
    rust_llm_stack = fetch_repo_directory_count(f"{GH_USER}/rust-llm-stack", "crates")
    packages = npm + pypi
    total_stars = fetch_total_stars()
    releases = fetch_recent_releases(limit=3)
    prs = fetch_recent_prs(limit=5)
    downloads = fetch_total_downloads()
    today_iso = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    write_shield_endpoint(
        "downloads/mo", downloads["combined"], "D4A853", ROOT / ".stats" / "downloads.json"
    )
    write_shield_endpoint(
        "npm/mo", downloads["npm"], "CB3837", ROOT / ".stats" / "npm.json"
    )
    write_shield_endpoint(
        "pypi/mo", downloads["pypi"], "3776AB", ROOT / ".stats" / "pypi.json"
    )
    write_shield_endpoint(
        "crates/mo", downloads["crates"], "DEA584", ROOT / ".stats" / "crates.json"
    )

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
    # Counts derived from the README itself (pre-refresh snapshot).
    hackathon_entries = count_section_entries(
        text, r"^### Hackathon Submissions", "| ["
    )
    hackathon_events = count_distinct_bolded(
        text, r"^### Hackathon Submissions"
    )
    cert_badges_shown = count_badge_images(text, r"^### Certifications")
    missing: list[str] = []
    for label, value in updates:
        text, ok = replace_after_label(text, label, value)
        if not ok:
            missing.append(label)
    # Optional marker-tagged numbers in the breakdown text. Markers are
    # `<!-- npm-count -->NNN<!-- /npm-count -->`; if a marker is absent the
    # README hasn't opted in to auto-refresh for that number and we skip
    # silently — keeps the editorial-only refresh path unchanged.
    marker_values: list[tuple[str, object]] = [
        ("npm-count", npm),
        ("pypi-count", pypi),
        ("crates-count", crates),
        ("mcp-registry-count", mcp_registry),
        ("hf-spaces-count", hf_spaces),
        ("hf-datasets-count", hf_datasets),
        ("hf-models-count", hf_models),
        ("ext-merged", external["merged"]),
        ("ext-open", external["open"]),
        ("ext-closed", external["closed"]),
        ("ext-total", external["total"]),
        ("ext-unique-repos", external["unique_repos"]),
        ("ext-merged-repos", external["merged_repos"]),
        ("ext-refresh-date", today_iso),
        ("mcp-stack-count", mcp_stack),
        ("rust-llm-stack-count", rust_llm_stack),
        ("hackathon-entries", hackathon_entries),
        ("hackathon-events", hackathon_events),
        ("cert-badges-shown", cert_badges_shown),
    ]
    for marker, value in marker_values:
        text, _ = replace_marker(text, marker, value)
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
        "NPM": npm,
        "PYPI": pypi,
        "CRATES_IO": crates,
        "MCP_REGISTRY": mcp_registry,
        "HF_SPACES": hf_spaces,
        "HF_DATASETS": hf_datasets,
        "HF_MODELS": hf_models,
        "EXT_MERGED": external["merged"],
        "EXT_OPEN": external["open"],
        "EXT_CLOSED": external["closed"],
        "EXT_TOTAL": external["total"],
        "EXT_UNIQUE_REPOS": external["unique_repos"],
        "EXT_MERGED_REPOS": external["merged_repos"],
        "MCP_STACK": mcp_stack,
        "RUST_LLM_STACK": rust_llm_stack,
        "HACKATHON_ENTRIES": hackathon_entries,
        "HACKATHON_EVENTS": hackathon_events,
        "CERT_BADGES_SHOWN": cert_badges_shown,
        "STARS": total_stars,
        "RECENT_RELEASES": len(releases),
        "RECENT_PRS": len(prs),
        "DOWNLOADS_NPM": downloads["npm"],
        "DOWNLOADS_PYPI": downloads["pypi"],
        "DOWNLOADS_CRATES": downloads["crates"],
        "DOWNLOADS_COMBINED": downloads["combined"],
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
