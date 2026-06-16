---
title: "Claude Code + Paperclip (Nate Herk)"
category: source
summary: YouTube tutorial by Nate Herk demonstrating Paperclip — an open-source multi-agent orchestration layer. Covers setup from scratch, agent configuration, heartbeats, skills, routines, and the "board" interaction model. Transcript ingested via n8n.
tags: [paperclip, multi-agent, orchestration, claude-code, open-source, ai-agents, heartbeat]
sources: 1
updated: 2026-05-09
source_path: "raw/Untitled.md"
source_date: 2026-03
authors: [Nate Herk]
ingested: 2026-05-09
---

# Claude Code + Paperclip (Nate Herk)

**Source:** [YouTube](https://www.youtube.com/watch?v=HJ-dwefABss) · March 2026
**Transcript:** Retrieved via n8n `CLUD_YouTube_Transcript` workflow · 2026-05-09

**Arek's note:** *"Check and suggest any updates, upgrades, or improvements that could benefit Arek&Co setup."*

## TL;DR

Paperclip is a free, open-source, self-hosted Node.js server (MIT license) that structures AI agent teams into an organisation with org charts, budgets, ticket-based tasks, heartbeats, and cost tracking. Launched early March 2026; 36,000+ GitHub stars in under 3 weeks. Claude Code is the primary execution agent. The user operates as a "board" — giving high-level goals, approving hires, the agents handle execution.

See [[paperclip]] for the full entity page.

## Core Concepts From the Transcript

### The Board Model
You are the board, not the operator. You give high-level goals and metrics; the CEO agent delegates down, hires sub-agents, creates tasks. Nate demonstrated managing 7 agents across 5 active tasks in ~30 minutes of board-level interaction.

### Heartbeats
Agents "wake up" on a schedule (every 4, 8, or 12 hours) with fresh context. On wake, they check their tasks, re-orient, and keep working. Four configuration files per agent: **agents** (context), **heartbeat** (execution checklist), **soul** (persona/values), **tools** (available tools). These files evolve over time; you can edit them manually.

### Agent Hierarchy & Hiring
Start with a CEO agent. CEO can request to hire sub-agents (e.g. engineer, QA) — each hire requires board approval by default (configurable in settings). Approved hires spawn as new agent sessions. Nate's live demo: CEO → Founding Engineer → QA Agent, each with task assignments from the CEO.

### Setup
```
npx paperclipai onboard
```
Runs on localhost by default. Can be moved to a VPS for remote access. Onboarding: name company → create first agent → set first task → launch.

### Skills
Skills installed per-agent or company-wide by pasting a GitHub URL into the dashboard. Source: [skills.sh](https://skills.sh) — free marketplace. Nate installed `frontend-design-skill` and `web-design-guidelines` during demo. All agents natively understand Paperclip skills out of the box.

### Routines (Beta)
Recurring scheduled tasks. Assign to an agent, set schedule/webhook/terminal trigger. Nate's example: nightly security check assigned to a security/QA agent.

### Company Templates
Pre-built company templates importable from the Paperclip GitHub (`/company` section). Examples: G-Stack (CEO, CTO, QA, release engineer, staff engineer), Agency Agents, scientific research org. Largest template has 48 agents.

### Budget & Cost Tracking
Per-agent token budgets. Dashboard shows spend per agent in real time (useful when on pay-per-token plans, not subscriptions). Multiple companies can run in parallel.

### Secrets / Environment Variables
No obvious UI for env vars, but Claude Code (with a Paperclip-aware project) can access and manage them internally. Nate's tip: set up a Claude Code project that understands the Paperclip architecture and API — it becomes your "partner in crime" for configuration, VPS migration, adding secrets, monitoring.

## Creator's Meta-Tip

Nate created a dedicated Claude Code project with the Paperclip GitHub repo ingested. That project knows: full architecture, API, heartbeat protocol, VPS migration path, agent configs, secrets management, gotchas. Result: Claude Code becomes a high-quality assistant for building and extending the Paperclip setup — especially useful during initial configuration.

This is directly applicable to Arek & Co — if/when Paperclip gets adopted, a CLAUDE.md or project file scoped to the Paperclip setup would be the right move.

## What Made This a "Destroyed OpenClaw" Moment

OpenClaw is a paid AI agent platform. Paperclip is free, open-source, and self-hosted — similar (or better) orchestration with full control and no per-seat cost. For anyone already using Claude Code, Paperclip as a coordination layer effectively obsoletes OpenClaw for many use cases.

## Relevance to Arek & Co

The Arek & Co system is already a multi-agent architecture (8 agents, each with a domain brief). Paperclip solves a different problem: **accountability infrastructure** — tracking which agent did what, cost per agent, task ticketing, escalation paths, and autonomous agent-to-agent delegation.

**Short-term (now):** Not needed. Arek's OS works via Operator routing + CLAUDE.md. Paperclip would add infrastructure overhead without clear gain at current scale.

**Medium-term (RealityRowHub):** High relevance. Production company structure maps well to Paperclip's org chart + budget model. When RealityRowHub involves multiple collaborators or automated cost-accountable AI pipelines, Paperclip is the right coordination layer.

**Sources:** this file
**Related:** [[paperclip]], [[claude-code]], [[n8n]], [[cli-for-agents]], [[agentic-browsing]]
