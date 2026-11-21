Created: 2026-06-09 11:15
#note

A curated landscape of open-source projects, guides, and papers in the field of [[Harness Engineering]]. It complements the conceptual hub and the practical [[Building an Agent Harness from Scratch]] note by pointing to concrete implementations one can read, run, or fork. Entries are grouped by what they *are* — a runtime to build on, a guide to learn from, or a research artefact — because the right resource depends on whether the goal is to ship, to learn, or to study the frontier.

## Harness Runtimes (build on these)

These are working agent runtimes — the substrate a harness rides on. They differ mainly in language, provider coverage, and how opinionated they are.

- **Pi** (`earendil-works/pi`) — a TypeScript monorepo billed explicitly as an "agent harness": its own agent runtime (`pi-agent-core`), a unified multi-provider LLM API (`pi-ai`), a coding-agent CLI, and a terminal UI. Notably it ships *no* built-in permission system — the project tells users to sandbox or containerise it themselves, a deliberate "thin harness" stance. A clean example of a harness with its own loop that treats frontier models as interchangeable providers rather than building on any vendor SDK.
- **goose** (`aaif-goose/goose`, formerly `block/goose`) — a mature, general-purpose agent written in Rust, now stewarded by the Linux Foundation's Agentic AI Foundation. Desktop app, CLI, and embeddable API; 15+ providers; tools via the [[MCP Protocol]]; skills and lifecycle hooks. The most production-hardened of the open runtimes.
- **Deep Agents** (`langchain-ai/deepagents`) — "the batteries-included agent harness," built on LangGraph, aimed at long-running tasks with planning, file tools, shell, and sub-agents out of the box. Includes a *Ralph-mode* example (a hook that forces the agent to keep working on exit). This is the codebase behind LangChain's harness-engineering experiments described in [[Harness Middleware Techniques]].
- **OpenHarness** (`HKUDS/OpenHarness`) — a Python implementation with a query→stream→tool-call loop, 40+ tools, on-demand skill loading, safety permissions, and lifecycle hooks; ships a personal agent ("ohmo") that opens its own pull requests.
- **HarnessX** (`Darwin-Agent/HarnessX`) — a Python "harness foundry" that treats the harness as a composable, first-class object: `agent = model.agentic(harness)`, any behaviour expressed as a `Processor` piped across a 9-dimension pipeline. Unusually it ships *two evolution loops* (harness search + RL model training) out of the box, so it doubles as an entry in the automated-optimisation section below. Developed in its own note: [[HarnessX (Harness Foundry)]].
- **Mecatl** (`stacklok/mecatl`) — an open-source, provider-agnostic agent harness engineered for cloud-native and local workloads on user-controlled infrastructure, exposing a permission-governed loop with durable state over gRPC and HTTP-SSE.
- **Nod** (`n8n-io/nod`) — n8n's open-source personal agent that operates inside its own isolated virtual computer environment on a local workstation, asking for confirmation before acting on external web interfaces.
- **Tau** (`huggingface/tau`) — a minimalist educational agent repository designed to teach the core mechanics of building a coding agent harness from scratch.

## Meta, Memory, and Skill-Based Harnesses

Harnesses expressed as composable skills, persistent memory layers, or tools that *generate* and *audit* harnesses.

