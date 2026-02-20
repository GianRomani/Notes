---
name: literature-map
description: |
  **Literature Map**: Research landscape analysis for a given topic. Scans existing paper notes and related topic notes in the vault, produces a Mermaid diagram showing relationships (agreements, contradictions, methodological lineages), prose summary of the research landscape, identifies seminal vs. incremental work, and identifies gaps.
  - MANDATORY TRIGGERS: map literature, literature review, research landscape, paper relationships, map papers, survey topic
---

## Purpose

The **literature-map** skill synthesizes the vault's existing research notes into a visual and textual analysis of a topic's research landscape. It reveals how papers relate, which works are foundational, where gaps exist, and how the field has evolved.

## Workflow

### Input

The agent accepts a **topic query**, such as:
- "prompt injection defences"
- "RAG evaluation"
- "transformer architecture"
- "recommender systems for recommendation"
- "OSCP exam preparation"

### Processing Steps

1. **Search the Vault**
   - Query Papers/ folder for notes matching the topic
   - Search topic folders (AI Safety/, NLP & LLMs/, MLOps/, etc.) for concept hubs
   - Extract title, creation date, content summary from each note
   - Note author mentions, methodologies, and key findings

2. **Build a Relationship Graph**
   - **Temporal order**: Sort papers by publication year (if available)
   - **Citation relationships**: Identify papers cited within vault notes (explicit or implicit)
   - **Methodological lineage**: Group papers by approach (e.g., rule-based vs. learning-based defences)
   - **Conceptual agreement/disagreement**: Note where papers support or challenge each other
   - **Incremental vs. seminal**: Distinguish foundational works from extensions

3. **Generate Mermaid Diagram**
   - **Node types**:
     - Seminal papers (filled circles)
     - Recent work (rectangles)
     - Concept hubs (diamonds)
     - Open problems (dashed boxes)
   - **Edge types**:
     - Solid arrows: "cites" or "builds on"
     - Dashed arrows: "contradicts" or "revisits"
     - Dotted arrows: "related concept"
   - **Layout**: Chronological flow left (earlier) → right (recent)
   - **Cluster by methodology** if applicable

   Example:
   ```mermaid
   graph LR
       A["Prompt Injection<br/>(2023)"] -->|cites| B["Semantic Attacks<br/>(2024)"]
       A -.->|challenges| C["Statistical Methods<br/>(2023)"]
       B -->|extends| D["Ensemble Defences<br/>(2025)"]
       E{{"Open Problem:<br/>Real-time Detection"}} -.->|suggested by| D
   ```

4. **Write Landscape Prose**
   - **Overview paragraph** (200–300 words): Current state of research, dominant approaches, key players/labs
   - **Evolution narrative**: How the field has moved from early work to present day
   - **Methodological trends**: Which approaches are gaining traction, which are outdated
   - **Consensus and controversies**: What the community agrees on vs. debates

5. **Identify Gaps**
   - **Unresolved questions**: Problems mentioned but not solved in the papers
   - **Methodological gaps**: Unexplored combinations or comparisons
   - **Domain gaps**: Application areas that lack research (e.g., non-English LLMs, specific domains)
   - **Temporal gaps**: Long periods without new work on a subtopic

6. **Classify Papers**
   - **Seminal**: Foundational work that spawned follow-ups (usually 10+ years old or highly cited)
   - **Incremental**: Extensions or refinements of existing approaches
   - **Orthogonal**: Parallel research addressing the same problem differently
   - **Survey/Review**: Meta-analyses of the field

7. **Format as Vault Note**
   - Type: `#note`
   - Place in: relevant topic folder (Papers/AI Safety/, Machine Learning/NLP & LLMs/, etc.) or create Papers/[Topic]-Landscape.md
   - Link back to all papers analyzed
   - Link forward to related hub concepts

### Output

A comprehensive `#note` containing:

1. **Opening**: Purpose and scope of the map
2. **Mermaid diagram**: Visual representation of paper relationships and temporal flow
3. **Research landscape prose**: 300–500 word narrative of the field's evolution
4. **Seminal vs. incremental breakdown**: Table or list categorizing papers
5. **Methodological trends**: Summary of dominant and emerging approaches
6. **Gaps and opportunities**: Explicitly listed open problems and research directions
7. **References**: Links to all papers and related vault notes analyzed
8. **Tags**: e.g., `literature_review, prompt_injection, ai_safety, research_landscape`

## Example Output Structure

```
Created: 2026-02-20 15:00
#note

This note synthesizes the research landscape on prompt injection
defences in large language models as of February 2026. It integrates
15 key papers from the vault and identifies methodological lineages,
seminal contributions, and remaining open problems.

## Research Landscape

[Narrative prose synthesizing evolution, trends, consensus, debates]

## Paper Relationships and Timeline

[Mermaid diagram showing temporal flow, citation relationships, methodologies]

## Seminal vs. Incremental Work

| Paper | Type | Contribution |
|-------|------|--------------|

## Methodological Trends

[Description of rule-based, learning-based, ensemble, and other approaches]

## Open Questions and Gaps

- Longitudinal evaluation across multiple LLM versions
- Detection in low-resource non-English settings
- ...

## Related Concepts

[[AI Safety]], [[LLM Security]], [[Adversarial Examples in NLP]]

## References

[Links to all papers and concepts]

#### Tags

literature_review, prompt_injection, ai_safety, research_landscape
```

## Notes

- Rely on vault content; do not search the web (unless explicitly requested in a separate search)
- If papers are undated, use creation date of the vault note as a proxy
- Gaps should be honest and constructive, not a criticism of existing work
- For large fields (>20 papers), consider breaking into subtopic maps (e.g., "Detection-focused" vs. "Prevention-focused")
- Update this note periodically as new papers are added to the vault

