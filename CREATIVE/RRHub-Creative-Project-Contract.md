---
title: RRHub Creative Project Contract
summary: Copy/paste implementation contract for tools that read and write the creative project vault.
updated: 2026-08-18
---

# RRHub Creative Project Contract

> **Purpose:** This is the implementation contract for Claude Code / RRHub tools. The Obsidian vault is the creative source of truth. RRHub reads and writes these Markdown files; it must not create a parallel project system.

## 1. Canonical locations

```text
/home/realityrove/Obsidian/Arek&Co/CREATIVE/
├── Projects/                         # Canonical creative project homes
├── Inspirations/                      # Unassigned sparks and references
├── Library/                           # Reusable cross-project creative material
├── Project-Catalog.md                 # Registry of every creative project
├── Project-File-Schema.md             # Filename + metadata contract
├── Operating-Rules.md                 # Creative-system rules
├── Writing-Types.md                   # Approved writing taxonomy
└── Knowledge/Writing-Craft/           # 13 playbooks for writing project documents
```

**Source of truth:** `CREATIVE/Projects/` and its Markdown files.

**Do not use or recreate:** `Song-Projects/`, `Music-Video-Projects/`, `Film-Projects/`, `Shorts-Projects/`, `Aiah-Syn-Projects/`, or any other domain-level project containers.

## 2. Project-home rule

Every creative project has exactly one canonical folder:

```text
CREATIVE/Projects/<Project-Name>/
```

Example:

```text
CREATIVE/Projects/Fog/
├── fog_brief.md
├── fog_song.md
├── fog_script.md
├── fog_scene_breakdown.md
├── fog_shot_breakdown.md
├── fog_storyboard_v01.md
└── fog_production_notes.md
```

- Project folders use **Title-Case with hyphens**: `Little-M`, `The-Kings-Chair`, `Imma-Nyala`.
- A song, music video, script, assets, bibles, and references for the same work remain in that **one** project folder.
- Never split components of a project into different project roots.
- Discover project folders dynamically; do not hard-code the current project list.

## 3. Flat-file rule and episodic exception

Projects are flat by default. The only permitted nested structure is for episodes:

```text
CREATIVE/Projects/<Project-Name>/
└── EPISODES/
    ├── EP01/
    │   ├── <project-name>_ep01_script.md
    │   ├── <project-name>_ep01_scene_breakdown.md
    │   └── <project-name>_ep01_shot_breakdown.md
    └── EP02/
        └── <project-name>_ep02_script.md
```

Rules:

- Use sequential IDs: `EP01`, `EP02`, `EP03`.
- Episode files live only inside their episode folder.
- Episode files include `episode: EP01` in frontmatter.
- Do not create component folders such as `SONG/`, `SCRIPTS/`, `ASSETS/`, `REFERENCES/`, or `MUSIC-VIDEO/`.

## 4. Canonical filenames

Non-episode files:

```text
<project-slug>_<file-type>[_<descriptor>][_vNN].md
```

Episode files:

```text
<project-slug>_epNN_<file-type>[_<descriptor>][_vNN].md
```

Examples:

```text
fog_song.md
fog_shot_breakdown.md
meow_song_v02.md
the-kings-chair_character_bible.md
imma-nyala_ep01_script.md
```

Use `_v01`, `_v02`, etc. only for genuinely active alternate versions. Once approved, retain the canonical filename without a version suffix (for example, `fog_song.md`).

## 5. Required YAML frontmatter

Every project Markdown file must begin with:

```yaml
---
type: song | script | scene_breakdown | shot_breakdown | note
title: Human-readable title
project: Exact project-folder name
stage: Idea | Development | Production | Post Prod | Review | Done | Paused | Archived
version: current | v01 | v02 | placeholder
updated: YYYY-MM-DD
---
```

Additional required metadata:

```yaml
# Required only for shot breakdowns
source: <canonical-script-filename.md>

# Required only for episode files
episode: EP01
```

### Metadata handling rules for RRHub

- Preserve unknown/additional frontmatter keys when editing an existing file.
- Never silently change `project`, `type`, `source`, `episode`, or existing RRHub shot `id:` values.
- Update `updated` whenever a meaningful content change is saved.
- Treat `title` as the human-facing RRHub tab/display label.
- Treat `type` as the RRHub element type, not merely a descriptive tag.

## 6. Approved file types

| Filename suffix | RRHub `type` | Purpose |
|---|---|---|
| `_brief` | `note` | Project purpose, status, next output |
| `_plot_outline` | `note` | Story, sequence, episode, or concept progression |
| `_treatment` | `note` | Readable visual/narrative experience of the work |
| `_script` | `script` | Screenplay, video script, or episode script |
| `_song` | `song` | Canonical lyrics plus Suno style direction |
| `_scene_breakdown` | `scene_breakdown` | Scene function, turn, conflict, staging, continuity |
| `_shot_breakdown` | `shot_breakdown` | Shot plan paired to a script via `source:` |
| `_storyboard` | `note` | Visual sequence / storyboard frames and captions |
| `_character_bible` | `note` | Character invariants, behavior, arc, and visual identity |
| `_set_bible` | `note` | Location geography, design language, and continuity |
| `_prop_bible` | `note` | Story-significant object identity and state timeline |
| `_voice_direction` | `note` | Performance/narration direction and vocal continuity |
| `_production_notes` | `note` | Dated decisions, risks, exceptions, and handoffs |
| `_reference` | `note` | Project-specific reference material only |

