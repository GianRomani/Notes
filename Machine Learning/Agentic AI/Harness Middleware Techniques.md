Created: 2026-06-02 09:13
#note

This note collects the concrete, transferable **middleware and prompting techniques** that LangChain derived from trace-driven experiments on their `deepagents-cli` coding agent. The techniques are the practical substance of [[Harness Engineering]]: by tuning only the harness and keeping the model fixed at `gpt-5.2-codex`, they improved the agent from **52.8% to 66.5%** on Terminal Bench 2.0 (a 13.7-point gain). "Middleware" is LangChain's term for deterministic hooks that wrap the model and tool calls within the agent loop.

## The Three Tunable Knobs

LangChain deliberately compressed the large optimisation space of an agent harness down to three knobs: the **system prompt**, the **tools** available (often delivered via the [[MCP Protocol]]), and the **middleware** (hooks around model and tool calls). The improvement process itself was made repeatable as a *trace analyzer skill* that fetches traces from observability tooling, spawns parallel error-analysis agents, and aggregates findings into targeted harness changes — a procedure analogous to boosting, which focuses on mistakes from previous runs. [[LLM Observability|Tracing]] thus acts as the feedback signal for the whole loop.

## Build-and-Self-Verify

The most impactful technique addressed the most common failure: an agent writing a solution, re-reading its own code, confirming it looked acceptable, and stopping. The fix paired system-prompt guidance — plan, build with tests, **verify against the task specification rather than against one's own code**, then fix — with a deterministic `PreCompletionChecklistMiddleware` that intercepts the agent before it exits and forces a verification pass. This relates to the "Ralph Wiggum loop", where a hook compels the agent to keep executing on exit.

## Environment Context Injection

A second family of techniques gives the agent context about its environment so it spends less effort on error-prone discovery. A `LocalContextMiddleware` runs on start-up to map the working directory and locate available tooling, onboarding the agent into its environment. Prompting that stresses the work will be measured against programmatic tests teaches the agent to write testable code and to follow file paths exactly. Injected **time-budget** warnings nudge the agent to stop working and shift to verification, compensating for the fact that agents estimate time poorly.

## Loop Detection

Agents can become myopic once committed to a plan, producing "doom loops" of small variations on the same broken approach (10+ times in some traces). A `LoopDetectionMiddleware` tracks per-file edit counts and, after N edits to the same file, injects a prompt suggesting the agent reconsider its approach. This is explicitly a guardrail engineered around a current model weakness, expected to become unnecessary as models improve.

## Reasoning-Budget Allocation

Reasoning compute is itself a tunable resource. LangChain adopted a **"reasoning sandwich"**: high reasoning for planning, lower reasoning for the bulk of implementation, and high reasoning again for verification. Counter-intuitively, running everything at maximum reasoning scored *worse* (53.9% versus 63.6% at "high") because of timeouts. In a multi-model harness this could be realised by using a larger model for planning and handing off to a smaller model for implementation.

## General Principles

LangChain distilled five takeaways: perform **context engineering on behalf of the agent** (onboarding it with directory structure, tooling, and problem-solving strategies); **help the agent self-verify** its work, since models are biased toward their first plausible solution; use **tracing as a feedback signal**; **detect and fix bad patterns** in the short term while expecting such guardrails to dissolve as models improve; and **tailor harnesses to specific models**, since Codex and Claude require different prompting (a Claude Opus 4.6 run scored 59.6% on an earlier harness that had not been iterated for it).

## References
1. [Improving Deep Agents with Harness Engineering — LangChain](https://blog.langchain.com/improving-deep-agents-with-harness-engineering/)

#### Tags
#harness_engineering #agentic_ai #ai_agents #middleware #llm_evaluation #context_engineering #mlops
