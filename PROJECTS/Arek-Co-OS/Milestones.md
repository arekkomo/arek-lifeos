---
title: Arek & Co. OS — Milestones & Roadmap
project: Arek-Co-OS
updated: 2026-05-13
---

# Milestones & Roadmap

> Status key: ✅ Done · 🔄 In Progress · 🔲 Planned · ⏸ On Hold
> Priority key: High · Medium · Low

---

## Phase 1 — Foundation
*Goal: A working vault with defined structure, agents, and an AI layer that can execute.*

| # | Task | Priority | Status | Notes |
|---|------|----------|--------|-------|
| 1.1 | Define vault folder structure | High | ✅ | CLAUDE.md is the schema |
| 1.2 | Write agent roster (8 agents) | High | ✅ | Briefs live in AGENTS/ |
| 1.3 | Connect CoWork + Obsidian file access | High | ✅ | |
| 1.4 | Connect Notion MCP | High | ✅ | |
| 1.5 | Connect Google Calendar MCP | Medium | ✅ | |
| 1.6 | Connect Gmail MCP | Medium | ✅ | |
| 1.7 | Ingest Notion knowledge base into LEARNING/ | High | ✅ | 4 clusters ingested |
| 1.8 | Build ABOUT-YOU/ profile files | High | ✅ | General, Creative, Finance, Health, Working-Patterns |
| 1.9 | Build SKILLS/ registry (initial set) | Medium | ✅ | ~40 skills defined |
| 1.10 | Set up CoWork project instructions per agent | High | ✅ | All 8 agents done |
| 1.11 | Create this project (Arek-Co-OS) | Medium | ✅ | 2026-05-09 |

---

## Phase 2 — Agent Activation
*Goal: Each agent has a tested brief, knows its tools, and can execute its core skills reliably.*

| # | Task | Priority | Status | Notes |
|---|------|----------|--------|-------|
| 2.1 | Write full project instructions for all 8 agents | High | ✅ | All 8 agents have CoWork-Instructions-LIVE.md — confirmed 2026-05-12 |
| 2.2 | Test each agent's core skill end-to-end | Medium | 🔲 | |
| 2.3 | Build Directing Curriculum (SK-ST-01) | High | 🔄 | Curriculum-Index + Module 01 done 2026-05-12. Modules 02–06 planned. |
| 2.4 | Set up VFX project tracking for current show | High | ✅ | `/VFX/VFX-Projects/Current-Show/` created 2026-05-12 — 5 files. Fill in when show starts. |
| 2.5 | Build RealityRowHub business plan skeleton | High | ✅ | Business-Plan.md + Content-Strategy.md + Market-Research/ created 2026-05-13 |
| 2.6 | Set up Accountant workflows (income, budget, tax) | Medium | 🔲 | |
| 2.7 | Set up Coach workflows (fitness, nutrition, sleep) | Medium | 🔲 | |
| 2.8 | Set up Connector workflows (contacts, social) | Low | 🔲 | |
| 2.9 | Add Heartbeat.md to each agent in AGENTS/ | High | ✅ | All 8 agents done 2026-05-13 |

---

## Phase 3 — Cadences & Automation
*Goal: The OS runs on rhythms — daily, weekly, monthly, quarterly — with minimal friction.*

| # | Task | Priority | Status | Notes |
|---|------|----------|--------|-------|
| 3.1 | Design daily briefing flow (Operator SK-OP-02) | High | ✅ | SK-OP-02-Briefing-Flow.md created 2026-05-13 |
| 3.2 | Design weekly review cadence | Medium | 🔲 | |
| 3.3 | Design monthly review cadence | Medium | 🔲 | |
| 3.4 | Design quarterly strategic review | Low | 🔲 | |
| 3.5 | Build n8n automations for data capture | Low | 🔲 | Finance, health, content metrics |
| 3.6 | Build Dashboard.md as live artifact | High | ✅ | arek-co-dashboard artifact live 2026-05-13. Calendar + priorities + agent status. |
| 3.7 | Set up scheduled tasks (auto-briefings) | Medium | 🔲 | CoWork schedule skill |

