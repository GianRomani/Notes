Created: 2026-06-10 10:00
#note

The static analysis tool market is large but maps cleanly onto a handful of buckets, defined by where a tool sits on [[The Code-Understanding Ladder]] and the [[Flow Scope]] it achieves. Understanding the buckets prevents redundant purchasing and makes capability claims legible.

## Bucket 1 — Syntax-only parsers (Rung 1)

**tree-sitter** is the dominant tool: fast, minimal, supports over 100 languages, no runtime dependencies, clean AST output. No data flow, no taint. Frequently used as the parsing foundation that heavier tools build on. The right default when structural queries are sufficient and no security findings are needed.

## Bucket 2 — Code navigation graphs (Rung 2)

Call-graph and symbol indexers (see [[Code Navigation Graphs]]). They resolve who-calls-whom across files and answer structural impact questions. Useful for navigation and change-impact analysis; not a substitute for taint.

## Bucket 3 — Heavy CPG engines (Rung 6)

**Joern** and **CodeQL** represent the state of the art in open-licensed analysis: full code property graphs, best-in-class cross-file taint, queryable with a traversal DSL. The price is operational — both are JVM-based, requiring hundreds of MB to several GB of memory. CodeQL's engine also carries commercial-use licence restrictions for certain deployment modes.

## Bucket 4 — Lightweight OSS scanners (Rungs 4–5, limited scope)

**Semgrep** and its open fork **Opengrep** are rule-based, lightweight (~100 MB, no JVM), and support many languages. The catch is [[Flow Scope]]: the free open-source edition offers intra-file cross-function taint; **cross-file taint requires the paid tier**. Fast, tunable, and excellent as a pattern scanner and "second opinion" layer.

## Bucket 5 — Promising newcomers

**YASA** (open-sourced by Ant Group) achieves context-, path-, and field-sensitive taint for Java and JavaScript at no licence cost. Typical newcomer trade-offs apply: narrow language coverage (no C#, limited Python), small community, unproven production maturity.

## Bucket 6 — Single-language / niche analysers

A long tail of powerful but language-locked tools: Java (Infer, Tai-e, Soot, Doop, FlowDroid), Python (Pysa), C/C++ (Phasar), Rust (MIRAI), Ruby/Rails (Brakeman). Rejected on multi-language requirements regardless of per-language quality.

## Bucket 7 — Commercial heavyweights

**Snyk Code, Fortify, Coverity, Checkmarx, Veracode, Bearer Pro, Semgrep Pro**. Full cross-file taint across many languages with enterprise support. Trade-offs: cost, SaaS or heavy on-prem models, and significant redundancy with each other — owning one capable commercial scanner usually makes justifying a second difficult to argue.

## How to read any tool comparison

For each tool, ask three questions:
1. **Capability** — what rung and scope does it reach?
2. **Fit** — does it cover the target languages?
3. **Cost** — runtime footprint, licence, and engineering effort to productise?

No tool maximises all three. Every real choice gives one up. A common pragmatic outcome is stacking complementary layers: a navigation indexer (Rung 2) + a focused taint engine (Rung 5) + a lightweight rule scanner as a second opinion, approximating the capability of a heavy CPG engine at lower footprint and cost. See [[Choosing a Static Analysis Tool]].

## References
1. [Joern](https://joern.io/)
2. [CodeQL](https://codeql.github.com/)
3. [Semgrep](https://semgrep.dev/)
4. [YASA](https://github.com/alibaba/ant-application-security-testing-benchmark)

#### Tags
#static_analysis #sast #tooling #security #code_property_graph
