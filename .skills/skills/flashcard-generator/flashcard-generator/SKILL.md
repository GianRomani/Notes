---
name: flashcard-generator
description: |
  **Flashcard Generator**: Convert vault notes into Anki-style Q&A flashcards for active recall learning.
  - MANDATORY TRIGGERS: flashcard, flashcards, generate cards, create cards, quiz, q&a, qna, spaced repetition
---

## Purpose

The flashcard generator transforms conceptual notes from the vault into high-quality study cards suitable for spaced repetition systems (Anki, Quizlet, RemNote). It emphasizes active recall, not passive recognition, and produces cards that test understanding rather than mere memorization.

## Input

Accepts:
- A full note or note selection from the vault
- Optional difficulty level specification (basic, intermediate, advanced)
- Optional topic/subtopic filter (e.g., "create intermediate cards only")
- Optional focus area (e.g., "create exploitation scenario cards")

## Output Format

Cards are generated as a markdown file saved to:
- `Study/OSCP/` for cybersecurity/OSCP content
- `Study/{topic}/` for non-OSCP topics (e.g., `Study/Machine Learning/`, `Study/NLP/`)

Format specification:
```markdown
2026-02-20 14:30
#quicknote

## Flashcard Set: [Topic Name]

Generated from [[original-note-title]].

### [Subtopic 1]

**Q:** [Question in active voice, testing understanding not definitions]
**A:** [Concise answer with 1-2 sentences, may include wikilinks]

**Q:** [Next question]
**A:** [Next answer]

### [Subtopic 2]

[Cards continue...]

---

**Total Cards Generated**: N

#### Tags
flashcards, active_recall, [topic_tag], [subtopic_tag]
```

## Card Quality Guidelines

The agent must create **atomic** cards:
- One concept per card (not compound questions)
- Answer is 1-3 sentences (not essays)
- No ambiguity in question or answer
- Testable: clear right/wrong answer

## Card Types

Mix all four types:

1. **Recall Questions** (30%)
   - "What is privilege escalation?"
   - "Name three methods for vertical privilege escalation."
   - Tests basic knowledge retrieval

2. **Scenario-Based Questions** (35%)
   - "You discover a buffer overflow vulnerability in a SUID binary. What is your first exploitation step?"
   - "During post-exploitation, you find plaintext credentials in /tmp/. What is the highest-value target?"
   - Tests application and decision-making

3. **Comparison Questions** (20%)
   - "Compare stack overflow vs. heap overflow: which is easier to exploit and why?"
   - "What is the key difference between supervised and unsupervised clustering?"
   - Tests deeper understanding and nuance

4. **Edge Case / "What Would You Do?" Questions** (15%)
   - "ASLR is enabled and you have a buffer overflow. How does this change your approach?"
   - "If your SQL injection payload is blocked by WAF, what alternative syntax might work?"
   - Tests practical problem-solving

## Process

1. **Parse the input note** — Extract key concepts, definitions, techniques, examples, and relationships
2. **Identify subtopics** — Group related concepts into logical study units
3. **Generate diverse questions** — Ensure mix of question types listed above
4. **Validate clarity** — Each Q/A must be unambiguous and testable
5. **Add internal links** — Use `[[wikilinks]]` to related vault notes where applicable
6. **Count and organize** — Group by subtopic, include total card count
7. **Add frontmatter** — Include today's date and `#quicknote` tag
8. **Save to vault** — Write file with appropriate path and filename

## Example Card (Good)

**Q:** You successfully gain low-privilege shell access to a Linux target. The system runs a custom SUID binary compiled with stack canaries but no ASLR. What vulnerability would you target first for privilege escalation?

**A:** A stack-based buffer overflow in the SUID binary. Stack canaries prevent simple overflow, but without ASLR the function return address location is known, allowing you to build a ROP gadget chain around the canary.

## Example Card (Poor — avoid)

**Q:** What are buffer overflows?

**A:** A type of vulnerability where data exceeds allocated memory.

## Special Rules for OSCP Content

- Emphasis on **enumeration-first** questions (reconnaissance, scanning, service version detection)
- Include **post-exploitation goal clarification** ("What do you do after gaining shell?")
- Scenario cards must reference **specific tools** where applicable (Nmap, Metasploit, Burp Suite, impacket, etc.)
- Include **time constraints** where relevant ("You have 15 minutes remaining in the exam...")
- Add difficulty estimation to group cards logically

## Integration

If the original note contains a `## References` section, create one card per major reference asking "What are the key takeaways from [source]?" to encourage deeper vault exploration.

After generation, the agent should suggest which existing vault notes the user might review alongside these cards to reinforce understanding.
