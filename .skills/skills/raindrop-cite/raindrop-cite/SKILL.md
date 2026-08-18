---
name: raindrop-cite
description: |
  **Raindrop Citing & Knowledge Lookup**: Search the user's curated Raindrop.io bookmark library across 7 structured collections (AI & LLMs, Cybersecurity, Software Engineering, Data Science, Papers & Research, Lifestyle, Inbox) using normalized tags. Formats findings into high-quality academic markdown citations for Obsidian note `## References` sections, technical ADRs, and study guides.
  - MANDATORY TRIGGERS: cite raindrop, raindrop cite, search raindrop, find raindrop bookmarks, enrich note with raindrop, lookup raindrop
---

## Purpose

The **raindrop-cite** skill enables the agent to discover, retrieve, and cite curated bookmarks, research papers, tool repos, and technical articles from the user's Raindrop.io account. Rather than inventing or searching external web citations blindly, this skill prioritizes the user's personal, vetted bookmark knowledge base.

---

## Raindrop Collection Taxonomy & ID Registry

| Collection               | ID         | Primary Domain & Topics                                                             | Target Tags                                                                                                                                |
| ------------------------ | ---------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **AI & LLMs**            | `74060706` | AI/ML systems, agent frameworks, LLM eval, prompt engineering, RAG, reasoning       | `ai`, `llm`, `agents`, `rag`, `reasoning`, `deep-learning`, `mcp`, `harness`, `claude`, `multi-agent`, `prompt`, `skills`, `llmevaluation` |
| **Cybersecurity**        | `74060707` | Offensive security, OSCP labs, PrivEsc, Active Directory, LLM security, red teaming | `cybersecurity`, `llmsecurity`, `pentesting`, `oscp`                                                                                       |
| **Software Engineering** | `74060708` | Architecture, systems design, developer tools, leadership, Python, TUI              | `software-engineering`, `engineering-leadership`, `github`, `python`, `obsidian`, `tools`                                                  |
| **Data Science**         | `74060709` | Data pipelines, ML ops, SQL, analytics, algorithms                                  | `data-science`, `sql`, `text2sql`, `algorithm`, `document_analysis`, `graph`                                                               |
| **Papers & Research**    | `74060710` | Academic papers, survey papers, formal benchmarks                                   | `paper`, `survey`, `explainability`                                                                                                        |
| **Lifestyle**            | `74060712` | Coffee, travel, cooking, personal care                                              | `coffee`, `cooking`, `house`, `travelling`, `Japan`, `german`, `personal-care`                                                             |
| **Inbox**                | `74060713` | Triage / newly captured bookmarks                                                   | _(unrouted items)_                                                                                                                         |

---

## Workflow

### 1. Identify Context & Query Intent

- Analyze the topic of the current Obsidian note, design log (ADR), or user question.
- Map the topic to one or more primary Collections (from table above) and relevant tags.

### 2. Search Raindrop

Query the Raindrop API or MCP server using search parameters:

- **By Tag**: `{"search": "#llmsecurity"}` or `{"search": "#agents"}`
- **By Collection**: Query `/rest/v1/raindrops/{collection_id}?search={keywords}`
- **Global Search**: Query `/rest/v1/raindrops/0?search={query}`

### 3. Filter & Synthesize

- Select the top 1 to 4 most relevant bookmarks.
- Extract:
  - Title and clean URL
  - Collection name and assigned tags
  - Highlights / excerpts / notes attached to the bookmark

### 4. Format Citations

Format the selected bookmarks into the standard markdown citation style for Obsidian and codebase notes:

```markdown
## References

1. [Article Title](https://example.com/url) — _Saved in AI & LLMs (`#agents`, `#llm`)_
2. [Research Repository](https://github.com/org/repo) — _Saved in Cybersecurity (`#llmsecurity`)_
```

If updating an existing Obsidian note:

- Check if `## References` section exists.
- Append newly discovered Raindrop links in numbered or bulleted list format.
- Preserve existing references.

---

## Example Usage

### Scenario: Drafting an Obsidian note on Prompt Injection Defenses

1. Agent queries Raindrop: `search="#llmsecurity prompt injection"` in collection `74060707`.
2. Raindrop returns `seojoonkim/prompt-guard` and `Numbat EDR Research`.
3. Agent inserts citations into the note:
   ```markdown
   ## References

   1. [seojoonkim/prompt-guard: Advanced prompt injection defense system](https://github.com/seojoonkim/prompt-guard) — _Saved in Cybersecurity (`#llmsecurity`)_
   2. [Securing Agents with Numbat](https://research.perplexity.ai/articles/securing-agents-across-perplexity%E2%80%99s-client-endpoints-with-numbat) — _Saved in Cybersecurity (`#llmsecurity`, `#harness`)_
   ```
