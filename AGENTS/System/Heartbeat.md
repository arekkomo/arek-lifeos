---
title: System Heartbeat
agent: System
summary: What the System agent checks at the start of every session.
updated: 2026-05-13
---

# System Heartbeat

> Run at the start of every System session — before any technical setup, inventory, or infrastructure work.

---

## 1. Check MCP connections
- Are all MCPs connected and functional? (Notion, Google Calendar, Gmail, n8n, bash)
- Any new MCPs added or disconnected since last session?
- Document any changes in `Technical-Setup/`

## 2. Check vault health
- Any broken file structures or missing folders?
- Are all 8 agent folders present with complete file sets (Brief.md, CoWork-Instructions-LIVE.md, Heartbeat.md)?
- Are CLAUDE.md instructions up to date with the current vault structure?

## 3. Check hardware / AI tools status
- DGX Spark — available and operational?
- ComfyUI, Runway, Kling — any updates or issues?
- Any new AI tools worth tracking for inventory?

## 4. Check task management system
- Are all agent tasks tracked correctly?
- Any stale or orphaned tasks in the system?

---

## Infrastructure Inventory
*(Keep this section current)*

| Tool | Type | Status | Notes |
|---|---|---|---|
| DGX Spark | Hardware | Active | Local AI inference |
| ComfyUI | AI tool | Active | Image/video gen |
| Runway | AI tool | Active | AI video |
| Kling | AI tool | Active | AI video |
| Notion | Knowledge | Connected | Via MCP |
| Google Calendar | Scheduling | Connected | Via MCP |
| Gmail | Communication | Connected | Via MCP |
| n8n | Automation | Connected | Via MCP |
| Obsidian | Vault | Active | CoWork file access |

---

## Key Files to Reference
- `AGENTS/System/Technical-Setup/` — full technical inventory
- `AGENTS/System/Task-Management.md` — task tracking reference
- `AGENTS/System/Reports/` — system health reports
- `CLAUDE.md` — vault schema (root of vault)
