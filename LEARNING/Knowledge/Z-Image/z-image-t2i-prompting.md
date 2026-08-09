---
title: Z-Image T2I Prompting
category: concept
summary: A reproducible prompt method for Z-Image storyboard frames: one visual intention, explicit composition, and controlled iteration.
tags: [z-image, text-to-image, prompting, storyboard, previsualization]
sources: 4
updated: 2026-08-09
---

# Z-Image T2I Prompting

Z-Image’s official examples are natural-language visual descriptions built from subject attributes, wardrobe/props, environment, lighting and focal treatment—not a special tag syntax. [[Z-Image Official Source Summary#Confirmed operating facts|[1]]] Write for a **single readable image intention**, then make the shot’s essential constraints explicit.

## Prompt construction order

1. **Story job + shot:** name the viewer’s required read: establish geography, isolate a reaction, reveal a prop, or register a turn.
2. **Subject and action:** state who/what is visible and one decisive, still-image-readable action or pose.
3. **Blocking and composition:** define subject placement, eyeline direction, relative depth and salient negative space.
4. **Environment and continuity:** specify location, time, recurring wardrobe, prop state and only the set details that affect the shot.
5. **Camera language:** give frame size, angle/height, lens *character* and depth intent; use this as a visual instruction, not decoration.
6. **Light, palette and texture:** state source direction/quality, exposure mood, grade/palette and medium/finish.
7. **Must-preserve clause:** end with the two or three constraints that would make the frame unusable if lost.

This order is a production heuristic. It makes a directorial shot specification legible to an image model; it is not a claim that Z-Image parses clauses in this order. [[Z-Image Official Source Summary#Evidence boundary|[1]]]

## Storyboard prompt template

```text
[shot job]. [framing] of [subject] [single pose/action],
[blocking / screen direction / eyeline].
[environment and continuity anchors].
[camera height / angle / lens character / depth].
[lighting direction and quality], [palette / grade], [medium / finish].
Must preserve: [constraint 1]; [constraint 2]; [constraint 3].
```

### Example: reaction plate

```text
Reaction plate: intimate medium close-up of Mara, stopped in the doorway,
looking screen-left toward the unseen speaker; her right hand still grips the
half-open apartment door. Rain-dark wool coat, brass key in her left hand,
1950s hallway behind her falling softly out of focus. Eye-level camera,
portrait-lens compression, shallow depth. Single warm practical from frame
right against cool blue window spill, muted teal and amber grade, restrained
35 mm film grain. Must preserve: screen-left eyeline; key in left hand;
doorway geography.
```

## Prompt constraints

- One frame should solve one dramatic read. Split competing actions or coverage needs into separate cards. [[AI-Video-Scene-Packet#AI-specific failure controls]]
- Prefer observable visual facts over evaluative labels: replace “cinematic” with the framing, light, palette and texture that create the intended look.
- Use precise relations for multiple subjects: left/right, foreground/background, looking toward/away from, and which hand holds which prop.
- Keep continuity anchors stable across sibling shots; change only the shot-specific variable (frame, action, light state, or camera relation).
- Avoid relying on quoted copy, logos or critical on-frame typography in a storyboard plate. Z-Image’s bilingual text rendering is a stated capability, but exact wording remains a separate acceptance test, not a safe prompt assumption. [[Z-Image Official Source Summary#Confirmed operating facts|[1]]]

## Negative prompting

For the standard Z-Image checkpoint, use a short negative prompt only to name **observed recurring failures** (for example, extra fingers, duplicate subject, unwanted text, watermark). Official guidance strongly recommends negative prompts for this checkpoint. [[Z-Image Official Source Summary#Confirmed operating facts|[1]]]

Do not carry this behavior to Turbo: the official Turbo example sets guidance to zero, and its model table declares no CFG. Use clear positive constraints, seed variation and selection instead. [[Z-Image Official Source Summary#Confirmed operating facts|[1]]]

## Related pages

- [[Z-Image Official Source Summary]]
- [[Z-Image Generation Settings]]
- [[Z-Image Storyboard Stills]]
- [[Purposeful-Shot-Lists]]
- [[AI-Video-Scene-Packet]]
