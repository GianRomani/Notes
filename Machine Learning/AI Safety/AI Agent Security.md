Created: 2026-02-20 10:00
#note

AI agent security represents a distinct and critical domain that extends far beyond traditional **LLM vulnerabilities**. While [[Vulnerabilities in LLM-base applications]] address language models themselves, agent security encompasses the autonomous, tool-using systems that execute decisions with real-world consequences. An **AI agent** combines perception, reasoning, and action—typically through external tool invocation—creating a multi-surface attack landscape. Threats span [[Prompt Injection]] attacks to supply chain compromises of integrated tools and plugins. The challenge is that security boundaries become diffuse: the model is not a security perimeter, reasoning is not deterministic, and tools operate with real permissions.

## Threat Landscape

| Threat Vector | Description | Attack Surface | Severity |
|---|---|---|---|
| **Prompt Injection** ([[Injection Prompts]]) | Adversary embeds malicious instructions in user input or data to override agent goals | User input, data sources | Critical |
| **Indirect Injection** | Attacker poisons external data sources (web pages, APIs, databases) that agent retrieves | Retrieved content, [[Multi-Agent Systems]] communication | High |
| **Data Exfiltration** | Agent extracts sensitive data via tool calls (email, APIs, logs) based on compromised reasoning | Tool output, inter-agent messages | High |
| **Privilege Escalation** | Attacker manipulates agent to invoke high-privilege tools or bypass access controls | Tool selection, credential injection | Critical |
| **Output Manipulation** | Agent produces false or misleading output to deceive users or downstream systems | Model reasoning, observation chains | High |
| **Cost Exhaustion** | Adversary triggers high-cost tool calls (API tokens, compute) to exhaust budgets | Token consumption, cascading tool use | Medium |

## OWASP Top 10 for Agentic AI

| Code | Risk Name | Description | Key Risk Factor |
|---|---|---|---|
| ASI01 | Agent Goal Hijack | Attacker redirects agent objectives through prompt injection or indirect instruction injection | Model takes conflicting instructions from multiple sources |
| ASI02 | Tool Misuse | Agent misapplies tools, uses tools for unintended purposes, or invokes wrong tool | Tool selection confusion, inadequate tool descriptions |
| ASI03 | Identity/Privilege Abuse | Agent assumes excessive privileges, impersonates users, or bypasses authentication | Weak access control, overpermissioned credentials (see [[Excessive Agency]] for related vulnerabilities) |
| ASI04 | Agent Supply Chain | Compromise of external tools, plugins, [[MCP Protocol]] integrations, or third-party models | Untrusted dependencies, lack of tool validation |
| ASI05 | Unexpected Code Execution | Agent constructs and executes code inadvertently through tool chains or interpreter tools | Code generation without validation, dangerous tools |
| ASI06 | Memory/Context Poisoning | Attacker corrupts agent memory, history, or context to alter future behavior | Persistent memory is trusted, no memory validation |
| ASI07 | Insecure Inter-Agent Communication | Messages between agents lack integrity checks, allowing injection or eavesdropping | No message signing/validation, plaintext comms |
| ASI08 | Cascading Failures | Failure in one agent or tool propagates to dependent agents or systems | Agents depend on each other without fault isolation |
| ASI09 | Human Trust Exploitation | Agent output is trusted by humans without verification; malicious output treated as fact | Output not fact-checked, users assume reliability |
| ASI10 | Rogue Agents | A deployed agent becomes compromised, misconfigured, or turns adversarial after deployment | Post-deployment control, monitoring gaps |

## Defensive Measures

### Prompt Hardening

**Important caveat**: Prompts are helpful guardrails but are not a security boundary. The model's reasoning cannot be fully constrained by instructions alone. That said, hardening reduces attack surface:
- **Minimal explicit system role**: Avoid lengthy system prompts that repeat goals; keep role definitions terse
- **Separate instructions from data**: Clearly demarcate user input boundaries; mark trusted vs. untrusted content
- **Sandwich pattern**: Place system instructions before and after user input to reduce injection efficacy
- **Input sanitization**: Remove or flag suspicious patterns (e.g., "Ignore previous instructions") in user input before processing

