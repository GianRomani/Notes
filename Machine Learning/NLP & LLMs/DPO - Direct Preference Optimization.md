Created: 2026-03-03 10:15
#quicknote

**Direct Preference Optimization (DPO)** collapses the three-stage [[RLHF - Reinforcement Learning from Human Feedback]] pipeline into a single supervised learning step by deriving a closed-form solution for the optimal policy directly from preference data. Introduced by Rafailov et al. (2023), DPO's key insight is that the language model itself is "secretly a reward model" — the optimal policy implicitly encodes the reward function, eliminating the need for explicit reward model training and PPO. By 2024, DPO became the practical default for commercial LLM alignment (used in Llama 3 Instruct, Claude, Gemini). Part of the [[LLM Training and Alignment Evolution]].

- **How it works:** Given preference pairs $(x, y_w, y_l)$, DPO optimises a binary cross-entropy loss that increases the relative log-probability of the preferred response $y_w$ over the rejected $y_l$, with a KL constraint to the reference policy. The intractable partition function cancels out during derivation, making the loss tractable
- **Implicit reward:** The policy parameterises an implicit reward $r(x,y) = \beta \log \frac{\pi_\theta(y|x)}{\pi_{ref}(y|x)}$ — no separate reward model needed
- **Advantages over RLHF:** Single training stage, no PPO instability, no sampling during training, dramatically lower computational cost, matches or exceeds RLHF on sentiment control, summarisation, and dialogue benchmarks
- **Limitations:** Prone to overconfidence with extended training (implicit reward gap grows unboundedly), sensitive to label noise, implicit reward model may not generalise well beyond the preference data distribution

## Key Variants

- **IPO (Identity Preference Optimization)** — regularised objective that prevents overconfidence; bounded optimisation
- **cDPO (Conservative DPO)** — handles annotation noise through conservative smoothing
- **rDPO (Robust DPO)** — minimises impact of noisy preference labels specifically
- **Margin Adaptive DPO** — leverages a reward model for granular control of preference margins

## Resources

1. [Rafailov et al. 2023 — DPO Paper](https://arxiv.org/abs/2305.18290)
2. [DPO Variants Analysis](https://arxiv.org/html/2404.14723v2)
3. [Cameron Wolfe — DPO Explained](https://cameronrwolfe.substack.com/p/direct-preference-optimization)

#### Tags
#dpo #alignment #llm #fine_tuning #training
