---
title: Creative Project Flat File Schema
summary: Canonical filename and metadata contract for CREATIVE/Projects and RealityRoveHub.
updated: 2026-08-16
---

# Creative Project Flat File Schema

## Location

Each project lives in one flat folder:

```text
CREATIVE/Projects/<Project-Name>/
```

No subfolders **except episodic work**. Every non-episode file follows:

```text
<project-name>_<file-type>[_<descriptor>][_vNN].md
```

For an episodic project, use the one permitted nested structure:

```text
<Project-Name>/
└── EPISODES/
    └── EP01/
        └── <project-name>_ep01_<file-type>[_vNN].md
```

Use sequential folder IDs: `EP01`, `EP02`, `EP03`.

Examples: `fog_song.md`, `fog_shot_breakdown.md`, `the-kings-chair_character_bible.md`, `meow_song_v02.md`.

## Required metadata

Every project Markdown file begins with:

```yaml
---
type: song | script | scene_breakdown | shot_breakdown | note
title: Human-readable title
project: Exact project-folder name
stage: Idea | Development | Production | Post Prod | Review | Done | Paused | Archived
version: current | v01 | v02 | imported | placeholder
updated: YYYY-MM-DD
---
```

`source:` is required on a `shot_breakdown` and names its paired script filename. Episode files also add `episode: EP01` matching their episode folder.

## File types

| Filename suffix | RRHub `type:` | Use |
|---|---|---|
| `_brief` | `note` | Project purpose, status, and current next output |
| `_song` | `song` | Canonical lyrics and the `=== SUNO STYLE ===` prompt in one file |
| `_script` | `script` | Screenplay, video script, or episode script |
| `_scene_breakdown` | `scene_breakdown` | Scene-level narrative, staging, or dramatic breakdown |
| `_shot_breakdown` | `shot_breakdown` | Shot list linked to its script via `source:` |
| `_plot_outline` | `note` | Story, episode, sequence, or concept outline |
| `_treatment` | `note` | Visual/narrative treatment |
| `_storyboard` | `note` | Storyboard progression or storyboard notes |
| `_character_bible`, `_set_bible`, `_prop_bible` | `note` | Reusable project asset definitions |
| `_voice_direction`, `_production_notes`, `_reference` | `note` | Supporting direction and project notes |

## Song rule

There is no standalone `_lyrics` or `_suno_prompt` file. A song is one RRHub element:

```markdown
---
type: song
...
---
[Verse 1]
Lyrics...

=== SUNO STYLE ===
Production prompt...
```

Use `_song_vNN` only for genuinely active alternate versions. Once a version is chosen, keep `<project>_song.md` as the canonical file.