---

## Phase 3.5 — Cowork Setup Optimisation
*Goal: Close identified gaps between current setup and best-practice Cowork configurations.*

| # | Task | Priority | Status | Notes |
|---|------|----------|--------|-------|
| C.1 | Create `ABOUT-YOU/Writing-Rules.md` | High | ✅ | Done 2026-05-13 — tone, voice, anti-AI guidelines |
| C.2 | Create `ABOUT-YOU/Notion-Context-Map.md` | Medium | 🔲 | Map Notion workspace via MCP; saves tokens on every Notion query |
| C.3 | Create MOCs for AI-Agents/ and Filmmaking/ | Medium | 🔲 | High-level index pages for Scholar; faster knowledge queries |
| C.4 | Add per-project memory files to active PROJECTS/ | Medium | 🔲 | Start with CHS and RealityRowHub |

---

## Phase 4 — Refinement
*Goal: The OS is battle-tested, gaps are patched, and it runs with low maintenance overhead.*

| # | Task | Priority | Status | Notes |
|---|------|----------|--------|-------|
| 4.1 | Audit all SKILLS/ files for accuracy | Low | 🔲 | |
| 4.2 | Refine agent briefs based on real usage | Medium | 🔲 | |
| 4.3 | Build inter-agent handoff protocols | Medium | 🔲 | Especially Director ↔ Strategist |
| 4.4 | Document lessons learned in this file | Low | 🔲 | |
| 4.5 | Quarterly OS review process | Low | 🔲 | |

---

## Phase 4.5 — Vault Token Efficiency
*Goal: Restructure the knowledge base so Claude retrieves the right content with minimum token overhead.*

| # | Task | Priority | Status | Notes |
|---|------|----------|--------|-------|
| V.1 | Add typed edge annotations to wikilinks in Knowledge/ | Low | 🔲 | Start with AI-Agents/ cluster |
| V.2 | Introduce `decision` and `playbook` node types to frontmatter | Low | 🔲 | Update CLAUDE.md schema |
| V.3 | Enforce ~300-line cap on Knowledge/ pages | Low | 🔲 | Audit + split pages over limit |

---

## Phase 5 — Ingest-Driven Improvements
*Goal: Implement recommendations surfaced from raw/ ingests on 2026-05-10.*

| # | Task | Priority | Status | Notes |
|---|------|----------|--------|-------|
| I.1 | Add proactive heartbeat scheduled task | High | ✅ | operator-daily-heartbeat task running at 8:35am daily — created 2026-05-13 |
| I.2 | Implement skill self-improvement loop on creative skills | Low | 🔲 | evals/eval.json with 25 binary assertions for song/film pipeline |
| I.3 | Formalise 8pm creative window with constraint-based sessions | Medium | 🔲 | Concrete output goal per session — add to Working-Patterns.md |
| I.4 | Implement micro habits starter stack | Low | 🔲 | Morning sunlight, water, intention, evening review, 2-breath buffer |

---

## Decisions Log

| Date | Decision | Outcome |
|---|---|---|
| 2026-05-09 | Create PROJECTS/ as first-class domain | Arek-Co-OS is first project |
| 2026-05-09 | Add Phase 4.5 — Vault Token Efficiency | Based on Infinite Brain architecture research |
| 2026-05-13 | Add Priority column to all milestone tables | Board now shows priority; vault is single source of truth |

---

## Next Actions

1. Continue Directing Curriculum — Module 02 (2.3 — High)
2. Set up Accountant workflows — income, budget, tax (2.6 — Medium)
3. Create MOCs for AI-Agents/ and Filmmaking/ (C.3 — Medium)
4. Design weekly review cadence (3.2 — Medium)
