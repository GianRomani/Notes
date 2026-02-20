# Obsidian Knowledge Vault

## Owner

Gianfranco Romani — Applied Machine Learning Scientist at Thomson Reuters (Zug, Switzerland). MSc in Engineering in Computer Science from Sapienza University of Rome, specializing in AI and Machine Learning.

## Purpose

This is a personal knowledge base built in Obsidian, started during Gianfranco's master's thesis work and grown into a living reference covering the topics he works with and studies. The vault serves as a second brain for professional development, research, and day-to-day work in ML engineering and AI security.

## Scope

The vault covers:

- **Machine Learning** — classical ML concepts (PCA, regularization, bias-variance), unsupervised methods (clustering, topic modelling), recommender systems, deep learning, NLP, and machine translation
- **AI Safety & Security** — LLM vulnerabilities (prompt injection, data poisoning, model theft), OWASP Top 10 for LLMs, red teaming, defensive measures, and the evolving threat landscape for AI-based applications
- **MLOps** — model deployment, training pipelines, serving infrastructure, LLM observability, evaluation, and production tooling (MLflow, Langfuse)
- **Cybersecurity** — Secure SDLC, threat modeling, penetration testing, vulnerability management, supply chain security, and OSCP-related notes
- **Agentic AI** — AI agents, multi-agent systems, agentic frameworks, MCP protocol, RAG, architectural patterns (hexagonal architecture, task capsule)
- **Papers** — summaries and notes on academic papers across the topics above
- **Miscellaneous** — programming notes, interview prep, and other reference material

## Structure

```
├── Machine Learning/
│   ├── Agentic AI/         # AI agents, RAG, MCP, multi-agent systems, frameworks
│   ├── AI Safety/          # LLM security, OWASP, prompt injection, red teaming
│   ├── Computer Vision/    # CNN, CLIP, image captioning, segmentation
│   ├── Deep Learning/      # Foundations: backprop, autoencoders, GANs, attention
│   ├── Knowledge Graph/
│   ├── MLOps/              # Deployment, observability, evaluation, tooling
│   │   ├── Agentic Systems/  # Hexagonal architecture, task capsule, prompt infra
│   │   └── ML Models Deployment/
│   ├── Measures and metrics/
│   ├── NLP & LLMs/         # Transformers, LLMs, fine-tuning, LoRA, PEFT
│   │   └── Machine Translation/
│   ├── Recommender Systems/
│   └── Unsupervised/       # Clustering, topic modelling, thesis work
├── Cybersecurity/
│   └── OSCP/
├── Papers/                 # Paper summaries organized by topic
├── Study/                  # Study artefacts: flashcards, scenarios, exam prep
│   └── OSCP/               # OSCP-specific flashcards and practice scenarios
├── Inbox/                  # Raw ideas, links, unprocessed thoughts — triage into proper notes
├── Miscellaneous/          # Programming, interviews, other
├── Templates/              # Note templates (#note, #quicknote, #paper)
└── Attachments/            # Images and other media
```

## Writing Conventions

See the `obsidian-notes` skill for the full style guide. Key points:

- **Frontmatter**: `Created: YYYY-MM-DD HH:MM` on line 1, tag type on line 2 (`#note`, `#quicknote`, `#paper`)
- **Headings**: H2 (`##`) for primary sections, H3 (`###`) for subsections. Never use H1 in the body
- **Links**: `[[wikilinks]]` for internal cross-references, `[title](URL)` for external sources
- **Tone**: Academic, third-person, formal vocabulary, no contractions
- **Structure**: Mix of prose paragraphs and bullet points with **bold** key terms
- **Tags**: `#### Tags` section at the bottom with lowercase, underscore-separated topic tags
- **References**: `## References` section with numbered `[title](URL)` entries
- **Images**: Embedded with `![[filename.ext]]`, stored in Attachments/
- **No code snippets** unless strictly necessary — prefer prose explanations and visual diagrams
- **Mermaid diagrams** are preferred over ASCII art for visual representations

## Linking Strategy

The vault uses a hub-and-spoke linking model:

- **Hub notes** (full `#note` docs) are central topics that many smaller notes point to
- **Spoke notes** (`#quicknote`) link UP to their hub concepts
- Cross-references between related topics create a connected knowledge graph
- When adding new notes, always link to existing related concepts and update existing notes to link back

## Templates

Three standard templates in `Templates/`:

- **Note** (`#note`) — full research notes with References and Code sections
- **Quick Note** (`#quicknote`) — brief summaries with Tags section
- **Paper** (`#paper`) — academic paper summaries with Main idea, Results, Ideas for future works, In deep, References, Code, Tags

## Inbox Workflow

The `Inbox/` folder is a staging area for raw ideas, links, paper titles, and unprocessed thoughts that are not yet ready to become proper vault notes. Items land here when captured quickly and get triaged later into full `#note` or `#quicknote` entries in the appropriate folders. Skills like `clip-to-vault`, `paper-ingest`, and `search-online` can process Inbox items into proper notes. The `knowledge-gap-finder` skill also checks the Inbox for items that have been sitting unprocessed.

## Skills

The vault includes 20 Claude Code agent skills in `.skills/skills/`. The foundational skill is `obsidian-notes`, which defines writing conventions and should always be consulted when creating or editing notes. The remaining 19 are task-specific:

**Research & Analysis** — `connect-ideas` (compare notes, find hidden connections), `elaborate` (expand terse notes with context), `devils-advocate` (generate counterarguments), `cross-domain-connector` (find parallels across ML ↔ Cybersecurity)

**Study & Exam Prep** — `flashcard-generator` (Anki-style Q&A cards → Study/), `oscp-scenarios` (penetration testing practice → Study/OSCP/), `feynman-explainer` (simplify complex concepts), `interview-prep` (multi-level technical interview questions)

**Content & Output** — `content-generation` (LinkedIn/blog posts from notes), `summarize-note` (concise schematic summaries), `diagram-generator` (Mermaid diagrams from any note)

**Vault Management** — `note-health-check` (audit notes against style guide), `restructure-vault` (analyse and reorganise folder structure), `knowledge-gap-finder` (find missing notes and thin coverage), `moc-generator` (generate Maps of Contents for topic areas)

**Research Ingest** — `paper-ingest` (PDF/URL → #paper note), `literature-map` (research landscape diagrams), `clip-to-vault` (web article → vault note), `search-online` (web research → synthesised note)
