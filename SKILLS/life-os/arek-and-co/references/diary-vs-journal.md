---
title: Diary vs. Journal - Conceptual Distinction
category: note
summary: Clear distinction between diary (what happened) and journal (what it means) for daily log workflows
tags: [daily, journal, diary, workflow]
sources: 1
updated: 2026-06-03
---

# Diary vs. Journal — Conceptual Distinction

Used in daily log workflows for Arek & Co. Life OS. When Arek says "both" or option 1, file into both Diary and Journal folders.

## Core Difference

| | Diary | Journal |
|---|--|--|
| **Direction** | Backward (what happened) | Forward (what I'm thinking) |
| **Content** | Events, activities, timeline | Reflections, insights, analysis |
| **Format** | "Today I did X, met Y, felt Z" | "Why did I feel X? What pattern is this?" |
| **Function** | Record of the day | Exploration of the self |
| **Question** | *What happened today?* | *What does it mean?* |

## Vault Locations

- `DAILY/Diary/` — daily timeline of events
- `DAILY/Journal/` — deeper reflection entries
- `DAILY/Briefings/` — ready for Strategist entries

## Workflow

When Arek dumps thoughts:
1. Extract facts/events → file as `Diary/YYYY-MM-DD-Diary.md`
2. Extract reflections/patterns/meanings → file as `Journal/YYYY-MM-DD-Journal.md`
3. Both get YAML frontmatter with `title`, `category`, `summary`, `tags`, `sources`, `updated`

## Mood/Energy Tracking

Both files include a `## Mood / Energy` section.
Use emojis (🟢🟡🔴) when the user provides energy info.
Use `|| Unknown ||` when establishing baseline.
