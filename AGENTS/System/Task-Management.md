---
title: Task Management — Apple Reminders
category: note
summary: Routing rules for all agents when creating tasks in Apple Reminders
tags: [system, tasks, reminders, routing]
updated: 2026-05-06
---

# Task Management — Apple Reminders

Arek uses **Apple Reminders** as the primary task management system. All agents must create tasks in the correct list.

## Lists

| List | Purpose | Owner Agent |
|------|---------|-------------|
| **Reminders** | Default catch-all. Any task not tied to a specific project. | All agents |
| **CHS** | Creative Home Solutions — renovation startup project tasks. | Strategist |
| **AI** | AI-related experiments, research, and tasks. | Scholar / System |

## Routing Rules

- **No clear project?** → `Reminders` (default)
- **Related to CHS startup / renovation company?** → `CHS`
- **Related to AI tools, experiments, or research?** → `AI`
- **More lists will be added** as new projects are defined — update this doc when they are.

## Technical Notes

- MCP tool: `mcp__apple-mcp__reminders` with `operation: create` and `listName` parameter
- Read access is limited — the tool can create reminders in named lists but cannot reliably enumerate all lists
- Always specify `listName` explicitly when creating a reminder
- Supports: `name`, `listName`, `dueDate`, `notes` fields

## CHS Project Context

CHS = Creative Home Solutions. This is a startup project for Arek's partner's renovation company. The **Strategist** agent owns this project. Tasks in the CHS list are managed and tracked by the Strategist.
