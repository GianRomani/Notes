---
name: devils-advocate
description: |
  **Skill Title**: Generate 3+ structured objections, counterarguments, risks, and alternative viewpoints to the claims in a note.
  - MANDATORY TRIGGERS: counterarguments, objections, criticisms, devil's advocate, alternative views, weak points, risks, limitations, challenges
---

## Purpose

This skill identifies potential weaknesses, oversimplifications, or blind spots in a note's arguments. It presents genuine objections and alternative perspectives—not to undermine the original argument, but to strengthen it through rigorous critique. Output is a structured "Counterarguments" section ready to append to a note, which demonstrates intellectual honesty and prepares readers for real-world complexity.

## Instructions

### 1. Analyze the Core Argument

Request the user provide:
- The note name/path or a specific claim/section to critique
- The intended context (e.g., "Is this theory universally applicable?" "Are there practical limitations?")
- Any particular domains or perspectives to emphasize in the critique

Read the note thoroughly. Extract:
- The main thesis or claim
- Supporting arguments and evidence cited
- Assumptions (stated and unstated)
- Scope and limitations already acknowledged
- Target audience or intended application domain

### 2. Identify Three or More Distinct Objections

Generate **at least three independent, substantive objections**. Each should attack from a different angle:

**Type A: Empirical Challenge**
- Does evidence exist that contradicts the claim? Is the cited evidence incomplete or selective?
- Example: "The note claims X is always true, but studies Z and Y show exceptions in domain B."

**Type B: Theoretical Limitation**
- Are there unstated assumptions that may not hold? Does the underlying theory have known limitations?
- Example: "This argument assumes rationality, but behavioral economics demonstrates that agents often act irrationally."

**Type C: Practical Constraint**
- Does the concept work in theory but fail in practice? Are there operational, resource, or environmental barriers?
- Example: "While theoretically sound, deploying this approach requires computational resources unavailable in resource-constrained environments."

**Type D: Scope Boundary**
- Is the claim overgeneralized? Does it apply across all domains, or only in specific contexts?
- Example: "This principle is well-established in supervised learning but may not transfer to reinforcement learning scenarios."

**Type E: Alternative Explanation**
- Could the evidence or observations be explained by a different mechanism or theory?
- Example: "Rather than causation, the observed correlation might reflect confounding variable Z."

**Type F: Value or Priority Conflict**
- Even if the argument is logically sound, does it prioritize one value over another? Would reasonable people disagree on that priority?
- Example: "Maximizing accuracy may come at the cost of interpretability; different stakeholders may weigh these trade-offs differently."

### 3. For Each Objection: State, Explain, Evidence, Strengthen

**State the objection clearly**:
- Phrase as a direct challenge or alternative view, not a question
- Use third-person academic tone
- Example: "The note's assumption that all datasets exhibit similar statistical properties is overstated."

**Explain the reasoning**:
- Why is this a legitimate concern? What logical or empirical foundation supports it?
- Walk through the reasoning step by step
- Reference domain knowledge from the vault (e.g., known vulnerabilities, experimental findings, established theory)

**Cite relevant counter-evidence or frameworks**:
- If possible, reference papers, vault notes, or concrete examples that support the objection
- Use format: `[[vault-note]]` for internal references, `[author, YEAR](URL)` for external sources
- If no direct evidence exists, acknowledge this: "While direct evidence is limited, this concern has been raised by [source]."

**Suggest how to strengthen the original argument**:
- What would the original note need to address this objection?
- Could the scope be narrowed? The assumptions made explicit? The evidence expanded?
- Example: "The argument would be stronger if it explicitly acknowledged its domain (supervised learning) and explored whether findings transfer to [[reinforcement-learning]]."

### 4. Assess Each Objection's Validity

Use a three-tier assessment:

**Tier 1 — Fundamental Challenge**: This objection strikes at the heart of the argument and cannot be easily dismissed. Addressing it requires substantial revision or scope narrowing.

**Tier 2 — Valid Limitation**: This objection is legitimate but does not invalidate the overall argument. It identifies boundary conditions or trade-offs.

