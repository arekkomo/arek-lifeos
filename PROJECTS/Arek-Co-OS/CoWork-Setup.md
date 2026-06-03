---
title: Arek & Co. OS — CoWork & Plugin Setup
project: Arek-Co-OS
updated: 2026-05-09
---

# CoWork & Plugin Setup

> Inventory of what's connected, what's working, and what's missing.
> Updated manually when integrations change.

---

## Connected MCPs

| MCP | Purpose | Status | Notes |
|---|---|---|---|
| Obsidian (file access) | Read/write vault files | ✅ Active | Core — mounted at Arek&Co/ |
| Notion | Read/write creative and project databases | ✅ Active | dtb Writing + dtb Knowledge |
| Google Calendar | Read/create calendar events | ✅ Active | |
| Gmail | Read/draft/search email | ✅ Active | |
| Apple Notes | Read/write Apple Notes | ✅ Active | |
| Apple Reminders / Contacts / Mail | Native macOS apps | ✅ Active | Via apple-mcp |
| Google Drive | File access and search | ✅ Active | |
| n8n | Workflow creation and execution | ✅ Active | Self-hosted instance |
| Computer Use | Desktop control for native apps | ✅ Active | |
| Claude in Chrome | Browser automation | ✅ Active | |

---

## Installed Plugins

| Plugin | Skills Included | Status |
|---|---|---|
| Anthropic core skills | pdf, docx, pptx, xlsx, pptx, summarize, schedule, skill-creator, etc. | ✅ Active |
| Creative Film Pipeline | creative-film-pipeline, creative-song-pipeline, creative-notion-integration | ✅ Active |
| Design plugin | design-critique, design-handoff, accessibility-review, ux-copy, etc. | ✅ Active |
| Operations plugin | process-doc, runbook, status-report, risk-assessment, etc. | ✅ Active |
| CoWork Plugin Management | cowork-plugin-customizer, create-cowork-plugin | ✅ Active |

---

## CoWork Projects (Agent Instructions)

| Agent | Project Name | Instructions Status |
|---|---|---|
| Operator | Operator | ✅ Written |
| Strategist | Strategist | ✅ Written |
| Scholar | Scholar | 🔲 Needed |
| Director | Director | 🔲 Needed |
| Accountant | Accountant | 🔲 Needed |
| Coach | Coach | 🔲 Needed |
| Connector | Connector | 🔲 Needed |
| System | System | 🔲 Needed |

---

## Skills Inventory Summary

> Full detail in `/SKILLS/`. This is a status summary.

| Agent | Skill IDs | Count | Status |
|---|---|---|---|
| Operator | SK-OP-01 to 05 | 5 | ✅ Defined |
| Strategist | SK-ST-01 to 05 | 5 | ✅ Defined |
| Scholar | SK-SC-01 to 04 | 4 | ✅ Defined |
| Director | SK-DR-01 to 03 | 3 | ✅ Defined |
| Accountant | SK-AC-01 to 06 | 6 | ✅ Defined |
| Coach | SK-CO-01 to 05 | 5 | ✅ Defined |
| Connector | SK-CN-01 to 04 | 4 | ✅ Defined |
| System | SK-SY-01 to 07 | 7 | ✅ Defined |

---

## Hardware / Compute

| Asset | Role | Status |
|---|---|---|
| DGX Spark | Local AI inference: ComfyUI, image/video generation | ✅ Active |
| MacBook Pro (primary) | Daily work + CoWork sessions | ✅ Active |

---

## Gaps & Wishlist

| Gap | Priority | Notes |
|---|---|---|
| Agent project instructions for 6 remaining agents | High | Phase 2 milestone |
| Automated daily briefing via schedule skill | Medium | Phase 3 |
| n8n workflows for finance data capture | Medium | Phase 3 |
| Suno MCP or integration | Low | For Director/music work |
| Health data integration (Oura, Apple Health) | Low | For Coach |

---

## Changelog

| Date | Change |
|---|---|
| 2026-04-27 | Initial CoWork setup |
| 2026-05-09 | This inventory created |
