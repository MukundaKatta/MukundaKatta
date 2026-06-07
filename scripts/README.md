# Profile automation scripts

These scripts keep the GitHub profile [`README.md`](../README.md) and the
shields.io badge endpoints under [`.stats/`](../.stats) in sync. They run
unattended on a schedule via the workflows in
[`.github/workflows/`](../.github/workflows) and push their results to `main`,
so the pure (non-network) helpers are covered by tests in
[`tests/`](../tests).

Both scripts use **only the Python standard library** — there are no
dependencies to install.

## `refresh_stats.py`

Refreshes the live numbers in the README and regenerates the badge JSON files.

What it updates:

- **Portfolio counts** — public repos, originals, active projects, forks,
  archived, merged upstream PRs (via the GitHub GraphQL API).
- **Marker-tagged numbers** — values wrapped in
  `<!-- marker -->…<!-- /marker -->` comments (npm / PyPI / crates counts, MCP
  Registry servers, HuggingFace spaces/datasets/models, external PR breakdown,
  meta-repo sizes, hackathon tallies, refresh date). A marker only updates if it
  is present in the README, so untagged prose is left untouched.
- **GitHub Stars badge** — the `![GitHub Stars](…)` shields.io URL.
- **"Recently Shipped" section** — latest npm/PyPI releases and the most
  prestigious recently-merged upstream PRs (ranked by repo stars), rewritten
  between the `<!-- recently-shipped:start -->` / `…:end -->` markers.
- **Download badges** — `.stats/{downloads,npm,pypi,crates}.json` shields.io
  "endpoint" files summing last-month downloads across npm, PyPI, and crates.io.

Environment variables:

| Variable | Required | Purpose |
| --- | --- | --- |
| `GH_TOKEN` / `GITHUB_TOKEN` | yes | GitHub API auth for repo/PR counts. |
| `STARS_TOKEN` | optional | PAT with `read:user` to include private self-stars in the Stars badge; falls back to the public count when unset. |

Run it:

```bash
GH_TOKEN=ghp_xxx python3 scripts/refresh_stats.py
```

The script exits non-zero if any managed README section cannot be located, so a
structural change to the README that breaks a marker fails loudly instead of
silently skipping the update.

## `sync_oss_highlights.py`

Pulls the curated `highlights.json` from the
[`oss-contributions`](https://github.com/MukundaKatta/oss-contributions) repo
and rewrites the "Recent OSS Highlights" list between the
`<!-- oss-highlights:start -->` / `…:end -->` markers.

Environment variables:

| Variable | Required | Purpose |
| --- | --- | --- |
| `OSS_HIGHLIGHTS_SOURCE` | optional | Override the source URL (defaults to the raw `oss-contributions/main/highlights.json`). |

Run it:

```bash
python3 scripts/sync_oss_highlights.py
```

## Running the tests

The test suite uses the standard-library `unittest` framework — no `pip
install` step is needed:

```bash
python3 -m unittest discover -s tests
```

The tests exercise the pure text-transformation and formatting helpers (badge
formatting, marker/label replacement, section counting, and the
highlights/recently-shipped renderers). Network-calling functions are not
exercised in CI by design.
