---
title: Alfred's Side-of-the-Deal
category: synthesis
summary: CEO-level governance and vault authority for Arek & Co.
tags: [alicia, governance, vault-structure, side-of-the-deal]
updated: 2026-06-05
---

# Arek & Co. — Personal Operating System

> **Owner:** Arek Komorowski
> **Initialized:** 2026-04-27
> **Tool:** Claude Code (Claudian). A vault-wide schema for AI agents working inside Obsidian.

---

## What This Is

This is Arek's personal operating system — a second brain and life management system built in Obsidian. It combines a structured life OS (agents, areas, projects) with a living knowledge base (articles, transcripts, research).

**Primary domains:** AI video generation, AI image generation, filmmaking, VFX, DaVinci Resolve, AI agents & automation, n8n, content creation, music production.

---

## Vault Structure

```
ArekCOVault/
│
├── raw/                          ← Immutable knowledge sources (read-only)
│   └── notion-export/            ← Notion exports organized by topic
│
├── LEARNING/                     ← Knowledge base (write target)
│   ├── Knowledge/                ← External-sourced knowledge
│   │   ├── AI-Video/
│   │   ├── AI-Image-Midjourney/
│   │   ├── AI-3D/
│   │   ├── AI-Agents-automation/
│   │   ├── Filmmaking/
│   │   ├── DaVinci-Resolve/
│   │   └── Motion-Capture/
│   ├── Notes/                    ← Arek's personal notes
│   ├── Books/                    ← Book summaries and notes
│   ├── Synthesis/                ← Cross-domain synthesis
│   ├── Directing-Path/              ← Structured learning path for directing
│   └── .templates/                ← Page templates
│
├── ABOUT-YOU/                    ← Personal profiles for all agents
│   ├── About-Me-General.md
│   ├── About-Me-Creative.md
│   ├── About-Me-Finance.md
│   ├── About-Me-Health.md
│   └── Working-Patterns.md
│
├── AGENTS/                       ← Agent roles (8 total)
│   ├── Accountant/               ← Finance & tax tracking
│   ├── Coach/                    ← Health, fitness, recovery
│   ├── Connector/                ← Relationships & contacts
│   ├── Director/                 ← Vision, creative direction
│   ├── Operator/                 ← Daily execution, routing
│   ├── Scholar/                  ← Learning & knowledge synthesis
│   ├── Strategist/               ← Planning & curriculum
│   └── System/                   ← Technical setup & inventory
│
├── Dashboard.md                  ← Live command center
├── PROJECTS/                     ← Business/creative projects
├── CREATIVE/                     ← Creative projects
├── DAILY/                        ← Daily journal & diar
├── FINANCE/                      ← Financial statements
├── HEALTH/                       ← Health metrics
├── META/                         ← Vault changelog & metadata
├── PEOPLE/                       ← Contacts & relationships
├── SKILLS/                       ← Skill tracking
└── VFX/                          ← VFX career & projects
```

---

## The Knowledge Layer

### Two layers

```
raw/              → knowledge sources only (articles, transcripts, research exports). IMMUTABLE. Read only.
LEARNING/         → the knowledge base. You write here. Never write to raw/.
```

### raw/ file lifecycle

- **Source documents** (Notion exports, articles, transcripts): keep in `raw/` permanently after ingest. They are the audit trail and allow re-ingestion if needed. If the folder grows cluttered, move processed files to `raw/archived/` — never delete them.
- **Loose captures** (voice notes, quick idea drops, test files): these are NOT source documents. After routing to the correct agent/folder, delete them from `raw/`. They have no archival value once acted on.
- **Operator responsibility**: during any `raw/` scan, flag unprocessed loose captures, route them, then delete. Source documents are Scholar's domain — do not delete without explicit instruction.

> **Important — raw/ is for knowledge sources only.** Personal records (bank statements, investment summaries, insurance docs, health reports, contracts) do NOT belong in `raw/`. File them directly in their section:
>
> | Document type | Correct location |
> |---|---|
> | Bank statements, investment summaries | `FINANCE/Statements/` |
> | Insurance documents | `FINANCE/Insurance/` or `HEALTH/Insurance/` |
> | Health reports, lab results | `HEALTH/` |
> | Legal / contracts | `META/` or relevant section |
> | Creative assets | `CREATIVE/` relevant subfolder |

### Page frontmatter (required on every Knowledge page)

```yaml
---
title: <Title>
category: entity | concept | source | synthesis | note
summary: <one-line summary>
tags: [tag1, tag2]
sources: <count of sources referencing this page>
updated: YYYY-MM-DD
---
```

For `source` pages, also include:
```yaml
source_path: raw/<path>
source_date: YYYY-MM
authors: [author1, agent2]
ingested: YYYY-MM-DD
```

---

## Operations

### Ingest (`/wiki-ingest <path>`)

1. Read the source at `raw/<path>`
2. **Discuss with the user first** — TL;DR, key claims, which pages will be touched
3. Wait for confirmation
4. Determine the correct `LEARNING/Knowledge/<discipline>/` subfolder
5. Create or update the source summary at `LEARNING/Knowledge/<slug>.md`
6. Create or update relevant entity/concept pages (typically 5–15 files)
7. Flag contradictions with `> ⚠️ Contradiction:` callouts on both sides
8. Update `LEARNING/index.md`
9. Append to LEARNING/log.md`:
`## [YYYY-MM-DD] ingest | <title>`
10. Report back with a bulleted list of touched pages

### Query (`/wiki-query <question>`)

1. Read `LEARNING/index.md` first
2. Pick 3–10 relevant pages across `Knowledge/`, `Synthesis/`, `Notes/`
3. Read them in full, follow wikilinks opportunistically
4. Synthesize: direct answer → supporting detail → `[[wikilinks]]` citations → related pages
5. Offer to file the answer back as a new `Notes/` or `Synthesis/` page

### Lint (`/wiki-lint`)

1. Check all pages have required frontmatter
2. Find broken wikilinks
3. Identify concepts mentioned without their own page
4. Check for stale `updated:` dates
5. Present findings as a markdown report
6. Append a `lint` entry to `LEARNING/log.md`

---

## Iron Rules

1. **`raw/` is immutable.** You read from it; you never write to it.
2. **All writes go to `LEARNING/`.** No exceptions.
3. **Every Knowledge page has YAML frontmatter** with `title`, `category`, `summary`, `updated`.
4. **Every ingest touches ≥ 5 files.** Source summary + entity/concept pages + `index.md` + `log.md`.
5. **Every claim has a citation.** Link back to the source summary page.
6. **Contradictions get flagged inline.** Both pages get the callout.
7. **Notes/ is for Arek's own thinking.** No citations required there.
8. **New discipline = new subfolder in `Knowledge/`.** Don't dump files at the top level.

---

## Log Format

```
## [YYYY-MM-DD] <op> | <title>
<optional detail — pages touched, what changed>
```

Valid ops: `ingest`, `query`, `lint`, `create`, `update`, `delete`, `note`.

---

## Agents Quick Reference

| Agent | Reads | Writes |
|-------|--:--------|
| Director | ABOUT-YOU/Creative, CREATIVE/ | CREATIVE/, HUB/ |
| Str

[...truncated CLAUDE.md: 8,620 chars total]