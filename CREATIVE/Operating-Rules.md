---
title: Creative Project Operating Rules
summary: Canonical project, file, Library, and RRHub rules for CREATIVE.
updated: 2026-08-16
---

# Creative Project Operating Rules

## Creative root

```text
CREATIVE/
├── Projects/       # one flat folder per creative project
├── Inspirations/   # unassigned sparks and references
└── Library/        # reusable ideas, concepts, and creative reference
```

Root reference notes—including `Creative-Style-Bible.md`, `Aiah-Syn-Style.md`, `Project-Catalog.md`, and `Project-File-Schema.md`—remain source-of-truth documents.

## One project, one flat folder

Every creative project lives at `CREATIVE/Projects/<Project-Name>/`.

- Never create project-type folders such as `Song-Projects/`, `Film-Projects/`, or `Music-Video-Projects/`.
- Never create subfolders inside a project **except for episodic work**.
- Episodic projects use `EPISODES/EP01/`, `EPISODES/EP02/`, and so on; each episode folder contains only that episode's files, named `<project>_ep01_<file-type>.md` and tagged `episode: EP01`.
- A song, music video, screenplay, assets, and references are otherwise files inside the same project folder.
- Use the filename and metadata contract in [[Project-File-Schema]].

## RRHub and vault matching

Every project file carries the shared metadata: `type`, `title`, `project`, `stage`, `version`, and `updated`.

- RRHub types are exactly: `song`, `script`, `scene_breakdown`, `shot_breakdown`, and `note`.
- A `song` file contains both lyrics and Suno style under `=== SUNO STYLE ===`; do not create standalone lyric or prompt files.
- A `shot_breakdown` must preserve `source:` and point to its paired script filename.
- Supporting creative material uses `type: note`, so it remains visible and editable in RRHub without pretending to be a script or song.

## Library and Inspirations

- **Inspirations:** unassigned references, sparks, images, links, and tonal discoveries. Route an item into a project once it has a home.
- **Library:** reusable ideas, concepts, story design, production assets, prompt reference, and curated craft captures. It is not project storage or administration.
- **HUB/Creative-Operations:** cleanup records, review dashboards, sync tooling, and system prompts.

## Lifecycle

```text
Idea → Development → Production → Post Prod → Review → Done / Archived
```

Sync to Notion only when a project reaches Production. The vault is the creative source of truth; RRHub reads the same project files.
