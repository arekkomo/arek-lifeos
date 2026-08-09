---
title: GPT Image 2 Reframe Iteration and QA
category: concept
summary: A staged editing loop and acceptance checklist for GPT Image 2 reframes and outpainted source plates.
tags: [gpt-image-2, reframe, outpainting, qa, iteration, vfx]
sources: 3
updated: 2026-08-09
---

# GPT Image 2 Reframe Iteration and QA

Source basis: [[GPT Image 2 Reframe — Source Summary]]. This production loop turns a generative edit into a reviewable plate rather than accepting the first plausible output.

## Staged workflow

1. **Geometry pass** — Extend the canvas with large scene structure only: sky, road, floor, wall, water, or principal background masses. Evaluate perspective and framing before adding detail.
2. **Continuity pass** — Correct horizon, lens feel, light direction, atmospheric depth, and tonal continuity using the same plate as input.
3. **Dressing pass** — Add secondary architecture, foliage, props, texture, or controlled negative space only after the large structure reads.
4. **Repair pass** — Make narrow local repairs for seam artifacts, repeated motifs, warped text, impossible reflections, or subject drift.
5. **Finishing pass** — Export/select the needed format and take the approved plate into compositing, color management, or reconstruction.

The Image API supports iterative image editing through image inputs; use that capability to isolate change intent rather than repeatedly requesting a wholly different image. [OpenAI Image generation guide](https://platform.openai.com/docs/guides/image-generation)

## Acceptance criteria

| Check | Question |
|---|---|
| Framing | Does the final aspect ratio create the intended shot, title space, or editorial handle? |
| Seam | At 100%, do linework, texture frequency, blur, grain, and depth remain continuous across the old/new boundary? |
| Geometry | Do horizon, perspective, scale, occlusion, and reflections agree with the original plate? |
| Light | Are key direction, shadow softness, exposure, color temperature, and practical-light logic continuous? |
| Identity | Are the protected subject, product, costume, pose, and text materially unchanged? |
| Editorial | Is the extension useful—rather than merely plausible—for crop, copy, camera move, or set-extension use? |

## Iteration language

Use a correction that names the defect and the smallest permitted change:

> Keep the original plate unchanged. In the added left region only, reduce the building scale so its window lines converge to the existing vanishing point. Preserve the warm camera-right key, wet-road reflections, and empty upper-left title space.

Avoid "fix it" or "make it better." They give no spatial target and invite uncontrolled changes.

## Downstream handoff

For a VFX pipeline, retain the original plate, the expanded canvas/mask, each approved generation, and the final prompt. This makes later paint fixes reproducible and keeps a clean source for [[Stable Layers]], [[Flux.Image.Edit]], or 3D extraction in [[image-blaster]].
