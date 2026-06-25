Created: 2026-06-10 10:00
#quicknote

**Code navigation graphs** build a resolved call graph and symbol index over a codebase so that an AI coding agent can answer structural questions cheaply and locally: "who calls this function?", "what does it call?", "what breaks if I change it?", "how does a request reach the database?" They sit at Rung 2 of [[The Code-Understanding Ladder]] — structure, not data flow — and are a distinct category from taint-based [[Static Code Analysis]] tools.

Key capabilities and limitations:
- **Can** resolve cross-file relationships: calls → definitions, imports → modules, class inheritance hierarchies.
- **Can** answer navigation and change-impact questions in a single query, substantially reducing an agent's token spend compared to file-by-file grepping.
- **Cannot** track data flow or taint. A call graph records that A *calls* B; it does not record that *tainted data flows* A→B. That requires a taint engine (see [[Taint Analysis]]).

Think of them as AST++ — the same parsing foundation as a syntax tree, plus resolved cross-file edges and a query interface.

**CodeGraph** ([github.com/colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)) is a representative example: local, pre-indexed on tree-sitter + SQLite, exposed over [[MCP]], with tools like `explore`, `callers`, `callees`, `impact`, and `search`. 100% local, no JVM, 20+ languages. Adjacent tools include Sourcegraph's **SCIP** indexers (`scip-java`, `scip-typescript`), GitHub's **stack-graphs**, and **ast-grep**.

For an automated vulnerability fixer, navigation and taint are complementary layers, not competitors: taint analysis identifies the vulnerability path; a navigation graph locates the right fix point and estimates blast radius. Both are needed for high-quality automated remediation.

Practical caveats when adopting a navigation graph: confirm the licence (many are young single-maintainer projects), check indexing cost in short-lived environments that re-index frequently, and verify the tool supports the languages in the codebase.

## Resources
1. [CodeGraph](https://github.com/colbymchenry/codegraph)
2. [SCIP — Sourcegraph](https://docs.sourcegraph.com/code_intelligence/explanations/precise_code_intelligence)

#### Tags
#agentic_ai #static_analysis #code_navigation #llm_tools #mcp
