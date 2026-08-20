---
title: Creative Project File Schema
summary: Simplified five-file RRHub/Vault contract for creative projects.
updated: 2026-08-18
---

# Creative Project File Schema

## Project location

```text
CREATIVE/Projects/<Project-Name>/
```

A project is flat except for episodic work:

```text
<Project-Name>/EPISODES/EP01/<project-slug>_ep01_<file-type>.md
```

Use `EP01`, `EP02`, etc. Episode files add `episode: EP01` to frontmatter.

## The five project files

| Canonical suffix | RRHub type | Purpose |
|---|---|---|
| `_brief` | `note` | **Master project file.** Concept, treatment, references, character/set/prop/voice direction, production notes, decisions, status, and next action. |
| `_plot_outline` | `note` | Story, sequence, episode, or concept progression. |
| `_script` | `script` | Executable screenplay, video script, or episode script. |
| `_song` | `song` | Canonical lyrics and Suno style direction in one file. |
| `_scene_shot_breakdown` | `shot_breakdown` | Combined scene analysis, visual/storyboard planning, and shot plan. |

Create only the files a project actually needs. Do not create standalone treatment, storyboard, production-notes, reference, character-bible, set-bible, prop-bible, voice-direction, scene-breakdown, or shot-breakdown files.

## Naming

```text
<project-slug>_<file-type>[_vNN].md
<project-slug>_epNN_<file-type>[_vNN].md
```

Examples:

```text
fog_brief.md
fog_plot_outline.md
fog_script.md
fog_song.md
fog_scene_shot_breakdown.md
imma-nyala_ep01_script.md
```

Use version suffixes only for genuinely active alternatives. Keep the unversioned file as the canonical approved/current version.

## Shared metadata

```yaml
---
type: song | script | shot_breakdown | note
title: Human-readable title
project: Exact project-folder name
stage: Idea | Development | Production | Post Prod | Review | Done | Paused | Archived
version: current | v01 | v02 | placeholder
updated: YYYY-MM-DD
---
```

Additional fields:

```yaml
# Required for a scene + shot breakdown
source: <canonical-script-filename.md>

# Required for episode files
episode: EP01
```

## Master brief sections

The `_brief` is the project’s **living master context and production-control file**. Start every project here, then continually add its information, loose ideas, references, decisions, and production notes. Use only the sections that serve the project:

```markdown
# <Project>
## Intent and audience
## Concept and treatment
## References and visual / sonic language
## Characters / sets / props / voice direction
## Production notes and decision log
## Status and next action
```

## Song rule

There is no standalone lyric or Suno-prompt file. A song is one RRHub element:

```markdown
[Verse 1]
Lyrics...

=== SUNO STYLE ===
[Genre: ...]
[Vocals: ...]
[Instrumentation: ...]
[Mood: ...]
[Production: ...]
```

The marker must be exactly `=== SUNO STYLE ===`. Lyrics stay above it; style direction stays below it.

## Combined scene + shot breakdown rule

`_scene_shot_breakdown` is a single RRHub `shot_breakdown` file. It must include `source:` pointing to its canonical script and contain, in order:

```markdown
## Scene intent
- Function, POV/objective, conflict, turn, staging, continuity, audience information.

## Visual / storyboard planning
- Optional keyframes, frame captions, screen direction, transitions, visual continuity anchors.

## Shot plan
### S01.SH01 — Label
- Narrative job, frame, camera, action/blocking, sound, timing/edit, continuity, execution, acceptance test, fallback.
```

Preserve existing RRHub shot `id:` fields. Do not create a separate storyboard or scene-breakdown file.
