---
title: Scene + Shot Breakdown
category: creative-writing-craft
file_suffix: _scene_shot_breakdown
rrhub_type: shot_breakdown
updated: 2026-08-18
---

# Scene + Shot Breakdown

## Purpose

This is one RRHub `shot_breakdown` file combining scene analysis, storyboard/keyframe planning, and shot-by-shot execution. It replaces standalone scene breakdown and storyboard files.

## Required structure

```markdown
## Scene intent
- Function, POV/objective, conflict, turn, staging, continuity, audience information.

## Visual / storyboard planning
- Keyframes/panels, captions, screen direction, transitions, visual anchors.

## Shot plan
### S01.SH01 — Label
- Narrative job
- Frame and camera
- Action / blocking
- Sound and timing / edit
- Continuity
- Execution and acceptance test
- Risk / fallback
```

## Writing rules

- The linked Script remains the authority for story events.
- State the scene’s before → after turn before choosing coverage.
- Use storyboard/keyframes to prove composition, screen direction, geography, and rhythm—not as a replacement for the plan.
- One shot has one dominant action and one camera idea.
- Split AI generations at major action, viewpoint, state, or continuity changes.
- Preserve all existing RRHub shot `id:` values.

## Quality gate

- [ ] `type: shot_breakdown` and `source:` point to a real canonical script.
- [ ] Every scene has function, pressure, turn, staging, and continuity.
- [ ] Every shot has a narrative job, execution plan, and acceptance test.
- [ ] Visual/keyframe planning uses the same shot IDs where applicable.
- [ ] No scene or shot introduces a story event absent from the script.
