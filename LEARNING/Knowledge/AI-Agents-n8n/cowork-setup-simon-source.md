---
title: "Set Up Claude Cowork Better Than 99% of People (Simon, BetterCreating)"
category: source
summary: 7-step Cowork power-user setup covering global instructions, About Me folder (about-me + writing-rules + memory files), tool connectors, built-in skills, plugins, and scheduled tasks — with context maps for token-efficient tool navigation.
tags: [cowork, setup, global-instructions, writing-rules, context-map, plugins, scheduled-tasks, about-me]
sources: 1
updated: 2026-05-09
source_path: "raw/Set Up Claude Cowork better than 99% of people.md"
source_date: 2026-04
authors: [Simon, BetterCreating / Systems Made Better]
ingested: 2026-05-09
---

# Set Up Claude Cowork Better Than 99% of People

**Source:** [YouTube](https://www.youtube.com/watch?v=pl90LATQlHI) · Simon (BetterCreating / Systems Made Better) · April 2026

**Arek's note:** *"Check and compare to my existing setup — propose any updates or upgrades that would benefit Arek&Co setup."*

## TL;DR

7-step Cowork setup that goes from blank slate to a personal AI assistant that knows who you are, connects your tools, remembers your history, creates professional files, and works for you while you sleep. The standout additions over a basic setup: writing rules file, Notion context map, and per-project memory.

## The 7 Steps

### Step 1 — Install & Select Workspace Folder
Workspace folder = shared working directory between you and Claude. Everything you want Claude to do goes here. Everything private stays outside.

### Step 2 — Global Instructions (CLAUDE.md)
The single most important setup step. Write rules Claude reads at the start of every session. Either write your own or have Claude generate them:

> *"Create some global system instructions for me. Include: who I am, my communication preferences, what I need help with, safety rules (never delete/send/publish without checking), and any recommendations for a solid system."*

### Step 3 — About Me Folder (3 key files)
Create a folder with three files Claude reads at the start of every session:

**about-me.md** — Who you are, what you do, your business/tools, current projects, audience, everything a smart new team member needs on day one.

**writing-rules.md** — How you like things written. Crucially: research anti-AI writing style and embed those rules explicitly. Ban phrases, tone guidelines, British/American spelling, formality level.

**memory.md** — A log Claude updates after every session. Append new entries, update existing ones. Prevents Claude from forgetting where you are with projects. Reference it in global instructions so Claude always fills it out.

### Step 4 — Connect Tools
Priority connectors: Claude in Chrome, Gmail, Google Calendar, Notion (or equivalent). For each connected tool with rich structure (like Notion), create a **context map**:

> *"Search my Notion workspace and create a context map — a clear breakdown of my workspace structure — so you can find things more efficiently in the future."*

Save the context map in your About Me folder. Result: Claude navigates the tool without burning tokens exploring it from scratch.

### Step 5 — Built-in Skills
Enable or create skills for specific output types (Word docs, PDFs, presentations). Folder structure recommendation:
- `outputs/` — where all Claude-created files land, organised by project
- `projects/` — per-project CLAUDE.md files + memory for ongoing context

### Step 6 — Plugins
Plugins = specialist agents with their own tools and knowledge bases. Built-in plugins worth enabling: legal, engineering. Can build custom plugins for domain-specific knowledge (YouTube strategy, customer support, etc.).

### Step 7 — Scheduled Tasks
Set recurring tasks to run automatically (computer must be on). Examples: weekly briefer (Gmail + Calendar + Notion → Monday morning report), daily inbox triage. Output can be an MD file, Word doc, or email.

**Bonus — Mobile Dispatch:** Control Cowork from your phone via the Claude mobile app → Dispatch. Requires always-on desktop.

## Comparison to Arek & Co Setup

| Feature | Arek's Current State | Gap / Action |
|---|---|---|
| Global Instructions (CLAUDE.md) | ✅ Vault-wide CLAUDE.md + project instructions per agent | Strong |
| About Me files | ✅ ABOUT-YOU/ folder with 5 files | Strong |
| Writing Rules file | ❌ Not present | **Create ABOUT-YOU/Writing-Rules.md** |
| Notion context map | ❌ Not present | **Create a Notion workspace map in ABOUT-YOU/** |
| Per-project memory/CLAUDE.md | ⚠️ Partial — vault memory exists, but no per-project CLAUDE.md files | Worth adding to active projects |
| Connected tools | ✅ Gmail, Calendar, Notion, Claude in Chrome | Strong |
| Skills | ✅ Full skills library | Strong |
| Scheduled tasks | ✅ Raw ingest scheduled | Good start |
| Mobile Dispatch | ❓ Unknown | Worth enabling if Arek has an always-on machine |

**See:** [[cowork-setup-improvements]] for consolidated action list.

**Sources:** this file
**Related:** [[cowork-setup-nick-milo-source]], [[knowledge-graph-architecture]]
