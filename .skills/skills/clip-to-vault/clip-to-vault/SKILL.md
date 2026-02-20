---
name: clip-to-vault
description: |
  **Clip to Vault**: Knowledge synthesis from web articles, blogs, and documentation. Takes a URL and produces an original vault note (either `#note` or `#quicknote`) that synthesizes the content in the vault's academic style, with internal wikilinks, references, and folder placement suggestions. NOT a web clipper—a knowledge synthesizer.
  - MANDATORY TRIGGERS: clip to vault, add article, vault note from, synthesize article, add resource, import article
---

## Purpose

The **clip-to-vault** skill transforms web content into vault notes through synthesis and integration, not copy-paste. It extracts key concepts from a URL, rewrites them in the vault's academic style, connects to related vault notes, and ensures no duplication of existing content.

## Workflow

### Input

The agent accepts a **URL** pointing to:
- Technical blog posts (e.g., Anthropic blog, Papers with Code)
- Official documentation (LLM APIs, ML frameworks)
- Conference talks or transcripts
- Medium articles, Dev.to, research blogs
- Educational tutorials (with substantial conceptual content)

**Excluded content**: News articles, opinion pieces, social media, outdated tutorials

### Processing Steps

1. **Fetch and Extract Content**
   - Navigate to the URL
   - Extract main text, headings, and structure
   - Identify key concepts, definitions, methodologies, code examples
   - Note publication date and author/organization

2. **Search Vault for Duplicates**
   - Query existing notes for overlapping topics
   - If a closely related note exists, consider:
     - Adding to the existing note as a reference instead
     - Merging the new information (with user approval)
     - Creating a complementary piece that addresses a different angle

3. **Determine Note Type**
   - **`#note`**: Substantial content (1000+ words, multiple concepts, detailed methodology, original research insights)
   - **`#quicknote`**: Brief content (500–1000 words, single concept, reference material, announcements)
   - Default to `#quicknote` unless content warrants depth

4. **Synthesize Content**
   - **NOT copy-paste**: Rewrite all content in your own words using the vault's style
   - Use **bold** to highlight key terms
   - Organize into logical sections (H2 primary, H3 subsections)
   - Convert examples to prose explanations (avoid code snippets unless technical necessity)
   - Add critical thinking: Why does this matter? How does it connect to existing vault knowledge?

5. **Determine Folder Placement**
   - Match to vault structure:
     - Machine Learning/NLP & LLMs/
     - Machine Learning/AI Safety/
     - Machine Learning/MLOps/
     - Cybersecurity/
     - Machine Learning/Agentic AI/
     - Miscellaneous/ (if topic doesn't fit cleanly)
   - Create new subfolder only if it represents a major new topic area

6. **Add Internal Linking**
   - Search vault for concepts mentioned in the article
   - Insert `[[wikilinks]]` to related hub notes and concepts
   - Link generously but meaningfully—every link should make sense to follow

7. **Create References Section**
   - Include the source URL as primary reference
   - Include any papers, books, or other resources cited in the article
   - Format: numbered list with `[Title](URL)`

8. **Add Tags**
   - Lowercase, underscore-separated topic tags
   - Match existing vault tags where possible (e.g., `llm_security`, `fine_tuning`, `transformers`)
   - Add 3–6 tags maximum

9. **Format Note**
   - Frontmatter: `Created: YYYY-MM-DD HH:MM` (line 1), `#note` or `#quicknote` (line 2)
   - No YAML fences
   - H2 for primary sections, H3 for subsections, never H1 in body
   - Academic third-person tone, no contractions
   - Proper markdown formatting

### Output

A complete vault note containing:

1. **Opening paragraph** (2–3 sentences): What is this about, why does it matter, connection to vault topics
2. **Body sections**: Rewritten and synthesized from the source
3. **Internal links**: Multiple `[[wikilinks]]` to related vault concepts
4. **References section**: Including the source URL
5. **Tags section** (if `#quicknote`) or inline tags (if `#note`)
6. **Suggested folder path**: e.g., Machine Learning/NLP & LLMs/Fine-tuning Techniques.md

## Example Output Structure

```
Created: 2026-02-20 14:00
#note

Anthropic's latest research on Constitutional AI (CAI) presents a
systematic framework for training language models to follow a set of
specified principles. This approach addresses the challenge of value
alignment by replacing human feedback with a model-generated critique
phase, reducing annotation costs while maintaining safety properties.

## Core Principles

[Synthesized explanation, NOT copy-paste from source]

## Training Methodology

...

## Empirical Results and Implications

...

## Connection to Existing Work

This builds on [[RLHF and Reinforcement Learning from Human Feedback]],
and extends [[AI Safety and Alignment]] by providing a scalable
alternative to traditional preference learning.

## References

1. [Constitutional AI paper](https://arxiv.org/abs/...)
2. [Anthropic blog post](https://www.anthropic.com/research/...)

#### Tags

constitutional_ai, value_alignment, llm_training, ai_safety
```

## Inbox Awareness

When the user requests a fast capture rather than a full synthesis (e.g., "clip this to inbox", "save to inbox quickly"), the skill should create a minimal capture instead:
- **File location**: `Inbox/[title].md` (at vault root)
- **Minimal format**: Title, URL, 1–2 sentence summary, no internal links or full synthesis required
- The Inbox serves as a staging area for rapid ideas; items can be processed into full notes later

The skill can also **process existing Inbox items** into proper notes. When the user says "process inbox clips" or "elaborate this Inbox item", convert minimal captures into full `#note` or `#quicknote` entries following the standard workflow.

## Important Notes

- **Synthesis over replication**: Rewrite content in your own words. If the source uses technical jargon, explain it. If it uses examples, generalize.
- **Citation ethics**: Always link to the source. Do not strip attribution.
- **Avoid outdated content**: Skip tutorials or guides more than 2 years old unless they address foundational concepts.
- **Check for duplicates**: Before creating a new note, verify that the vault does not already contain this information.
- **Style consistency**: Match the vault's academic tone. No casual language, no contractions, third-person perspective.
- **Link with intention**: Every wikilink should be meaningful. Readers should want to follow them to deepen understanding.

