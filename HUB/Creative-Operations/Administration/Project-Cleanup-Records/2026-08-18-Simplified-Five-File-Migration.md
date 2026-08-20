---
title: Simplified Five-File Project Migration
completed: 2026-08-18
scope: CREATIVE/Projects
---

# Simplified Five-File Project Migration

## Decision

Each project now uses only the files it needs from this core system:

- `_brief` — master context: treatment, references, asset/voice direction, production notes, decisions, status
- `_plot_outline`
- `_script`
- `_song`
- `_scene_shot_breakdown` — combined scene analysis, storyboard planning, and shot plan

## Migration performed

- Folded 25 standalone support documents into their projects’ master briefs.
- Folded The King’s Chair’s episode-engine material into its sole plot outline.
- Moved Chaotic Baking’s historic script revision into its master brief as an archived draft appendix.
- Replaced three legacy shot/scene/storyboard sets with combined scene + shot breakdown files:
  - `chaotic-baking_scene_shot_breakdown.md`
  - `fog_scene_shot_breakdown.md`
  - `meow_scene_shot_breakdown.md`
- Repaired project links pointing to removed support files.

## Validation

- Project Markdown files: **54 → 27**.
- Canonical projects: **10**.
- Valid project document metadata/types: **27 / 27**.
- Scene + shot breakdowns with valid script `source:`: **3 / 3**.
- Remaining project subfolders: only `Imma-Nyala/EPISODES/EP01/`.

## Source-of-truth documents updated

- `CREATIVE/Project-File-Schema.md`
- `CREATIVE/Operating-Rules.md`
- `CREATIVE/Writing-Types.md`
- `CREATIVE/RRHub-Creative-Project-Contract.md`
- `CREATIVE/Projects/README.md`
