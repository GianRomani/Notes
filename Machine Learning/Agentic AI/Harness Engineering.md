Created: 2026-06-02 09:00
#note

**Harness Engineering** (also referred to as building an **agent harness**) is the practice of optimising the scaffolding that surrounds a large language model so that an agent processes a task and returns the best possible response, without changing the underlying model. It is best captured by the equation popularised by Birgitta Böckeler: `agent = model + harness`. Where [[AI Agents|prompt engineering]] defined how one interacts with a model and [[Context Constraints for AI Agents|context engineering]] defined how one fills the context window, harness engineering concerns the systems, tooling, and methodology built around the model. It rose to prominence in early 2026 as practitioners observed that the difference between a mediocre and an excellent agent increasingly lies in the harness rather than in the choice of frontier model.

This note is the hub for the topic. Specific aspects are developed in their own notes: [[Building an Agent Harness from Scratch]] (the practical bootstrapping method and the harness-versus-framework distinction), the [[Research-Plan-Implement Loop]] and its [[Plan Annotation Cycle]] (the core workflow), [[Atelier (Agent Harness)|Atelier]] (a concrete skill-based harness), [[Harness Middleware Techniques]] (transferable engineering techniques), and the [[Managed Agent Harness (Bedrock AgentCore)|Managed Agent Harness]] (productised deployment).

## The Lineage: Prompt, Context, Harness

The discipline emerged as a natural progression in how builders extract value from language models. **Prompt engineering** entered the mainstream with the launch of ChatGPT in late 2022, defining the craft of phrasing requests effectively. **Context engineering** came to the fore in 2025, as builders sought to cram the maximum useful information into the prompt while respecting context limits. **Harness engineering** became the prominent topic of 2026, shifting attention from the contents of a single prompt to the entire apparatus that mediates between a user request and the model's response.

The central insight is economic and architectural: the gap between frontier models such as Claude, Gemini, and GPT shrinks with every release, so *which* model is used matters less than *how* it is used. Agent builders can therefore stand on the shoulders of frontier labs and produce better results by engineering the harness, rather than passively waiting for the next model release to improve quality.

## Definitions and Goals

Two complementary definitions are worth recording. **Mitchell Hashimoto**, who named the practice in February 2026, offers a *reactive* definition: harness engineering is the idea that any time an agent makes a mistake, one takes the time to engineer a solution so the agent never makes that mistake again. **Martin C. Richards** generalises this into a *proactive* definition: a harness is a set of skills, workflows, and methodology that teaches the agent how the engineer thinks and builds. Models are unpredictable by nature, and that cannot be changed; however, a methodology can be taught that makes success the likely outcome rather than the lucky one.

Böckeler frames the purpose in terms of two goals. A well-built outer harness increases the probability that the agent gets the task right on the first attempt, and it provides a feedback loop that self-corrects as many issues as possible before they ever reach human eyes. LangChain frames the same idea differently: the goal of a harness is to mould the inherently spiky intelligence of a model toward the tasks one cares about.

In his own adoption journey, Hashimoto situates harness engineering as a late stage of maturity, reached only after dropping the chatbot for an agent, reproducing one's own manual work to build expertise, and learning when *not* to reach for an agent. The two practical forms he identifies are better implicit prompting (an `AGENTS.md` whose every line derives from an observed bad behaviour) and actual programmed tools (screenshot scripts, filtered test runners) that let the agent verify itself.

## The Knobs of a Harness

LangChain's experimental work provides the clearest taxonomy of what a harness engineer actually tunes. An agent harness exposes many knobs, including system prompts, tool selection, hooks and middleware, [[Agentic AI Frameworks|skills]], sub-agent delegation, and memory systems. In their study they deliberately compressed the optimisation space to three — the **system prompt**, the **tools** available (frequently delivered through the [[MCP Protocol|Model Context Protocol]]), and the **middleware** (deterministic hooks around the model and tool calls).

The empirical result is the headline argument for the entire discipline: LangChain improved their coding agent from **52.8% to 66.5%** on Terminal Bench 2.0 by tuning only the harness while keeping the model fixed. The specific techniques behind that gain are catalogued in [[Harness Middleware Techniques]].

## The Core Workflow

A striking observation is convergent evolution: multiple practitioners independently arrived at the same pattern, which separates planning from execution and is often abbreviated **RPI (Research → Plan → Implement)**. The full pattern, including why backflow between phases is expected, is developed in [[Research-Plan-Implement Loop]]. Boris Tane's distinctive refinement — making the plan document into shared mutable state that the human corrects through inline notes — is developed in [[Plan Annotation Cycle]]. [[Atelier (Agent Harness)|Atelier]] is a concrete implementation of this workflow as a set of auto-loading skills.

## Harnesses at Scale

Birgitta Böckeler's commentary on OpenAI's write-up extends the concept from individual workflows to large-scale, long-lived codebases. OpenAI's team used "no manually typed code at all" as a forcing function and, after five months, maintained a product exceeding one million lines of code. Their harness mixed deterministic and LLM-based approaches across three categories: **context engineering** (a continuously enhanced in-repository knowledge base plus dynamic context such as observability data); **architectural constraints** (enforced not only by LLM agents but also by deterministic custom linters and structural tests); and **"garbage collection"** (agents that run periodically to find documentation inconsistencies and architectural violations, fighting entropy).

Böckeler draws out several forward-looking hypotheses. Harnesses may become the new **service templates** — golden paths from which teams instantiate new applications. Greater AI autonomy may require *constraining* the runtime, trading some "generate anything" flexibility for enforced architectural patterns, which may in turn push the industry toward a **convergence on fewer, more "AI-friendly" tech stacks and topologies**. She also notes a key gap in OpenAI's account: it emphasises internal quality and maintainability but says little about verifying functionality and behaviour — precisely the gap that LangChain's self-verification work targets.

## Significance

Harness engineering reframes agent quality as an engineering discipline rather than a property inherited from the model. Its core claims are that the harness should be engineered with the same care as the software it produces; that the discipline (research, planning, verification) matters more than the specific tools; and that many current harness components are guardrails engineered around *today's* model shortcomings, likely to dissolve as models improve. For practitioners building [[Multi-Agent Systems|agentic systems]], the immediate, transferable lessons are to separate planning from execution, to give agents fast feedback so they can self-verify, to onboard agents with environmental context, and to treat every observed failure as a prompt to improve the harness.

## References
1. [Building an agent harness — Heeki Park (Medium)](https://heeki.medium.com/building-an-agent-harness-31942331d605)
2. [Building Your Own Agent Harness — Martin C. Richards](https://www.martinrichards.me/post/building_your_own_agent_harness/)
3. [Improving Deep Agents with Harness Engineering — LangChain](https://blog.langchain.com/improving-deep-agents-with-harness-engineering/)
4. [Harness Engineering — Birgitta Böckeler, Martin Fowler / Thoughtworks](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html)
5. [My AI Adoption Journey — Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey)
6. [Harness Engineering — OpenAI](https://openai.com/index/harness-engineering/)

## Related Topics

[[Building an Agent Harness from Scratch]], [[Research-Plan-Implement Loop]], [[Plan Annotation Cycle]], [[Atelier (Agent Harness)]], [[Harness Middleware Techniques]], [[Managed Agent Harness (Bedrock AgentCore)]], [[AI Agents]], [[Context Constraints for AI Agents]], [[Agentic AI Frameworks]], [[MCP Protocol]]

#### Tags
#harness_engineering #agentic_ai #ai_agents #context_engineering #prompt_engineering #agent_harness #mlops #llm_tooling
