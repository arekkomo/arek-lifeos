---
name: Apple Reminders Task Management Setup
description: Arek uses Apple Reminders with 3 lists for task management — routing rules for all agents
type: project
originSessionId: b7c6a186-08fe-4f3f-91a1-57c0bb07ce95
---
Arek's primary task management system is **Apple Reminders** with three lists:

- **Reminders** — default catch-all for anything not project-specific
- **CHS** — Creative Home Solutions (renovation startup, Strategist's domain)
- **AI** — AI-related tasks, experiments, research

Routing: default to Reminders unless task clearly belongs to CHS or AI.

**Why:** Arek wants agents to create tasks directly in Apple Reminders rather than tracking them elsewhere. More lists will be added as projects grow.

**How to apply:** When any agent creates a task for Arek, use `mcp__apple-mcp__reminders` with `operation: create`, `name`, and `listName` (one of: "Reminders", "CHS", "AI"). Documented in vault at `AGENTS/System/Task-Management.md`.
