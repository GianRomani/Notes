---
name: search-online
description: |
  **Search Online**: Research synthesis from authoritative web sources. Takes a topic query and produces a vault note synthesizing findings from recent academic papers, official documentation, and reputable blogs. Follows vault conventions with complete references, wikilinks, and folder placement—original synthesis, never copy-paste.
  - MANDATORY TRIGGERS: research topic, search literature, investigate topic, find papers, survey topic online, latest research
---

## Purpose

The **search-online** skill researches a topic across the web and synthesizes findings into a vault note. It differs from **clip-to-vault** by aggregating multiple sources into a cohesive overview, rather than processing a single URL.

## Workflow

### Input

The agent accepts a **topic query**, such as:
- "latest advances in retrieval-augmented generation"
- "OSCP exam prerequisites and study strategies"
- "LLM evaluation benchmarks 2025"
- "multi-agent systems in production"
- "secure code review practices"

### Processing Steps

1. **Define Search Strategy**
   - Primary sources (priority order):
     - Academic papers (arXiv, OpenReview, conference proceedings)
     - Official documentation and whitepapers
     - Reputable tech blogs (Anthropic, OpenAI, DeepMind, research labs)
     - Conference talks and technical talks (ACL, NeurIPS, USENIX, etc.)
   - Avoid: SEO content farms, unverified claims, blogspam, outdated tutorials (>3 years)

2. **Conduct Web Search**
   - Use multiple search queries to capture breadth and depth
   - Include year qualifiers for recency (e.g., "2025", "2024–2025")
   - Search for: seminal works, recent advances, benchmark datasets, practical implementations

3. **Evaluate Sources**
   - **Credibility**: Check author credentials, organization, peer review status
   - **Recency**: Prioritize sources from the last 2 years; flag older works that remain foundational
   - **Technical depth**: Prefer sources with rigorous methodology over marketing hype
   - **Diversity**: Balance academic papers with practical tutorials and tool documentation

4. **Extract Key Information**
   - Main concepts and definitions
   - Recent research findings (with numbers, benchmarks, results)
   - Practical methodologies and best practices
   - Open problems and limitations acknowledged by the field
   - Tool ecosystem and available implementations

5. **Search Vault for Related Content**
   - Query existing notes on the topic
   - Identify hub notes and spoke notes to link to
   - Avoid duplicating existing vault content; instead link to and expand on it

6. **Synthesize Findings**
   - **NOT copy-paste**: Synthesize information from multiple sources into original prose
   - Integrate perspectives: Where do sources agree? Where do they differ?
   - Highlight key insights and novel findings from the search
   - Note dates of sources and recency of research

7. **Determine Note Type and Scope**
   - **`#note`**: Comprehensive overview (5+ sources, 1500+ words, multiple subtopics)
   - **`#quicknote`**: Focused summary (2–4 sources, 800–1200 words, single topic)
   - Add section: **Search date and sources consulted** (transparency about freshness)

8. **Determine Folder Placement**
   - Match to vault structure (same as clip-to-vault)
   - If topic is broad, consider whether a new hub note or landscape analysis is more appropriate

9. **Add Internal Linking**
   - Link to existing vault notes on related or foundational topics
   - Insert `[[wikilinks]]` strategically to connect to the vault's knowledge graph

10. **Compile Full References**
    - List all consulted sources (papers, blogs, docs) with full URLs
    - Indicate source type (e.g., "arXiv paper", "official documentation", "technical blog")
    - Include access date and relevance to the topic

11. **Format and Validate**
    - Frontmatter: `Created: YYYY-MM-DD HH:MM` (line 1), `#note` or `#quicknote` (line 2)
    - H2 for primary sections, H3 for subsections
    - Academic tone, third-person, no contractions
    - Add section: **Search metadata** (search date, queries used, number of sources)

### Output

A comprehensive vault note containing:

1. **Opening paragraph** (3–4 sentences): Topic scope, why it matters, current state of the field
2. **Search metadata** (small section): Date searched, sources consulted (count by type: papers, blogs, docs)
3. **Main content sections**: Synthesized findings from multiple sources
4. **Key trends and insights**: What's emerging, what consensus exists, what's debated
5. **Open problems**: Gaps in current knowledge or practice
6. **Tools and resources**: Implementations, benchmarks, datasets (if applicable)
7. **Internal links**: `[[wikilinks]]` to related vault concepts
8. **References section**: Full list of all consulted sources with types
9. **Tags section**: lowercase underscore-separated topic tags (3–6 tags)

## Example Output Structure

```
Created: 2026-02-20 16:00
#note

Retrieval-augmented generation (RAG) has emerged as a critical pattern
for extending language models with current knowledge and domain-specific
information. This note synthesizes recent research and best practices
from 2024–2026, covering evaluation methodologies, benchmark datasets,
and production deployment considerations.

## Search Metadata

Sources consulted (February 20, 2026):
- Academic papers: 8
- Technical blogs: 5
- Official documentation: 3

## Core Concepts and Recent Advances

[Synthesized from multiple sources—not copy-paste]

## Evaluation Methodologies

...

## Open Challenges and Research Directions

...

## Tools and Implementations

...

## Related Vault Concepts

[[Retrieval Systems]], [[Vector Databases]], [[LLM Prompt Engineering]]

## References

1. [Paper title](https://arxiv.org/abs/...)
2. [Blog post](https://blog.anthropic.com/...)
3. [Documentation](https://docs.example.com/)

#### Tags

rag, retrieval_augmented_generation, llm_systems, information_retrieval
```

## Quality Standards

- **Synthesis**: Combine insights from 3+ sources; never regurgitate a single source
- **Attribution**: Cite specific claims to their source (use footnotes or inline citations if needed)
- **Freshness**: Note the search date and prioritize recent sources; flag older works as "foundational"
- **Balance**: Acknowledge both established practices and cutting-edge research
- **Honesty**: Highlight open problems and limitations; do not oversell consensus that does not exist
- **Deduplication**: If this topic already exists well-covered in the vault, link to it instead of recreating

## Inbox Capture Option

Research results can optionally be saved to `Inbox/` as quick captures when the user prefers a fast save over full synthesis. When requested (e.g., "save search results to inbox"), create a minimal entry with:
- Topic query, search date, list of key sources with URLs
- 1–2 sentence summary of main findings
- This allows rapid capture of research; items can later be promoted to full vault notes via **clip-to-vault** or **paper-ingest**

## Important Notes

- Search thoroughly: Use multiple query variations to ensure comprehensive coverage
- Verify recency: Include publication/update dates for all sources
- Avoid SEO traps: Skip listicles, outdated rankings, and unverified claims
- Link intentionally: Every wikilink should make sense in context
- Add disclaimer if information is rapidly evolving (e.g., LLM benchmarks, security landscapes)

