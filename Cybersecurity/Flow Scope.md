Created: 2026-06-10 10:00
#quicknote

**Flow scope** is the qualifier on [[Taint Analysis]] that determines how far the analysis is allowed to follow data across the codebase. It is the single most important dimension separating a practical tool from a toy, and it is where most tool fine-print, tier limitations, and upsell conditions live.

- **Intra-procedural** — taint tracked only within a single function. Very cheap; nearly useless for real applications because real vulnerabilities cross function boundaries.
- **Intra-file** — taint follows calls across functions but only within one file. Better; catches helper-method laundering within a module.
- **Inter-procedural** — taint follows function and method calls across the codebase in general.
- **Inter-file (cross-file)** — taint follows calls across file and module boundaries. This is the capability that actually matters for any non-trivial application.

Cross-file scope is both the most valuable and the most expensive: the analyser must resolve calls across the entire project. It is also the feature vendors most frequently reserve for paid tiers or that requires a JVM-based runtime with several GB of memory. Reading any tool comparison table through this lens makes limitations immediately legible — most constraints are some flavour of "cross-file taint is missing, gated behind a paid edition, or computationally heavy." See [[Static Analysis Tooling Landscape]] for how specific tools sort into these buckets.

## Resources
1. [Semgrep — Taint Mode Documentation](https://semgrep.dev/docs/writing-rules/data-flow/taint-mode/)

#### Tags
#static_analysis #taint #data_flow #security #sast
