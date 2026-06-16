---
title: "Hermes vs OpenClaw vs Custom Agentic OS (Simon Scrapes)"
category: source
summary: Two-video series comparing off-the-shelf agentic frameworks (Hermes, OpenClaw) against building a custom Claude Code Agentic OS — covers 5 core features, hidden costs, and what's worth implementing.
tags: [claude-code, hermes, openclaw, agentic-os, skills, memory, scheduled-tasks, arek-and-co]
sources: 2
source_path: raw/This is the Ultimate Claude Code Setup - Beats OpenClaw and Hermes!.md
source_date: 2026-04
authors: [Simon Scrapes]
ingested: 2026-05-28
updated: 2026-05-28
---

# Hermes vs OpenClaw vs Custom Agentic OS (Simon Scrapes)

**Sources:** Simon Scrapes · April–May 2026
**Videos:**
- *This is the Ultimate Claude Code Setup - Beats OpenClaw and Hermes!* (2026-04-18)
- *I Rebuilt Hermes in Claude Code (It's Ridiculously Good)* (2026-05-23)

**User Comment (Video 1):** "interesting for my setup — review and compare to Arek & Co, see what we can implement. Like the idea of self-learning skills and communication through Discord/Telegram/WhatsApp."
**User Comment (Video 2):** "since I would like to bring some Hermes functionality to Arek & Co — check and compare, tell me what could be good to implement."

---

## TL;DR

Both videos argue that building your own Claude Code Agentic OS beats off-the-shelf frameworks (Hermes, OpenClaw) because you understand every assumption, can build modularly, and can maintain it at scale. Video 1 outlines the 5 core features needed. Video 2 critiques Hermes's hidden costs and explains what's worth lifting.

---

## The 5 Core Features (Video 1)

| Feature | What it is | Arek & Co status |
|---|---|---|
| Persistent memory | Context organised in layers — agent instructions, business context, user profile, project memory | ✅ ABOUT-YOU/, auto memory, Obsidian vault |
| Self-improving skills | Skills ask for feedback, accumulate rules, improve over time | ⚠️ Calibrate skill exists but not per-skill feedback loops |
| Multi-goal interface | Manage multiple agent goals in parallel — Kanban, phone access, channels | ⚠️ Channels (Telegram/Discord) not yet configured |
| Scheduled tasks | Chain skills together into automated workflows with human checkpoint | ✅ mcp__scheduled-tasks live |
| Business context | Shared context folder pulled by every skill at runtime | ✅ ABOUT-YOU/, CLAUDE.md, agent-specific context |

---

## Hermes Hidden Costs (Video 2)

1. **Self-validation problem** — same model writes *and* grades its own skills. No external guardrails. Can silently overwrite good skill work with worse versions. No version control or audit log.
2. **Security** — OpenClaw had 200+ filed vulnerabilities; 386 malicious packages found on skills marketplace from a single threat actor. Inheriting someone else's architecture = inheriting their security problems.
3. **Single-client assumption** — Hermes requires a separate install per brand/client. Skills don't share across installs. Maintenance nightmare for multiple projects.

---

## What Hermes Does Well (Worth Lifting)

- **Identity layer injection** — memory.md + user.md injected at the start of every session (capped ~1,300 tokens for recency). Keeps agent grounded in who you are.
- **Modular skill components** — don't bake context (voice, ICP, formatting) into each skill. Keep as separate reference files; skill systems chain them. One update → propagates everywhere.
- **Human checkpoint pattern** — automated workflows do 80% of the work; outputs land in a review folder for approval before anything goes live.

---

## Skill Systems Pattern

The key architectural insight from Video 2:

> A skill is not a one-off task. A skill is a modular component that feeds into a skill system. Each one does one job, lives in one place, has a consistent name, and gets updated in one place.

Instead of a `write-linkedin-post` skill that bakes in voice + ICP + formatting → maintain `voice.md`, `icp.md`, `formatting.md` as separate reference files. The LinkedIn post skill *chains* them. When brand voice shifts → one file update → all skill systems updated automatically.

**Arek & Co relevance:** ABOUT-YOU/About-Me-Creative.md should be the single voice reference. Check that `creative-film-pipeline` and `creative-song-pipeline` reference it rather than duplicating context.

---

## Memory Architecture Comparison

| Aspect | Hermes | Arek & Co |
|---|---|---|
| Short-term injection | memory.md + user.md (1,300 token cap) | auto memory MEMORY.md loaded each session |
| Long-term recall | Keyword search only — poor if you can't remember exact words | Obsidian vault (semantic via wikilinks + structure) |
| Multi-brand/client | Separate install per client | Single install, ABOUT-YOU/ handles persona context |

Hermes's recall is weaker for long-term memory. Arek & Co's Obsidian vault + structured LEARNING/ gives better semantic retrieval.

---

## Actionable Recommendations for Arek & Co

**1. Telegram/Discord via Claude Code Channels** (low effort, high daily value)
Native Anthropic feature. Fire tasks at Arek & Co from phone, get briefings pushed out. Supports Telegram, iMessage, Discord out of the box.

**2. Per-skill feedback loops with human validation** (medium effort)
Add `learnings.md` to top skills. Each run ends with a feedback prompt. You approve changes — not autonomous (avoids Hermes's self-validation problem). Target skills: morning briefing, journal, creative-film-pipeline, creative-song-pipeline.

**3. Skill systems audit** (low-medium effort)
Verify ABOUT-YOU/About-Me-Creative.md is referenced (not duplicated) in creative skill files. One update should propagate everywhere.

---

## Related

- [[agentic-os-architecture]] — concept page
- [[skill-systems-pattern]] — concept page
- [[claude-code]] — underlying tool
- [[self-improving-skills-source]] — prior Simon Scrapes video on Karpathy loop evals
- [[clawdbot-assistant-source]] — related: Clawdbot custom assistant setup
