---
name: content-generation
description: |
  **Content Generator**: Transform vault notes into professional social media posts, blog articles, or published content by extracting key insights and adapting tone for the target platform.
  - MANDATORY TRIGGERS: publish, linkedin, blog, article, post, social, content, share, make shareable
---

## Overview

This skill transforms academic or technical knowledge vault notes into polished, platform-appropriate content for LinkedIn, blog posts, and articles. The agent adapts Gianfranco's insider perspective on ML engineering, AI security, and MLOps into engaging narratives that resonate with professionals while maintaining credibility and depth.

## Target Platforms & Tone Adaptation

**LinkedIn Posts** (150–300 words):
- Conversational, first-person voice ("I've learned...", "Here's what I found...")
- Hook opening: provocative question, surprising insight, or personal observation
- 2–3 key takeaways, clearly structured
- Call-to-action: question to readers, invitation to discuss, or "Save this for later"
- Hashtags: 3–5 relevant (`#MachineLearning`, `#MLOps`, `#AISecure`, etc.)
- Tone: accessible, relatable, thought-leadership

**Blog Posts** (600–1,500 words):
- Narrative-driven introduction with real-world context
- Structured sections with H2/H3 headers
- Mix of explanation, examples, and actionable insights
- Assume moderately technical audience (engineers, ML practitioners)
- Include visuals or diagrams where helpful
- Closing: implications or broader lessons learned
- Hashtags: not required; metadata/SEO keywords optional

**Technical Articles** (800–2,000+ words):
- Depth and nuance; cite sources and vault cross-references
- Professional, authoritative tone (suitable for Medium, Dev.to, personal site)
- Code snippets or architecture diagrams allowed
- Deep-dive into methodology, results, implications
- Conclusion with future directions or open questions

## Workflow

### 1. Input Detection
- User selects text from a vault note or provides note reference
- Agent asks (if unclear): "What format would you like? **LinkedIn post**, **blog article**, or **technical deep-dive**?"

### 2. Insight Extraction
- Identify **2–3 most shareable, non-obvious insights** from the note
- Prioritize: novel findings > practical lessons > conceptual clarity
- Avoid generic statements; surface surprising or underexplored angles
- Look for personal experience or lessons learned (Gianfranco's voice)

### 3. Structure & Adaptation
- Rewrite content in target tone; remove academic formality
- Create engaging opening hook (question, stat, or observation)
- Restructure information for readability (short paragraphs, bullets for LinkedIn; narrative flow for blog)
- Preserve technical accuracy; simplify jargon without losing precision

### 4. Call-to-Action & Engagement
- LinkedIn: end with question, invitation to debate, or "What's your experience?"
- Blog: conclusion with implications, link to related vault notes, or "What's next?"
- Article: future directions, open problems, or invitation for feedback

### 5. Output & Polish
- Generate markdown ready to copy-paste
- Suggest hashtags for LinkedIn (include in output)
- For blog/article: include title, optional subtitle, and metadata notes
- Offer revision options: "Shorter version?", "More technical?", "Different angle?"

## Example Workflow

**Input**: Selection from `[[AI Safety/Prompt Injection Vulnerabilities]]` note
```
[User selects technical explanation of prompt injection attack vectors]
```

**Agent Detects**: Blog-post request (length and depth suggest longer form)

**Agent Extracts**:
- Insight 1: Most attacks succeed via **indirect injection** (document upload, search results), not direct user input
- Insight 2: Defense requires **multi-layered approach** (parsing, sandboxing, monitoring), not single mitigation
- Insight 3: Teams overlook **supply-chain injection** (third-party APIs as attack surface)

**Agent Outputs** (Blog post structure):
```markdown
# The Supply Chain Blind Spot in LLM Security

## Why Prompt Injection Is Harder Than You Think

[Opening narrative about real-world vulnerability discovered in production]

## The Indirect Injection Problem

[Explanation of attack vectors beyond direct user input]
- Document uploads
- Web search results
- Third-party API responses

## A Layered Defense

[Multi-part strategy with examples]

## The Overlooked Vector: API Dependencies

[Deep dive on supply-chain risks]

## What's Next?

[Implications and future directions]
```

## Key Instructions

- **Tone Shift**: Remove "this paper discusses" or "one might argue"; use "here's what I learned" or "the key insight is"
- **Brevity First**: LinkedIn ≤ 300 words; cut ruthlessly
- **Preserve Links**: Convert `[[wikilinks]]` to markdown `[Title](url)` where possible; note internal references for clarity
- **Hashtags**: Suggest only if requested; for LinkedIn, include naturally woven + 3–5 topic tags
- **Offer Alternatives**: After draft, suggest: "Version without technical jargon?", "More specific to your role at Thomson Reuters?", "Shorter for LinkedIn?"
- **Do Not**: Use generic affirmations ("Great topic!", "Very important"); avoid spam-like language; never exaggerate findings
- **Metadata**: For blog/article, note SEO keywords, target audience, and reading time estimate

## Output Format

Return a markdown file with:
1. **Title** and optional **Subtitle**
2. **Metadata** (platform, word count, reading time, suggested hashtags)
3. **Content** (ready to publish)
4. **Revision Notes** (optional tweaks or alternatives suggested)

## Safety & Voice

- Maintain Gianfranco's credibility and expertise (ML scientist, OSCP-focused)
- Align with his professional identity and current role at Thomson Reuters
- Avoid over-personalizing or adding voice not supported by vault notes
- Never misrepresent findings or overstate conclusions
- Link back to vault for readers seeking deeper context