For exact writing rules and templates, RRHub/Claude Code can read:

```text
CREATIVE/Knowledge/Writing-Craft/Index.md
```

## 7. RRHub document semantics

### Song: exactly one canonical source

A song must contain both lyrics and production direction in the same file:

```markdown
---
type: song
title: Fog
project: Fog
stage: Production
version: current
updated: 2026-08-18
---

[Verse 1]
Lyrics go here.

=== SUNO STYLE ===
[Genre: ...]
[Vocals: ...]
[Instrumentation: ...]
[Mood: ...]
[Production: ...]
```

Rules:

- The marker must be exactly `=== SUNO STYLE ===`.
- Lyrics are above the marker; style direction is below it.
- Do **not** create standalone `_lyrics` or `_suno_prompt` files.
- Editing lyrics must not overwrite style direction; editing style must not overwrite lyrics.

### Script, scene, shot, and storyboard relationship

```text
Script → Scene Breakdown → Shot Breakdown → Storyboard / Keyframes → Generation → Edit
```

- **Script** is the authority for story events, action, dialogue, and sound.
- **Scene Breakdown** explains why a scene exists: function, objective, pressure, turn, staging, continuity.
- **Shot Breakdown** specifies exact coverage: shot ID, narrative job, frame, camera, action, timing, continuity, execution, and acceptance test.
- **Storyboard** visually proves selected shots; it does not replace the shot breakdown.
- A breakdown must not introduce a story event absent from its script. Revise the script first.

### Shot-breakdown contract

```yaml
---
type: shot_breakdown
title: <Project> — Shot Breakdown
project: <Project-Name>
stage: Development
version: current
updated: YYYY-MM-DD
source: <project>_script.md
---
```

- `source` must name a real canonical script file in the same project or episode folder.
- Preserve existing shot IDs (`id:`) because RRHub may link them to generated storyboard images and promoted records.
- Use stable IDs such as `S01.SH01` in headings and only create a new `id:` if RRHub requires it; never overwrite an existing one.

## 8. Read/write behavior

### When reading

1. Read `CREATIVE/Project-Catalog.md` to discover projects and current status.
2. Locate `CREATIVE/Projects/<Project-Name>/`.
3. Read the project’s `_brief` first, then the requested file and its upstream/downstream linked documents.
4. For Aiah Syn projects, read `CREATIVE/Aiah-Syn-Style.md` before creative changes.
5. For document-writing work, read the matching file in `CREATIVE/Knowledge/Writing-Craft/` before drafting.

### When editing

1. Edit the existing canonical file in place whenever it exists.
2. Create a file only after confirming no canonical file of the same purpose already exists.
3. Preserve YAML keys, RRHub shot IDs, linked filenames, and the exact song delimiter.
4. Keep creative intent in brief/outline/treatment/script; keep model settings, seed/reference IDs, take selection, and technical exceptions in shot breakdowns or production notes.
5. If an upstream story decision changes, update the script first, then scene/shot/storyboard documents as required.
6. Update `Project-Catalog.md` when creating, renaming, archiving, or materially changing a project’s status or next action.

### When creating a new project

1. Check `Project-Catalog.md` and `CREATIVE/Projects/` for a naming conflict.
2. Create `CREATIVE/Projects/<Project-Name>/`.
3. Create `<project-slug>_brief.md` with shared metadata and a clear next output.
4. Add only files the project needs; do not scaffold empty component folders.
5. Add reusable discoveries to Library and update the catalog.
6. Only mirror/sync to Notion when the project moves to **Production**.

## 9. Library, Inspirations, and operations boundaries

| Location | Put here | Do not put here |
|---|---|---|
| `CREATIVE/Projects/` | Material specific to one project | Cross-project reusable concepts or administration |
| `CREATIVE/Inspirations/` | Unassigned visual, tonal, musical, or narrative sparks | Committed project assets |
| `CREATIVE/Library/` | Reusable ideas, story design, production assets, prompt reference, craft captures | Active-project storage, cleanup records, or sync mechanics |
| `HUB/Creative-Operations/` | Cleanup records, project review, Notion-sync tooling, system prompts | Creative project source files |

## 10. Notion rule

- The Obsidian vault is the creative source of truth.
- Notion is a mirror, not project storage.
- Import/transfer material must be **merged into its canonical project files** (brief, song, notes, etc.) and then removed.
- Do not create or preserve a permanent `Notion-Creative-Mirror`, `NOTION-SOURCE`, or `*_notion_source.md` system.
- Sync a project to Notion only at the **Production** stage and update the mirror again at **Done**.

## 11. Guardrails

- Never create duplicate project folders or duplicate canonical documents.
- Never split a song and its music video into separate project roots.
- Never create permanent project subfolders except `EPISODES/EPxx/`.
- Never use Notion as the sole or primary source of a creative document.
- Never replace or delete content without first reading the existing file.
- Never remove unknown YAML metadata or existing RRHub shot IDs.
- Never create a separate lyric or Suno prompt file for a song.
- Never put generic reusable ideas in an active project when they belong in Library.

## 12. Current state (for migration checks)

At the time of this contract:

- There are **10 canonical project folders** under `CREATIVE/Projects/`.
- Project files are flat except `CREATIVE/Projects/Imma-Nyala/EPISODES/EP01/`.
- There are **no** project-level Notion transfer/source files remaining.
- The canonical project registry is `CREATIVE/Project-Catalog.md`.
- The flat-file schema is `CREATIVE/Project-File-Schema.md`.
