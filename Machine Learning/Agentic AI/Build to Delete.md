Created: 2026-06-10 20:00
#note

The philosophy of **Build to Delete** (also phrased as "write code that is easy to delete, not easy to extend") is a paradigm in software engineering that prioritizes ephemerality, modularity, and simplicity over long-term permanence and complex abstraction. While it has roots in traditional software architecture, it has recently emerged as a core design principle for building agentic harnesses and AI systems.

## The Traditional Software Philosophy
First popularized by programmer **Tef** in his 2016 essay, the core idea is that software engineering's biggest challenge is not writing code, but modifying and deleting it when requirements change.

* **Avoid Premature Abstractions:** Traditional paradigms encourage building highly extensible, abstract systems. However, guessing future requirements leads to bloated, tightly-coupled codebases.
* **Isolation over Extensibility:** If code is split into self-contained, decoupled modules with simple interfaces, deleting or replacing them is trivial.
* **Copy-Paste vs. Bad Abstractions:** Under this model, copying and pasting a block of code is often preferred over creating a shared helper function that couples unrelated features together. Duplicated code is easy to delete; a shared helper with many dependencies is not.

## The Agentic Harness Perspective
In the context of AI agents (such as **OpenClaw**, powered by Mario Zechner's **Pi framework**), **Build to Delete** is a hedge against the rapid evolution of Large Language Models (LLMs).

### Harness Decay
An **Agentic Harness** is the custom software wrapper (prompts, parsers, routing logic, and tools) built around an LLM to make it execute tasks. 
* **The Volatility Risk:** Because underlying models improve exponentially, the complex scaffolding built today to patch current model limitations (such as manual state machines, intricate prompt chains, or strict format validators) will become redundant tomorrow.
* **The Solution:** Treat all harness code as temporary. Keep orchestration logic thin and modular so that when a model natively supports a capability (like structured JSON outputs or multi-step reasoning), the custom code can be easily pruned.

### Negative Space Architecture
Introduced in the design of the **Pi Agent**, this concept argues that an agent framework should be defined by what it excludes rather than what it includes.
* **Minimalist Core:** Monolithic agent frameworks suffer from extreme bloat by bundling pre-configured sub-agents, model contexts, and complex toolsets.
* **Native Extensions:** The Pi Framework keeps the core engine tiny. Instead of using complex static configuration files, developers write custom hooks and skills in **native TypeScript**. This makes it easy to splice logic directly into the agent’s execution loop and, crucially, to delete or refactor that logic as the agent evolves.

## Key Design Patterns for Disposability
To implement the **Build to Delete** mindset:

| Pattern | Traditional Approach | "Build to Delete" Approach |
| :--- | :--- | :--- |
| **Code Structure** | Layered by technology (all controllers, all views, all types grouped). | Grouped by feature (a single folder containing everything for a feature). |
| **Abstractions** | Heavy inheritance, interfaces, and DRY (Don't Repeat Yourself). | WET (Write Everything Twice) before abstracting. Single-purpose utilities. |
| **AI Orchestration** | Rigid, multi-step agent graphs and state machines. | Dynamic prompts, direct API calls, and native TypeScript hooks. |

> [!TIP]
> **Rule of Thumb:** When building helper tools or agent prompts, ask yourself: "If the next LLM release solves this natively, how many lines of code must be touched to remove this workaround?" If the answer is more than a few, the code should be refactored for disposability.

## Related Notes
* [[Negative Space Architecture]]
* [[Negative Space and Disposability across Domains]]

#### Tags
#agentic_ai #software_design #architecture
