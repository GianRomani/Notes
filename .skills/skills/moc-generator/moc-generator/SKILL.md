---
name: moc-generator
description: |
  **MOC Generator**: Generate or update Maps of Contents (MOCs) for topic folders. Creates hub notes listing and organizing all notes in a folder, includes Mermaid graphs, identifies central notes, highlights gaps. Output as #note with vault formatting.
  - MANDATORY TRIGGERS: create moc, map of contents, topic overview, generate outline, folder moc, knowledge map, topic summary, organize folder
---

## Purpose

Generates comprehensive Map of Contents (MOC) notes that serve as navigable hubs for topic areas. MOCs enable quick orientation and reveal structural insights about knowledge organization.

## MOC Structure

Each MOC is a `#note` containing:

### Header Section

```
Created: YYYY-MM-DD HH:MM
#note
```

### Overview Paragraph

Brief summary (100-150 words) of the topic scope, main themes, and strategic importance to the vault.

### Organized Note Listings

Subdivides all notes in the folder into logical groups with:

- **Section heading** (H3): category name (e.g., "Foundational Concepts", "Practical Techniques", "Research Frontiers")
- **Bulleted list**: each note as `[[Note Name]]` with parenthetical 1-2 word descriptor
- **Links**: wikilinks to every note in the folder; external links for key references

### Connectivity Mermaid Diagram

Visual graph showing relationships. Examples:

```
graph TB
    MOC["Topic MOC"]
    MOC --> |foundational| Note1["[[Foundation Note]]"]
    MOC --> |builds on| Note2["[[Advanced Note]]"]
    Note1 --> Note2
    Note2 --> |related| Note3["[[Applied Note]]"]
```

Diagram includes:

- Nodes for each note in folder (labeled with `[[name]]`)
- Edges showing major dependencies or thematic connections
- Node styling to indicate hub vs. spoke (e.g., larger nodes for high-link-count notes)
- Grouping of closely related concepts

### Centrality Analysis

Table or paragraph identifying:

- **Most-linked notes** (incoming wikilinks from vault): indicates hub status
- **Bridge notes**: high in-degree and out-degree, connect multiple sub-clusters
- **Isolated notes**: 0-1 links; candidates for integration or removal

Example:

```
| Note | Incoming Links | Outgoing Links | Centrality |
|------|----------------|----------------|-----------|
| [[Transformers]] | 14 | 8 | HIGH |
| [[BERT]] | 7 | 5 | MEDIUM |
| [[Tokenization]] | 2 | 1 | LOW |
```

### Gap Analysis (H3)

Notes missing from the folder that would strengthen coverage:

- Forward references that should exist
- Concepts mentioned in existing notes but undocumented
- Suggested new notes with placement rationale

### References Section

Numbered external references (papers, articles, courses) supporting the topic area, compiled from constituent notes.

### Tags Section

`#### Tags` with topic-specific tags, e.g., `deep_learning, attention, transformers`

## Placement Convention

MOCs are placed at the top level of the relevant folder:

- `Machine Learning/Agentic AI/Agentic AI MOC.md`
- `Machine Learning/NLP & LLMs/NLP & LLMs MOC.md`
- `Cybersecurity/OSCP/OSCP MOC.md`
- Naming: `[FolderName] MOC.md`

## Generation Algorithm

The skill:

1. **Scans target folder** for all `#note`, `#quicknote`, `#paper` files recursively
2. **Extracts metadata**: created date, tag section, incoming/outgoing wikilinks
3. **Clusters notes** by analyzing tag similarity and wikilink patterns
4. **Ranks notes** by centrality (link count)
5. **Builds diagram** showing major relationships
6. **Identifies gaps** via forward references and cross-vault mention analysis
7. **Formats output** with vault conventions (no H1, bold key terms, academic tone)
8. **Generates References** section by collecting external links from constituent notes

## Update Behavior

When regenerating an existing MOC:

- Preserves user-added custom sections (marked with `<!-- CUSTOM: ... -->`)
- Detects new/deleted notes and updates lists and diagrams
- Recalculates centrality metrics
- Merges References (removes stale, adds new)
- Reports what changed (3 new notes, 1 moved, 2 references added)

## Usage Example

```
/moc-generator create "Machine Learning/Deep Learning"
/moc-generator update "Machine Learning/NLP & LLMs" --auto
/moc-generator analyze "Cybersecurity/OSCP" --suggest-gaps
```

## Quality Assurance

Generated MOCs:

- Always validate no H1 headings
- Include at least one Mermaid diagram
- Link every note in the folder
- Maintain consistent styling with vault conventions
- Suggest feedback if MOC becomes >2000 words (may need sub-MOCs)

#### Tags

obsidian, moc, hub_note, knowledge_architecture, navigation, visualization, automation
