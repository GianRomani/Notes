---
name: summarize-note
description: |
  **Summarize Note**: Distill vault notes into concise, schematic bullet-point summaries—extracting only key concepts, eliminating redundancy, and preserving internal links.
  - MANDATORY TRIGGERS: summarize, tl;dr, condense, brief, schematic, extract essence, outline, synopsis
---

## Overview

This skill condenses verbose or detailed vault notes into **schematic, precise, non-redundant bullet points** that capture only essential concepts and relationships. Gianfranco prefers tight, structured notes without filler; this skill delivers exactly that.

## Core Principles

- **Extract Only**: Remove all fluff, examples, and tangential explanations; keep only core ideas
- **Schematic Format**: Bold key term at the start of each bullet; structure supports scanning and recall
- **No Redundancy**: Each bullet expresses one unique concept; eliminate overlap between bullets
- **Logical Flow**: Restructure bullets into coherent hierarchy (if needed) for better conceptual understanding
- **Preserve Links**: Retain all `[[wikilinks]]` and internal references; add new cross-references if structure changes
- **Significantly Shorter**: Target 20–40% of original length for detailed notes; 50% for notes already concise

## Output Modes

The agent should infer or ask which mode fits the user's intent:

### Mode A: Replace Note Content
- Rewrite the entire note as schematic bullet points
- Keeps original metadata (frontmatter, tags, references)
- Best for: Notes that are verbose or poorly structured
- Result: Leaner, more scannable version of same note

### Mode B: TL;DR Prepend
- Add a `## TL;DR` section at the top of the existing note
- Provides quick reference; original content remains below
- Best for: Important notes that readers should digest quickly
- Result: Fast scanning + deeper reading option

### Mode C: Standalone #quicknote
- Create a new `#quicknote` file linked to the original
- Cross-reference both notes
- Best for: Creating a summary note to link in hub-and-spoke structure
- Result: Parallel quick reference; original note untouched

## Workflow

### 1. Input Reception
- User selects text from a note or names a note to summarize
- Agent asks (if unclear): "How would you like the summary? **Replace content**, **add TL;DR section**, or **create new quicknote**?"

### 2. Content Analysis
- Identify the note's core topic and intended audience
- Scan for repeated or overlapping ideas
- Extract 2–5 primary concepts; note relationships
- Flag any examples, case studies, or tangential sections for removal

### 3. Extraction & Structuring
- Create bullet-point outline of essential ideas only
- Use **bold key terms** to start each bullet (enables visual scanning)
- Arrange bullets in logical order (conceptual hierarchy, process flow, or importance)
- Convert paragraphs into concise statements (subject + main idea)
- Eliminate: passive voice, hedging language, unnecessary qualifiers

### 4. Link Preservation & Addition
- Copy all original `[[wikilinks]]` into corresponding summary bullets
- Identify new conceptual connections; suggest additional cross-references
- Example: If summarizing LLM prompt injection note, suggest links to `[[AI Safety/Defense Mechanisms]]` and `[[MLOps/LLM Observability]]`

### 5. Validation
- Read summary in isolation: Does it make sense?
- Count redundancies: Are all bullets independent?
- Measure compression: Is it 20–50% of original?
- Check tone: Is it still academic and professional (not dumbed down)?

## Example Transformation

**Original Note Excerpt** (from `[[Machine Learning/NLP & LLMs/Fine-tuning]]`):
```
Fine-tuning is a technique where a pre-trained language model is adapted to a specific task
or domain by training it further on task-specific data. This process involves several steps,
including data preparation, where relevant examples are gathered. During training, the model
parameters are updated using backpropagation. The learning rate must be carefully chosen
because high learning rates can cause instability, while low learning rates result in slow
convergence. Fine-tuning works well for many applications and can be very effective when
applied to domain-specific tasks. Practitioners often find that fine-tuning with a small
dataset achieves good results faster than training from scratch.
```

**Schematic Summary** (Mode A output):
```
## Fine-Tuning

- **Core concept**: Adapt pre-trained LLM to task/domain via continued training on domain data
- **Process**: Data preparation → parameter updates via backpropagation
- **Key hyperparameter**: Learning rate (high = instability; low = slow convergence)
- **Advantage**: Achieves strong results on domain-specific tasks with small datasets faster than training from scratch
- Related: [[Machine Learning/Deep Learning/Transfer Learning]], [[Machine Learning/NLP & LLMs/LoRA]]
```

**Word count**: Original ~150; summary ~50 (67% compression)

## Schematic Format Guidelines

**Bullet Structure**:
```
- **Key Term**: Concise definition or main idea
- **Relationship**: How this concept connects to others
- **Implication**: What this means or enables
```

**Nesting** (for complex topics):
```
- **Main concept**
  - **Sub-concept A**: Details
  - **Sub-concept B**: Details with link [[related]]
  - **Trade-off**: X vs Y consideration
```

**Avoid**:
- "It is important to note that..." (filler)
- Repeating the same idea twice (remove redundancy)
- Examples unless they're essential for understanding
- Disclaimer language ("It could be argued that...")

**Use**:
- Active voice: "Model learns patterns" vs "Patterns are learned"
- Parallel structure: Bullets at same level follow same grammar pattern
- Specificity: "Gradient clipping prevents exploding gradients" vs "Prevents problems"

## Link Handling

**Preserve Original Links**:
```
Original: "This is related to [[AI Safety/Prompt Injection Vulnerabilities]]"
Summary: "- **Vulnerability surface**: [[AI Safety/Prompt Injection Vulnerabilities]]"
```

**Add New Links** (if improved clarity):
```
Before summary: Disconnected concept
After summary: "- **Mitigation approach**: [[MLOps/LLM Observability]] + [[AI Safety/Defense Mechanisms]]"
```

**Update Hub Notes**: If summarizing a spoke note, suggest update to hub note's links

## Metadata & Output

**For Mode A (Replace)**:
```
---
Created: 2026-02-20 14:30
#note
---

[Schematic bullets here]

## Tags
#foundational, #concept-extraction, relevant-tags-from-original
```

**For Mode B (TL;DR Prepend)**:
```
---
Created: [original date]
#note
---

## TL;DR

[3–5 schematic bullets]

## [Original first section]

[Original content below]
```

**For Mode C (New Quicknote)**:
```
---
Created: 2026-02-20 14:30
#quicknote
---

[Schematic bullets]

See full analysis: [[Original Note Title]]

## Tags
#summary, inherited-tags
```

## Quality Checklist

- [ ] Each bullet is **independent** (no overlap)
- [ ] Original length **reduced by 20–50%**
- [ ] All `[[wikilinks]]` preserved
- [ ] Bullets follow **parallel grammar** (e.g., all "**Term**: definition")
- [ ] **No examples** included (unless essential for clarity)
- [ ] Key terms are **bold** at start of each bullet
- [ ] Logical flow: Related bullets grouped or sequenced sensibly
- [ ] Tone remains **academic and professional**
- [ ] Summary is **understandable in isolation**

## Revision Prompts

After generating summary, offer:
- "Would you like this even more concise?"
- "Should I restructure this hierarchically?"
- "Should I add more cross-links to related notes?"
- "Would bullet examples help, or keep it purely conceptual?"
