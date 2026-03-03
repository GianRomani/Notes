Created: 2026-03-03 10:16
#quicknote

**Kahneman-Tversky Optimization (KTO)** applies behavioural economics — specifically prospect theory's loss aversion — to LLM alignment. Unlike [[DPO - Direct Preference Optimization]] which requires paired preferences (A > B), KTO operates on simple binary desirable/undesirable labels, making it far more data-efficient and practical for real-world feedback. Introduced by Ethayarajh et al. (2024), KTO matches or exceeds preference-based methods at 1B–30B parameter scales. Part of the [[LLM Training and Alignment Evolution]].

- **Loss aversion principle:** Humans overweight losses relative to gains ($\lambda \approx 1.5$–$2.5$). KTO translates this into the **Human-Aware Loss Objective (HALO)**: undesirable outputs are penalised much more heavily than desirable outputs are rewarded
- **No paired preferences needed:** Only requires binary labels (good/bad), which are far more abundant than paired comparisons — every company has customer interaction data naturally marked this way
- **Performance:** Matches or exceeds DPO and IPO on alignment benchmarks across multiple model scales
- **When to use KTO:** When you have abundant binary feedback but scarce preference pairs, when scaling alignment without expensive annotation, or when diverse feedback sources (logs, ratings) are available

| Aspect | DPO | KTO |
|--------|-----|-----|
| **Input** | Paired preferences (A > B) | Binary labels (good/bad) |
| **Foundation** | Bradley-Terry model | Prospect theory |
| **Data needs** | Preference pairs | Any labelled data |

## Resources

1. [Ethayarajh et al. 2024 — KTO Paper](https://arxiv.org/abs/2402.01306)
2. [Contextual AI — KTO Overview](https://contextual.ai/better-cheaper-faster-llm-alignment-with-kto/)

#### Tags
#kto #alignment #llm #fine_tuning #training
