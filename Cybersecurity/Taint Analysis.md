Created: 2026-06-10 10:00
#quicknote

**Taint analysis** is data-flow analysis specialised for security. It marks values that descend from attacker-controlled input as "tainted" and tracks whether those values reach a sensitive operation without being neutralised first. It is the security overlay on Rung 4 of [[The Code-Understanding Ladder]], producing Rung 5 — the first rung at which real vulnerabilities can be characterised, not just flagged as suspicious patterns.

Three ingredients are required:
- **Sources** — where untrusted data enters: HTTP parameters, request bodies, file input, environment variables, user-supplied filenames.
- **Sinks** — sensitive operations where tainted data is dangerous: SQL execution, HTML rendering, shell commands, file-system paths, deserialisation.
- **Sanitizers** — operations that neutralise taint: escaping functions, parameterised queries, validation routines, encoding transforms.

A finding is a **source → sink** path with no sanitizer anywhere along it. See the worked example in [[Vulnerabilities Are Data Paths]].

The claim "supports taint analysis" is nearly meaningless by itself. What actually varies between tools is (1) **how far** taint propagation reaches — within one function, across files, across services — which is the subject of [[Flow Scope]]; and (2) **how precisely** the analysis avoids false positives, which depends on [[Precision Concepts in Static Analysis]].

For engineers from a data background, taint is provenance tracking through a dependency graph: mark the inputs that are not trusted, propagate that mark forward through every assignment and call, and flag anywhere a marked value lands in a sensitive position. Sanitizers are the nodes that clear the mark.

## Resources
1. [Livshits & Lam — Finding Security Vulnerabilities in Java Applications Using Static Analysis (2005)](https://suif.stanford.edu/papers/defect05.pdf)
2. [OWASP — Testing for Taint-style Vulnerabilities](https://owasp.org/www-project-web-security-testing-guide/)

#### Tags
#security #taint #static_analysis #sast #data_flow
