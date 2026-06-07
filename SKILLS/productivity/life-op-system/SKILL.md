---
name: life-op-system
title: Life OS Architecture
description: Build and operate a personal operating system with a multi-agent vault (Obsidian), routing, and a Chief-of-Staff/Operator agent that manages daily rhythm.
---

# Life OS — Personal Operating System Architecture

> Umbrella skill for building and operating a personal operating system: multi-agent vault (typically Obsidian) that organizes different life domains into specialized agents with a central routing/Chief-of-Staff agent.

## Architecture

A Life OS has two layers:
1. **Obsidian vault** -- structured knowledge base (agents, projects, daily journal, personal profiles)
2. **AI agents** -- specialized roles that manage sub-domains, routed by a central Operator/Chief-of-Staff

### Standard 8-Agent Layout

| Agent | Domain | Reads | Writes |
|-------|--------|-------|--------|
| **Operator** (Chief of Staff) | Intake, routing, briefing, journaling, contacts, email | Operator/ folder, DAILY/ | Operator/Logs/, DAILY/ |
| **Strategist** | Planning, curriculum, milestones, roadmaps | ABOUT-YOU, SKILLS/, PROJECTS/ | SKILLS/, PROJECTS/ |
| **Director** | Creative direction, vision, pipelines | ABOUT-YOU/Creative, CREATIVE/ | CREATIVE/ |
| **Scholar** | Learning, knowledge curation, synthesis | LEARNING/, raw/ | LEARNING/ |
| **Accountant** | Finance, tax, investments, insurance | ABOUT-YOU/Finance, FINANCE/ | FINANCE/ |
| **Coach** | Health, fitness, nutrition, sleep | ABOUT-YOU/Health, HEALTH/ | HEALTH/ |
| **Connector** | Relationships, contacts, social calendar | PEOPLE/ | PEOPLE/ |
| **System** | Tech setup, tools, hardware inventory | AGENTS/System/ | AGENTS/System/ |

### Vault Structure

```
VaultRoot/
|-- ABOUT-YOU/           <- personal profiles (General, Creative, Finance, Health)
|-- AGENTS/              <- 8 agent roles, each with Brief.md, CoWork-Instructions.md, Heartbeat.md
|-- Dashboard.md         <- top-level command center
|-- PROJECTS/            <- non-creative projects
|-- CREATIVE/            <- creative projects (film, music, content)
|-- DAILY/               <- daily journal entries
|-- FINANCE/             <- financial statements & tracking
|-- HEALTH/              <- health metrics, fitness plans
|-- LEARNING/            <- knowledge base + raw sources
|   |-- Knowledge/       <- processed knowledge pages
|   |-- raw/             <- immutable sources
|-- PEOPLE/              <- contacts & relationships
|-- SKILLS/              <- skill tracking
|-- META/                <- changelog, infrastructure
```

## The Operator (Chief of Staff)

The first point of contact for everything. Receives all input, routes to specialist agents, delivers daily briefing.

### Routing Table (Input Processing)

**95% Confidence Rule:** Before routing, assess confidence. If below 95%, stop and ask: *"Confidence below 95%. Should this be [PREFIX]?"* Do NOT auto-route on uncertain input.

| Input Type | Route To |
|------------|----------|
| Creative idea, film, song, music, video | Director |
| Article, transcript, research, link | Scholar |
| Task, project, deadline, planning | Strategist |
| Finance, tax, spending, income | Accountant |
| Fitness, nutrition, sleep, health | Coach |
| Contact, relationship, event | Connector |
| Tech, tools, vault, agent setup | System |
| Anything else / ambiguous | Ask user |

### Prefix Legend

| Prefix | Purpose |
|---|---|
| `*fin:*` | Finance, investing, money |
| `*write:*` | Drafting, editing, prose |
| `*project:*` | Task updates, blockers, goals |
| `*research:*` | Deep dive, web investigation |
| `*diary:*` | Personal daily reflection |
| `*context:*` | Archive info/learnings to vault |
| `*meta:*` | IT, setups, configs, devops |

### Morning Briefing Structure (Standard)

1. **Date + Day** + notable events
2. **📂 Previous Days Log** -- scan `DAILY/` for last 2-3 days: key decisions, progress, open threads
3. **🔥 Open Decisions** -- flag items needing Arek's input (search vault `PROJECTS/`, session history)
4. **📰 Top 5 Headlines** -- Google News RSS
5. **🎬 Film/VFX Industry** -- THR, Variety, Animation Magazine, After Effects World, VFX Voice (exclude sports)
6. **🎪 Vancouver Events** -- Daily Hive, Vancouver.com/events, Meetup (non-sport only)
7. **🧠 Chief's Recommendation** -- 1-3 actionable items based on living context

