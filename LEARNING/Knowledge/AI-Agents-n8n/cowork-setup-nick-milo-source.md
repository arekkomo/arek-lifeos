---
title: "Give Me 20 Minutes. I'll Teach You 80% of Claude Cowork (Nick Milo)"
category: source
summary: YouTube tutorial combining Claude Cowork with Obsidian — covers auto-generating an About Me dossier from vault notes, using Maps of Content for AI navigation, writing partner workflows, and weekly review from Obsidian.
tags: [cowork, obsidian, about-me, maps-of-content, weekly-review, knowledge-management]
sources: 1
updated: 2026-05-09
source_path: "raw/Give Me 20 Minutes. I'll Teach You 80% of Claude Cowork.md"
source_date: 2026-03
authors: [Nick Milo, Linking Your Thinking]
ingested: 2026-05-09
---

# Give Me 20 Minutes. I'll Teach You 80% of Claude Cowork

**Source:** [YouTube](https://www.youtube.com/watch?v=s3ccD6m6WKc) · Nick Milo (Linking Your Thinking) · March 2026

**Arek's note:** *"Check and compare to Arek&Co setup — suggest any updates or features that could benefit my setup."*

## TL;DR

Cowork + Obsidian is a powerful combination when you use the vault as Claude's context architecture. The key insight: structure your notes well (with links and folder hierarchy) and Claude can navigate them intelligently — extracting dossiers, running reviews, and building Maps of Content automatically.

## Key Techniques

### 1. Auto-Generated About Me Dossier
Rather than manually writing an About Me file, ask Claude to read your vault and build a dossier for you:

> *"Review my Obsidian vault, especially my Atlas folder, and build a dossier on me. Pull from my highest-ranked notes, manifestos, values, goals, sources. Write my intellectual DNA — what I believe, how I think, what I keep coming back to."*

Then paste the result into Global Instructions (Settings → Personal Preferences). Updates Claude's responses to be tuned to you, not generic.

**Value:** More accurate than manually written files because it reflects what you've actually been thinking about, not what you think you should say about yourself.

### 2. Maps of Content (MOC) for AI Navigation
Create a Map of Content that gives Claude a high-level index of your vault. When Claude has a MOC, it can navigate the vault without reading everything from scratch — reducing token cost and improving relevance.

> *"Create a map of content linking the rich ideas across my vault that might work in [project]. Mark it as AI generated."*

MOCs + linked notes = Claude can traverse the graph intelligently rather than brute-force reading.

### 3. Writing Partner Workflow
Point Claude at a specific research folder (not the whole vault):

> *"I'm trying to synthesize all of this research alongside my own thinking. Identify common themes across the sources. Surface areas where their approaches contradict or extend my existing frameworks. Pull the most relevant insights so I can start building a curriculum."*

Output: a structured markdown file with themes, contradictions, and a curriculum arc — directly editable in Obsidian.

### 4. Weekly Review from Vault
Ask Claude to scan recent activity across the vault:

> *"Based on my recent activity in active projects, where am I? What matters? What am I missing?"*

Output includes: active projects ranked by priority, progress notes, open questions, what you might be forgetting (taxes, upcoming launches, logistics). Drops as an MD file into Obsidian automatically.

### 5. Folder-Level Context Control
Instead of giving Claude full vault access, point it at a specific subfolder:
- Right-click any folder in Obsidian → Copy path from vault → Paste into Cowork
- Claude reads only those files — faster, cheaper, more focused

## Comparison to Arek & Co Setup

| Technique | Arek's Current State | Gap / Action |
|---|---|---|
| About Me dossier | Manual ABOUT-YOU/ files | Could run auto-generation to enrich existing files — especially About-Me-General.md |
| Maps of Content | Not present | Worth creating MOCs for key clusters (AI Agents, Filmmaking) to speed up Scholar queries |
| Weekly vault review | No automated cadence | Could be a scheduled task — already have the skill for it |
| Writing partner (folder-level) | Ad hoc | Pattern worth formalising for Scholar: always point at subfolder, not full vault |

**See:** [[cowork-setup-improvements]] for consolidated recommendations.

**Sources:** this file
**Related:** [[cowork-setup-simon-source]], [[knowledge-graph-architecture]], [[claude-in-chrome]]