- **Atelier** (`martinffx/atelier`) — the skill-based Claude Code harness already covered in [[Atelier (Agent Harness)]].
- **revfactory/harness** — a meta-skill that designs domain-specific agent teams and generates the skills they use; harness-building as a skill rather than a framework.
- **Chachamaru127/claude-code-harness** — a Plan → Work → Review autonomous cycle layered over a coding agent; a concrete instance of the [[Research-Plan-Implement Loop]] expressed as verb-skills.
- **Autoharness** (`tigerless-labs/autoharness`) — a self-learning skill layer that distills reusable skills from real coding sessions, updates them incrementally, and prunes unused skills without requiring background daemons.
- **OpenSpec** (`Fission-AI/OpenSpec`) & **brain.md** (`mindmuxai/brain.md`) — spec-driven development and persistent, zero-dependency file-based project memory layers that give coding agents durable architectural decisions, requirements, and constraints across sessions.
- **Guard Skills & Security Auditors** (`amElnagdy/guard-skills`, `AI-Coding-Shield/ai-coding-shield`, `NVIDIA/SkillSpector`, `trailofbits/claude-code-config`) — quality gates and static security scanners that audit `.agents/` rules, skills, and MCP servers for failure modes and prompt-injection vulnerabilities (see [[Local Coding Agent Runtime Security and Sandboxing]]).
- **Token I/O Compression & Codebase Graphs** (`rtk-ai/rtk`, `headroomlabs-ai/headroom`, `tirth8205/code-review-graph`) — CLI proxies and local AST review graphs that compress tool outputs and scope context retrieval, cutting coding-agent token consumption by 60–95%.

## Guides and Learning Resources

- **Harness Engineering Guide** (`nexu-io/harness-engineering-guide`, harness-guide.com) — an open guide with runnable code covering the agentic loop, tool systems, memory and context, guardrails, sandboxing, sub-agents, and multi-agent orchestration. A good first-principles reference; several of its chapters surface concepts not yet captured in this vault (see "Concepts worth extracting" below).
- **learn-harness-engineering** (`walkinglabs`) and **learn-claude-code** (`shareAI-lab`) — zero-to-one tutorials that build a harness incrementally, each lesson motivated by an observed failure.
- **Awesome lists** — `ai-boost/awesome-harness-engineering`, `walkinglabs/awesome-harness-engineering`, `Picrew/awesome-agent-harness`, and the weekly-ranked `RyanAlberts/best-of-Agent-Harnesses` (100+ harnesses scored). `YennNing/Awesome-Code-as-Agent-Harness-Papers` collects the academic side. GitHub topics [`harness-engineering`] and [`agent-harness`] are the live feed.

## Research: Automated Harness Optimisation

The frontier is treating the harness itself as the object of search, with the model held fixed. A useful way to organise the entries is *who* does the improving: a human, a stronger external agent, or the agent itself. This vault already covers [[Synthesizing Multi-Agent Harnesses for Vulnerability Discovery|AgentFlow]]; its companions:

- **Meta-Harness** (Stanford IRIS Lab; arXiv:2603.28052) — searches over harness *code* with an agentic proposer that reads the source, scores, and full execution traces of all prior candidates. A *stronger external agent* improving a target harness. Developed in its own note: [[Meta-Harness - End-to-End Optimization of Model Harnesses]].
- **Self-Harness** (Shanghai AI Lab; arXiv:2606.09498) — the agent improves *its own* harness with no human and no stronger teacher, via a Weakness Mining -> Proposal -> Validation loop; up to +21.4pp / +138% on Terminal-Bench-2.0 with the model frozen, and the retained edits are model-specific. This is the third paradigm, *self-improvement*, completing the human / external-agent / self triad. Developed in its own note: [[Self-Harness - Harnesses That Improve Themselves]].
- **Agentic Harness Engineering / AHE** (`china-qijizhifeng/agentic-harness-engineering`) — concurrent work on observability-driven *automatic evolution* of a coding-agent harness; reports a frozen, discovered harness that transfers across base models and from Terminal-Bench 2 to SWE-bench-Verified without re-tuning. The transfer result is the interesting claim: a harness as a reusable artefact rather than a per-target build.
- **HarnessX** (`Darwin-Agent/HarnessX`) — the runtime that operationalises the above: an in-repo `MetaHarness` runs the Self-Harness-style self-observation loop, and reward-annotated trajectories feed RL model training, so harness and model can co-evolve. Listed as a runtime above; note at [[HarnessX (Harness Foundry)]].
- **TerminalBench-2**: the long-horizon, dependency-heavy command-line benchmark most of the above optimise against, and the de facto yardstick for coding-harness quality.

