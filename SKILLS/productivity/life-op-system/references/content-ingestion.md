---
name: content-ingestion
description: When the user shares a link, video, article, or other content for learning, scan the existing vault for similar topics, synthesize a rapport or honest opinion, and log to the vault for future retrieval and reasoning.
version: 1.0.0
author: Emily
license: MIT
metadata:
  hermes:
    tags: [vault-ingestion, learning, youtube, article, research]
    related_skills: [youtube-content]
    category: note-taking
---

# Content Ingestion Protocol

## When to use
- User pastes a URL, video link, article link, or other content for learning or a project
- User explicitly asks to research or learn about a topic

## Core Workflow (always 3 steps)

1. **Vault Scan** — Search `LEARNING/Knowledge/`, `LEARNING/transcripts/`, and `ABOUT-YOU/` for overlapping topics, entities, or tags. Use grep/rg for fast scanning.

2. **Vault Rapport OR Honest Opinion:**
   - **If overlap found:** Provide "Vault Rapport" — what we already know and what's new
   - **If no overlap:** Provide "Honest Opinion" — direct analysis of the content's value and connection to user's projects

3. **Log to Vault** — Create/Update files in `LEARNING/Knowledge/` and `LEARNING/transcripts/`. Update indexes and logs.

## Critical Vault Rules
- **NEVER write to `raw/`** — that folder is strictly immutable source documents the user controls
- New ingestions go to `LEARNING/transcripts/` (transcript/raw material) and `LEARNING/Knowledge/` (processed learning)
- User's preferences and work style are stored in `LEARNING/Knowledge/about-you/`

## Pitfalls
- Don't paste full transcripts into chat — summarize insights, log the full thing to vault
- Don't guess routing if confidence is below 95% — ask the user which prefix bucket
- Don't overwrite existing vault files — merge findings into existing knowledge rather than creating duplicates
- Always scan the vault FIRST before fetching the content, so you can report what we already know
