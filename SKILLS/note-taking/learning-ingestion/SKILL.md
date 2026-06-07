---
name: learning-ingestion
description: When the user shares a video, article, or link for learning or a project, check the existing vault for similar topics, synthesize a rapport/opinion, and log the insights to LEARNING/.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [learning, vault-ingestion, youtube, article, research]
    related_skills: [youtube-content, kanban-codex-lane]
---

# Learning Ingestion Protocol

## When to use
- The user pastes a YouTube link (or other media) related to one of their areas of life or an active project.
- The user explicitly asks for research or learning on a topic.

## Workflow

1. **Fetch & Analyze**
   - If YouTube: use `youtube-content` skill to fetch transcript/metadata.
   - If article/podcast: fetch the content and extract key insights.

2. **Check the Vault (Vault Scan)**
   - Search `LEARNING/Knowledge/` (using `grep` or `rg`) for topics, entities, or tags that overlap with the new input.
   - Search `ABOUT-YOU/` to see if this relates to Arek's current preferences, projects, or business strategy.
   - *Note: Do not write to the `raw/` folder. Those are strictly immutable source documents. Place new transcripts/sources in `LEARNING/transcripts/` instead.*

3. **Synthesize & Report**
   - **If overlap exists:** Provide a "Vault Rapport." e.g., "We already logged [Topic X] on [Date]. This new source adds [Point A] which contradicts [Point B] from last month, but aligns with our current [Project Y] strategy."
   - **If no overlap (New):** Provide "Honest Opinion." Analyze the content's value and how it might serve your Life OS or active projects. Be direct: "This is solid for [X] but completely irrelevant for your movie project," or "This directly supports the strategy you defined for Arek & Co."

4. **Log to Vault**
   - Create/Update the page in `LEARNING/Knowledge/<topic>.md` with YAML frontmatter.
   - Add the source to `LEARNING/transcripts/` (transcript, summary, key quotes).
   - Update `LEARNING/index.md`
   - Append to `LEARNING/log.md` using the standard log format.

## Output Format (for the user)
```
## 🧠 Vault Rapport / New Insight
**Source:** [Title/URL]
**Status:** [Overlap with existing vault / Brand new topic]
**Synthesis:** [Your analysis]

## 📝 Vaulted
**Created:** `LEARNING/Knowledge/...`
**Source:** `LEARNING/transcripts/...`
**Index Updated:** `LEARNING/index.md`
**Log Updated:** `LEARNING/log.md`
```

## Common Pitfalls
- **Context Rot:** Don't paste a full transcript into the chat. Summarize the insights, then log the full thing to the vault.
- **Confusing `raw/` and `LEARNING/`:** `raw/` is for *you* (the user) to put things that never get touched. `LEARNING/` is for *me* (the agent) to actively use. New ingestions go to `LEARNING/`.

## Verification
- [ ] Did we find any existing related topics in the vault?
- [ ] Is the new content logically connected to the vault or the user's current life/projects?
- [ ] Was the content actually logged (not just summarized in the reply)?
