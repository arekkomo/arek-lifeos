---
title: Arek & Co. OS — Vault Architecture
project: Arek-Co-OS
updated: 2026-05-09
---

# Vault Architecture

> The authoritative reference for how the vault is structured. Changes here should be reflected in `CLAUDE.md`.

---

## Top-Level Structure

```
Arek&Co/
├── ABOUT-YOU/          ← Personal profiles, read by all agents
├── AGENTS/             ← Agent briefs and working files
├── BUSINESS/           ← Business ventures (RealityRowHub, etc.)
├── CREATIVE/           ← Creative projects (film, music, YouTube)
├── DAILY/              ← Daily journal entries
├── FINANCE/            ← Financial statements and tracking
├── HEALTH/             ← Health metrics and fitness plans
├── LEARNING/           ← Knowledge base (Scholar's domain)
├── META/               ← Vault changelog and metadata
├── PEOPLE/             ← Contacts and relationships
├── PROJECTS/           ← Non-creative projects (incl. this one)
├── SKILLS/             ← Skill registry, shared across agents
├── VFX/                ← VFX career (projects, expertise, memberships)
├── raw/                ← IMMUTABLE source documents (read only)
├── CLAUDE.md           ← Master schema file, read by all agents
└── Dashboard.md        ← Command centre (planned: live artifact)
```

---

## Domain Boundaries

| Domain | What Goes Here | What Doesn't |
|---|---|---|
| `CREATIVE/` | Film projects, Aiah Syn songs, YouTube content | Business plans, project management |
| `PROJECTS/` | Business ventures, system projects, platforms | Creative work, VFX career work |
| `VFX/` | Industry career: current show, expertise, memberships | Creative personal projects |
| `BUSINESS/` | RealityRowHub and other ventures | Creative project execution |
| `LEARNING/` | External knowledge, ingested and synthesised | Personal notes (→ LEARNING/Notes/) |
| `raw/` | Source documents for ingest only | Anything else |

---

## LEARNING/ Layer Detail

```
LEARNING/
├── Knowledge/              ← Processed knowledge (Scholar writes here)
│   ├── AI-Video/
│   ├── AI-Image-Midjourney/
│   ├── AI-3D/
│   ├── AI-Agents/
│   ├── Filmmaking/
│   ├── DaVinci-Resolve/
│   └── Motion-Capture/
├── Notes/                  ← Arek's own thinking (no citations required)
├── Books/                  ← Book summaries
├── Synthesis/              ← Cross-domain overviews
├── Directing-Path/         ← Directing curriculum (Strategist writes here)
├── .templates/             ← Page templates
├── index.md                ← Content catalog
├── log.md                  ← Append-only operation log
└── Synthesis.md            ← Cross-domain synthesis
```

---

## Frontmatter Schema

### Required on every Knowledge page
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

### Additional for source pages
```yaml
source_path: raw/<path>
source_date: YYYY-MM
authors: [name]
ingested: YYYY-MM-DD
```

### Project pages (this folder)
```yaml
title: <Title>
project: Arek-Co-OS
status: Active | On Hold | Completed
updated: YYYY-MM-DD
```

---

## Key Architectural Rules

1. `raw/` is immutable — never write to it
2. All writes go to `LEARNING/` (for knowledge) or their respective domain folder
3. Every Knowledge page must have YAML frontmatter
4. Each ingest must touch ≥ 5 files (source summary + entity pages + index + log)
5. Contradictions flagged with `> ⚠️ Contradiction:` callouts on both sides
6. New knowledge discipline = new subfolder in `Knowledge/`
7. Personal notes live in `LEARNING/Notes/` — no citations required there

---

## Evolution Log

| Date | Change | Reason |
|---|---|---|
| 2026-04-27 | Initial vault structure defined | System setup |
| 2026-05-09 | PROJECTS/ established as first-class domain | Needed project tracking for OS build |

---

## Pending Architecture Decisions

- [ ] Should `BUSINESS/` be a subfolder of `PROJECTS/` or stay top-level?
- [ ] Does `DAILY/` need a subfolder by year as it grows?
- [ ] Template for PROJECTS/ pages (should match VFX-Projects pattern or diverge?)
