---
title: Creative Project Operating Rules
summary: Simplified five-file project, Library, and RRHub rules for CREATIVE.
updated: 2026-08-18
---

# Creative Project Operating Rules

## Creative root

```text
CREATIVE/
├── Projects/       # one canonical project folder per creative work
├── Inspirations/   # unassigned sparks and references
└── Library/        # reusable cross-project ideas and craft material
```

Reference documents: `Project-Catalog.md`, `Project-File-Schema.md`, `Writing-Types.md`, and `RRHub-Creative-Project-Contract.md`.

## One project, one home

- Every project lives at `CREATIVE/Projects/<Project-Name>/`.
- Never create project-type containers such as `Song-Projects/`, `Film-Projects/`, or `Music-Video-Projects/`.
- Keep the project flat, except for episodic work under `EPISODES/EP01/`, `EPISODES/EP02/`, etc.
- Use only the five canonical file types in [[Project-File-Schema]].
- Do not split songs, videos, assets, or production context into different project roots.

## Simplified project documents

- `_brief` is the single master project file: concept, treatment, references, character/set/prop/voice direction, production notes, decisions, and status.
- `_plot_outline` is the story/sequence map.
- `_script` is the executable story source.
- `_song` is the sole lyrics-plus-Suno source.
- `_scene_shot_breakdown` combines scene analysis, storyboard/keyframe planning, and the shot plan.

## RRHub and vault matching

- Every file uses shared metadata: `type`, `title`, `project`, `stage`, `version`, `updated`.
- RRHub types are `song`, `script`, `shot_breakdown`, and `note`.
- Song lyrics sit above the exact `=== SUNO STYLE ===` delimiter; style direction sits below it.
- Scene + Shot Breakdown uses `type: shot_breakdown` and must carry `source:` naming its script.
- Preserve unknown YAML metadata and RRHub shot IDs during edits.

## Library, Inspirations, and operations

- **Inspirations:** unassigned sparks, references, images, links, and tonal discoveries.
- **Library:** reusable future-project ideas, story design, production assets, prompt reference, and craft captures—not active project storage.
- **HUB/Creative-Operations:** cleanup records, review dashboards, sync tooling, and system prompts.

## Lifecycle

```text
Idea → Development → Production → Post Prod → Review → Done / Archived
```

The vault is the source of truth. Notion is a mirror only at Production and Done; imported material is merged into canonical project files and removed.
