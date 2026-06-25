Created: 2026-06-10 10:00
#quicknote

A vulnerability is almost never one bad line of code. It is a **path** that untrusted data travels through the program, from the point it enters to the operation where it causes harm. This shift from "bad line" to "bad path" is the foundational mental model for understanding what [[Static Code Analysis]] tools actually detect and why shallow pattern matching misses most real bugs.

- **Source** — where attacker-controlled data enters the system: HTTP parameters, request bodies, file contents, environment variables.
- **Sink** — a sensitive operation where tainted data causes damage: SQL execution, HTML rendering, shell commands, file-system paths, deserialisation.
- **Flow** — the chain of assignments and function calls connecting a source to a sink, potentially traversing multiple helper functions and files.
- **Sanitizer** — an operation that neutralises the data along the path: parameterised queries, escaping, validation routines. A source-to-sink path with proper sanitisation is safe; the same path without it is a vulnerability.

The mental model maps cleanly onto ML provenance tracking. Mark the values that descend from untrusted sources, propagate that mark forward through every assignment and call, and flag anywhere a marked value reaches a sensitive operation. This is precisely what [[Taint Analysis]] does. The practical implication for remediation is that the correct fix location depends on the whole path — sometimes the fix is at the sink (parameterise the query), sometimes at the source (validate on entry), sometimes at a chokepoint in between. A tool that sees only individual lines will patch the wrong place or miss a parallel path entirely.

## Resources
1. [OWASP — Input Validation](https://owasp.org/www-community/vulnerabilities/Improper_Input_Validation)

#### Tags
#security #static_analysis #data_flow #taint #sast
