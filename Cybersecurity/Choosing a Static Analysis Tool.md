Created: 2026-06-10 10:00
#quicknote

Raw capability is rarely the deciding factor when selecting a static analysis tool. Three practical constraints prune the candidate list far more aggressively than rung depth does.

- **Runtime footprint** — the most capable engines (Joern, CodeQL) are JVM-based and memory-hungry: hundreds of MB of image, multiple GB of RAM at analysis time. In resource-constrained environments — serverless functions, small CI runners, edge deployments — "most capable" and "fits the budget" point in opposite directions. Lightweight binaries (OCaml, Go, Node) trade depth for deployability.
- **Licensing** — a hard gate for commercial software. MIT and Apache-2.0 are safe. GPL is viral and typically a non-starter for proprietary products. Weak copyleft (LGPL) needs legal review. Source-available licences (Elastic, Business Source) often restrict commercial or SaaS use and must not be mistaken for open source.
- **Redundancy and engineering effort** — if a capable commercial scanner is already in place, a second commercial tool must offer clear differential value, not overlap. **Library** tools (frameworks requiring months of engineering to productise) routinely lose to weaker **turnkey** tools despite superior raw capability. See [[Precision Concepts in Static Analysis]] for the turnkey vs. library distinction.

The decision is a trade-off between three axes: capability (rung + scope from [[The Code-Understanding Ladder]] and [[Flow Scope]]), fit (language coverage), and cost (footprint + licence + engineering effort). A pragmatic strategy under tight constraints is stacking cheap complementary layers — a navigation indexer, a focused taint engine, a lightweight rule scanner — rather than betting on one heavy CPG engine. See [[Static Analysis Tooling Landscape]] for how specific tools map to these buckets.

## Resources
1. [OWASP — Source Code Analysis Tools](https://owasp.org/www-community/Source_Code_Analysis_Tools)

#### Tags
#static_analysis #sast #tooling #security #decision
