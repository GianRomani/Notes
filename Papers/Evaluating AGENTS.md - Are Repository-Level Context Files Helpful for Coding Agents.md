Created: 2026-02-24 15:00
#paper

Gloaguen et al. (ETH Zurich, 2026) investigate whether AGENTS.md-style context files actually help coding agents solve real tasks. The answer is surprising: across multiple agents and LLMs, context files tend to **reduce task success rates** while **increasing inference cost by over 20%**. This contradicts the common practice of adding repo-level context files, which is strongly encouraged by agent developers (OpenAI Codex, Claude Code, Cursor, etc.).

**Note:** this directly contrasts with Lulla et al. (2026) who found AGENTS.md reduces runtime by ~29% and output tokens by ~17%. The difference likely comes from what is measured -> Lulla et al. measure efficiency (time, tokens), Gloaguen et al. measure task success rate. An agent can be faster and cheaper while solving fewer tasks.

## Main idea

The paper asks: do repository-level context files (AGENTS.md, CLAUDE.md, CODEX.md, etc.) actually improve coding agent performance on real software engineering tasks?

Experimental setup: same task, same agent, vary only whether a context file is present. Three conditions:
- No context file (baseline)
- LLM-generated context file (following agent-developer recommendations)
- Developer-written context file (committed to the repo by humans)

Two benchmarks:
- **SWE-bench Lite** — 300 tasks from popular open-source repos, with LLM-generated context files added
- **AGENTbench** (new) — 138 instances from 12 Python repos that already have developer-written context files, derived from 5,694 real GitHub PRs

Agents tested: Claude Code (Sonnet 4.5), Codex (GPT-5.2, GPT-5.1 Mini), Qwen Code (Qwen3-30B-Coder).

## Results

Context files hurt more than they help:

| Benchmark | No context | LLM-generated | Developer-written |
|-----------|-----------|---------------|-------------------|
| SWE-bench Lite (GPT-4o) | 33.5% | 32.0% | 29.6% |
| AGENTbench (GPT-4o) | 32.5% | — | 24.2% |

- LLM-generated context files reduce success by 0.5% (SWE-bench) to 2% (AGENTbench) on average
- Developer-written context files improve success by ~4% on AGENTbench compared to LLM-generated, but still worse than no context
- Inference cost increases by >20% across both benchmarks
- Reasoning tokens increase by 22% (GPT-5.2) and 14% (GPT-5.1 Mini) on SWE-bench Lite

### Why it happens

Agents do follow the instructions in context files (e.g., `uv` usage jumps from <0.01 to 1.6 times per instance when mentioned). The problem is not instruction-following, it is that **the extra instructions make the task harder**.

When given context files, agents:
- Explore more files
- Run more tests
- Call more tools
- Take more steps before interacting with the files that actually need fixing

-> thoroughness increases but problem-solving is delayed. The agent gets distracted by the additional requirements.

**One exception:** when documentation is removed from the repo, LLM-generated context files perform better than developer-written ones -> context files help most when they replace information that is hard to find in the codebase itself.

## Ideas for future works

- **Minimal context files** — the paper suggests human-written context files should describe only minimal requirements. What is the optimal level of detail? Too much hurts, too little is useless
- **Task-adaptive context** — instead of a static context file, generate context dynamically based on the specific task. This connects to [[RAG]] and [[AI Agents]] planning strategies
- **Context file quality metrics** — how do you measure whether a context file is helping or hurting before running expensive benchmarks?
- **Reconciling with Lulla et al.** — one paper says context files improve efficiency, the other says they reduce success. A study measuring both simultaneously on the same tasks would be valuable
- **Impact on different task types** — bug-fixing vs feature addition vs refactoring may benefit differently from context files. The paper hints at this but does not fully explore it
- **Agent architectures that filter context** — instead of prepending everything, agents could selectively attend to relevant parts of the context file based on the task

Limitations:
- Limited agent/model coverage — only 4 agents tested, results may differ with other architectures
- AGENTbench is Python-only (12 repos) -> may not generalise to other languages or larger repos
- The study does not separate the effect of different types of instructions in context files (style rules vs tool preferences vs architecture docs)
- No analysis of context file length vs performance -> is there a sweet spot?

## In deep

AGENTbench construction: sourced from repos that already have developer-committed context files. 5,694 real GitHub PRs filtered down to 138 tasks across 12 repos. Tasks include both bug fixes and feature additions -> more representative than synthetic benchmarks.

The behavioural analysis is the most interesting part. Agents become more "thorough" with context files (more file exploration, more tool calls, more tests) but this does not translate into solving more tasks. The extra exploration delays the agent from getting to the actual fix. This suggests that context files may be introducing a form of **distraction** -> the agent tries to satisfy all the requirements in the context file rather than focusing on the task.

The contrast with Lulla et al. is worth unpacking. Their study (10 repos, 124 PRs) found AGENTS.md reduces runtime by 28.64% and output tokens by 16.58%. But they measured efficiency, not correctness. An agent that follows instructions and finishes faster is not necessarily an agent that produces correct solutions. The two papers together suggest context files make agents **faster but less accurate** -> they constrain the search space (faster convergence) but sometimes constrain it in the wrong direction (missing the actual fix).

**Note:** this has practical implications for how we write CLAUDE.md and similar files. The takeaway is: keep it minimal, focus on genuinely missing knowledge (things hard to find in the code itself), and avoid prescriptive rules that constrain the agent's problem-solving. As the authors put it: "the best documentation for an AI agent is code that does not need one."

## References
1. [Paper](https://arxiv.org/abs/2602.11988)
2. [Lulla et al. — On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents](https://arxiv.org/abs/2601.20404)
3. [SWE-bench](https://www.swebench.com/)

## Code
1. [AGENTbench dataset and evaluation](https://arxiv.org/abs/2602.11988)

#### Tags
#agentic_ai #agents #evaluation #benchmark #coding_agents #llm #software_engineering
