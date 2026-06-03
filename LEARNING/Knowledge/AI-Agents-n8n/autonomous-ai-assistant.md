---
title: Autonomous AI Assistant (Cloudbot Pattern)
category: concept
summary: Architecture pattern for running Claude Code as an always-on personal executive assistant — heartbeat scheduling, identity files, Kanban tracking, proactive workflows, and memory discipline.
tags: [claude-code, cloudbot, autonomous-agent, scheduled-tasks, personal-assistant, arek-and-co]
sources: 1
updated: 2026-05-10
---

# Autonomous AI Assistant (Cloudbot Pattern)

A design pattern for running Claude Code as an always-on executive assistant that works proactively, builds deliverables overnight, and self-directs through a heartbeat loop.

---

## Core Pattern

```
Identity files (soul.md + user.md)
     ↓
Heartbeat cron (every 30–60 min)
     ↓
Pick up queued tasks → execute → log → commit
     ↓
Scheduled deliverables (daily/weekly)
     ↓
Dashboard (status + Kanban + log + docs)
```

---

## Key Principles

**Identity before tasks.** Start with a long "getting to know you" session. Let Claude interview you. This creates persistent soul + user files that anchor every future session.

**Plan-first convention.** For any multi-step task, ask Claude to write a plan doc first, then execute from that doc. Context is preserved even when Claude "wakes up" with no memory.

**Heartbeat loop.** A cron that wakes Claude every 30 min — checks dashboard notes, picks up pending tasks, updates Kanban, runs scheduled deliverables. This is what enables overnight builds.

**Memory discipline.** Claude chooses what to remember. Explicitly direct saves: "log this to project memory", "add this to long-term memory". Don't assume.

**Proactivity mandate.** Ask Claude: "Based on everything you know about me, what would you proactively do to save me time without being asked?" Then schedule those answers.

---

## Infrastructure

- Dedicated machine (Mac Mini or VPS) — must stay on
- Separate Gmail / Drive / task management accounts for Claude (not directly in your environment)
- API billing (not Claude subscription — TOS issues with Cloudbot usage)
- `.env` file for credentials (never in conversation history)

---

## Sources

- [[clawdbot-assistant-source|Klaus (Nate Herk) — Ultimate Personal Assistant]] — Full Klaus implementation walkthrough
