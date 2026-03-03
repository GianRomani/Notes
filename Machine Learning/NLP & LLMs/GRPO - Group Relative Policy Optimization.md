Created: 2026-03-03 10:17
#quicknote

**Group Relative Policy Optimization (GRPO)** is a reinforcement learning algorithm that eliminates the critic model entirely by estimating advantages from the statistics of a group of sampled outputs. Introduced in DeepSeek-Math (2024) and used as the core RL algorithm in DeepSeek-R1 (2025), GRPO reduces memory requirements by ~50% compared to PPO, making RL training practical even on consumer hardware (1B models trainable with 16GB VRAM). It is the algorithm of choice for [[RLVF - Reinforcement Learning from Verifiable Feedback]] pipelines. Part of the [[LLM Training and Alignment Evolution]].

- **How it works:** For each prompt, sample $G$ outputs from the current policy. Evaluate each using a reward function (learned RM or verifier). Compute advantage as $\hat{A}_i = (r_i - \mu_G) / \sigma_G$ where $\mu_G$ and $\sigma_G$ are the group mean and standard deviation. Apply PPO-style clipped policy gradient with these group-relative advantages
- **No critic model:** Traditional PPO trains a value function (critic) of the same size as the policy. GRPO replaces this with simple group statistics → ~50% memory reduction
- **KL penalty:** Added directly to the loss function rather than subtracted from the reward, providing more stable optimisation
- **DeepSeek-R1 results:** R1-Zero (no SFT, pure RL with GRPO) achieved 71% on AIME 2024 (from 15.6%), with 86.7% under majority voting, matching OpenAI o1

## Connection to RLVF

GRPO and RLVF are distinct but complementary: GRPO is the **optimisation algorithm** (how to update the policy), RLVF is the **reward setting** (where rewards come from verifiers). GRPO can work with learned reward models too, but its efficiency shines in RLVF settings where the verifier is cheap to evaluate.

## Emerging Variants (2025)

- **G2RPO-A** — Guided GRPO with Adaptive Guidance
- **NGRPO** — Negative-enhanced GRPO for better rejection sampling
- **GiGPO** — Group-in-Group Policy Optimization for multi-turn agent training

## Resources

1. [DeepSeek-Math — arXiv](https://arxiv.org/abs/2402.03300)
2. [DeepSeek-R1 — arXiv](https://arxiv.org/abs/2501.12948)
3. [Cameron Wolfe — GRPO Explained](https://cameronrwolfe.substack.com/p/grpo)
4. [GRPO Breakdown — Ebrahim Pichka](https://epichka.com/blog/2025/grpo/)

#### Tags
#grpo #reinforcement_learning #llm #alignment #reasoning #training
