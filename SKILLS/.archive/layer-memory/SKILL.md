---
name: layer-memory
domain: life-os
version: 1.0
description: Hot/Warm/Cold memory architecture for multi-agent systems. Separates ephemeral, working, and permanent data across channels and scopes.
---

# Layered Memory Architecture (Hot / Warm / Cold)

## Overview

A three-tier memory model for multi-agent and personal knowledge systems. Keeps context windows clean while ensuring nothing is lost to ephemeral conversation history.

### Architecture

```
┌─────────────────────┐
│   HOT (Ephemeral)   │   Real-time chat / CLI / Telegram
│  - Conversation     │
│  - Trigger briefings│
│  - Quick captures   │
└─────────────────────┘
        │ writes ──→
┌─────────────────────┐
│  WARM (Working)     │   Daily active state, decisions in flight
│  - DAILY/           │
│  - shared_sync.md   │
│  - Active plans     │
└─────────────────────┘
        │ writes ──→
┌─────────────────────┐
│  COLD (Permanent)   │   Archive, indexed knowledge
│  - LEARNING/        │
│  - PROJECTS/        │
│  - INDEX.md         │
└─────────────────────┘
```

### Why Three Tiers?

Without layers, LLM context windows fill with either garbage (long-lived conversations) you can't prune, or important data that gets "lost to the void." By separating concerns:

- Chat channels stay lean (no need to remember the full context of every session)
- Working context is discoverable and scoped to the right lifespan
- Permanent data is always query-able by index
- Agents have clear boundaries on what to write vs. read-only

### Tier Details

| Tier | Name | Retention | Primary Storage |
|------|------|-----------|----------------|
| 1 | Hot | Session-to-session | Real-time chat, CLI, Telegram, Discord |
| 2 | Warm | Weeks | DAILY/ active plans, briefings, AGENTS/ shared logs |  
| 3 | Cold | Permanent | LEARNING/, PROJECTS/, INDEX.md |

### Flow of Information

Data flows Hot → Warm → Cold by default:

1. **Ingest** (Hot → Warm): When user shares a link/idea in chat, Emily files to LEARNING/Knowledge/ (Cold) and logs to shared_sync
2. **Briefing** (Warm → Hot): Morning brief pulls from Warm layer to provide context
3. **Synthesis** (Cold → Warm): Alfred creates cross-domain Synthesis pages from Cold data
4. **Governance** (Cold): Only the designated CEO agent writes to INDEX.md

### Pitfalls

- **Writing to Hot as permanent storage** — Chat history degrades; if it matters, it goes to Warm/Cold
- **No write boundaries** — Without lanes, both agents overwrite each other's files. Define scopes.
- **No indexing protocol** — Cold data without updates to INDEX.md becomes an unreadable dump
- **Sync latency** — If agents don't read shared_sync.md each morning, the split-brain problem emerges

### When to Add a Fourth Tier

Some systems add a **Flash Memory** layer: LLM persistent memory (config files, skill docs, CLAUDE.md) that survives across sessions but lives outside the vault. This is the meta-level about system configuration, not about content.

## See Also

- [Life OS: Emily/Alfred Example](./life-os.md) — A concrete implementation of this pattern