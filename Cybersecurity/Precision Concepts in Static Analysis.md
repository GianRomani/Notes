Created: 2026-06-10 10:00
#quicknote

Precision in static analysis is about reducing false positives — findings that flag safe code as vulnerable. Several distinct dimensions contribute to precision; understanding them makes tool capability claims and comparisons legible.

- **Points-to / alias analysis** — determines which references may point to the same underlying object. If `a` and `b` might alias, tainting `a` may require propagating taint to `b`. Getting alias analysis right is the foundation under any serious [[Taint Analysis]] engine; academic-grade alias analysis is expensive and is what separates high-precision tools from shallow pattern matchers.
- **Context-sensitivity** — distinguishes different *call sites* of the same function. Without it, the analyser merges what happens when module A calls a helper with what happens when module B calls it, producing spurious flows between unrelated paths.
- **Path-sensitivity** — distinguishes different *branches* of the control flow, reasoning about the `if` path and the `else` path separately. Prevents false positives from flows that can only occur in impossible combinations of conditions.
- **Field-sensitivity** — distinguishes different *fields of an object*, so tainting `obj.x` does not automatically taint `obj.y`. Critical for precision in object-heavy codebases.

A tool advertised as "context-, path-, and field-sensitive" is claiming high precision across all three dimensions. Each adds computational cost.

Two further distinctions apply across the category:
- **Queryable graph vs. rule-based** — CPG engines like CodeQL and Joern expose a query language over the underlying graph, enabling custom queries for novel vulnerability patterns. Rule-based scanners like Semgrep emit findings based on authored rules; flexible and fast, but not the same as free graph traversal.
- **Turnkey vs. library** — a turnkey tool runs and emits findings; a library is a framework requiring significant engineering effort to productise. Capable-but-library tools frequently lose to weaker-but-ready ones in practice. See [[Choosing a Static Analysis Tool]].

## Resources
1. [Reps et al. — Precise Interprocedural Dataflow Analysis via Graph Reachability (1995)](https://dl.acm.org/doi/10.1145/199448.199462)

#### Tags
#static_analysis #precision #data_flow #sast #security
