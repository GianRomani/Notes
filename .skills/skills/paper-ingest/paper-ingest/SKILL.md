---
name: paper-ingest
description: |
  **Paper Ingest**: Automated ingestion of academic papers into the vault. Takes a PDF, URL, or arXiv link and produces a formatted `#paper` note following the vault's paper template with metadata extraction, abstract synthesis, analysis sections, vault linking, and folder suggestion.
  - MANDATORY TRIGGERS: ingest paper, add paper, import paper, paper arxiv, paper pdf, paper url
---

## Purpose

The **paper-ingest** skill automates the process of adding academic papers to the vault. Rather than manually creating paper notes, this skill extracts metadata, synthesizes content, and generates properly formatted `#paper` notes that integrate with the vault's existing knowledge graph.

## Workflow

### Input

The agent accepts:
- **PDF file** uploaded directly or from local system
- **arXiv URL** (e.g., `https://arxiv.org/abs/2312.xxxxx`)
- **Paper URL** (conference sites like OpenReview, ACL Anthology, IEEE Xplore, etc.)
- **DOI** (converted to a resolvable URL)

### Processing Steps

1. **Extract Metadata**
   - Title, authors, publication year, venue (conference/journal)
   - Abstract (if available)
   - PDF download link or arXiv identifier

2. **Search Vault for Related Notes**
   - Query the vault's Papers/ and topic folders
   - Identify existing notes on similar topics, authors, or methods
   - Note which concepts from the paper already have hub notes

3. **Generate Opening Paragraph**
   - 2–4 sentences synthesizing: what the paper does, why it matters, gap it addresses
   - Write in the vault's academic, third-person style

4. **Populate Paper Sections**
   - **Main idea**: 3–5 sentences on core contribution and novelty
   - **Results**: Key findings, metrics, benchmarks (include numbers where quantifiable)
   - **Ideas for future works**: Extensions suggested by the paper or identified by the reader
   - **In deep**: Detailed analysis of methodology, key figures/tables, technical details
   - **References**: Link to the paper itself + key cited works from the vault or external sources
   - **Code**: Link to official repository, implementation details, or leave empty if none
   - **Tags**: lowercase underscore-separated topic tags (e.g., `#prompt_injection`, `#llm_safety`, `#machine_learning`)

5. **Add Internal Linking**
   - Insert `[[wikilinks]]` to related vault notes discovered in step 2
   - Update existing hub notes to link back to this new paper

6. **Determine Folder Placement**
   - Suggest location: Papers/ root, or Papers/[Topic]/ subfolder
   - Align with vault structure (e.g., Papers/AI Safety/, Papers/NLP & LLMs/)

7. **Format & Validate**
   - Frontmatter: `Created: YYYY-MM-DD HH:MM` on line 1, `#paper` on line 2
   - H2 for section headers, H3 for subsections
   - No H1 in body
   - Proper markdown link formatting
   - No code snippets unless technical methodology requires it (use prose instead)

### Output

A complete `#paper` note ready to file into the vault with:
- All metadata and sections filled
- Internal vault links established
- Suggested folder path
- List of existing notes that should cross-reference this paper

## Example Output Structure

```
Created: 2026-02-20 14:30
#paper

This paper introduces a novel approach to prompt injection detection
by combining semantic embedding analysis with adversarial examples.
Published at ACM CCS 2025, it addresses a critical gap in LLM
security by proposing detection mechanisms that operate at inference
time without requiring model fine-tuning.

## Main idea

...

## Results

...

## Ideas for future works

...

## In deep

...

## References

1. [Paper Title](https://arxiv.org/abs/2312.xxxxx)
2. [Related vault concept](Papers/AI Safety/Prompt Injection Defences.md)

## Code

[Official repository](https://github.com/...)

#### Tags

prompt_injection, llm_security, ai_safety, detection
```

## Inbox Processing

The skill can scan `Inbox/` for paper-related items (titles, links, arXiv URLs) and batch-process them into proper `#paper` notes. When the user requests "process inbox papers" or "ingest papers from inbox":
- Identify paper citations, arXiv links, or paper titles sitting in Inbox items
- Offer to convert each into a full `#paper` note following the standard workflow
- Report which papers were successfully ingested and suggest folder placements

## Notes

- Agent should preserve academic rigor: synthesize rather than paraphrase abstracts
- Dates and venues must be accurate
- Search the vault thoroughly before assuming a related concept doesn't exist
- If a paper contradicts or extends an existing vault note, explicitly mention this in the opening paragraph or Ideas section
- For highly technical papers, the **In deep** section can be substantial (500+ words); for surveys, focus on **Main idea** and **Results**

