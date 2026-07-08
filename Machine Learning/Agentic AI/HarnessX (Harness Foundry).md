Created: 2026-07-07 10:44
#note

**HarnessX** (`Darwin-Agent/HarnessX`) is an open-source (MIT, Python) *harness foundry*: not one agent, but a factory to build many [[Harness Engineering|agent harnesses]] from reusable parts, pair each with any model, and evolve them through training. Its slogan is *Compose. Adapt. Evolve.* The thesis is the one behind this whole topic: the harness, not just the model, decides agent performance, because the same base model behaves very differently depending on how context is managed, how tools are orchestrated, how errors are recovered, and how evaluation signals feed back. It is the most complete runtime in this vault for the "harness as a searchable, trainable artefact" idea from [[Harness Engineering Resources]].

## The core separation

HarnessX turns `agent = model + harness` into an actual API:

```python
agent = model.agentic(harness)
```

- **`ModelConfig`** -> provider routing, fallback, per-role model assignment (6 backends).
- **`HarnessConfig`** -> the behaviour pipeline: tools, memory, processors, tracing, sandbox.

The claim is that most frameworks already solved model swapping, but behaviour swapping is still expensive. Turning a coding agent into a research agent, or adding memory or guardrails, usually means rewriting the agent. HarnessX makes behaviour a config object. The **X** stands for eXtensible Behaviour Composition: any behaviour is a **Processor**, and processors compose with a `|` pipe over a 9-dimension pipeline. Processors sit in 7 categories:

1. context (system prompt, history, user wrapping)
2. control (13 safety and reliability processors)
3. evaluation (LLM judge, PRM, self-verify)
4. memory (extraction, retrieval, 5 strategies)
5. multi-model routing
6. observability (OpenTelemetry, checkpoints, metrics)
7. tools (skill loader, schema adapter, filters)

Sandboxes are local, Docker, or E2B.

## Two evolution loops

This is what makes HarnessX relevant to the automated-optimisation frontier ([[Meta-Harness - End-to-End Optimization of Model Harnesses]], [[Self-Harness - Harnesses That Improve Themselves]], [[Synthesizing Multi-Agent Harnesses for Vulnerability Discovery|AgentFlow]]):

- **Harness Evolution** -> an in-repo `MetaHarness` reads run trajectories and searches for better processor combinations, prompt strategies and tool configs, without touching the model. This is the [[Self-Harness - Harnesses That Improve Themselves|Self-Harness]] idea as runnable code.
- **Model Evolution** -> every run emits reward-annotated trajectories that feed SFT / RL fine-tuning (via [VERL](https://github.com/volcengine/verl)), improving the model itself.

The two compose: evolve the harness first, then the model on top. Reported GAIA results (v0.1.0 beta, so read them as directional):

| Loop | Model | Result |
|------|-------|--------|
| Harness Evolution | Qwen 3.5 9B | 33% -> 47% over 3 rounds (+14pp, no model change) |
| Harness Evolution | GPT-5 | 62% -> 84% overall |
| Model + Harness co-evolution | Qwen 3.5 9B | 33.97% -> 41.67% (harness) -> 55.77% (model), +64% relative |

The co-evolution number is the one they push: the two loops compound instead of substituting, and a 9B model plus an evolved harness plus RL closes a large part of the gap to a frontier model.

## Where it sits

HarnessX is a runtime you build on, like the ones in [[Harness Engineering Resources]] (Pi, goose, Deep Agents, OpenHarness), but it treats the harness as a first-class, composable and self-evolving object rather than a fixed loop. Its `MetaHarness` plus reward-annotated trajectories make it the practical bridge between the [[Loop Engineering]] discourse (design the loop, and put something inside it that can say no) and the papers on automated harness optimisation. It also ships:

- a CLI (`hx`) and a Lab UI
- an IM gateway (Feishu, Telegram, Slack, Discord, DingTalk)
- Light-Memory, a self-developed file-based memory (time-decay, daily compression, git versioning)
- a roadmap: Bayesian-optimisation search over its ~10^6-config space, and HarnessHUB, a marketplace for publishing `HarnessConfig` bundles

Caveat: at ~30 stars and v0.1.0 beta, the benchmark numbers are self-reported and the meta-optimisation parts (Bayesian search, HarnessHUB) are roadmap, not shipped. Best read as the clearest *architecture* of a composable self-evolving harness, not a battle-tested one. For production maturity, goose is the safer pick.

## References
1. [HarnessX (GitHub)](https://github.com/Darwin-Agent/HarnessX)
2. [Architecture docs (9-dimension pipeline)](https://github.com/Darwin-Agent/HarnessX/blob/main/docs/architecture.md)
3. [GAIA evolver recipe](https://github.com/Darwin-Agent/HarnessX/blob/main/recipe/gaia_evolver)
4. [VERL (RL training backend)](https://github.com/volcengine/verl)

## Related Topics
[[Harness Engineering]], [[Harness Engineering Resources]], [[Self-Harness - Harnesses That Improve Themselves]], [[Meta-Harness - End-to-End Optimization of Model Harnesses]], [[Loop Engineering]], [[Building an Agent Harness from Scratch]], [[Harness Middleware Techniques]], [[Managed Agent Harness (Bedrock AgentCore)]], [[Agentic AI Frameworks]], [[MCP Protocol]]

#### Tags
#harness_engineering #agentic_ai #ai_agents #agent_harness #self_improving_agents #open_source #llm_tooling #mlops
