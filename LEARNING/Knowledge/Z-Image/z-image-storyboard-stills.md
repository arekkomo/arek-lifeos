---
title: Z-Image Storyboard Stills
category: concept
summary: A shot-card workflow for generating selectable, continuity-aware Z-Image stills before AI-video production.
tags: [z-image, storyboard, previz, directing, continuity, text-to-image]
sources: 4
updated: 2026-08-09
---

# Z-Image Storyboard Stills

Use Z-Image stills as **previsualization decisions**, not decorative concept art: each accepted frame should clarify geography, performance, screen direction, prop state, light or edit intent for a later shot. This extends the vault’s [[Purposeful-Shot-Lists]] and [[AI-Video-Scene-Packet]] process using Z-Image’s documented natural-language T2I path. [[Z-Image Official Source Summary#Confirmed operating facts|[1]]]

## Board generation sequence

1. Start with the completed scene analysis and purposeful shot list—not a pile of unranked visual ideas. [[Purposeful-Shot-Lists#Coverage design pass]]
2. Generate the **geography anchor** first: an orienting wide or two-shot that locks location, line of action, key lighting and repeated props.
3. Generate the **performance anchors**: readable singles/reactions at the relevant beat, preserving the same wardrobe, eyeline, screen direction and grade.
4. Generate the **story-specific inserts** only where a prop/detail carries information or creates an editorial option.
5. Approve one canonical still per shot and make it the visual reference for downstream image-to-video or edit exploration. Record the run data described in [[Z-Image Generation Settings#Controlled storyboard test ladder]].

## Z-Image shot card

```text
SCENE / SHOT / VERSION:
Beat + audience job:
Reference-state ID (look / wardrobe / props / geography):
Prompt:
Negative prompt (base model only, if used):
Checkpoint / dimensions / steps / guidance / CFG-normalization:
Seed and batch position:
Acceptance test: framing | eyeline | props | light | palette | usable cut relation
Approved still path / reference ID:
```

## Board acceptance criteria

A still is accepted only when it:

- communicates the stated beat/job at thumbnail size;
- preserves the declared screen direction, eyeline and key prop state;
- belongs to the shared look bible (wardrobe, location, light direction, palette and lens language);
- supplies a distinct editorial option rather than duplicating another shot; and
- has recorded prompt/run metadata so it can be recreated or revised intentionally.

## Work in board families, not isolated winners

Build a family from a stable source frame: anchor wide → character single → reaction → insert → altered post-turn state. This is a directing workflow heuristic, not a claim that text prompting alone guarantees identity or continuity. When a subsequent tool supports image reference, use the approved still as the state handoff; the vault’s scene packet treats references as a stronger continuity contract than repeatedly restating a long description. [[AI-Video-Scene-Packet#AI-specific failure controls]]

## Deliberate handoff to AI video

For each approved Z-Image board, give the video-generation card the still plus only the variables allowed to change: action, camera movement, duration, sound/edit intention and any approved lighting transition. The still locks visual state; the video prompt adds temporal state. [[AI-Video-Scene-Packet#Per-shot generation card]]

## Related pages

- [[Z-Image T2I Prompting]]
- [[Z-Image Generation Settings]]
- [[Z-Image Official Source Summary]]
- [[Purposeful-Shot-Lists]]
- [[AI-Video-Scene-Packet]]
