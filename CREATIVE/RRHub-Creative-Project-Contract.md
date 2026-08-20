---
title: RRHub Creative Project Contract
summary: Simplified five-file implementation contract for RRHub read/write tools.
updated: 2026-08-18
---

# RRHub Creative Project Contract

> **Authority:** The Obsidian vault is the creative source of truth. RRHub reads and writes the files below. Do not create a parallel creative-project system.

## Canonical paths

```text
/home/realityrove/Obsidian/Arek&Co/CREATIVE/
├── Projects/                         # Canonical project homes
├── Inspirations/                      # Unassigned sparks/references
├── Library/                           # Reusable cross-project creative material
├── Project-Catalog.md                 # Project registry
├── Project-File-Schema.md             # File/metadata contract
├── Writing-Types.md                   # Five-file taxonomy
└── Knowledge/Writing-Craft/           # Craft playbooks
```

Never recreate legacy containers such as `Song-Projects/`, `Music-Video-Projects/`, `Film-Projects/`, `Shorts-Projects/`, or `Aiah-Syn-Projects/`.

## Project structure

Each project has exactly one home:

```text
CREATIVE/Projects/<Project-Name>/
```

Projects are flat. The only permitted nesting is episodic work:

```text
<Project-Name>/EPISODES/EP01/<project-slug>_ep01_<file-type>.md
```

Use `EP01`, `EP02`, etc. Episode files must include `episode: EP01`.

## Five-file contract

| File | RRHub type | Responsibility |
|---|---|---|
| `<project>_brief.md` | `note` | Master context and production control: intent, treatment, references, character/set/prop/voice direction, decisions, notes, status, next action. |
| `<project>_plot_outline.md` | `note` | Causal story / sequence / episode progression. |
| `<project>_script.md` | `script` | Executable story: action, dialogue, narration, sound. |
| `<project>_song.md` | `song` | One canonical lyric plus Suno style source. |
| `<project>_scene_shot_breakdown.md` | `shot_breakdown` | Scene intent, visual/storyboard planning, and executable shot plan. |

Create only the files a project needs. Do not create standalone treatment, storyboard, production-notes, reference, character-bible, set-bible, prop-bible, voice-direction, scene-breakdown, or shot-breakdown files.

## Required metadata

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

```yaml
# Required in scene+shot breakdowns
source: <canonical-script-filename.md>

# Required in episode files
episode: EP01
```

Preserve unknown YAML fields, `source`, `episode`, and existing RRHub shot `id:` values.

## Special parsing rules

### Song

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

- The delimiter is exactly `=== SUNO STYLE ===`.
- Lyrics are above it; style direction is below it.
- Never create separate lyric or Suno-prompt files.

### Scene + Shot Breakdown

```yaml
type: shot_breakdown
source: <project>_script.md
```

Body order:

```markdown
## Scene intent
Function, POV/objective, conflict, turn, staging, continuity.

## Visual / storyboard planning
Keyframes/panels, frame captions, screen direction, transitions, visual anchors.

## Shot plan
### S01.SH01 — Label
Narrative job, frame, camera, action/blocking, sound, timing/edit, continuity, execution, acceptance test, fallback.
```

- Storyboard material is contained here; no standalone storyboard file.
- Scene analysis is contained here; no standalone scene-breakdown file.
- Preserve existing shot IDs.
- `source` must refer to a real canonical script in the same project or episode folder.

## Tool behavior

### Read

1. Read `Project-Catalog.md` to discover projects/status.
2. Read a project’s `_brief` first, then the requested file.
3. Read `Aiah-Syn-Style.md` before Aiah Syn changes.
4. Read the appropriate writing-craft playbook before authoring.

### Write

1. Edit the existing canonical file in place.
2. Create a file only after confirming no same-purpose canonical file exists.
3. Keep upstream story intent in Brief/Outline/Script; keep visual execution inside Scene + Shot Breakdown.
4. Update `Project-Catalog.md` when a project’s name, status, or next action materially changes.
5. Never split the five-file system into component folders or standalone support documents.

## Boundaries

| Location | Purpose |
|---|---|
| `Projects/` | Project-specific creative material |
| `Inspirations/` | Unassigned sparks/references |
| `Library/` | Reusable cross-project ideas/craft captures |
| `HUB/Creative-Operations/` | Cleanup, review, sync, and system operations |

Notion is a mirror only. Import material must be merged into canonical project files, then removed—never kept as a permanent transfer/mirror file.
