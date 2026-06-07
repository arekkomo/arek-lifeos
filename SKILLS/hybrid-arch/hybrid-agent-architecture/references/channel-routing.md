---
name: channel-routing
description: "Route incoming messages to the correct bucket using a [prefix]: convention. When confidence drops below 95%, pause and ask user which prefix to use rather than auto-routing."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [routing, channel, prefix, messaging, workflow]
    related_skills: [learning-ingestion]
---

# Channel Routing

## Core Rule

All user messages arrive on the primary channel (Telegram DM). Use prefix-based routing to direct messages to the correct bucket.

## Prefix Map

| Prefix | Purpose | Target Bucket |
|---|---|---|
| ``*finance:*`` 💰 | Money, investing, budgets, spending | Financial analysis |
| ``*write:*`` ✍ | Drafting, editing, prose, emails | Writing assistant |
| ``*project:*`` 🛠 | Task updates, blockers, goals, status | Kanban board |
| ``*research:*`` 🧠 | Deep dive, web investigation, comparisons | Web search + synthesis |
| ``*diary:*`` 📝 | Daily reflection, mood, life events | Vault DAILY/ |
| ``*context:*`` 📁 | Dump info, learning notes, archival saves | Vault LEARNING/ |
| ``*meta:*`` 🔧 | IT, setups, configs, devops, tools | Terminal/CLI |

When user drops a link (YouTube, article, etc.) without prefix → default to ``*research:*``, then run the ``learning-ingestion`` workflow (vault scan + rapport/opinion + log to ``LEARNING/``).

## Ambiguity Threshold (Hard Rule)

If confidence that a message belongs to exactly one prefix bucket is below 95%, I MUST pause and explicitly ask:

> *"Confidence below 95%. Should this be [PREFIX1] or [PREFIX2]?"*

**Do NOT auto-route or guess.** This is a hard rule.

### Low-confidence examples (must ask):
- "We spent $2,300 on a consultant, also did the gym" → finance vs diary overlap
- "New AI agent tool, link below" → research vs context overlap
- "The vault backup needs X change" → meta vs project overlap

### High-confidence (auto-route):
- ``*finance:*`` Q2 budget review
- ``*context:*`` [paste dump]
- Pure link with no text → research
