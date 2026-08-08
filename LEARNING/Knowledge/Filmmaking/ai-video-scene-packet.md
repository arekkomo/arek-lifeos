---
title: AI Video Scene Packet
category: concept
summary: A production packet that translates directing analysis and a shot list into discrete, continuity-aware AI-video generation tasks.
tags: [ai-video, directing, previz, shot-list, continuity, production]
sources: 5
updated: 2026-08-08
---

# AI Video Scene Packet

AI video benefits from the same directorial preparation as a physical shoot, but it needs an additional **state handoff** between shots. Treat each generated clip as a controlled take that must inherit the scene’s approved story state rather than as an isolated prompt. The directing foundation is [[Script-to-Scene-Analysis]] and [[Purposeful-Shot-Lists]]; the operational translation is an AI-native production adaptation.

## End-to-end workflow

1. **Lock the scene brief.** Define dramatic event, POV, objective/obstacle, beat map, turn and start/end power state. [[Script-to-Scene-Analysis]]
2. **Lock the staging map.** Draw the space, screen direction, actor marks, key prop states and line-of-action assumption before generating coverage. [[Directing Craft Reference Sources#1 — Rabiger|[1]]]
3. **Write the purposeful shot list.** Give each shot one beat/job plus frame, block, camera behaviour and edit intention. [[Purposeful-Shot-Lists]]
4. **Create a continuity bible.** Assign immutable IDs and approved reference frames for character appearance, wardrobe, environment, time of day, lighting, grade, lens/height language, screen direction and props.
5. **Generate in dependency order.** Generate the geography/reference shot and key performance anchors first; use approved stills or terminal frames as image/video references for dependent shots.
6. **Review by cut, not clip.** Place candidate clips in sequence, checking whether each edit preserves the beat, eyeline, direction, lighting, action and emotional escalation.
7. **Retake against diagnosis.** Name one failed constraint (for example, “B’s gaze must remain screen-left toward A”) before changing a prompt; avoid broad “make it cinematic” retries.
8. **Conform and finish.** Stabilise chosen clips, then perform editorial, sound, grade and VFX finishing against the locked scene intention.

## Per-shot generation card

```text
SCENE / SHOT / VERSION:
Dramatic beat + audience job:
Start state → end state:
Character IDs, wardrobe and emotional action:
Set / time / lighting / grade reference:
Blocking, screen direction, eyeline and prop state:
Frame: size, height, angle, lens-language, depth intent:
Camera: static or one motivated move; start → end:
Action and duration:
Must-preserve constraints:
Prompt / reference images / seed or workflow version:
Editorial in/out: preceding shot, cut trigger, following shot:
QC: identity | gaze | blocking | props | light | movement | usable handle
```

## AI-specific failure controls

- **One shot, one primary action:** complex simultaneous actions increase temporal and spatial failure risk; split complex coverage into editable units.
- **Use stateful references:** reference frames are more reliable continuity contracts than restating a long visual description each time.
- **Separate performance from spectacle:** secure readable acting/reaction plates before adding ambitious movement or effects.
- **Budget handles:** request or generate clean pre-action and post-action frames so editorial can enter and leave the clip.
- **Track approved versions:** record workflow, references and constraints for every selected shot; otherwise a later retake can silently break the scene.

## Template bundle

A minimum short-film packet contains: scene brief, staging map, shot list, continuity bible, per-shot cards, and a cut-review checklist. This is intentionally compatible with the per-shot lighting, grade, sound and focus specifications already described in [[Visual Storytelling]].

## Related pages

- [[Script-to-Scene-Analysis]]
- [[Purposeful-Shot-Lists]]
- [[Visual Storytelling]]
- [[Module-01-Visual-Language]]
