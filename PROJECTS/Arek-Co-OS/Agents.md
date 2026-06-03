---
title: Arek & Co. OS — Agent Roster
project: Arek-Co-OS
updated: 2026-05-09
---

# Agent Roster

> 8 agents, each with a distinct mandate. No overlap by design.
> Status: ✅ Brief written · 🔄 Project instructions in progress · 🔲 Not started

---

## The 8 Agents

| Agent | Core Mandate | Brief | CoWork Instructions | Primary Skills |
|---|---|---|---|---|
| **Operator** | Daily execution, routing, morning briefing | ✅ | ✅ | SK-OP-01 to 05 |
| **Strategist** | Planning, curriculum, business strategy | ✅ | ✅ | SK-ST-01 to 05 |
| **Scholar** | Knowledge curation, vault management, learning | ✅ | 🔲 | SK-SC-01 to 04 |
| **Director** | Creative vision, film/music projects | ✅ | 🔲 | SK-DR-01 to 03 |
| **Accountant** | Finance, tax, investment tracking | ✅ | 🔲 | SK-AC-01 to 06 |
| **Coach** | Health, fitness, nutrition, recovery | ✅ | 🔲 | SK-CO-01 to 05 |
| **Connector** | Relationships, contacts, social calendar | ✅ | 🔲 | SK-CN-01 to 04 |
| **System** | Technical setup, software inventory, vault maintenance | ✅ | 🔲 | SK-SY-01 to 07 |

---

## Agent Design Notes

### Operator
- First point of contact each day
- Routes inputs to the right agent
- Owns the morning briefing and journal facilitation
- Lives at: `/AGENTS/Operator/`

### Strategist
- Long-horizon thinker: quarters and years
- Owns the Directing Curriculum and RealityRowHub strategy
- Tracks VFX professional memberships (VES, AMPAS)
- Lives at: `/AGENTS/Strategist/` (instructions embedded in CoWork project)

### Scholar
- Owns the knowledge layer (`LEARNING/`)
- Ingests and synthesizes external sources
- Never writes to `raw/` — only reads from it
- Lives at: `/AGENTS/Scholar/`

### Director
- Owns all creative output: film projects, Aiah Syn, YouTube
- Takes high-level brief from Strategist, executes creative development
- Lives at: `/AGENTS/Director/`

### Accountant
- Processes bank statements, tracks income, manages budget
- Monitors investment portfolio toward condo and retirement goals
- Lives at: `/AGENTS/Accountant/`

### Coach
- Tracks fitness, nutrition, sleep, and recovery metrics
- Connects health to performance: energy for creative and strategic work
- Lives at: `/AGENTS/Coach/`

### Connector
- Manages PEOPLE/ vault, tracks relationships
- Flags networking opportunities relevant to directing and RRH
- Lives at: `/AGENTS/Connector/`

### System
- Technical infrastructure: software inventory, CoWork setup, integrations
- Documents what's installed, connected, and working
- Lives at: `/AGENTS/System/`

---

## Inter-Agent Handoff Patterns

| From | To | When |
|---|---|---|
| Director | Strategist | Creative project needs business/timeline alignment |
| Strategist | Director | Strategic goal needs creative execution (e.g., portfolio piece) |
| Operator | Any | Routes incoming input to the right agent |
| Scholar | Strategist | New knowledge relevant to curriculum or RRH |
| Accountant | Strategist | Financial milestone affects 3-year arc |
| System | Operator | New tool or integration available |

---

## Open Questions

- [ ] What's the exact handoff protocol between Operator and other agents?
- [ ] Should Director have read access to Strategist's RRH plan?
- [ ] How do agents share context across sessions without duplication?
