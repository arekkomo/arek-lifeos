---
title: Paperclip
category: entity
summary: Open-source multi-agent orchestration platform that structures AI agents into a company with org charts, budgets, ticket-based tasks, and cost accountability. Self-hosted, MIT licensed.
tags: [paperclip, multi-agent, orchestration, open-source, claude-code, ai-agents]
sources: 1
updated: 2026-05-09
---

# Paperclip

**Type:** Open-source tool / self-hosted server
**GitHub:** [paperclipai/paperclip](https://github.com/paperclipai/paperclip)
**Launch:** March 2, 2026 · 30k+ GitHub stars in 3 weeks
**License:** MIT
**Install:** `npx paperclipai onboard`

## What It Does

Paperclip is a coordination layer for multi-agent systems. Rather than running agents in isolation, it structures them into an organisation with:

- **Org charts** — define which agents report to which (CEO → Marketing → Copywriter)
- **Budget / cost tracking** — token budgets per agent; throttles when over
- **Ticket-based tasks** — tasks are assigned, tracked, and completed like a project board
- **Session persistence** — conversations and context survive reboots
- **Agent flexibility** — Claude Code sessions, OpenClaw bots, Python scripts, shell commands, HTTP webhooks — anything that accepts a heartbeat signal

## How It Integrates with Claude Code

Claude Code is the primary execution agent. When a higher-level agent (e.g. a "CEO" agent) decides a task is needed, Paperclip routes it to the appropriate Claude Code session with the right context and budget.

## Why It Matters (Context)

Before Paperclip, running multiple agents required custom orchestration code or expensive SaaS platforms (like OpenClaw). Paperclip provides that infrastructure free, open-source, and self-hosted — making it accessible to solo operators and small teams.

## Relevance to Arek & Co

| Timeframe | Verdict |
|---|---|
| Now | Not needed — Arek's 8-agent OS works via Operator routing and CLAUDE.md. Adding infra overhead without clear gain. |
| RealityRowHub (3–5 years) | High value — production company structure maps well to Paperclip's org chart + budget model. Enables cost accountability across AI pipelines. |

**Sources:** [[paperclip-source]]
**Related:** [[claude-code]], [[n8n]], [[cli-for-agents]], [[agentic-browsing]]
