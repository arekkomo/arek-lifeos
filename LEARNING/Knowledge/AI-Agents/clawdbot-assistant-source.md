---
title: "I Turned Clawdbot Into the Ultimate Personal Assistant"
category: source
summary: Full walkthrough of building Klaus — an always-on AI executive assistant using Claude Code (Cloudbot) with a Kanban dashboard, heartbeat scheduling, proactive tasks, and 5 key hacks.
tags: [claude-code, ai-assistant, cloudbot, automation, scheduled-tasks, arek-and-co]
sources: 1
source_path: raw/I Turned Clawdbot Into the Ultimate Personal Assistant.md
source_date: 2026-01
authors: [Nate Herk]
ingested: 2026-05-10
updated: 2026-05-10
---

# Clawdbot — Ultimate Personal Assistant Setup (Klaus)

**Source:** Nate Herk / AI Automation · January 2026
**Routed by:** Operator — AI-Agents
**User Comment:** "analyze and suggest features and improvements that could benefit my Arek&Co system"

---

## TL;DR

A Claude Code (Cloudbot) instance called "Klaus" is configured as an always-on executive assistant running on a Mac Mini (or VPS). It has a custom HTML dashboard, heartbeat scheduling (every 30 min), proactive task monitoring, and builds deliverables overnight. Core setup: soul.md + user.md + heartbeat cron + Kanban dashboard + dedicated Gmail/Drive/ClickUp.

---

## Key Setup Components

**Identity files:**
- `soul.md` — who is the AI, its role and personality
- `user.md` — who is the user, business context, team, goals

**Dashboard (HTML app):**
- Status panel (idle / thinking / working + active subagents)
- Kanban board (To-Do / In Progress / Done) — AI updates as it works
- Activity log — timestamped record of every action
- Notes panel — drop a note, Claude processes within 5 min
- Docs tab — searchable file browser for generated reports

**Heartbeat (cron, every 30 min):**
- Wakes Claude, checks dashboard notes, syncs status
- Runs scheduled deliverables (daily pulse, email monitoring, ClickUp summary)
- Picks up pending Kanban tasks and works through them overnight

**Proactive workflows (weekly/daily):**
- Morning AI news briefing (personalised to user's business)
- ClickUp task summary + proactive research on flagged items
- Email monitoring every 10 min
- Weekly YouTube SWAT analysis (sent as branded PDF)
- Weekly security audit

---

## 5 Key Hacks

1. **Plan first, then create a plan doc** — ask Claude to plan, have it write that plan as a file, then say "execute plan-doc.md" — avoids context loss between steps
2. **Proactivity mandate** — explicitly tell Claude: "Based on everything you know about me, what would you proactively do to save me time? Don't wait to be asked." Then set those as scheduled tasks.
3. **Discipline through learning** — when Claude makes a mistake, ask it to spin up subagents to audit why it broke, write the analysis as a doc, and propose a permanent fix
4. **Memory discipline** — Claude wakes with no memory; explicitly prompt: "log this to your daily log / project memory / long-term memory" — don't assume it'll save the right things
5. **Queue multiple tasks** — send multiple instructions in one message; Claude queues them and executes in order. Separate messages = separate sessions with no cross-context.

---

## Memory Architecture

- `daily-log.md` — raw notes, decisions, context from each day (chosen by Claude — inconsistent)
- `long-term-memory.md` — curated highlights: facts, lessons, business context
- Project-specific memory files — per-project context (read at task start, updated at end)

**Key limitation:** Claude chooses what to save. Explicitly directing memory saves (with instructions like "log this to project memory") is critical.

---

## Cost & Infrastructure

- Runs on VPS or dedicated Mac Mini (~$50/month minimum — author estimates higher in practice)
- Costs ~$223 in tokens over 3 days using Opus 4.5 API (~quarter billion tokens)
- API required (Anthropic banning Claude Max plan usage for Cloudbot)
- Separate accounts for Gmail, Drive, Docs, ClickUp (safety: no direct access to personal env)

---

## Arek & Co Applicability Assessment

### What Arek's system already has
- Global instructions + AGENTS/Operator/ as equivalent to soul.md
- ABOUT-YOU/ folder as equivalent to user.md
- Scheduled tasks (SK-OP-02 morning briefing, this raw-ingest task)
- Log files (LEARNING/log.md, AGENTS/Operator/Logs/)
- Memory system in /memory/

### Gaps worth considering

| Klaus Feature | Arek&Co Status | Recommendation |
|---|---|---|
| Proactive task-scanning heartbeat | Missing | Add a scheduled task: daily scan of pending Operator items and surface actionable ones |
| Plan-first for complex tasks | Not formalised | Add to Operator SK: before multi-step tasks, write a plan-doc first |
| Activity Kanban dashboard | Missing | Could build a simple Dashboard.md or live artifact tracking active sessions |
| Memory discipline prompting | Partial — auto-memory exists | Add explicit memory-save steps to end of each skill workflow |
| "Save me time" prompt | Missing | Periodic Operator audit: ask Claude to surface time-saving automation opportunities |

> **Verdict:** Klaus's architecture closely mirrors Arek&Co's existing setup. The most transferable addition is the **proactive heartbeat pattern** — a short daily check-in that scans open tasks and surfaces actions without Arek having to ask. The plan-first convention is also worth formalising in complex Operator skills.

---

## Related

- [[claude-code]] — the underlying tool
- [[agentic-browsing]] — browser automation layer
- [[autonomous-ai-assistant]] — concept page for this pattern
