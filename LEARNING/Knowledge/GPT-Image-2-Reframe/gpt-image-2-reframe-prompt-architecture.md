---
title: GPT Image 2 Reframe Prompt Architecture
category: concept
summary: Prompt grammar for asking GPT Image 2 to paint only into an extended image region while retaining the source plate.
tags: [gpt-image-2, prompting, reframe, outpainting, image-editing]
sources: 3
updated: 2026-08-09
---

# GPT Image 2 Reframe Prompt Architecture

Source basis: [[GPT Image 2 Reframe — Source Summary]]. The API edit/mask behavior is documented by OpenAI; the grammar below is a practical prompting convention.

## Core rule

Describe **what is newly visible beyond the original frame**, not a new image and not a list of things to preserve. Attach the source image and use an edit canvas/mask that exposes the added region. [OpenAI Image generation guide](https://platform.openai.com/docs/guides/image-generation)

## Prompt grammar

`Extend [direction / final framing]. In the newly revealed region, paint [new visual content]. Continue [scene geometry + perspective]. Match [lens / camera height + light + grade + texture]. Keep [identity-critical source facts] unchanged.`

Use one clause per decision. Lead with the extension direction because it anchors the spatial task; name content next; then constrain the physical and photographic continuity.

## Good reframe prompt

> Extend the frame 30% to camera-left. In the newly revealed region, paint the continuation of the rain-wet alley: recessed shop fronts, a narrow pavement, and pooled reflections. Continue the existing one-point perspective and low camera height. Match the sodium-vapor practicals, blue ambient fill, 35 mm lens perspective, shallow depth of field, and film-grain level. Keep the person, wardrobe, sign text, and original right-hand composition unchanged.

## Weak prompt

> Make this image wider and cinematic. Do not change anything.

It does not specify the invented region, scene continuation, or continuity targets. The model must infer all three and may spend its freedom altering the plate.

## Decision order

1. **Frame instruction** — direction and approximate amount or target composition.
2. **New-region content** — objects, architecture, terrain, sky, or negative space to paint.
3. **Spatial continuation** — horizon, vanishing direction, ground plane, occlusion order, and scale.
4. **Photographic continuation** — lens behavior, camera height, depth of field, exposure, key/fill direction, grade, grain.
5. **Lock list** — only the source facts that must survive: hero subject, product, text, pose, or protected composition.

## Practical limit

Do not overload a single edit with a reframe plus a major style change, relight, wardrobe swap, and subject replacement. Separate those into successive edits; the source image is the continuity anchor for each pass. [[GPT Image 2 Reframe Iteration and QA]]

## Related pages

- [[GPT Image 2 Outpaint Continuity Controls]]
- [[GPT Image 2 Canvas and Mask Preparation]]
- [[Flux.Image.Edit]]
