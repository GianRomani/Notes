---
name: restructure-vault
description: |
  **Restructure Vault**: Analyze vault organization and suggest or execute file reorganization. Two modes—AUDIT (report placement issues, suggest moves) and EXECUTE (move files after approval, update references, refresh CLAUDE.md).
  - MANDATORY TRIGGERS: reorganize vault, folder structure, move note, vault cleanup, restructure, folder analysis, placement audit, vault organization
---

## Purpose

Maintains optimal vault structure as the knowledge base grows. Identifies misplaced notes, overgrown folders, notes that should be split or merged, and executes safe reorganization with user approval.

## Placement Guidelines

The skill enforces Gianfranco's folder taxonomy:

- **Deep Learning/**: Foundational concepts only (backpropagation, autoencoders, GANs, attention mechanisms)
- **NLP & LLMs/**: Language-specific techniques, transformers, fine-tuning, LoRA, PEFT, LLM vulnerabilities
- **MLOps/**: Deployment pipelines, serving, observability, evaluation, MLflow, Langfuse; subdivided into **Agentic Systems/** and **ML Models Deployment/**
- **AI Safety/**: LLM security, OWASP Top 10, prompt injection, data poisoning, red teaming, defensive measures
- **Agentic AI/**: AI agents, multi-agent systems, MCP protocol, RAG, frameworks, architectural patterns
- **Cybersecurity/OSCP/**: Penetration testing, vulnerability management, supply chain security, OSCP study materials
- **Papers/**: Academic paper summaries cross-indexed by topic
- **Study/OSCP/**: OSCP exam prep, practice notes, lab writeups
- **Miscellaneous/**: Programming references, interview prep, utilities

## Capabilities

### AUDIT Mode

Scans all notes and reports:

- **Misplaced Notes**: Identifies files in folders that do not match their content (e.g., security note in Machine Learning/)
- **Folder Bloat**: Flags folders exceeding 25 notes; suggests subdivision or creation of subtopics
- **Orphaned Folders**: Detects empty or near-empty directories
- **Candidate Merges**: Identifies thin notes that could consolidate into a single hub
- **Candidate Splits**: Flags oversize hub notes (2000+ words) better split into focused pieces
- **Structural Imbalance**: Reports topics with significant depth but missing breadth (e.g., 20 NLP notes, 0 tokenization notes)

### EXECUTE Mode

After explicit user approval, performs:

- **File Moves**: Relocates notes to correct folders with atomic operations
- **Reference Updates**: Scans all notes for hardcoded folder paths or cross-folder assumptions; updates them
- **CLAUDE.md Refresh**: Updates the structure section to reflect new layout, adds newly discovered folders
- **Link Preservation**: Ensures `[[wikilinks]]` remain valid after reorganization
- **Audit Trail**: Creates a move log noting what changed and when

## Output Format

```
VAULT STRUCTURE AUDIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MISPLACED NOTES (3):
  Machine Learning/Cybersecurity Threat Modeling.md → Cybersecurity/
  NLP & LLMs/Graph Neural Networks.md → Machine Learning/Deep Learning/
  Papers/OSCP Lab Writeup.md → Study/OSCP/

FOLDER BLOAT (2):
  Machine Learning/NLP & LLMs/ (31 notes) → Consider sub-dividing
  Machine Learning/Deep Learning/ (18 notes) → Near threshold

CANDIDATE MERGES (2):
  "Gradient Descent Variants" + "SGD" + "Adam" → Consolidate into optimizer hub

EXECUTE RESTRUCTURING?
  Estimated moves: 5 | Reference updates: 8 | Risk: LOW
```

## Safety Guarantees

- Never moves files without explicit user confirmation
- Performs dry-run validation before executing
- Maintains immutable note IDs where possible
- Creates backup reference of original structure
- Rolls back on reference update failure

#### Tags

obsidian, vault, organization, file_structure, refactoring, automation, curation
