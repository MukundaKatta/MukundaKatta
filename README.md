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

| Public Repos | Originals | Active Projects | Forks | Archived |
|:---:|:---:|:---:|:---:|:---:|
| **505** | **136** | **99** | **369** | **329** |

Every repo is indexed in **[claude-workspace](https://github.com/MukundaKatta/claude-workspace)** — wired for Multica, Claude Code, Codex, OpenClaw, and Cursor to reason across the portfolio.

</div>

---

### Open Source Focus

I contribute practical fixes to **AI SDKs, MCP tooling, eval frameworks, agent infrastructure, and developer experience**.

Recent contribution areas:

- **OpenAI** — SDKs, tokenizer tooling, docs, and error handling
- **Anthropic** — SDK examples and developer experience fixes
- **Google** — structured output and SDK documentation clarifications
- **Microsoft** — Playwright MCP docs and browser tooling
- **Stanford / Princeton** — HELM, benchmark, and evaluation ecosystem improvements

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

| Package | What it does | Install |
|---|---|---|
| [`@mukundakatta/mcpcheck`](https://www.npmjs.com/package/@mukundakatta/mcpcheck) | Lint MCP (Model Context Protocol) config files for Claude Desktop, Cursor, Cline, Windsurf, Zed. CLI + GitHub Action + SARIF for Code Scanning. | `npm i -g @mukundakatta/mcpcheck` |
| [`@mukundakatta/designlint`](https://www.npmjs.com/package/@mukundakatta/designlint) | HTML/CSS accessibility + design linter — contrast, touch targets, headings, form labels, secrets. CLI + GitHub Action + SARIF. | `npm i -g @mukundakatta/designlint` |
| [`@mukundakatta/skillint`](https://www.npmjs.com/package/@mukundakatta/skillint) | Linter for Claude Code `SKILL.md` files — frontmatter, required fields, descriptions, hardcoded secrets. CLI + GitHub Action. | `npm i -g @mukundakatta/skillint` |
| [`@mukundakatta/kavach`](https://www.npmjs.com/package/@mukundakatta/kavach) | Small, inspectable threat-scoring library for AI-app security monitoring. Signals → weighted score → tier + playbook. | `npm i @mukundakatta/kavach` |

**PyPI:**

| Package | What it does | Install |
|---|---|---|
| [`claude-skill-check`](https://pypi.org/project/claude-skill-check/) | Python linter for Claude Code `SKILL.md` files. Validates YAML frontmatter, required fields, description length, and flags common secret patterns. CLI + library API. | `pip install claude-skill-check` |

Each ships a CLI, a programmatic API, and (for the linters) a composite GitHub Action you can drop into any workflow in 3 lines.

---
### Featured Projects

<table>
  <tr>
    <td width="50%">
      <h4><a href="https://github.com/MukundaKatta/karna">Karna</a> — AI Agent Platform</h4>
      <p>Self-hosted AI assistant with 7 messaging channels (Telegram, Slack, Discord, WhatsApp, SMS, iMessage, Web), extensible plugin SDK, semantic memory, and voice. TypeScript monorepo with Next.js dashboard and React Native mobile app.</p>
      <sub>TypeScript &bull; Node.js &bull; Next.js &bull; Supabase &bull; WebSocket &bull; pgvector</sub>
    </td>
    <td width="50%">
      <h4><a href="https://github.com/MukundaKatta/chetana">Chetana</a> — AI Consciousness Research Platform</h4>
      <p>Research-driven platform exploring machine consciousness through 14 indicators grounded in 6 scientific theories. Built to turn abstract AI-consciousness questions into structured experiments, scoring, and analysis.</p>
      <sub>AI Research &bull; Evaluation &bull; Experimentation &bull; Python</sub>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h4><a href="https://github.com/MukundaKatta/AgentRAG">AgentRAG</a> — Modular RAG Pipeline</h4>
      <p>Provider-agnostic RAG framework with pluggable vector stores, chunking strategies, and retrieval methods. Designed for agentic workflows with clean API boundaries.</p>
      <sub>RAG &bull; Vector Search &bull; Embeddings &bull; TypeScript</sub>
    </td>
    <td width="50%">
      <h4><a href="https://github.com/MukundaKatta/astra-agent">Astra Agent</a> — AI Agent Runtime</h4>
      <p>Standalone AI agent runtime with tool execution, context management, and multi-model routing. Foundation for building autonomous AI assistants with structured tool use.</p>
      <sub>TypeScript &bull; LLM Orchestration &bull; Tool Use &bull; Agents</sub>
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
    <td colspan="4" align="center"><strong>At Work</strong></td>
  </tr>
  <tr>
    <td align="center" width="25%">
      <strong>78%</strong><br/>
      <sub>Infrastructure cost reduction<br/>SageMaker → Bedrock migration</sub>
    </td>
    <td align="center" width="25%">
      <strong>600x</strong><br/>
      <sub>Retrieval latency improvement<br/>ML prediction system</sub>
    </td>
    <td align="center" width="25%">
      <strong>30K+</strong><br/>
      <sub>Knowledge base entries<br/>9-stage agentic RAG pipeline</sub>
    </td>
    <td align="center" width="25%">
      <strong>370+</strong><br/>
      <sub>Unit tests & evaluations<br/>Production ML systems</sub>
    </td>
  </tr>
  <tr>
    <td colspan="4" align="center"><strong>In Open Source</strong></td>
  </tr>
  <tr>
    <td align="center" width="25%">
      <strong>93</strong><br/>
      <sub>Merged PRs<br/>in external public repos</sub>
    </td>
    <td align="center" width="25%">
      <strong>5</strong><br/>
      <sub>Published packages<br/>across npm + PyPI</sub>
    </td>
    <td align="center" width="25%">
      <strong>136</strong><br/>
      <sub>Original public repos<br/>maintained on GitHub</sub>
    </td>
    <td align="center" width="25%">
      <strong>6+</strong><br/>
      <sub>Orgs contributed to<br/>OpenAI, Anthropic, Google,<br/>Microsoft, Stanford, Princeton</sub>
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

| Role | Company | Duration |
|------|---------|----------|
| **AI/ML Engineer** | Southwest Airlines | Aug 2025 — Present |
| **AI/ML Engineer** | GPS IT Solutions | Jun 2024 — Aug 2025 |
| **Software Development Engineer** | Amazon Web Services (AWS) | Aug 2022 — May 2024 |
| **Data Engineer** | Cigna | Jan 2022 — Aug 2022 |
| **Software Engineer** | American Express | Feb 2017 — Dec 2020 |

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

**Cigna** — Data Engineer
- Led end-to-end migration of healthcare data pipelines from on-prem to AWS (Glue, PySpark)

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

<div align="center">

**Open to opportunities** — Senior AI/ML Engineer &bull; GenAI Platform Engineer &bull; Software Engineer

[mukunda-ai.vercel.app](https://mukunda-ai.vercel.app) &bull; Las Vegas, NV

<br/>

![Profile Views](https://komarev.com/ghpvc/?username=MukundaKatta&color=D4A853&style=flat-square&label=Profile+Views)

</div>
