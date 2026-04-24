# Blog post outline: "I built 4 linters for Claude Code in a weekend"

> This is a STRUCTURE ONLY. Fill in each section in your own voice — first-person, specific, no em dashes, no "game-changing" / "revolutionized" / corporate language. Readers can smell AI-drafted posts in the first paragraph. The whole point of posting this is that it sounds like YOU.

---

## Target length
700-1200 words. Any longer, readers bounce. Any shorter, it feels thin.

## Target audience
AI engineers using Claude Code. People writing MCP servers. Anyone running skills or slash commands and wondering "is my config correct?"

## Suggested title options (pick one, edit to taste)
- "Four linters for Claude Code that I wish existed"
- "What I learned shipping 4 Python linters in a day"
- "Claude Code configs quietly fail. I built tools to catch that."

## Structure (fill each section yourself)

### 1. Opening hook (1-2 paragraphs)
- Concrete moment: a specific bug or footgun that burned you. (`rm -rf` that shouldn't have been there? A typo in a SKILL.md frontmatter field name? A hardcoded key in an env block?)
- Why this kept happening to you specifically. Be honest: "I kept doing X and Claude kept running it" beats "enterprises need governance"
- One-line of what you ended up doing about it.

### 2. The four tools (short pitches, 2-3 sentences each — link each to PyPI + GitHub)
- `claude-skill-check` — what specifically it caught for you.
- `mcp-config-check` — a real MCP config mistake it would have caught.
- `claude-hooks-check` — an actual hook you wrote that this tool would have flagged.
- `claude-commands-check` — something specific about your slash commands.

### 3. What surprised me while building them (the actual content — 3-5 bullets)
Pick the ones that are TRUE for you, drop the rest, add more of your own. These are starting points, not fill-ins:
- "I expected YAML frontmatter to be the hard part. The hard part was X."
- "I thought Python's stdlib was enough. It wasn't because Y."
- "The `mcpServers` vs `context_servers` split across clients took longer to map than I expected."
- "Writing regex for 'is this a real API key' without false positives on example keys was trickier than I thought."
- "I almost shipped my own Anthropic key in a test fixture."

### 4. What I got wrong the first time (this is the section readers actually remember)
Be specific. One real mistake > five vague ones.
- Did you ship with a broken release workflow?
- Did you leak something into a commit?
- Did you misunderstand a spec?

### 5. What's next (short — 3-4 sentences)
- Which of the 4 got installed the most in the first week (real number, not "lots of interest")
- What you'll improve in v0.2.0 of the most-used one
- What you won't build and why

### 6. Call to action (1-2 sentences)
- "Install one, try it on your config, tell me what it got wrong."
- Link to one package's issue tracker, not all four. Concentrate the feedback loop.

---

## Anti-patterns to delete if you notice yourself writing them

- "In today's fast-paced AI landscape..."
- "I'm excited to announce..."
- "This tool is game-changing for..."
- Em dashes used as rhetorical pauses (you already avoid these, keep doing so)
- Lists of features with marketing adjectives ("powerful", "seamless", "comprehensive")
- Gratitude-theater ("shoutout to the incredible community...")

## Things to include that will help it stand out
- A single screenshot of one of the linters catching a real issue (SKILL.md in VS Code with a squiggle, or CLI output on a bad MCP config). One image, not five.
- A "receipts" line at the bottom: honest download numbers after week 1, even if they're small. Small-number honesty beats big-number fluff.
- A link to the profile page where all four live, so a reader who likes one can find the others.

## Posting checklist

- [ ] Draft written in your voice
- [ ] No em dashes
- [ ] One screenshot
- [ ] Canonical URL pointed at your own blog (mukunda-ai.vercel.app) if you post to dev.to, Hashnode, Medium
- [ ] Schedule for a weekday morning US time if you want the US dev audience; weekday evening India time for the India audience
- [ ] Don't post to 5 places in 10 minutes. Post to one. Watch for 48 hours. Then syndicate.
