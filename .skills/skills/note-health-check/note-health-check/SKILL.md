---
name: note-health-check
description: |
  **Note Health Check**: Audit notes against the vault's style guide and conventions. Validates frontmatter format, heading structure, tag consistency, wikilink integrity, and content quality.
  - MANDATORY TRIGGERS: audit note, check note quality, style guide, frontmatter check, vault style, health check, validate note, wikilink check, tag audit, orphan notes
---

## Purpose

Ensures all notes in Gianfranco's Obsidian vault conform to established conventions. Detects formatting issues, style violations, and structural problems that diminish vault quality.

## Capabilities

### Validation Checks

The skill performs comprehensive audits across multiple dimensions:

- **Frontmatter**: Verifies `Created: YYYY-MM-DD HH:MM` format on line 1, validates tag on line 2 (`#note`, `#quicknote`, `#paper`, `#agenda`, `#to-do`), flags YAML fence usage
- **Heading Structure**: Ensures no H1 headings in body, checks H2 for primary sections, H3 for subsections, validates consistent hierarchy
- **Tag Section**: Confirms `#### Tags` exists at bottom, validates lowercase underscore-separated formatting (e.g., `machine_learning`, `nlp`)
- **References Section**: For `#note` types, checks presence of `## References` with numbered URL entries; flags missing references
- **Wikilinks**: Detects broken `[[wikilinks]]`, identifies orphan notes (zero incoming/outgoing links), flags concepts mentioned in prose not yet linked
- **Content Quality**: Identifies empty sections, code blocks replaceable with Mermaid diagrams, missing bold key terms, wall-of-text paragraphs
- **Consistency**: Checks tone (academic, third-person, no contractions), link style compliance (`[[wikilinks]]` vs `[title](URL)`)

### Execution Modes

**Single Note Audit**: Provide a note path; receives detailed report with pass/fail per criterion, specific fixes, severity levels (ERROR vs WARNING).

**Vault-Wide Scan**: Audits all notes recursively, generates summary statistics, prioritizes issues by severity and frequency.

**Smart Linking**: Analyzes prose to find concepts that match existing note titles but lack wikilinks; suggests linking opportunities.

## Output Format

```
NOTE HEALTH REPORT: [filename]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ERROR] Malformed frontmatter: missing Created timestamp
[WARNING] H1 heading detected in body (line 15)
[ERROR] Tags section missing
[OK] References section present with 5 entries

SUGGESTED WIKILINKS:
- "gradient descent" → [[Gradient Descent]] (exists, not linked)
- "transformer architecture" → [[Transformers]] (exists, not linked)

SEVERITY SUMMARY: 2 errors, 1 warning | Estimated fix time: 5 min
```

## Hub and Spoke Awareness

The skill understands the vault's hub-and-spoke topology:

- **Hub notes** (`#note`): Should have incoming links and comprehensive References; sparse links indicate isolation
- **Spoke notes** (`#quicknote`): Should link UP to hub concepts; missing backlinks suggest poor integration

## Usage Example

```
/note-health-check audit Machine Learning/Deep Learning/Backpropagation.md
```

Outputs detailed findings with actionable remedies.

#### Tags

obsidian, vault, style_guide, automation, qa, wikilinks, frontmatter, linting
