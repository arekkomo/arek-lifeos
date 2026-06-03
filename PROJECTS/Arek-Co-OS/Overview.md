---
title: Arek & Co. Operating System — Project Overview
project: Arek-Co-OS
status: Active
phase: Foundation
started: 2026-04-27
updated: 2026-05-09
owner: Strategist
---

# Arek & Co. Operating System

## What This Is

A meta-project: the design, build, and ongoing evolution of the entire Arek & Co. personal operating system — the vault structure, the agent roster, the skill library, and the CoWork/Claude integration that runs it all.

This is the project that governs all other projects. When something about how the OS works needs to change — a new agent brief, a schema revision, a new skill — it lives here.

## Why It Exists

Arek's life spans multiple domains (VFX career, film directing, RealityRowHub, music, finance, health) with a full-time job consuming peak hours. Without a deliberate operating system, strategic work drowns in daily execution noise. The OS exists to:

- Reduce cognitive load on routine decisions
- Keep long-horizon goals visible when short-term pressure spikes
- Make accumulated knowledge and context reusable across sessions
- Give each agent a clear mandate so nothing falls through the cracks

## The Strategic Arc It Serves

```
VFX Supervisor (now)
    → AI-enabled Film Director (2–3 years)
        → RealityRowHub as production company (3–5 years)
```

The OS is the infrastructure that makes that arc executable — not just aspirational.

## Scope

This project tracks four workstreams:

1. **Agent Design & Briefs** — each agent's mandate, scope, skills, and interaction patterns
2. **Vault Architecture** — folder structure, templates, frontmatter schema, CLAUDE.md evolution
3. **CoWork & Plugin Setup** — connected MCPs, skills, plugins; what's working and what's missing
4. **Roadmap & Milestones** — what needs to be built, in what order, current status

## Key Decisions Made

| Decision | Rationale | Date |
|---|---|---|
| Obsidian as the vault | Markdown-native, portable, no lock-in | 2026-04-27 |
| 8-agent model | Separation of concerns across life domains | 2026-04-27 |
| Claude / CoWork as the AI layer | Best model quality + agentic file access | 2026-04-27 |
| `raw/` is immutable | Source integrity, re-ingest capability | 2026-04-27 |
| SKILLS/ as shared registry | Agents pick up skills; skills aren't embedded in agent files | 2026-04-27 |
| PROJECTS/ for non-creative work | CREATIVE/ handles creative projects; PROJECTS/ handles business/system work | 2026-05-09 |

## Related Files

- [[Architecture]] — vault structure and schema rules
- [[Agents]] — agent roster and design status
- [[CoWork-Setup]] — plugin, MCP, and skill inventory
- [[Milestones]] — phases and task tracking
- `/CLAUDE.md` — the authoritative vault schema read by all agents

## Contacts / Stakeholders

- **Owner:** Arek Komorowski
- **Primary agent:** Strategist (this project), Operator (daily execution), System (technical setup)
