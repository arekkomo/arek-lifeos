---
title: "Claude in Chrome — Beginner Setup Guide & Uses (Elliot Prince)"
category: source
summary: YouTube tutorial covering Claude in Chrome installation, safety, key features (teach mode, shortcuts, quick mode), and integration with Claude Cowork for browser-driven SEO auditing.
tags: [claude-in-chrome, browser-automation, cowork, anthropic, agentic-browsing]
sources: 1
updated: 2026-05-09
source_path: "raw/Claude in Chrome Clearly Explained (beginner setup guide & uses).md"
source_date: 2026-04
authors: [Elliot Prince]
ingested: 2026-05-09
---

# Claude in Chrome — Beginner Setup Guide & Uses

**Source:** [YouTube](https://www.youtube.com/watch?v=52Fc0xjVCBc) · Elliot Prince · April 2026

**Arek's note:** *"Could be interesting functionality — not sure how this supplements my existing setup."*

## TL;DR

Claude in Chrome is a browser extension from Anthropic that turns Claude into an agentic browser controller. The real leverage is the Cowork + Chrome combo: Claude can drive websites and tools that have no API/MCP connector, extract data, and deposit results into files or Google Docs — without any technical setup.

## Core Features

- **Model selection** — Opus, Sonnet, or Haiku per task. Opus is safer (better prompt-injection resistance); Haiku for lightweight summarisation.
- **Quick mode** — faster execution, can be paired with any model.
- **Ask before acting** — Claude presents a plan and waits for approval before touching the browser. Recommended until comfortable.
- **Teach mode** — walk Claude through a multi-step process step-by-step; it records it as a reusable shortcut. Shortcuts can be scheduled.
- **Tab grouping** — explicit control over which tabs Claude can access.
- **Screenshot** — pass the current page state to Claude as context.

## Safety: Prompt Injection

The main risk with agentic browsing is **prompt injection** — malicious instructions hidden in web pages, emails, or images that could trick Claude into acting on them. Mitigations:
- Only use on trusted sites until comfortable
- Keep "ask before acting" on
- Use Opus for higher-stakes tasks (better at detecting injections)

## Cowork Integration

The power combination: Claude Cowork drives the task logic, Claude in Chrome executes the browser steps. Demonstrated via full SEO audit:

1. Pull Search Console performance data (90-day)
2. Read top-performing pages for content quality
3. Run PageSpeed Insights technical audit
4. Write everything into a Google Doc with brand formatting

Equivalent to a half-day of manual agency work, done automatically.

## Teach Mode Workflow (Google Search Console Example)

1. Open teach mode → narrate the process step-by-step
2. Claude records click targets, inputs, wait conditions
3. Converts to a named shortcut (e.g. "Request Indexing")
4. Future runs: say the shortcut name → Claude executes

## Relevance to Arek & Co

- **Already connected**: Claude in Chrome is available in Arek's Cowork setup as a connector.
- **Value**: Acts as a universal fallback for any web tool without an MCP — effectively a "no-API-needed" bridge.
- **Teach mode**: Worth recording for any repetitive browser workflow (e.g. platforms used in VFX, YouTube Studio, any web app without a connector).
- See also: [[claude-in-chrome]], [[agentic-browsing]], [[claude-code]]
