<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=4000&pause=1000&color=D4A853&center=true&vCenter=true&multiline=true&repeat=true&width=1000&height=100&lines=Hey!+I+am+Mukunda+Rao+Katta;Senior+AI%2FML+Engineer+%7C+Ex-AWS+%7C+Building+at+Scale" alt="Typing SVG" />

<br/>

[![Portfolio](https://img.shields.io/badge/Portfolio-1a1a1a?style=for-the-badge&logo=vercel&logoColor=D4A853)](https://mukunda-ai.vercel.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-1a1a1a?style=for-the-badge&logo=linkedin&logoColor=D4A853)](https://www.linkedin.com/in/mukunda-katta-728155220/)
[![X](https://img.shields.io/badge/X-1a1a1a?style=for-the-badge&logo=x&logoColor=D4A853)](https://x.com/katta_mukunda)
[![Email](https://img.shields.io/badge/Email-1a1a1a?style=for-the-badge&logo=gmail&logoColor=D4A853)](mailto:mukunda.vjcs6@gmail.com)

</div>

<br/>

<div align="center">

```
  8+ years building production systems at Fortune 100 scale
  Former SDE at Amazon Web Services  •  Currently at Southwest Airlines
  Deep expertise in ML systems, distributed architectures, and full-stack engineering
```

</div>

---

### Portfolio at a Glance

<div align="center">

<table>
  <tr>
    <td align="center" width="20%">
      <sub>PUBLIC REPOS</sub><br/>
      <strong>505</strong>
    </td>
    <td align="center" width="20%">
      <sub>ORIGINALS</sub><br/>
      <strong>136</strong>
    </td>
    <td align="center" width="20%">
      <sub>ACTIVE PROJECTS</sub><br/>
      <strong>99</strong>
    </td>
    <td align="center" width="20%">
      <sub>FORKS</sub><br/>
      <strong>369</strong>
    </td>
    <td align="center" width="20%">
      <sub>ARCHIVED</sub><br/>
      <strong>329</strong>
    </td>
  </tr>
</table>

Every repo is indexed in **[claude-workspace](https://github.com/MukundaKatta/claude-workspace)** — wired for Multica, Claude Code, Codex, OpenClaw, and Cursor to reason across the portfolio.

</div>

---

### Open Source Focus

I contribute practical fixes to **AI SDKs, MCP tooling, eval frameworks, agent infrastructure, structured outputs, and developer experience**.

My lane is finding the sharp edges that slow builders down: unclear contracts, brittle tool calls, docs that almost answer the question, eval gaps where regressions hide, and AI tooling that needs better failure signals. I like small, reviewable patches with clear intent, and compact packages that turn repeated manual checks into reusable workflows.

Recent contribution areas (merged upstream):

- **Microsoft** — security and architecture docs for internal AI-engineering toolchains (`hve-core`, `physical-ai-toolchain`)
- **Pydantic** — `pydantic-ai` integration with the Vercel AI SDK
- **Hugging Face ecosystem** — `safetensors` Python bindings, `sentence-transformers` trainer migration docs
- **Meilisearch** — `heed` multi-target docs.rs infrastructure
- **Vercel** — `next.js` documentation
- **Apache Software Foundation** — doc / comment fixes across `iceberg`, `pulsar`, `skywalking`, `ozone`, `iotdb`

I keep a public log of selected OSS work in **[oss-contributions](https://github.com/MukundaKatta/oss-contributions)**.

### Recent OSS Highlights
<!-- oss-highlights:start -->
- [openai/openai-node #1831](https://github.com/openai/openai-node/pull/1831) — improved fallback handling for non-standard JSON error bodies
- [openai/tiktoken #529](https://github.com/openai/tiktoken/pull/529) — added PyInstaller hooks for dynamic encoding plugins
- [googleapis/python-genai #2298](https://github.com/googleapis/python-genai/pull/2298) — clarified response_schema vs response_json_schema
- [microsoft/playwright-mcp #1562](https://github.com/microsoft/playwright-mcp/pull/1562) — clarified extension connection and tab-selection flow
- [anthropics/anthropic-sdk-python #1412](https://github.com/anthropics/anthropic-sdk-python/pull/1412) — fixed async memory tool example docs
- [stanford-crfm/helm #4210](https://github.com/stanford-crfm/helm/pull/4210) — fixed later-page deep links for run instances
<!-- oss-highlights:end -->

---
### Published Packages

**npm** (scope [`@mukundakatta`](https://www.npmjs.com/~mukundakatta)):

Flagship packages:

<table>
  <tr>
    <th align="left">Package</th>
    <th align="left">Why it matters</th>
    <th align="left">Install</th>
  </tr>
  <tr>
    <td><strong><a href="https://www.npmjs.com/package/@mukundakatta/mcpcheck">@mukundakatta/mcpcheck</a></strong><br/><sub>MCP config quality gate</sub></td>
    <td>Lint MCP config files for Claude Desktop, Cursor, Cline, Windsurf, and Zed. CLI, GitHub Action, and SARIF for code scanning.</td>
    <td><code>npm i -g @mukundakatta/mcpcheck</code></td>
  </tr>
  <tr>
    <td><strong><a href="https://www.npmjs.com/package/@mukundakatta/designlint">@mukundakatta/designlint</a></strong><br/><sub>frontend quality checks</sub></td>
    <td>HTML/CSS accessibility and design linter for contrast, touch targets, headings, form labels, and leaked secrets.</td>
    <td><code>npm i -g @mukundakatta/designlint</code></td>
  </tr>
  <tr>
    <td><strong><a href="https://www.npmjs.com/package/@mukundakatta/skillint">@mukundakatta/skillint</a></strong><br/><sub>AI skill validation</sub></td>
    <td>Lint Claude Code <code>SKILL.md</code> files for frontmatter, required fields, descriptions, and hardcoded secrets.</td>
    <td><code>npm i -g @mukundakatta/skillint</code></td>
  </tr>
  <tr>
    <td><strong><a href="https://www.npmjs.com/package/@mukundakatta/ai-eval-forge">@mukundakatta/ai-eval-forge</a></strong><br/><sub>eval harness</sub></td>
    <td>Zero-dependency eval harness for comparing model, prompt, and agent behavior. CLI plus programmatic API; also on PyPI.</td>
    <td><code>npm i @mukundakatta/ai-eval-forge</code></td>
  </tr>
  <tr>
    <td><strong><a href="https://www.npmjs.com/package/@mukundakatta/codex-skill-kit">@mukundakatta/codex-skill-kit</a></strong><br/><sub>Codex skill tooling</sub></td>
    <td>Scaffold and validate Codex skills from the command line. Published for npm and PyPI workflows.</td>
    <td><code>npm i -g @mukundakatta/codex-skill-kit</code></td>
  </tr>
  <tr>
    <td><strong><a href="https://www.npmjs.com/package/@mukundakatta/kavach">@mukundakatta/kavach</a></strong><br/><sub>AI-app threat signals</sub></td>
    <td>Small, inspectable threat-scoring library for AI-app security monitoring: signals to weighted score to tier and playbook.</td>
    <td><code>npm i @mukundakatta/kavach</code></td>
  </tr>
</table>

<details>
<summary><strong>More npm packages (33)</strong> — grouped by area</summary>

<br/>

**Agent infrastructure (6)**

| Package | What it does |
|---|---|
| [`@mukundakatta/agent-loop-breaker`](https://www.npmjs.com/package/@mukundakatta/agent-loop-breaker) | Detect repeated agent steps and stop runaway loops. |
| [`@mukundakatta/agent-regression-lens`](https://www.npmjs.com/package/@mukundakatta/agent-regression-lens) | Detect regressions between baseline and current AI agent runs. |
| [`@mukundakatta/agent-trajectory-replay`](https://www.npmjs.com/package/@mukundakatta/agent-trajectory-replay) | Replay and diff AI agent event trajectories for debugging regressions. |
| [`@mukundakatta/tool-call-contracts`](https://www.npmjs.com/package/@mukundakatta/tool-call-contracts) | Validate LLM tool-call payloads with small JSON-like contracts. |
| [`@mukundakatta/tool-permission-gate`](https://www.npmjs.com/package/@mukundakatta/tool-permission-gate) | Policy-check agent tool calls before execution. |
| [`@mukundakatta/tool-result-taint`](https://www.npmjs.com/package/@mukundakatta/tool-result-taint) | Track untrusted tool output before it enters prompts or actions. |

**RAG & retrieval (6)**

| Package | What it does |
|---|---|
| [`@mukundakatta/rag-quality-kit`](https://www.npmjs.com/package/@mukundakatta/rag-quality-kit) | Heuristic quality metrics for RAG retrieval and grounded answers. |
| [`@mukundakatta/rag-staleness-auditor`](https://www.npmjs.com/package/@mukundakatta/rag-staleness-auditor) | Find stale RAG chunks by age, version, and freshness requirements. |
| [`@mukundakatta/retrieval-acl-filter`](https://www.npmjs.com/package/@mukundakatta/retrieval-acl-filter) | Enforce document ACLs after retrieval and before prompting. |
| [`@mukundakatta/vector-poison-score`](https://www.npmjs.com/package/@mukundakatta/vector-poison-score) | Score retrieved documents for vector/RAG poisoning signals. |
| [`@mukundakatta/embedding-dedupe`](https://www.npmjs.com/package/@mukundakatta/embedding-dedupe) | Deduplicate near-identical embedding records by cosine similarity. |
| [`@mukundakatta/context-drift-detector`](https://www.npmjs.com/package/@mukundakatta/context-drift-detector) | Detect topic drift between user intent, retrieved context, and AI answers. |

**Prompt & output safety (5)**

| Package | What it does |
|---|---|
| [`@mukundakatta/pii-sentry`](https://www.npmjs.com/package/@mukundakatta/pii-sentry) | Detect and redact PII and secret-like values before AI processing. |
| [`@mukundakatta/prompt-injection-shield`](https://www.npmjs.com/package/@mukundakatta/prompt-injection-shield) | Prompt-injection risk scanner for untrusted AI context. |
| [`@mukundakatta/llm-output-sanitizer`](https://www.npmjs.com/package/@mukundakatta/llm-output-sanitizer) | Sanitize LLM outputs before rendering, SQL, shell, or markdown sinks. |
| [`@mukundakatta/system-prompt-leak-scan`](https://www.npmjs.com/package/@mukundakatta/system-prompt-leak-scan) | Detect system prompt leakage in model outputs. |
| [`@mukundakatta/jailbreak-corpus-mini`](https://www.npmjs.com/package/@mukundakatta/jailbreak-corpus-mini) | Small local jailbreak + prompt-injection fixture set for tests. |

**Context & prompt engineering (4)**

| Package | What it does |
|---|---|
| [`@mukundakatta/context-forge`](https://www.npmjs.com/package/@mukundakatta/context-forge) | Context engineering toolkit for ranking, packing, and risk-scanning RAG context. |
| [`@mukundakatta/context-window-packer`](https://www.npmjs.com/package/@mukundakatta/context-window-packer) | Pack context chunks into a budget by relevance and priority. |
| [`@mukundakatta/prompt-token-trim`](https://www.npmjs.com/package/@mukundakatta/prompt-token-trim) | Trim prompt messages to fit a token budget while preserving priority. |
| [`@mukundakatta/prompt-version-diff`](https://www.npmjs.com/package/@mukundakatta/prompt-version-diff) | Diff prompt templates and flag risky instruction changes. |

**Evals & tracing (3)**

| Package | What it does |
|---|---|
| [`@mukundakatta/eval-dataset-smith`](https://www.npmjs.com/package/@mukundakatta/eval-dataset-smith) | Generate balanced eval cases from bugs, docs, examples, and policies. |
| [`@mukundakatta/eval-flake-detector`](https://www.npmjs.com/package/@mukundakatta/eval-flake-detector) | Detect flaky LLM eval cases across repeated runs. |
| [`@mukundakatta/llm-trace-sampler`](https://www.npmjs.com/package/@mukundakatta/llm-trace-sampler) | Sample LLM traces by risk, errors, latency, and deterministic ids. |

**Cost, routing & caching (4)**

| Package | What it does |
|---|---|
| [`@mukundakatta/llm-cost-guard`](https://www.npmjs.com/package/@mukundakatta/llm-cost-guard) | Estimate AI request cost and enforce per-request or session budgets. |
| [`@mukundakatta/model-fallback-planner`](https://www.npmjs.com/package/@mukundakatta/model-fallback-planner) | Plan model fallback chains from capability, cost, and health data. |
| [`@mukundakatta/model-router-policy`](https://www.npmjs.com/package/@mukundakatta/model-router-policy) | Policy-based model routing by capability, cost, latency, and privacy. |
| [`@mukundakatta/semantic-cache-key`](https://www.npmjs.com/package/@mukundakatta/semantic-cache-key) | Stable semantic cache keys for AI prompts, tools, models, and retrieval context. |

**Supply chain, citations, consent (5)**

| Package | What it does |
|---|---|
| [`@mukundakatta/ai-supply-chain-manifest`](https://www.npmjs.com/package/@mukundakatta/ai-supply-chain-manifest) | Build and validate lightweight AI model / data / tool manifests. |
| [`@mukundakatta/citation-integrity-check`](https://www.npmjs.com/package/@mukundakatta/citation-integrity-check) | Verify answer citations refer to supplied source ids. |
| [`@mukundakatta/consent-redaction-log`](https://www.npmjs.com/package/@mukundakatta/consent-redaction-log) | Record consent-aware redactions for privacy review trails. |
| [`@mukundakatta/hallucination-risk-meter`](https://www.npmjs.com/package/@mukundakatta/hallucination-risk-meter) | Estimate hallucination risk from answer, context, citations, and uncertainty language. |
| [`@mukundakatta/llm-response-schema-lite`](https://www.npmjs.com/package/@mukundakatta/llm-response-schema-lite) | Tiny schema validator for structured LLM responses. |

Install any of them with `npm i @mukundakatta/<package>`.

</details>

**PyPI:**

<table>
  <tr>
    <th align="left">Package</th>
    <th align="left">Purpose</th>
    <th align="left">Install</th>
  </tr>
  <tr>
    <td><strong><a href="https://pypi.org/project/claude-skill-check/">claude-skill-check</a></strong></td>
    <td>Lint Claude Code <code>SKILL.md</code> files for YAML frontmatter, required fields, description quality, and secret patterns.</td>
    <td><code>pip install claude-skill-check</code></td>
  </tr>
  <tr>
    <td><strong><a href="https://pypi.org/project/mcp-config-check/">mcp-config-check</a></strong></td>
    <td>Validate MCP configs across Claude Desktop, Cursor, Cline, Windsurf, and Zed; catches auth, transport, duplicate, and placeholder issues.</td>
    <td><code>pip install mcp-config-check</code></td>
  </tr>
  <tr>
    <td><strong><a href="https://pypi.org/project/claude-hooks-check/">claude-hooks-check</a></strong></td>
    <td>Audit Claude Code hooks for malformed matchers, dangerous commands, invalid events, and hardcoded secrets.</td>
    <td><code>pip install claude-hooks-check</code></td>
  </tr>
  <tr>
    <td><strong><a href="https://pypi.org/project/claude-commands-check/">claude-commands-check</a></strong></td>
    <td>Validate Claude Code slash-command files for naming, frontmatter, model values, allowed-tools shape, and secret leakage.</td>
    <td><code>pip install claude-commands-check</code></td>
  </tr>
  <tr>
    <td><strong><a href="https://pypi.org/project/llm-usage-report/">llm-usage-report</a></strong></td>
    <td>Parse raw LLM API response logs and generate token and cost reports by provider, model, day, project, or user.</td>
    <td><code>pip install llm-usage-report</code></td>
  </tr>
  <tr>
    <td><strong><a href="https://pypi.org/project/codex-skill-kit/">codex-skill-kit</a></strong></td>
    <td>Scaffold and validate Codex skills from Python environments; mirrors the npm CLI workflow.</td>
    <td><code>pip install codex-skill-kit</code></td>
  </tr>
  <tr>
    <td><strong><a href="https://pypi.org/project/ai-eval-forge/">ai-eval-forge</a></strong></td>
    <td>Zero-dependency LLM and agent eval harness with exact, regex, token-F1, JSON, and citation-coverage checks.</td>
    <td><code>pip install ai-eval-forge</code></td>
  </tr>
  <tr>
    <td><strong><a href="https://pypi.org/project/agent-run-diff/">agent-run-diff</a></strong></td>
    <td>Compare baseline and current agent runs across success, errors, tools, output drift, steps, latency, and cost.</td>
    <td><code>pip install agent-run-diff</code></td>
  </tr>
</table>

**GitHub Marketplace (Actions):**

All four Python linters are also published as composite GitHub Actions, discoverable on the [GitHub Marketplace](https://github.com/marketplace):

- [`claude-skill-check`](https://github.com/marketplace/actions/claude-skill-check)
- [`mcp-config-check`](https://github.com/marketplace/actions/mcp-config-check)
- [`claude-hooks-check`](https://github.com/marketplace/actions/claude-hooks-check)
- [`claude-commands-check`](https://github.com/marketplace/actions/claude-commands-check)

**Homebrew tap** — [`mukundakatta/tools`](https://github.com/MukundaKatta/homebrew-tools):

```bash
brew tap mukundakatta/tools
brew install claude-skill-check mcp-config-check claude-hooks-check claude-commands-check
```

Each ships a CLI, a programmatic API, and (for the linters) a composite GitHub Action you can drop into any workflow in 3 lines.

---
### Featured Projects

<table>
  <tr>
    <td width="50%" valign="top">
      <h4><a href="https://github.com/MukundaKatta/karna">Karna</a> — AI Agent Platform</h4>
      <p>Self-hosted AI assistant with 7 messaging channels (Telegram, Slack, Discord, WhatsApp, SMS, iMessage, Web), extensible plugin SDK, semantic memory, and voice. TypeScript monorepo with Next.js dashboard and React Native mobile app.</p>
      <p><sub><strong>Stack</strong> · TypeScript &bull; Node.js &bull; Next.js &bull; Supabase &bull; WebSocket &bull; pgvector</sub></p>
    </td>
    <td width="50%" valign="top">
      <h4><a href="https://github.com/MukundaKatta/chetana">Chetana</a> — AI Consciousness Research Platform</h4>
      <p>Research-driven platform exploring machine consciousness through 14 indicators grounded in 6 scientific theories. Built to turn abstract AI-consciousness questions into structured experiments, scoring, and analysis.</p>
      <p><sub><strong>Stack</strong> · AI Research &bull; Evaluation &bull; Experimentation &bull; Python</sub></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4><a href="https://github.com/MukundaKatta/AgentRAG">AgentRAG</a> — Modular RAG Pipeline</h4>
      <p>Provider-agnostic RAG framework with pluggable vector stores, chunking strategies, and retrieval methods. Designed for agentic workflows with clean API boundaries.</p>
      <p><sub><strong>Stack</strong> · RAG &bull; Vector Search &bull; Embeddings &bull; TypeScript</sub></p>
    </td>
    <td width="50%" valign="top">
      <h4><a href="https://github.com/MukundaKatta/astra-agent">Astra Agent</a> — AI Agent Runtime</h4>
      <p>Standalone AI agent runtime with tool execution, context management, and multi-model routing. Foundation for building autonomous AI assistants with structured tool use.</p>
      <p><sub><strong>Stack</strong> · TypeScript &bull; LLM Orchestration &bull; Tool Use &bull; Agents</sub></p>
    </td>
  </tr>
</table>

<details>
<summary><strong>More Projects</strong></summary>
<br/>

| Project | Description |
|---------|-------------|
| [Sadhak](https://github.com/MukundaKatta/sadhak) | AI-powered job search command center — automated evaluation, resume tailoring, application tracking |
| [Chetana](https://github.com/MukundaKatta/chetana) | AI consciousness research platform — 14 indicators from 6 scientific theories |
| [Prithvi](https://github.com/MukundaKatta/prithvi) | Container security scanner — vulnerability detection, compliance checks, Docker audits |
| [Amogha Cafe](https://github.com/MukundaKatta/amogha-cafe) | Full-stack Firebase restaurant platform — real-time ordering, QR dine-in. [Live](https://amogha-cafe.web.app) |
| [RNHT](https://github.com/MukundaKatta/rnht) | Temple community platform — events, donations, priest scheduling |
| [Patchly](https://github.com/MukundaKatta/patchly) | AI code review bot — flags bugs, suggests fixes, explains why, like a senior engineer |
| [Evalharness](https://github.com/MukundaKatta/evalharness) | Prompt, agent, and RAG test harness — red teaming, regression testing, CI/CD for AI |
| [AgentMem](https://github.com/MukundaKatta/agentmem) | Pluggable memory management for AI agents |
| [LLM Bench CLI](https://github.com/MukundaKatta/llm-bench-cli) | CLI for benchmarking local LLMs — speed, throughput, quality |
| [TokenWise](https://github.com/MukundaKatta/TokenWise) | Token usage optimization across providers |

</details>

---

### Impact at a Glance

<table>
  <tr>
    <td colspan="4" align="center"><strong>Production AI / ML Impact</strong></td>
  </tr>
  <tr>
    <td align="center" width="25%">
      <sub>COST EFFICIENCY</sub><br/>
      <strong>78%</strong><br/>
      <sub>infrastructure cost reduction<br/>SageMaker → Bedrock migration</sub>
    </td>
    <td align="center" width="25%">
      <sub>LATENCY</sub><br/>
      <strong>600x</strong><br/>
      <sub>retrieval latency improvement<br/>ML prediction system</sub>
    </td>
    <td align="center" width="25%">
      <sub>RAG SCALE</sub><br/>
      <strong>30K+</strong><br/>
      <sub>knowledge base entries<br/>9-stage agentic RAG pipeline</sub>
    </td>
    <td align="center" width="25%">
      <sub>QUALITY</sub><br/>
      <strong>370+</strong><br/>
      <sub>unit tests & evaluations<br/>production ML systems</sub>
    </td>
  </tr>
  <tr>
    <td colspan="4" align="center"><strong>Open Source Footprint</strong></td>
  </tr>
  <tr>
    <td align="center" width="25%">
      <sub>UPSTREAM</sub><br/>
      <strong>93</strong><br/>
      <sub>merged PRs<br/>in external public repos</sub>
    </td>
    <td align="center" width="25%">
      <sub>PACKAGES</sub><br/>
      <strong>47</strong><br/>
      <sub>published packages<br/>across npm + PyPI</sub>
    </td>
    <td align="center" width="25%">
      <sub>ORIGINAL WORK</sub><br/>
      <strong>136</strong><br/>
      <sub>original public repos<br/>maintained on GitHub</sub>
    </td>
    <td align="center" width="25%">
      <sub>ECOSYSTEMS</sub><br/>
      <strong>6+</strong><br/>
      <sub>major org ecosystems<br/>OpenAI, Anthropic, Google,<br/>Microsoft, Stanford, Princeton</sub>
    </td>
  </tr>
</table>

---

### What I Build

```
 ML Systems           Fault prediction, embedding pipelines, model evaluation, cost-optimized inference
 Agentic AI           RAG pipelines, LangGraph workflows, query routing, hallucination detection
 Cloud Infrastructure AWS (Bedrock, SageMaker, ECS, OpenSearch), GCP, Azure, Kubernetes, Terraform
 Full-Stack           React/TypeScript + Java/Python backend APIs, CI/CD, zero-downtime deployments
```

---

### Experience

<table>
  <tr>
    <th align="left">Role</th>
    <th align="left">Company</th>
    <th align="left">Era</th>
    <th align="left">Primary arena</th>
  </tr>
  <tr>
    <td><strong>AI/ML Engineer</strong></td>
    <td>Southwest Airlines</td>
    <td>Aug 2025 — Present</td>
    <td>production ML, agentic RAG, Bedrock migration</td>
  </tr>
  <tr>
    <td><strong>AI/ML Engineer</strong></td>
    <td>GPS IT Solutions</td>
    <td>Jun 2024 — Aug 2025</td>
    <td>RAG platforms, model-risk governance, vector search</td>
  </tr>
  <tr>
    <td><strong>Software Development Engineer</strong></td>
    <td>Amazon Web Services</td>
    <td>Aug 2022 — May 2024</td>
    <td>enterprise cloud systems, React/Java/Python, CI/CD</td>
  </tr>
  <tr>
    <td><strong>Data Engineer</strong></td>
    <td>GPS IT Solutions</td>
    <td>Jan 2022 — Aug 2022</td>
    <td>data pipelines, AWS Glue, PySpark, analytics workflows</td>
  </tr>
  <tr>
    <td><strong>Software Engineer</strong></td>
    <td>American Express</td>
    <td>Feb 2017 — Dec 2020</td>
    <td>Python backend services, REST APIs, enterprise platforms</td>
  </tr>
</table>

<details>
<summary><strong>Highlights</strong></summary>
<br/>

**Southwest Airlines** — AI/ML Engineer
- Architected ML fault prediction system for aircraft maintenance — 5 prediction types, 10K+ records, sub-second retrieval
- Led SageMaker → Bedrock migration: 78% cost reduction ($1,740→$371/mo), 600x latency improvement
- Designed 9-stage agentic RAG pipeline (LangGraph, Bedrock Nova Pro/Micro, FAISS + BM25) over 30K+ KB entries

**GPS IT Solutions** — AI/ML Engineer
- Built GPT-4 + RAG content generation platform with compliance validation, reducing production time by 40%
- Designed AI model risk governance framework with 23 automated evaluation tests achieving regulatory compliance
- Architected FastAPI microservices with FAISS/Pinecone vector search on Kubernetes

**Amazon Web Services (AWS)** — Software Development Engineer
- Built and shipped features for AWS Application Manager (Systems Manager) serving enterprise customers globally
- Owned full-stack delivery: React/TypeScript frontend + Java/Python backend APIs with operational excellence
- Designed CI/CD and IaC patterns enabling zero-downtime deployments at enterprise scale

**GPS IT Solutions** — Data Engineer
- Led end-to-end migration of data pipelines from on-prem to AWS (Glue, PySpark)

**American Express** — Software Engineer
- Developed Python backend services and RESTful APIs for enterprise platforms handling high-volume transactions at scale

</details>

---


### Follow For

If you follow my work here, you’ll mostly see:

- open-source contributions to AI SDKs and agent tooling
- MCP, eval, and developer-experience improvements
- practical full-stack and infrastructure-heavy AI projects
- systems thinking around memory, retrieval, orchestration, and production reliability

---

### Education

**University of Central Missouri** — M.S. in Big Data Analytics and Information Technology (Jan 2021 — May 2022)

**SRM University** — B.Tech in Mechanical Engineering (2012 — 2016)

---

### Certifications

<div align="center">

**Anthropic**

![MCP Advanced](https://img.shields.io/badge/MCP_Advanced_Topics-1a1a1a?style=flat-square&logo=anthropic&logoColor=D4A853)
![Claude with Bedrock](https://img.shields.io/badge/Claude_with_Amazon_Bedrock-1a1a1a?style=flat-square&logo=anthropic&logoColor=D4A853)
![Claude with Vertex AI](https://img.shields.io/badge/Claude_with_Vertex_AI-1a1a1a?style=flat-square&logo=anthropic&logoColor=D4A853)
![Intro to MCP](https://img.shields.io/badge/Intro_to_MCP-1a1a1a?style=flat-square&logo=anthropic&logoColor=D4A853)
![Claude Code](https://img.shields.io/badge/Claude_Code_in_Action-1a1a1a?style=flat-square&logo=anthropic&logoColor=D4A853)
![Building Claude API](https://img.shields.io/badge/Building_with_Claude_API-1a1a1a?style=flat-square&logo=anthropic&logoColor=D4A853)
![Agent Skills](https://img.shields.io/badge/Intro_to_Agent_Skills-1a1a1a?style=flat-square&logo=anthropic&logoColor=D4A853)
![Subagents](https://img.shields.io/badge/Intro_to_Subagents-1a1a1a?style=flat-square&logo=anthropic&logoColor=D4A853)
![AI Fluency](https://img.shields.io/badge/AI_Fluency:_Framework_&_Foundations-1a1a1a?style=flat-square&logo=anthropic&logoColor=D4A853)
![Claude 101](https://img.shields.io/badge/Claude_101-1a1a1a?style=flat-square&logo=anthropic&logoColor=D4A853)

**AWS**

![AWS GenAI Apps](https://img.shields.io/badge/AWS_Generative_AI_Applications-232F3E?style=flat-square&logo=amazonaws&logoColor=FF9900)
![AWS AI Solutions](https://img.shields.io/badge/AWS_Services_for_AI_Solutions-232F3E?style=flat-square&logo=amazonaws&logoColor=FF9900)
![AWS AI Fundamentals](https://img.shields.io/badge/AI_Fundamentals_&_the_Cloud-232F3E?style=flat-square&logo=amazonaws&logoColor=FF9900)
![Amazon Q](https://img.shields.io/badge/Amazon_Q_for_Software_Dev-232F3E?style=flat-square&logo=amazonaws&logoColor=FF9900)

**Cloud & Infrastructure**

![Terraform GCP](https://img.shields.io/badge/Advanced_Terraform_with_GCP-4285F4?style=flat-square&logo=terraform&logoColor=white)
![Vertex AI Agent](https://img.shields.io/badge/Build_&_Deploy_Agent_with_Reasoning_Engine-4285F4?style=flat-square&logo=googlecloud&logoColor=white)

**Stanford / Wharton**

![ML](https://img.shields.io/badge/Machine_Learning-8C1515?style=flat-square&logo=stanford&logoColor=white)
![Stats](https://img.shields.io/badge/Introduction_to_Statistics-8C1515?style=flat-square&logo=stanford&logoColor=white)
![Business Analytics](https://img.shields.io/badge/Business_Analytics-011F5B?style=flat-square&logo=coursera&logoColor=white)
![Customer Analytics](https://img.shields.io/badge/Customer_Analytics-011F5B?style=flat-square&logo=coursera&logoColor=white)
![People Analytics](https://img.shields.io/badge/People_Analytics-011F5B?style=flat-square&logo=coursera&logoColor=white)

**Microsoft**

![GenAI for Devs](https://img.shields.io/badge/Generative_AI_for_Software_Devs-0078D4?style=flat-square&logo=microsoft&logoColor=white)
![GitHub Copilot](https://img.shields.io/badge/GitHub_Copilot_Productivity-0078D4?style=flat-square&logo=microsoft&logoColor=white)
![Copilot PM](https://img.shields.io/badge/Copilot_for_Project_Management-0078D4?style=flat-square&logo=microsoft&logoColor=white)

**LinkedIn Learning**

![Deep Learning](https://img.shields.io/badge/Deep_Learning:_Image_Recognition-0A66C2?style=flat-square&logo=linkedin&logoColor=white)
![TensorFlow](https://img.shields.io/badge/Deep_Learning_with_TensorFlow-0A66C2?style=flat-square&logo=linkedin&logoColor=white)
![NLP Python](https://img.shields.io/badge/NLP_with_Python_for_ML-0A66C2?style=flat-square&logo=linkedin&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache_Spark_Essential-0A66C2?style=flat-square&logo=linkedin&logoColor=white)

</div>

---

### Tech Stack

<div align="center">

![TypeScript](https://img.shields.io/badge/TypeScript-1a1a1a?style=flat-square&logo=typescript&logoColor=D4A853)
![Python](https://img.shields.io/badge/Python-1a1a1a?style=flat-square&logo=python&logoColor=D4A853)
![JavaScript](https://img.shields.io/badge/JavaScript-1a1a1a?style=flat-square&logo=javascript&logoColor=D4A853)
![Java](https://img.shields.io/badge/Java-1a1a1a?style=flat-square&logo=openjdk&logoColor=D4A853)
![Go](https://img.shields.io/badge/Go-1a1a1a?style=flat-square&logo=go&logoColor=D4A853)
![React](https://img.shields.io/badge/React-1a1a1a?style=flat-square&logo=react&logoColor=D4A853)
![Next.js](https://img.shields.io/badge/Next.js-1a1a1a?style=flat-square&logo=nextdotjs&logoColor=D4A853)
![Node.js](https://img.shields.io/badge/Node.js-1a1a1a?style=flat-square&logo=nodedotjs&logoColor=D4A853)
![Claude](https://img.shields.io/badge/Claude-1a1a1a?style=flat-square&logo=anthropic&logoColor=D4A853)
![OpenAI](https://img.shields.io/badge/OpenAI-1a1a1a?style=flat-square&logo=openai&logoColor=D4A853)
![AWS](https://img.shields.io/badge/AWS-1a1a1a?style=flat-square&logo=amazonaws&logoColor=D4A853)
![GCP](https://img.shields.io/badge/GCP-1a1a1a?style=flat-square&logo=googlecloud&logoColor=D4A853)
![Snowflake](https://img.shields.io/badge/Snowflake-1a1a1a?style=flat-square&logo=snowflake&logoColor=D4A853)
![Supabase](https://img.shields.io/badge/Supabase-1a1a1a?style=flat-square&logo=supabase&logoColor=D4A853)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-1a1a1a?style=flat-square&logo=postgresql&logoColor=D4A853)
![Docker](https://img.shields.io/badge/Docker-1a1a1a?style=flat-square&logo=docker&logoColor=D4A853)
![Kubernetes](https://img.shields.io/badge/Kubernetes-1a1a1a?style=flat-square&logo=kubernetes&logoColor=D4A853)
![Terraform](https://img.shields.io/badge/Terraform-1a1a1a?style=flat-square&logo=terraform&logoColor=D4A853)
![FastAPI](https://img.shields.io/badge/FastAPI-1a1a1a?style=flat-square&logo=fastapi&logoColor=D4A853)
![Redis](https://img.shields.io/badge/Redis-1a1a1a?style=flat-square&logo=redis&logoColor=D4A853)
![Apache Airflow](https://img.shields.io/badge/Airflow-1a1a1a?style=flat-square&logo=apacheairflow&logoColor=D4A853)
![Apache Spark](https://img.shields.io/badge/Spark-1a1a1a?style=flat-square&logo=apachespark&logoColor=D4A853)
![LangChain](https://img.shields.io/badge/LangChain-1a1a1a?style=flat-square&logo=chainlink&logoColor=D4A853)

</div>

---

### GitHub Stats

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats-sigma-five.vercel.app/api?username=MukundaKatta&show_icons=true&bg_color=0d1117&title_color=D4A853&icon_color=D4A853&text_color=c9d1d9&hide_border=true&count_private=true&include_all_commits=true" />
  <img src="https://github-readme-stats-sigma-five.vercel.app/api?username=MukundaKatta&show_icons=true&bg_color=0d1117&title_color=D4A853&icon_color=D4A853&text_color=c9d1d9&hide_border=true&count_private=true&include_all_commits=true" height="180" />
</picture>
&nbsp;&nbsp;
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=MukundaKatta&layout=compact&bg_color=0d1117&title_color=D4A853&text_color=c9d1d9&hide_border=true" />
  <img src="https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=MukundaKatta&layout=compact&bg_color=0d1117&title_color=D4A853&text_color=c9d1d9&hide_border=true" height="180" />
</picture>

</div>

<br/>

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=MukundaKatta&background=0d1117&ring=D4A853&fire=D4A853&currStreakLabel=D4A853&sideLabels=D4A853&currStreakNum=c9d1d9&sideNums=c9d1d9&dates=555555&hide_border=true" />
  <img src="https://streak-stats.demolab.com?user=MukundaKatta&background=0d1117&ring=D4A853&fire=D4A853&currStreakLabel=D4A853&sideLabels=D4A853&currStreakNum=c9d1d9&sideNums=c9d1d9&dates=555555&hide_border=true" />
</picture>

</div>

<br/>

<div align="center">

<img src="https://github-readme-activity-graph.vercel.app/graph?username=MukundaKatta&bg_color=0d1117&color=D4A853&line=D4A853&point=D4A853&area_color=D4A853&area=true&hide_border=true" width="95%" />

</div>

---

### Live Signals

<div align="center">

![Profile Views](https://komarev.com/ghpvc/?username=MukundaKatta&color=D4A853&style=for-the-badge&label=PROFILE+VIEWS)
![GitHub Followers](https://img.shields.io/github/followers/MukundaKatta?style=for-the-badge&logo=github&label=FOLLOWERS&color=D4A853&labelColor=1a1a1a)
![GitHub Stars](https://img.shields.io/github/stars/MukundaKatta?affiliations=OWNER%2CCOLLABORATOR&style=for-the-badge&logo=github&label=STARS&color=D4A853&labelColor=1a1a1a)

![ai-eval-forge npm](https://img.shields.io/npm/v/%40mukundakatta%2Fai-eval-forge?style=flat-square&logo=npm&label=ai-eval-forge&color=D4A853&labelColor=1a1a1a)
![agent-regression-lens npm](https://img.shields.io/npm/v/%40mukundakatta%2Fagent-regression-lens?style=flat-square&logo=npm&label=agent-regression-lens&color=D4A853&labelColor=1a1a1a)
![codex-skill-kit PyPI](https://img.shields.io/pypi/v/codex-skill-kit?style=flat-square&logo=pypi&label=codex-skill-kit&color=D4A853&labelColor=1a1a1a)
![OSS log activity](https://img.shields.io/github/last-commit/MukundaKatta/oss-contributions?style=flat-square&logo=github&label=oss-contributions&color=D4A853&labelColor=1a1a1a)

</div>

---

<div align="center">

**Open to opportunities** — Senior AI/ML Engineer &bull; GenAI Platform Engineer &bull; Software Engineer

[mukunda-ai.vercel.app](https://mukunda-ai.vercel.app) &bull; Las Vegas, NV

</div>
