---
title: Creative Project Operating Rules
summary: Canonical structure and lifecycle for all work in CREATIVE.
updated: 2026-08-16
---

# Creative Project Operating Rules

## The Creative Root

`CREATIVE/` has exactly three working subfolders:

```text
CREATIVE/
├── Projects/       # one canonical home per creative project
├── Inspirations/   # incoming references and sparks
└── Library/        # reusable elements and studio reference material
```

Root-level reference notes such as `Creative-Style-Bible.md`, `Aiah-Syn-Style.md`, and `Project-Catalog.md` remain source-of-truth documents—not project folders.

## One Project, One Home

Every creative project lives at:

```text
CREATIVE/Projects/<Project-Name>/
```

- Use title case with hyphens: `The-Kings-Chair`, `Little-M`, `Angel-In-Hell-Devil-In-Heaven`.
- Never create domain containers such as `Song-Projects/`, `Film-Projects/`, or `Music-Video-Projects/`.
- A song, its music video, and their shared development belong in the **same project folder**.
- `Project-Catalog.md` is the index of all project homes.

## Required Project Structure

```text
CREATIVE/Projects/<Project-Name>/
├── Project-Brief.md
├── SONG/                 # lyrics, song structure, Suno prompts
├── MUSIC-VIDEO/          # treatment, storyboard, shot list
├── SCRIPTS/              # film / narrative scripts when applicable
├── ASSETS/               # character, set, prop, visual assets
├── REFERENCES/           # project-specific inspiration
└── NOTES/                # decisions, learnings, supporting material
```

Use only the component folders a project needs. A film may use `SCRIPTS/`, `STORYBOARD/`, `SHOT-LIST/`, and `REFERENCES/`; a YouTube concept may only need `DEVELOPMENT.md` at first. Do not create empty folders simply to match the example.

## Project Brief

Every project must have `Project-Brief.md` at its root with:

- YAML frontmatter: `title`, `summary`, `stage`, `domain`, `created`
- A one-line concept and emotional or creative intent
- Links or a list of active component folders
- Current status and one concrete next output

## Library and Inspirations

- **Inspirations:** unassigned references, sparks, images, links, and tonal discoveries. Route a reference into a project once it has a home.
- **Library:** reusable ideas, concepts, story design, production assets, prompt reference, and curated craft captures. It is not project storage or administration.
- Reusable material created inside a project should be logged to `Library/` while remaining in its project home.

## Lifecycle

```text
Idea → Development → Production → Post Prod → Review → Done / Archived
```

Only sync a project to Notion when it moves to **Production**. Obsidian remains the primary source; Notion is a mirror.
