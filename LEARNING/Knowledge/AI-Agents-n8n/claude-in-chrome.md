---
title: Claude in Chrome
category: entity
summary: Anthropic's browser extension that gives Claude agentic control over Chrome/Brave — navigate, click, extract, and teach reusable shortcuts without any API or MCP setup.
tags: [claude-in-chrome, browser-automation, anthropic, cowork, agentic-browsing]
sources: 1
updated: 2026-05-09
---

# Claude in Chrome

**Type:** Browser extension (Chromium-based)
**Maker:** Anthropic
**Access:** Bundled with Claude subscription — no extra cost

## What It Does

Turns Claude into an agentic browser controller. Claude can navigate pages, click UI elements, extract data, fill forms, and take screenshots — all driven by natural language prompts.

Key differentiator: works on **any website**, even those with no API or MCP connector. It's the universal fallback for web-based tool automation.

## Key Capabilities

| Feature | Description |
|---|---|
| Model selection | Opus / Sonnet / Haiku per task |
| Quick mode | Faster execution, available on all models |
| Ask before acting | Claude presents plan, waits for approval |
| Teach mode | Record a multi-step workflow → reusable shortcut |
| Shortcuts | Named, schedulable tasks from teach sessions |
| Tab grouping | Control which tabs Claude can see/access |
| Screenshot | Pass current page state to Claude |

## Cowork Integration

When Claude in Chrome is connected to Cowork, Cowork can hand off browser tasks mid-workflow:

> *"Pull the data from that dashboard"* → Cowork invokes Chrome → Chrome navigates, extracts, returns data → Cowork incorporates into the output.

This fills the API/MCP gap for tools like Google Search Console, YouTube Studio, or any web platform without a connector.

## Prompt Injection Risk

The primary security concern. Malicious instructions can be embedded in web pages and trick Claude into unintended actions. Mitigations:
- Use "ask before acting" mode
- Prefer Opus for sensitive workflows
- Only use on trusted sites

## Use in Arek & Co

Already connected as a Cowork connector. Practical applications:
- Any repetitive browser workflow without an MCP (web tools, platforms)
- Teach mode: record once, run via shortcut forever
- Filling the connector gap for new tools while MCPs are being built

**Sources:** [[claude-in-chrome-source]]
**Related:** [[agentic-browsing]], [[claude-code]], [[n8n]]