### Architectural Constraints

These enforce security through design rather than prompting:
- **Action selector with allow-list**: Agent chooses only from an explicitly defined, verified set of tools; no dynamic tool generation
- **Plan-then-execute with immutable plans**: Agent generates a plan first; plan is shown to human or validated; only then executed
- **Isolation with role separation**: Different agents handle different trust domains (user-facing vs. backend); data flows one direction
- **Inter-agent message validation**: All messages between agents are cryptographically signed or checksummed; schema validation enforced

### Tool Security

- **Sandboxing**: Tools run in isolated environments with resource limits, network restrictions, file system boundaries
- **Least-privilege credentials**: Each tool gets minimal credentials needed for its function; no shared admin keys
- **Validate every tool call**: Agent's choice of tool and parameters is validated *outside* the model before execution; never blindly execute model output
- **Human approval for high-risk actions**: Destructive or costly operations (delete, transfer, send) require human review
- **Supply chain vigilance**: Treat plugins, [[MCP Protocol]] integrations, and external models as supply chain risks; vet and audit dependencies

### Monitoring and Filtering

- **Output and action monitoring**: Log all agent decisions and tool invocations; flag anomalies (unexpected tool, unusual parameters, new behaviors)
- **Anomaly detection**: Establish baselines for normal agent behavior; alert on deviations (e.g., sudden spike in API calls, new recipient emails)
- **Audit trails**: Immutable logs of reasoning chains, tool calls, and outputs for forensics and compliance
- **Kill switch and circuit breaker**: Ability to pause or halt an agent immediately if misbehavior is detected; automatic rate limiting

## Mapping Risks to Defenses

| Risk Category | Prompt Hardening | Architectural Constraints | Tool Security | Monitoring |
|---|---|---|---|---|
| Prompt Injection (ASI01) | Input sanitization, sandwich pattern | Plan-then-execute validation | - | Anomaly detection |
| Indirect Injection (ASI02, ASI06) | Data/instruction separation | Message validation, role isolation | Input validation from tools | Log data sources |
| Privilege Escalation (ASI03) | Goal clarity | Allow-listed actions | Least-privilege credentials | Audit excessive calls |
| Supply Chain Compromise (ASI04) | - | - | Dependency vetting, supply chain validation | Monitor tool behavior |
| Unexpected Code Execution (ASI05) | Avoid code generation tasks | Plan-then-review | Sandboxing, disable dangerous tools | Flag dynamic execution |
| Context Poisoning (ASI06) | Separate memory from reasoning | Memory validation schemas | - | Audit memory writes |
| Inter-Agent Infection (ASI07) | - | Message signing, schema validation | - | Log inter-agent comms |
| Cascading Failures (ASI08) | - | Fault isolation, rollback plans | Timeouts, resource limits | Circuit breaker |
| Human Trust Exploitation (ASI09) | Clear confidence metrics | Human-in-loop approval | Confidence scoring | Output monitoring |
| Rogue Agents (ASI10) | - | Version control, deployment approvals | Disable compromised agents | Behavior anomaly detection |

## Security Testing Tools

**PyRIT** (Prompt Risk Identification Toolkit) — Red-teaming framework for systematically generating adversarial prompts and measuring agent robustness; supports multi-turn attacks.

**Giskard** — Open-source ML testing platform with LLM-specific tests for bias, hallucination, prompt injection, and jailbreaks; integrates with model evaluation pipelines.

**Promptfoo** — CLI and dashboard for evaluating LLM outputs across test cases; supports evals for safety, accuracy, and regression testing.

**Lakera** — API-based prompt injection and jailbreak detection service; real-time filtering of malicious prompts before they reach the model.

**ProtectAI** — Monitoring and threat detection for deployed LLM applications; tracks unusual token patterns, reasoning chains, and tool usage.

## References

- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [OWASP Agentic AI Threats](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)
- [NIST AI RMF](https://www.nist.gov/artificial-intelligence/executive-order-safe-secure-and-trustworthy-artificial-intelligence)
- [Google SAIF](https://saif.google/)

#### Tags: #aisecurity #ai_agents #llm #cybersecurity #owasp