## Concepts Worth Extracting

Beyond the named papers, the guides above surface several transferable ideas not yet in this vault — candidates for their own notes: classifier-based permissioning (replacing approval fatigue with a model-based gate), eval-infrastructure noise (resource configuration alone swinging benchmark scores by several points), long-running harness design (context anxiety, self-evaluation bias, a generator-evaluator split), the brain/hands/session decoupling of managed agents, and large parallel agent teams coordinating through git. These extend [[Harness Middleware Techniques]] and the [[Managed Agent Harness (Bedrock AgentCore)]] note.

## References

1. [Pi agent harness (GitHub)](https://github.com/earendil-works/pi)
2. [goose (GitHub)](https://github.com/aaif-goose/goose)
3. [Deep Agents (GitHub)](https://github.com/langchain-ai/deepagents)
4. [OpenHarness (GitHub)](https://github.com/HKUDS/OpenHarness)
5. [HarnessX (GitHub)](https://github.com/Darwin-Agent/HarnessX)
6. [Harness Engineering Guide (GitHub)](https://github.com/nexu-io/harness-engineering-guide)
7. [Meta-Harness (arXiv:2603.28052)](https://arxiv.org/abs/2603.28052)
8. [Self-Harness (arXiv:2606.09498)](https://arxiv.org/abs/2606.09498)
9. [Agentic Harness Engineering (GitHub)](https://github.com/china-qijizhifeng/agentic-harness-engineering)
10. [best-of-Agent-Harnesses (GitHub)](https://github.com/RyanAlberts/best-of-Agent-Harnesses)
11. [Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents — A Source-Code Study of Eleven Systems (arXiv:2609.00006)](https://arxiv.org/abs/2609.00006v1) — _Saved in AI & LLMs (`#ai-agents`, `#harness`, `#paper`)_
12. [stacklok/mecatl: Open-Source Provider-Agnostic Agent Harness (GitHub)](https://github.com/stacklok/mecatl) — _Saved in Cybersecurity (`#ai-agents`, `#harness`, `#llmsecurity`)_
13. [tigerless-labs/autoharness: Self-Learning Skill Layer for Coding Agents (GitHub)](https://github.com/tigerless-labs/autoharness) — _Saved in AI & LLMs (`#harness`, `#ai-agents`, `#github`)_
14. [n8n-io/nod: Open-Source Personal Agent With Its Own Computer (GitHub)](https://github.com/n8n-io/nod) — _Saved in AI & LLMs (`#ai-agents`, `#github`)_
15. [mindmuxai/brain.md: Persistent File-Based Memory Layer for Coding Agents (GitHub)](https://github.com/mindmuxai/brain.md) — _Saved in AI & LLMs (`#ai-agents`, `#github`)_
16. [Fission-AI/OpenSpec: Spec-Driven Development for AI Coding Assistants (GitHub)](https://github.com/Fission-AI/OpenSpec) — _Saved in AI & LLMs (`#ai-agents`)_

## Related Topics

[[Harness Engineering]], [[Agentic SDLC]], [[Local Coding Agent Runtime Security and Sandboxing]], [[Building an Agent Harness from Scratch]], [[Harness Middleware Techniques]], [[Atelier (Agent Harness)]], [[HarnessX (Harness Foundry)]], [[Managed Agent Harness (Bedrock AgentCore)]], [[Research-Plan-Implement Loop]], [[Loop Engineering]], [[Synthesizing Multi-Agent Harnesses for Vulnerability Discovery]], [[Meta-Harness - End-to-End Optimization of Model Harnesses]], [[Self-Harness - Harnesses That Improve Themselves]], [[Agentic AI Frameworks]], [[MCP Protocol]]

#### Tags
#harness_engineering #agentic_ai #ai_agents #agent_harness #open_source #llm_tooling #mlops
