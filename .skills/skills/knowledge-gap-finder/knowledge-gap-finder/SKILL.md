---
name: knowledge-gap-finder
description: |
  **Knowledge Gap Finder**: Identify coverage gaps in the vault. Finds broken wikilinks, concepts mentioned but undocumented, thin notes with high centrality, breadth gaps (depth without breadth), and generates a prioritized "notes to write" list.
  - MANDATORY TRIGGERS: knowledge gap, gap analysis, missing notes, coverage gaps, what to write next, thin notes, broken links, undocumented concepts, content gaps, vault gaps
---

## Purpose

Helps Gianfranco identify where his vault has incomplete or shallow coverage. Surfaces emerging topics, orphaned concepts, and high-impact notes worth developing next.

## Gap Categories

### Forward References (Broken Wikilinks)

Detects `[[wikilinks]]` pointing to non-existent notes:

- Reports all broken links with their source context
- Identifies clusters of broken links (e.g., multiple missing NLP notes)
- Distinguishes between "typo links" (likely misnamed) and "true gaps" (legitimate concepts needing new notes)

### Undocumented Concepts

Scans prose for key terms that appear 3+ times across the vault but lack a dedicated note:

- Extracts candidate concept names from existing content
- Cross-references against existing note titles to confirm absence
- Ranks by frequency and cross-vault mention count
- Example: "gradient descent" mentioned 12 times but no dedicated note

### Thin Hub Notes

Identifies hub notes (high incoming link count) that are sparse (under 100 words):

- Lists notes sorted by link count vs. content depth ratio
- Indicates which topics have many satellite notes pointing to under-developed centers
- Prioritizes hubs as expansion candidates

### Breadth vs. Depth Gaps

Analyzes folder-level coverage:

- **Depth without breadth**: "MLOps has 15 notes on serving, but 0 on monitoring"
- **Breadth without depth**: "AI Safety has 12 topics, each with only quicknotes"
- Reports imbalances and suggests what category to develop

### Orphaned Topic Clusters

Detects disconnected subgraphs:

- Topics with internal links but no bridges to the rest of the vault
- Indicates siloed knowledge areas that could be better integrated
- Suggests linking points

## Output Format

```
KNOWLEDGE GAP REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BROKEN WIKILINKS (7):
  [[Attention Mechanism]] (source: Transformers.md) → TYPO: exists as [[Attention]]
  [[Reinforcement Learning]] (5 sources) → TRUE GAP: missing, high priority
  [[Gradient Descent Variants]] (3 sources) → POSSIBLE: subsumed in other notes

UNDOCUMENTED CONCEPTS (12):
  "prompt injection" (mentioned 8x) → Should be #note in AI Safety/
  "loss function" (mentioned 6x) → Consider hub in Deep Learning/
  "k-means clustering" (mentioned 5x) → Suggested #quicknote in Unsupervised/

THIN HUBS (4):
  [[Recommender Systems]] (12 incoming links, 85 words) → Expand with algorithms
  [[OSCP]] (8 incoming links, 110 words) → Add domain breakdown
  [[MLOps]] (14 incoming links, 95 words) → Add deployment patterns

BREADTH GAPS (3):
  NLP & LLMs: depth in transformers, missing tokenization, embeddings
  Cybersecurity: OSCP focused, missing threat modeling, secure SDLC
  MLOps: serving coverage strong, missing observability/monitoring

NOTES TO WRITE NEXT (Prioritized):
  1. [[Prompt Injection Techniques]] (#note in AI Safety/) — enables 5 spoke notes
  2. [[Tokenization]] (#quicknote in NLP & LLMs/) — foundational gap
  3. [[Recommender Systems Algorithms]] (#note) — expands existing hub
  4. [[Model Monitoring and Observability]] (#note in MLOps/) — breadth expansion
```

## Scoring System

Prioritization combines:

- **Impact**: Notes that would unblock broken links or serve as central hubs rank highest
- **Demand**: Forward references + mention frequency indicate community interest
- **Urgency**: Breadth gaps in main focus areas (ML, AI Safety, Agentic AI) prioritized over peripheral topics
- **Effort**: Estimated effort to write (quicknote vs. full note)

## Inbox Awareness

The skill should also check `Inbox/` for unprocessed items and include this in gap analysis:
- **Report unprocessed Inbox items**: Count items and flag any sitting longer than 1 week (check `Created:` timestamp)
- **Identify staging patterns**: Note if certain topics (e.g., paper links, web clips) accumulate in Inbox without being processed
- **Suggest batch processing**: If multiple papers or research items are present, recommend running **paper-ingest** or **clip-to-vault** batch jobs
- This helps identify workflow bottlenecks and ensures Inbox doesn't become a black hole for unfinished work

## Usage Example

```
/knowledge-gap-finder scan all
/knowledge-gap-finder focus Machine Learning/
/knowledge-gap-finder find-thin-hubs
```

#### Tags

obsidian, gap_analysis, coverage, content_strategy, vault_growth, knowledge_mapping
