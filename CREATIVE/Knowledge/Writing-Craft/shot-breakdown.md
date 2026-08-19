---
title: Shot-Breakdown
category: creative-writing-craft
file_suffix: _shot_breakdown
rrhub_type: shot_breakdown
updated: 2026-08-18
---

# Shot-Breakdown

## Definition
The director’s ordered, editorially motivated plan for discrete images, sound coverage, and execution.

## Pipeline job
Create after scene breakdown. It translates scene intention into generateable or shootable shots, then feeds boards, generation, and edit.

## Metadata
Use the shared project frontmatter: `type`, `title`, `project`, `stage`, `version`, and `updated`. Add `source:` when the document is directly paired to a script; keep the canonical file inside its project folder.

## Required sections
- Required `source:` paired script filename
- Scene intention
- Stable shot ID and narrative job
- Frame, composition, and camera start → end
- Action / blocking and eyelines
- Light, design, sound, timing, and edit
- Continuity packet
- Execution mode and acceptance test
- Risk and fallback

## House writing rules
- One shot has one dominant action and camera idea.
- State why this image now before decorating it.
- Specify screen direction and end state.
- Split AI shots at changes of action, viewpoint, state, or continuity.
- Never change an existing RRHub shot `id:`.

## Quality gate
- [ ] `source:` points to the canonical script.
- [ ] Every shot has an acceptance test and continuity anchor.
- [ ] Boards use matching shot IDs but do not replace the breakdown.

## Starter template
```markdown
## S01 — Scene intention
### S01.SH01 — Label
- **Narrative job:**
- **Frame:**
- **Camera:** start → end
- **Action / blocking:**
- **Light / sound:**
- **Timing / edit:**
- **Continuity:**
- **Execution:**
- **Acceptance test:**
- **Risk / fallback:**
```

## Sources
- StudioBinder: Shot List — https://www.studiobinder.com/blog/shot-list
- Wrapbook: Shot List — https://www.wrapbook.com/blog/shot-list