Format: Scannable headers, short bullets, no lengthy prose.

### Morning Briefing Structure (Expanded -- user-triggered via "Want the AI research section?")

8. **🤖 AI Industry** -- latest Claude Code, LLM, and AI tool news
9. **🔮 Emerging Tech** -- notable announcements in AI, robotics, web3, or adjacent spaces
10. **🎯 Cross-Domain Synthesis** -- connections the user would miss (e.g., "this VFX news aligns with X project")

### Journal Protocol

When user says "journal" -- ask questions one at a time, don't dump. Synthesize into entry.
Sections: narrative, Wins, Challenges, Insights, Tomorrow's Focus.

### Operator Working Style

- Concise. No preamble. No filler phrases. No "Great question!" or lengthy sign-offs.
- Direct pushback when patterns are worth challenging.
- Start broad, go deep only when asked.
- Accountability over hand-holding.
- Connect ideas across domains -- synthesis over details.

## Long-Term Career Goals (Multi-Agent Pattern)

When the user sets a career or professional goal that spans agent domains, do NOT just file it under one agent. Use this pattern:

**Step 1: Identify the primary agents** — the goal likely touches Strategist (career strategy), Director (creative alignment/portfolio), Connector (relationships/network), and potentially others.

**Step 2: Create a central strategy doc** in the relevant domain folder (e.g. `VFX/Career-Goals/<Goal-Name>.md`). The doc should include:
- Why this goal matters (not just "get a job" but what the goal represents)
- The target's aesthetic/values (what they actually look for — not just the name)
- Key people/studios to study and why
- Phased plan (years, not months)
- Success criteria (concrete signals, not "get hired")
- Cross-agent division of labor (what each agent does)
- Key tensions (especially time/portfolio balance)

**Step 3: Update Brief.md in each affected agent** — add a "Strategic Career Goal" section to each Brief with:
- Their specific role in this goal
- The concrete deliverable they produce (not "help with career" — "build the creative portfolio pieces in the right aesthetic")
- A link to the central strategy doc

**Step 4: Update Strategist Brief** — add the goal to Active Goals list. Use markdown bold for strategic (long-term) goals to distinguish them from operational goals.

**Critical pitfall:** The early work on a career goal is almost always **understanding the aesthetic/values of the target**, not the logistics. A24 doesn't hire on technique alone — on creative taste alignment. The Director's job is to build pieces IN that aesthetic, not just "make a reel."

## Core Rules

1. raw/ is immutable -- read only, never write.
2. All writes go to their proper domain folder -- no exceptions.
3. Every agent has read/write boundaries -- respect them.
4. Ask before routing if ambiguous -- never guess.
5. Route to primary agent but flag secondary if input crosses domains.

## Real-World Reference

Designed from the Arek & Co. Life OS (implemented Claude Code, migrated to Hermes). See references/ for detailed architecture files.

## Absorbed Operational Playbooks

This skill is the umbrella for Life OS architecture plus its core operational roles and maintenance protocols. Former narrow role/protocol skills are preserved as references:

- `references/alfred.md` — CEO/strategic agent role definition
- `references/operator.md` — Emily/Operator field-ops role definition
- `references/operator-emily-alfred-routing.md` — Emily/Alfred routing notes
- `references/operator-news-source-accessibility.md` — news/source accessibility notes
- `references/content-ingestion.md` — link/article/video ingestion protocol
- `references/backup-and-sync.md` — Obsidian + `.hermes` backup workflow
- `references/backup-and-sync-backup-state-2026-06-03.md` — session-specific backup state

### Alfred / CEO role

Alfred is the strategic/CEO side of the Life OS: company governance, creative strategy, project architecture, high-level synthesis, and root index authority. Keep Alfred's write scope focused on `PROJECTS/`, `CREATIVE/`, `LEARNING/Synthesis/`, `AGENTS/alfred/`, and top-level index governance.

### Emily / Operator role

Emily is the mobile Chief-of-Staff/field-ops side: intake, routing, journaling, briefings, news, daily admin, and knowledge filing. Keep Emily's write scope focused on `LEARNING/Knowledge/`, `DAILY/`, and `AGENTS/emily/`; she reads strategic areas for context but does not own root strategy.

### Content ingestion protocol

For links, articles, videos, and learning dumps: scan the vault first, produce either a vault rapport (if overlap exists) or an honest opinion (if it is new), then log processed material to the correct Life OS locations. Never write into immutable `raw/` as if it were processed knowledge.

### Backup and sync protocol

For Life OS maintenance, check both the Obsidian vault and `.hermes` state, commit meaningful changes, and push to the configured remote. Preserve backup-state notes as references, not separate active skills.