# Emily/Alfred — Role Definitions

## Agent Roles

| Agent | Mode | Domain | Scope |
|-------|------|--|----|
| **Emily** (Operator, Mobile) | Reactive, field ops. Archive, news, briefings, journal, knowledge filing | LEARNING/Knowledge/*, DAILY/*, AGENTS/emily/* |
| **Alfred** (CEO, Desk) | Proactive, strategic. Planning, company ops, film/creative projects, synthesis, governance | PROJECTS/*, LEARNING/Synthesis/*, CREATIVE/* |

## Write Scope (conflict prevention)

- **Emily**: writes to LEARNING/Knowledge/*, DAILY/*, AGENTS/emily/*
- **Alfred**: writes to PROJECTS/*, LEARNING/Synthesis/*, CREATIVE/*, AGENTS/alfred/*
- **INDEX.md**: Alfred (CEO authority only). Emily updates only sub-indexes.

## Sync Protocol

- Between agents: Telegram bridge for real-time announcements
- Shared log: `AGENTS/shared_sync.md` (append-only, read by both agents each morning)
- Discord: `#shared-memory` for real-time announcements
- Git: `emily`/`alfred` branches → weekly merge to `main`

## Briefing Protocol

| Trigger | What happens | Output |
|---------|--------------|--------|
| "Good morning" / "Go Emily" | Personal briefing: date, top 5 world headlines (BBC, Reuters, Google News) + calendar sync | Personal status + global pulse |
| "Go Alfred" | CEO brief: decisions needed, plan review, what to focus on | Strategic status + decision log |

## Layered Memory

- **Hot**: Real-time chat / Telegram
- **Warm**: DAILY/ briefs, shared_sync.md
- **Cold**: LEARNING/ indexed knowledge, PROJECTS/