**Tier 3 — Context-Dependent Concern**: This objection applies in certain contexts but not universally. Its relevance depends on how the note is applied.

Include the tier assessment in your output so readers understand the severity and applicability of each concern.

### 5. Identify Blind Spots or Implicit Assumptions

Beyond direct objections, flag:
- **Unstated assumptions**: What must be true for the argument to hold? (e.g., "The argument assumes unbounded computational resources.")
- **Excluded perspectives**: What viewpoint is conspicuously absent? (e.g., "The note emphasizes efficiency but does not discuss ethical implications.")
- **Temporal sensitivity**: Is this argument time-dependent? (e.g., "This was state-of-the-art in 2020, but recent work [note] suggests evolution.")

### 6. Suggest Related Notes or Disagreements in the Vault

If the vault contains:
- Notes that directly contradict the original note's claims
- Notes that explore the same question from a different angle
- Papers or resources that present alternative viewpoints

Flag these and suggest adding reciprocal wikilinks to create productive intellectual tension in the vault.

## Output Format

Structure the counterargument section as follows:

```
## Counterarguments and Limitations

The claims in [Original Note] rest on solid foundations but merit critical examination. Below are significant objections and boundary conditions that strengthen understanding of both the argument and its constraints.

### Objection 1: [Clear, Specific Title]
**Assessment Tier**: [Tier 1 / 2 / 3]

**Objection**: [Direct statement of the counterargument or alternative view]

**Reasoning**: [Explanation of why this is a legitimate concern. Reference logical foundations and domain knowledge.]

**Evidence or Support**: [[vault-note]] discusses this in depth. Additionally, [external source or established principle] suggests [specific point].

**How to Strengthen the Original Argument**:
- Narrow scope to [specific domain] where the claim holds more robustly
- Acknowledge that [assumption] may not universally apply
- Integrate discussion of [[related-complexity-note]] to address this limitation

---

### Objection 2: [Clear, Specific Title]
**Assessment Tier**: [Tier 1 / 2 / 3]

[Same structure as above]

---

### Objection 3: [Clear, Specific Title]
**Assessment Tier**: [Tier 1 / 2 / 3]

[Same structure as above]

---

### Implicit Assumptions
The note assumes:
- [Assumption A]: This holds in [context] but may break down in [[alternative-context]]
- [Assumption B]: This reflects [one perspective] but [[other-perspective]] might challenge this

### Productive Tensions in the Vault
- See [[note-that-contradicts]] for an alternative theoretical framework
- [[related-practical-challenge]] explores the boundary conditions of this concept in practice

---

## Tone and Principles

- **Intellectual honesty**: Critiques should be fair and substantive, not strawmanning or dismissing the original argument
- **Constructive intent**: Frame objections as ways to deepen understanding, not to tear down
- **Academic rigor**: Ground objections in evidence, logic, or established frameworks
- **Specificity**: Avoid vague critiques like "this is too simplistic." Instead: "This argument does not account for [specific factor], which is documented in [[note]]."
- **Reciprocity**: Acknowledge where the original argument has validity and where objections have limits

## Questions to Guide Critique

For each claim in the note, ask:

1. What evidence would disprove this claim?
2. In what contexts might this claim not hold?
3. What competing theory or framework reaches a different conclusion?
4. What practical obstacles might prevent implementation or validation?
5. Who might reasonably disagree with this argument? On what grounds?
6. Is this claim about reality, about values, or about trade-offs? (Different types require different critique approaches.)
7. Are there known exceptions or edge cases that deserve mention?

## Common Objection Patterns

- **Overgeneralization**: Claim applies in narrow domain but is presented as universal
- **Outdated foundations**: Claim rests on older literature; newer work has evolved the understanding
- **Theory-practice gap**: Elegant in theory; problematic in practice
- **Assumptions not stated**: Implicit assumptions aren't made explicit
- **Competing values**: Different stakeholders optimize for different outcomes
- **Incomplete evidence**: Supporting studies have limitations or modest effect sizes
- **Domain transfer failure**: Works in domain A but not in domain B despite surface similarity

---

#### Tags
devils_advocate, critical_analysis, objections, counterarguments, intellectual_rigor, peer_review
