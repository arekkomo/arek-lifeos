---
title: "Kanban Multi-Agent System Architecture"
category: concept
summary: "Kanban board as the coordination layer for multi-agent fleets — cards as work units, SQLite-backed state, auto-routing, event-driven fan-out/fan-in, self-healing, and one human approval gate."
tags:
  - kanban
  - multi-agent
  - orchestration
  - architecture-pattern
  - self-healing
  - event-driven
sources:
  - "https://youtu.be/EKVRqcpTT6s" — Tombi Studio — 2026-06-02
updated: 2026-06-02
---

## Overview

A multi-agent coordination architecture using a **Kanban board as the single source of truth**. Agents never communicate directly — they only read and write board state. This eliminates conflicts, duplicate work, and the need for message queues or orchestration glue code.

Built and demonstrated with **Hermes Agent + Kanban plugin** (SQLite-backed).

> See also: [[hermes-openclaw-agentic-os-source]], [[autonomous-ai-assistant]], [[paperclip]]

## Core Design

### Board as State (Not Memory)

- Every unit of work = a **card** with title, assignee, status.
- Board lives in a **SQLite file** — survives restarts and crashes.
- No agent-to-agent chat, no message queues, no polling.
- Single source of truth; no duplicate work.

### Card → Agent

1. Dispatcher claims a **ready** card.
2. Spawns the **assigned agent profile** in a clean workspace.
3. Agent does the work, marks card **done**.
4. Loop ticks continuously.

### Dependency Routing (Auto Fan-out/Fan-in)

- Cards sit in **to-do** until parent card(s) finish.
- Then they **promote to ready** automatically.
- Fan-out → 3 parallel researchers → fan-in → orchestrator routes once all parents done.
- Zero glue code, zero polling, zero babysitting.

### Self-Healing

- Detects missing output directories or stale temp files.
- Re-reruns the failed phase to a persistent path autonomously.
- Orchestrator model catches and fixes without human involvement.

### One Human Gate

- All proposals reach human via Telegram once ready.
- Replies: `approve` / `shelve` / `modify`.
- Protects from runaway work and wasted tokens.

## Pipeline Pattern (Pain-Point → Deliverable)

```
Scouts (X, Web) → Orchestrator Judge → Research (3x parallel)
  → Orchestrator Route [build | video | shelve]
  → Human Approval Gate
    ├── Build path: Analyst → Builder → Tester → Code deliverable
    └── Video path: Video Researcher → Producer → Slides + Script
```

## Judging Rubric (Orchestrator)

| Criterion | Description |
|--|--|
| Frequency | How often this issue appears |
| Pain Intensity | Severity of the problem |
| Solvability | Can it be fixed or explained? |
| Strategic Fit | Alignment with channel/project goals |
| Solution Gap | Are existing solutions broken or missing? |

Scoring out of 100. Threshold = **65** (balances throughput vs. quality).

## Source Files

> Tombi Studio open-sourced a generalized version under `TombiStudio / hermes-multi-agent-workflow`. Adaptable skeleton for any Kanban-based workflow.

## Relevance to Arek & Co

- Provides the **coordination layer pattern** for any multi-agent setup in our system.
- Each of the 8 agents could be assigned cards via profiles.
- Human gate aligns with Arek's control preference.
- Can power: content creation pipeline, skill self-improvement loop, cross-discipline synthesis tasks.
- Directly applicable to [[autonomous-ai-assistant]], [[creative-flow-constraints]], and RealityRowHub tooling.
