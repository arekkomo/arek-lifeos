# Kanban Multi-Agent Architecture — Notes & Reference

**Source:** Tombi Studio — "Nukti Agentic System" (YouTube, 2026-06-02). Open-sourced under `TombiStudio/hermes-multi-agent-workflow`.

## Architecture Overview

A multi-agent coordination pattern using a **Kanban board as the single source of truth**. Agents never communicate directly — they only read/write board state. Eliminates conflicts, duplicate work, and glue code.

### Core Components

1. **Kanban Board** — SQLite-backed card state file. Every unit of work = a card with title, assignee, status. Survives restarts/crashes.
2. **Dispatcher** — Loop that claims ready cards and spawns assigned agent profiles in clean workspaces.
3. **Agent Profiles** — Hermes profiles (one per specialist). Each has its own model + prompt.
4. **Dependency Router** — Cards auto-promote from to-do → ready when parent tasks complete. Zero glue code.
5. **Human Gate** — One approval step via Telegram, protecting against runaway work.

## Pipeline Pattern

```
Scouts (X, Web) → Orchestrator Judge → Research (3x parallel)
  → Orchestrator Route [build | video | shelve]
  → Human Approval Gate
    ├── Build path: Analyst → Builder → Tester → Code deliverable
    └── Video path: Video Researcher → Producer → Slides + Script
```

## Key Design Decisions

| Feature | How It Works | Why It Matters |
|--|--|--|
| State = board, not memory | SQLite card state survives restarts | No lost work, crash recovery |
| Fan-out/fan-in | Cards sit in to-do until parents done | Parallel execution with sync, zero polling |
| Self-healing | Orchestrator detects failed phases (e.g., deleted temp dirs) and auto-regenerates | Handles file I/O failures without human intervention |
| One human gate | All proposals reach human via Telegram; replies: approve/shelve/modify | Prevents runaway work and wasted tokens |
| Agent = profile | Each role is a Hermes profile with its own model + prompt | Different models for different tasks; easy to swap |

## Scoring Rubric (Orchestrator Judge)

For pain-point → action pipeline:

| Criterion | Description |
|--|--|
| Frequency | How often the issue appears in complaints |
| Pain Intensity | Severity of the problem for users |
| Solvability | Can it be fixed (tool) or explained (video)? |
| Strategic Fit | Alignment with project/channel goals |
| Solution Gap | Are existing solutions broken or missing? |

**Threshold: 65/100.** Balances throughput vs. quality.

## Relevance to Arek & Co

- Coordination layer for any multi-agent setup
- Each of the 8 agents could be assigned cards via profiles
- Applies to: content pipelines, skill self-improvement, cross-discipline synthesis, RealityRowHub tooling

## See Also

- [[autonomous-ai-assistant]] — Cloudbot pattern (also uses Kanban)
- [[hermes-openclaw-agentic-os-source]] — Similar multi-agent comparison
- [[paperclip]] — Alternative: Paperclip multi-agent orchestration platform
- [[skill-systems-pattern]] — Shared context files for skill consistency
