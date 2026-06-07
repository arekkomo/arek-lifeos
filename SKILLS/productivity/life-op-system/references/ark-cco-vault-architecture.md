---
title: Arek & Co. Vault Architecture
description: Full vault schema from the Arek & Co. Life OS implementation. Last updated 2026-04-27.
---

# Arek & Co. -- Personal Operating System

> Owner: Arek Komorowski
> Initialized: 2026-04-27

## Vault Structure

```
ArekCoVault/
|-- raw/                       <- IMMUTABLE sources. Read only, never write.
|   |-- notion-export/         <- Exported Notion knowledge base
|   |-- archived/              <- Processed archival files
|-- LEARNING/                  <- Knowledge base. You write here. Never write to raw/.
|   |-- Knowledge/             <- External sourced material
|   |-- Notes/                 <- Personal notes
|   |-- Books/                 <- Book summaries
|   |-- Synthesis/             <- High-level overviews across disciplines
|   |-- Directing-Path/        <- Structured learning path for directing
|   |-- index.md               <- Content catalog
|   |-- log.md                 <- Append-only operation log
|-- ABOUT-YOU/                 <- Personal profiles read by all agents
|   |-- About-Me-General.md    <- Core reference
|   |-- About-Me-Creative.md
|   |-- About-Me-Finance.md
|   |-- About-Me-Health.md
|   |-- Working-Patterns.md
|-- AGENTS/                    <- The 8 agent roles
|-- Dashboard.md               <- Command center
|-- PROJECTS/                  <- Non-creative projects
|-- CREATIVE/                  <- Creative projects
|-- DAILY/                     <- Daily journal
|-- FINANCE/                   <- Financial statements & tracking
|-- HEALTH/                    <- Health metrics, fitness plans
|-- META/                      <- Vault changelog & metadata
|-- PEOPLE/                    <- Contacts & relationships
|-- SKILLS/                    <- Skill tracking
|-- VFX/                       <- VFX industry work
```

## Knowledge Layer

raw/ = knowledge sources only (immuteable, read only).
LEARNING/ = the knowledge base (write here).

### raw/ lifecycle
- Source docs: keep permanently, move to raw/archived/ if cluttered, never delete
- Loose captures (voice notes, drops): route then delete after actioning
- Operator responsibility: flag unprocessed captures, route, delete

### Frontmatter (required on every Knowledge page)
```yaml
---
title: <Title>
category: entity | concept | source | synthesis | note
summary: <one-line summary>
tags: [tag1, tag2]
sources: <count>
updated: YYYY-MM-DD
---
```

### Iron Rules
1. raw/ is immutable
2. All writes go to LEARNING/
3. Every page has YAML frontmatter (title, category, summary, updated)
4. Every ingest touches >= 5 files
5. Every claim has a citation
6. Contradictions get flagged inline on both pages
7. Notes/ is for personal thinking, no citations required
8. New discipline = new subfolder