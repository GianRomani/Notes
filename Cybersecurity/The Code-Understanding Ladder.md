Created: 2026-06-10 10:00
#note

Every static analysis tool sits on a **rung** describing how deeply it understands code. Lower rungs are fast and shallow; higher rungs are powerful but computationally expensive. Most debates about tool quality — capability, false-positive rates, scope limitations — are really arguments about which rung a tool occupies and whether that rung is sufficient for the task at hand.

| Rung | Representation | What it knows | Examples |
|------|---------------|---------------|---------|
| 0 | **Text** | Nothing about structure or meaning | `grep` |
| 1 | **AST** (abstract syntax tree) | Grammatical structure of code | tree-sitter |
| 2 | **Call graph** | Who calls whom, across files | SCIP indexers, CodeGraph |
| 3 | **CFG** (control-flow graph) | Possible execution order within functions | Foundation inside larger engines |
| 4 | **DFG** (data-flow graph) | Where each value originates and propagates | Dataflow analysers |
| 5 | **Taint** | Which untrusted values reach dangerous sinks | SAST engines (Semgrep Pro, Pysa) |
| 6 | **CPG** (code property graph) | AST + CFG + DFG unified in a queryable graph | Joern, CodeQL |

## Rung by rung

**Rung 0 — Text.** Treat source code as a character sequence. Instant and knows nothing. `grep` and basic pattern matchers live here.

**Rung 1 — AST.** Parse code into its grammatical structure: this is a function, this is a string concatenation. tree-sitter is the dominant fast parser. The AST reveals *what the code is*, not where data flows. Structural patterns and syntax errors are visible; data movement is not.

**Rung 2 — Call graph.** A directed graph of function call relationships resolved across files. Answers navigation questions ("what calls this?", "what does this call?") and impact questions ("what breaks if I change this function?"). Critically, a call graph records that A *calls* B; it does not record that *tainted data flows* A→B. Structure, not data. See [[Code Navigation Graphs]].

**Rung 3 — CFG.** The order in which statements can execute: branches, loops, early returns within a function. The foundation for reasoning about which execution paths are possible.

**Rung 4 — DFG.** Tracks definitions and uses of values — where each value originates and every place it reaches. At this rung, "the value in `query` descends from `username`" becomes provable. This is what people usually mean by *dataflow analysis*.

**Rung 5 — Taint analysis.** The security overlay on the DFG: of all data flows, identify specifically those from untrusted sources to dangerous sinks, accounting for sanitisation along the path. This is what characterises vulnerabilities. See [[Taint Analysis]].

**Rung 6 — CPG.** Merges AST, CFG, and DFG into a single graph queryable with a traversal language (CodeQL's QL, Joern's Gremlin-like DSL). Maximum expressiveness — custom queries can hunt for novel vulnerability patterns. Maximum resource cost: typically JVM-based, several GB of RAM.

## Why the rung determines fix quality

A fixer operating at Rung 1 must reconstruct data-flow reasoning from raw syntax — inherently fragile and error-prone. Moving to Rung 5 provides real source→sink paths. Every rung up adds memory, compute, and often a heavier runtime. The right rung depends on the task: navigation agents benefit from Rung 2; taint-based vulnerability detection needs at least Rung 5. See [[Choosing a Static Analysis Tool]] for how to trade off depth against deployment constraints.

## References
1. [Yamaguchi et al. — Modeling and Discovering Vulnerabilities with Code Property Graphs (2014)](https://ieeexplore.ieee.org/document/6956589)
2. [CodeQL documentation](https://codeql.github.com/docs/)

#### Tags
#static_analysis #sast #data_flow #taint #code_understanding #security
