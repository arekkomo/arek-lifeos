---
title: "I Tried 100+ Claude Code Skills. These 6 Are The Best (Nate Herk)"
category: source
summary: Practitioner breakdown of the 6 highest-value Claude Code skills for client work — skill-creator, superpowers, GSD, /review, context-mode, and claude-mem.
tags: [claude-code, skills, context-engineering, agentic-workflows, productivity]
sources: 1
source_path: raw/I Tried 100+ Claude Code Skills. These 6 Are The Best.md
source_date: 2026-05
authors: [Nate Herk (Uppitai)]
ingested: 2026-05-14
updated: 2026-05-14
---

# Source: I Tried 100+ Claude Code Skills. These 6 Are The Best

**Original:** https://www.youtube.com/watch?v=eRS3CmvrOvA  
**Channel:** Nate Herk  
**Published:** 2026-05-03  

> **Arek's Comment:** "those are also interesting skills for claude code, can you check if i already have those skills and if not can we implement some of them that could be useful?"
> ⚠️ **Action Required:** Arek wants these skills reviewed against his current setup and useful ones implemented. This requires a live session — flagged for follow-up.

---

## TL;DR

After 400 hours in Claude Code across real estate, HVAC, coaching, and marketing agency clients, Nate identifies 6 skill categories that clients actually pay for. The theme: skills that prevent mistakes, manage context, and build reliably. Two of the six (skill-creator, frontend-design) are already installed in Arek's setup.

---

## Current Install Status vs. Arek's Setup

| Skill | Status | Install Command |
|---|---|---|
| skill-creator | ✅ Already installed | — |
| superpowers | ❌ Not installed | `npx get-shit-done-cc --claude --global` (same npm, separate) |
| GSD (get-shit-done) | ❌ Not installed | `npx get-shit-done-cc --claude --global` |
| /review & /ultra-review | ✅ Built-in (CC 2.1.86+) | No install needed |
| context-mode | ❌ Not installed | `/plugin marketplace add mksglu/context-mode` then `/plugin install context-mode@context-mode` |
| claude-mem | ❌ Not installed | `/plugin marketplace add thedotmack/claude-mem` then `/plugin install claude-mem` |
| frontend-design (bonus) | ✅ Referenced in existing setup | `/plugin install frontend-design@claude-plugins-official` |

---

## The 6 Skills

### 1. Skill Creator (✅ Installed)
**Purpose:** Build, test, and package new skills from plain English.  
- Describe what you want; Claude drafts the skill, iterates, and packages it
- Can convert an SOP document into a reusable skill
- Install globally so it's available in any project
- The "factory" — every other skill is built with this one

**Key insight:** Skills don't need to be hand-coded. Claude Code builds its own tools.

### 2. Superpowers
**Purpose:** Senior developer discipline — plan before coding.  
- Forces plan → isolated environment → tests before code → 2-stage review (spec match + code quality)
- 150,000+ GitHub stars; one of the most popular community skills
- Addresses the #1 failure mode: Claude sprints to write code before thinking
- Targets 80% first-pass quality vs. 60% without it — fewer debug cycles, lower token costs

**Why it matters for Arek:** Any automation or agent built for RealityRowHub or client work benefits from this discipline. Production-grade output.

### 3. GSD — Get Shit Done
**Purpose:** Context engineering — fresh sub-agents prevent context rot.  
- Spawns a clean sub-agent for each task; main session stays uncluttered
- Built-in quality gates: scope detection (catches silently dropped requirements), security enforcement
- Autonomous mode: hand Claude a spec, it plans/executes/commits without babysitting
- **Context rot:** Around session midpoint, long context causes Claude to forget requirements, skip steps, and call things done prematurely. GSD prevents this.

**Install:** `npx get-shit-done-cc --claude --global`  
**Help:** `/gsd-help` inside Claude Code

**Trade-off:** Not a token saver — sub-agents cost tokens. Saves the hours wasted redoing broken work.

### 4. /review & /ultra-review (✅ Built-in)
**Purpose:** Structured code review without extra installation.  
- `/review` — local, fast, free (beyond usage tokens). Catches bugs, edge cases, design issues.
- `/ultra-review` — cloud sandbox, parallel reviewer agents, only confirmed bugs reported (each bug independently reproduced before surfacing). Costs $5–20/run; Pro/Max plans get 3 free tries.
- **Workflow:** Plan (Superpowers) → Execute (GSD) → Review (/ultra-review before any important merge)
- **Requires:** Claude Code 2.1.86+, signed-in Claude account (API key alone won't work)
- **When to use /ultra-review:** Big refactors, anything touching payments/auth/database migrations

### 5. Context Mode
**Purpose:** Compress raw tool output; rebuild session context after compaction.  
- Routes tool calls through a sandbox; returns only the relevant extract to context (56KB Playwright → 299 bytes; 315KB total output → 5KB per session)
- Tracks every file edit, task, decision, error in local SQLite
- When Claude compacts the conversation, Context Mode rebuilds a snapshot and injects it back — Claude picks up exactly where it left off
- Sessions that previously fell apart at 30 min now run for 3 hours

**Install:** `/plugin marketplace add mksglu/context-mode` then `/plugin install context-mode@context-mode`  
**Stats:** Run `/contextmode:ctx-stats` to see your compression numbers

### 6. Claude Mem
**Purpose:** Cross-session memory — eliminates the "startup tax" on every new session.  
- Hooks into session lifecycle: captures file edits, decisions, bug fixes, commands
- Compresses into semantic summaries stored in local SQLite with vector search
- On session start: injects only relevant past context (3-layer retrieval: index → timeline → details)
- Auto-generates and updates folder-level CLAUDE.md files as you work
- Reports ~10× token savings on retrieval vs. dumping everything at session start

**Install:** `/plugin marketplace add thedotmack/claude-mem` then `/plugin install claude-mem`  
**Warning:** Do NOT run `npm install` directly — that installs the SDK only; hooks never register. Use the two plugin commands above.

### Bonus: Frontend Design (✅ Referenced in existing setup)
**Purpose:** Makes Claude Code HTML/UI output look less AI-generated.  
**Install:** `/plugin install frontend-design@claude-plugins-official` (install globally)

---

## Key Concept: Context Rot
A predictable degradation pattern: ~halfway through a long Claude Code session, context fills up and Claude starts forgetting requirements, skipping steps, and marking incomplete work as done. GSD (sub-agents) and Context Mode (compression + session tracking) are both solutions to this problem.

---

## Relevance to Arek & Co.

- **Superpowers** — high value for any coding work (n8n, agents, web); enforces plan-before-code
- **GSD** — high value for long-running agentic tasks (Operator scheduling, complex Director pipelines)
- **Context Mode** — high value for Arek's daily Cowork sessions which run long
- **Claude Mem** — high value; Arek already has a manual memory system — ClaudeMem would automate it further (evaluate overlap with existing /AGENTS/Operator memory system before installing)

## Related Pages
- [[claude-code]] — main entity page
- [[claude-code-skill-patterns]] — patterns and taxonomy across all skill tutorials
- [[claude-code-skills-daily-7-source]] — companion tutorial from RoboNuggets (Jay)
- [[skill-self-improvement-loop]] — Karpathy eval loop for skill quality
