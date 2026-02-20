---
name: elaborate
description: |
  **Skill Title**: Expand a terse note or selection with deeper explanation, context, and supporting examples.
  - MANDATORY TRIGGERS: expand note, elaborate on, unpack, go deeper, add context, explain more, fill in details
---

## Purpose

This skill takes a condensed note or selected passage and provides richer exposition without losing academic rigor. It adds context about why concepts matter, includes relevant examples or analogies, suggests related ideas to explore, and ensures the output adheres to the vault's writing conventions. Ideal when a note feels underdeveloped or assumes too much prior knowledge.

## Instructions

### 1. Understand the Target Content

Request the user provide:
- The note name/path or a specific passage to elaborate
- The intended audience (e.g., "someone new to the topic" vs. "someone with ML background")
- Any specific sections or claims that need deeper treatment
- Preferred length (e.g., "add 1-2 paragraphs per point" vs. "comprehensive expansion")

Read the source material. Identify:
- Claims that lack sufficient justification or evidence
- Terminology that could benefit from clearer definition
- Gaps where background context would improve understanding
- Concepts that could be illustrated with concrete examples

### 2. Expand Key Concepts

For each concept that needs elaboration:

**Define precisely**: Provide a clear, academic definition. Distinguish from similar or related terms.
- Example: "**Regularization** differs from feature selection; it penalizes model complexity without removing features."

**Provide historical or theoretical context**: Why does this concept exist? What problem does it solve?
- Example: "Regularization emerged to address the overfitting problem identified in early statistical learning theory, particularly as model capacity increased."

**Cite foundational ideas**: Reference key papers, researchers, or frameworks when relevant.
- Link to vault notes with `[[relevant-concept]]`
- Reference external sources with `[author et al., YEAR](URL)` format

### 3. Add Context About Why It Matters

For each expanded concept, explain:
- **Practical significance**: How does this concept apply in real-world scenarios?
- **Theoretical importance**: What broader principles or fields does it connect to?
- **Current relevance**: Is this concept still important, evolving, or superseded? Why?

Use concrete domains from the vault (ML, AI Safety, cybersecurity, MLOps) as anchors.

### 4. Include Examples and Analogies

Add **one to two concrete examples per concept** when possible:

**For technical concepts**: Use pseudocode, mathematical notation, or step-by-step walkthroughs sparingly. Prefer prose explanations.
- Example: Instead of code, write "a model with high regularization strength prioritizes simplicity over training accuracy, reducing variance at the cost of slightly higher bias."

**For abstract concepts**: Use analogies grounded in familiar domains.
- Example: "Just as a legal contract uses constraints and penalties to enforce compliance, **loss functions** with regularization terms enforce model simplicity."

**For domain concepts**: Reference real applications from the vault's scope (e.g., OSCP scenarios, real recommender systems, actual LLM vulnerabilities).

### 5. Suggest Related Concepts to Explore

For each elaborated section, list 2-3 related ideas:
- Use format: "See also: `[[related-note-A]]`, `[[related-note-B]]` for deeper context on [topic]."
- If related notes don't exist, suggest them as potential new notes: "[A note on X would complement this discussion.]"

### 6. Preserve Original Structure and Voice

Maintain the original note's:
- Main argument and conclusions
- Existing wikilinks and references
- Academic tone (third-person, formal vocabulary, no contractions)
- Organizational logic

Slot elaborated content into appropriate sections (usually expanding existing paragraphs or sections marked as needing detail).

### 7. Apply Vault Writing Conventions

Ensure the expanded text follows these rules:
- **Bold** key terms on first introduction
- Use `[[wikilinks]]` for internal vault references
- Use `[title](URL)` for external sources
- Mix prose paragraphs with bullet points where lists improve clarity
- If a concept benefits from visual representation, suggest a Mermaid diagram (but do not include code unless necessary)
- Maintain academic vocabulary; avoid contractions and colloquialisms

## Output Format

Present the elaboration as:

```
## Elaboration: [Original Note Title]

### [Section Being Expanded]

[Original condensed text, slightly refined]

**[First Key Concept]**: [Definition and expanded explanation. Context on why it matters. Example or analogy. See also: [[related-note]] for deeper exploration.]

**[Second Key Concept]**: [Similar structure: definition, justification, example, related notes.]

### [Next Section if Applicable]

[Continue with same pattern]

---

## Suggested Additions for Future Versions

- A note on [[related-topic]] would deepen the discussion of [concept]
- The practical applications of this concept in [[domain-note]] merit a dedicated section
- Consider cross-referencing [[methodology-note]] to strengthen the theoretical foundation

```

## Tone and Style Reminders

- Write in **third-person, academic voice**. Example: "The concept of **regularization** addresses overfitting" not "I'll explain regularization to you."
- Use **formal vocabulary** and avoid contractions: write "does not" instead of "doesn't."
- **Bold key terms** on first mention; do not over-bold common words.
- Integrate examples naturally into prose; avoid isolated "Example:" headers unless the note already uses them.
- Assume the reader is intelligent but may lack domain-specific knowledge; avoid unnecessary simplification.

## Questions to Guide Elaboration

Ask yourself for each section:

1. Would a reader unfamiliar with this topic understand all the terms used?
2. Does the note explain *why* this concept matters, not just *what* it is?
3. Are there concrete examples that illustrate the abstract principle?
4. What foundational concepts does this build on? Are those referenced?
5. How does this fit into the broader landscape of the vault's topics?
6. Are there wikilinks that would naturally connect this to related ideas?

## Common Elaboration Patterns

- **Definition-heavy notes**: Expand with historical origin and evolution of the term
- **List-based notes**: Add explanatory paragraphs between or after list items; include examples
- **Method/algorithm notes**: Expand with application context and common pitfalls
- **Concept notes**: Add theoretical grounding and practical implications
- **Quick notes**: Can be promoted toward full notes by adding references, deeper context, and related concepts

---

#### Tags
elaborate, expand_notes, enrich_content, clarity, writing_support, vault_development
