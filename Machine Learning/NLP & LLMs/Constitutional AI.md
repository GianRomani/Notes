Created: 2026-03-03 10:18
#quicknote

**Constitutional AI (CAI)** is Anthropic's approach to alignment that replaces human feedback with AI-generated feedback guided by explicit principles — a "constitution." Instead of relying on human annotators for preference data, CAI has the model critique and revise its own outputs against written rules, then trains a preference model from AI evaluations. This enables **Reinforcement Learning from AI Feedback (RLAIF)**, dramatically reducing the cost and scaling constraints of [[RLHF - Reinforcement Learning from Human Feedback]]. Part of the [[LLM Training and Alignment Evolution]].

- **Phase 1 — Supervised self-critique:** The model generates responses, critiques them against constitutional principles (e.g., "be helpful," "avoid harm," "be honest"), and produces revised versions. The model is fine-tuned on these improved outputs
- **Phase 2 — RLAIF:** The model evaluates pairs of its own outputs based on constitutional adherence, generating preference data. A preference model is trained on these AI judgements and used as the reward signal for PPO training
- **Key advantage:** Alignment becomes transparent (principles are explicit, auditable) and scalable (AI feedback is cheap). Achieves 88% harmless rate vs RLHF's 76% without sacrificing helpfulness
- **Collective Constitutional AI (2024)** — sources principles from diverse public stakeholders rather than a single design team, reducing bias across nine social dimensions while maintaining performance
- **Public Constitutional AI (2025)** — renders AI principles transparent and supports democratic legitimacy in deployment

## Connection to Other Methods

CAI is complementary to other techniques: it can replace the human annotation step in [[RLHF - Reinforcement Learning from Human Feedback]], the preference data collection for [[DPO - Direct Preference Optimization]], or serve as a safety layer on top of [[RLVF - Reinforcement Learning from Verifiable Feedback]]. The principles-based approach also connects to [[Synthetic Data for LLM Training]] — constitutional critique generates synthetic preference data.

## Resources

1. [Bai et al. 2022 — Constitutional AI](https://arxiv.org/abs/2212.08073)
2. [Anthropic — Constitutional AI Research](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback)
3. [Collective Constitutional AI — Anthropic](https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input)
4. [C3AI Framework (2025)](https://arxiv.org/pdf/2502.15861)

#### Tags
#constitutional_ai #rlaif #alignment #llm #aisecurity #training
