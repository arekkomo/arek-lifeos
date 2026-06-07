---
name: arek-and-co
domain: life-os
version: 1.1
description: Full Arek & Co. Life OS schema — vault structure, agent roles, operations, iron rules. Loaded to keep me aligned with the vault system. Updated 2026-05-31 to reflect Brief.md fixes.
---

# Arek & Co. — Personal Operating System

> **Owner:** Arek Komorowski
> **Vault:** ~/Obsidian/Arek&Co/
> **Schema file:** CLAUDE.md (the complete schema — always read that as primary reference)
> **Operator:** Alfred (Chief of Staff)

## What This Is

Arek's personal operating system — a second brain and life management system built in Obsidian.

**Primary domains:** AI video generation, AI image generation, filmmaking, VFX, DaVinci Resolve, AI agents & automation, n8n, content creation, music production.

## Vault Structure Summary

- **raw/** — IMMUTABLE sources. READ ONLY. Never write.
- **LEARNING/** — Knowledge base. All writes go here.
  - **Knowledge/** — 8 disciplines: AI-3D, AI-Agents-n8n, AI-Image-Midjourney, AI-Video, DaVinci-Resolve, Filmmaking, Motion-Capture, Web-Design
  - **Notes/** — Arek's personal notes (currently nearly empty)
  - **Books/** — Book summaries
  - **Synthesis/** — High-level overviews
  - **Directing-Path/** — Directing curriculum
  - **index.md** — Content catalog
  - **log.md** — Append-only op log
  - **Synthesis.md** — Cross-domain synthesis
- **ABOUT-YOU/** — Personal profiles: General, Creative, Finance, Health, Working-Patterns, Writing-Rules
- **AGENTS/** — 8 agents with Brief.md, CoWork instructions, Heartbeat.md
  - Accountant, Coach, Connector, Director, Operator, Scholar, Strategist, System
- **Dashboard.md** — Command center (last updated 2026-05-31)
- **PROJECTS/** — Arek-Co-OS, CHS, RealityRowHub, Hermes-Installation
- **CREATIVE/** — Aiah-Syn, Film Projects, Song Projects, etc.
- **DAILY/** — Briefings (20+) + Journal. Subfolders: `Briefings/`, `Journal/`, `Diary/`
  - **NB:** Schema defines DAILY/ but subfolders may not exist on disk. Always verify+create on first use.
- **FINANCE/** — CHS-Accounting-Setup, CHS-Expenses
- **HEALTH/** — Fitness, Nutrition, Insurance, Measurements
- **META/** — Changelog, Templates
- **PEOPLE/** — Contacts, Directors
- **SKILLS/** — 39 skill files (SK-XX-NN format)
- **VFX/** — Expertise, Projects, Memberships

## ⚠️ Pitfalls

- **Vault path quoting**: The vault at `~/Obsidian/Arek&Co/` has an ampersand in the name. **Never interpolate this path in shell commands without quoting** — unquoted `&` causes shell parsing to split the path (`/home/realityrove/Obsidian/Arek` only). Always use `"` or `'` around the path, or prefer file tools (read_file, write_file, search_files) which accept raw paths without shell interpretation.
- **DAILY folders may be empty on disk**: The schema defines `DAILY/` structure but subfolders (`Briefings/`, `Journal/`, `Diary/`) may not exist. Verify with `ls` or file tools, create if missing before first use.

## Knowledge Operations

### Ingest (/wiki-ingest <path>)
1. Read raw/<path> — present TL;DR to user
2. Wait for confirmation
3. Write to LEARNING/Knowledge/<discipline>/<slug>.md
4. Create entity/concept pages (5-15 files)
5. Flag contradictions with `> ⚠️ Contradiction:`
6. Update index.md + log.md
7. Report touched pages

### Query (/wiki-query <question>)
1. Read LEARNING/index.md first
2. Pick 3-10 relevant pages across Knowledge/, Synthesis/, Notes/
3. Synthesize: direct answer → supporting detail → [[wikilinks]] citations
4. Offer to file answer as new Notes/ or Synthesis/ page

### Lint (/wiki-lint)
1. Check frontmatter on all pages
2. Find broken wikilinks
3. Identify orphans
4. Report findings

## Iron Rules
1. raw/ is immutable. Never write.
2. All writes → LEARNING/.
3. Every page has YAML frontmatter (title, category, summary, tags, sources, updated).
4. Every ingest touches ≥ 5 files.
5. Every claim has a citation.
6. Contradictions flagged inline.
7. Notes/ = Arek's thinking, no citations.
8. New discipline = new subfolder.

## Log Format
```
## [YYYY-MM-DD] <op> | <title>
<optional detail>
```

## Agent Reference (Legacy — 7 agents)
| Agent | Reads | Writes |
|-------|-------|--|
| Director | ABOUT-YOU/Creative, CREATIVE/ | CREATIVE/ |
| Strategist | ABOUT-YOU, SKILLS/, PROJECTS/ | SKILLS/, VFX/, PROJECTS/ |
| Accountant | ABOUT-YOU/Finance, FINANCE/ | FINANCE/ |
| Coach | ABOUT-YOU/Health, HEALTH/ | HEALTH/ |
| Operator | AGENTS/Operator/, DAILY/ | DAILY/, AGENTS/Operator/Logs/ |
| Scholar | LEARNING/, raw/ | LEARNING/ |
| Connector | PEOPLE/ | PEOPLE/ |
| System | AGENTS/System/ | AGENTS/System/Tech-Setup/ |

## Live Agents (Emily / Alfred dual-operator architecture)

See `references/emily-alfred-architecture.md` for the full Hot/Warm/Cold memory model and sync protocol.

| Role | Agent | Write Scope | Brief Trigger |
|------|-------|------------|--------------|
| Field/Mobile | **Emily** | `LEARNING/Knowledge/*`, `DAILY/*`, `AGENTS/emily/*` | "Good morning" or "Go Emily" |
| CEO/Desk | **Alfred** | `PROJECTS/*`, `CREATIVE/*`, `LEARNING/Synthesis/*`, `AGENTS/alfred/*` | "Go Alfred" (on demand) |

**Index management**: Alfred updates root `INDEX.md`. Emily updates sub-indexes only.
**Sync**: Via `AGENTS/shared_sync.md` (append-only log) + Telegram (interface layer).
**Backups**: Unified `arek-lifeos` repo on GitHub — covers both vault + `.hermes` config. Automated daily cron backup runs both.

## Agent Brief.md Status
> **IMPORTANT (2026-05-31):** Originally, 7 of 8 agent Brief.md files were identical 10-line empty shells with `[DATE]` as the date. All have now been populated from the CoWork instruction files. If a Brief.md still has `[DATE]`, it hasn't been filled yet and needs attention.

## Style
- Concise. Pages are read, not generated.
- Short paragraphs, bullets where appropriate.
- Cite with [[wikilinks]].
- When unsure, say so. Update updated: frontmatter on every edit.

## Vault-as-Single-Source Principle
> Nothing important should exist ONLY outside the vault. Everything that matters should be stored in the vault first; `.hermes/` copies are working mirrors/shortcuts.

### Skill Mirroring
- Vault source: `~/Obsidian/Arek&Co/SKILLS/` — this is the authoritative copy
- Working dir: `~/.hermes/skills/` — symlinked to `~/Obsidian/Arek&Co/SKILLS/`
- `.skill` files (compiled format) go into vault as-is
- See `references/skill-vault-mirroring.md` for full implementation details and pitfalls

## Status (2026-05-31)
| Area | Status |
|------|--------|
| Vault structure | Complete |
| Knowledge subfolders | Complete (8 disciplines) |
| Agent Briefs | ✅ Complete (8 agents — filled from CoWork) |
| Agent Brief.md stubs | ⚠️ Originally 7/8 were empty (now fixed) |
| SKILLS | 39 skills |
| LEARNING/Notes/ | 1 file — needs content |
| Knowledge content | Thin — needs depth |
| Accountant workflow | Pending |
| Connector workflow | Pending |
See Also:
- CLAUDE.md (vault - full schema)
- [Layered Memory Architecture](../../layer-memory) — Hot/Warm/Warm/Cold memory model
- [Kanban Multi-Agent Architecture](references/kanban-multi-agent-architecture.md) — SQLite-backed coordination pattern for multi-agent fleets (Tombi Studio)
- references/emily-alfred-architecture.md — Emily/Alfred dual-agent schema, triggers, sync protocol, write scopes
- references/skill-vault-mirroring.md — Vault-as-single-source pattern and skill mirroring implementation
