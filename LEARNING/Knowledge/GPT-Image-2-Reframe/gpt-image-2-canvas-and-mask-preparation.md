---
title: GPT Image 2 Canvas and Mask Preparation
category: concept
summary: Plate-preparation checklist for reliable GPT Image 2 reframes, including extension geometry and mask-boundary safeguards.
tags: [gpt-image-2, canvas, mask, image-editing, plate-prep]
sources: 3
updated: 2026-08-09
---

# GPT Image 2 Canvas and Mask Preparation

Source basis: [[GPT Image 2 Reframe — Source Summary]]. OpenAI documents image editing with image inputs and alpha-bearing masks; this page adds production preparation decisions for reframing. [OpenAI Image generation guide](https://platform.openai.com/docs/guides/image-generation)

## Prepare the plate before prompting

1. **Pick the final delivery frame first.** Decide the target aspect ratio and whether the extension is left, right, top, bottom, or asymmetric. API size/output options belong in the request configuration, while the prompt says what should exist in the new region. [OpenAI Images API reference](https://platform.openai.com/docs/api-reference/images)
2. **Place the original plate on that larger canvas.** Preserve its pixel scale; do not resize it merely to fill the target frame unless a scale change is desired.
3. **Define protected versus editable areas.** In the mask/canvas, expose the new canvas region for painting while keeping identity-critical plate pixels protected.
4. **Leave a safety margin.** Do not align a critical face, hand, product edge, logo, or legible text exactly to the edit boundary.
5. **Record the continuation cues.** Note horizon, vanishing direction, light vector, lens feel, palette, and usable negative-space requirement before writing the prompt.

## Alpha/mask interpretation

Treat transparency as an editing instruction, not decoration. The Image API guide explains mask-based editing through alpha-channel regions and notes that results may not track a mask edge perfectly. [OpenAI Image generation guide](https://platform.openai.com/docs/guides/image-generation) Build for this uncertainty: give the model overlap/context around an edge and keep critical information away from it.

## Canvas decision table

| Goal | Canvas/mask setup | Prompt focus |
|---|---|---|
| 16:9 to 2.39:1 | Add lateral canvas, usually on the compositionally weaker side | New set extension plus intentional negative space. |
| Portrait to landscape | Add substantial left/right canvas; retain subject scale | Environment architecture, horizon, and camera geometry. |
| Tight shot to establishing frame | Add all sides conservatively in stages | First ground/sky geometry, then set dressing; avoid a one-pass radical expansion. |
| Product or character poster | Add clean region for copy and preserve hero silhouette | Background continuation, lighting, and explicitly empty copy space. |

## Preflight checklist

- Does the source plate contain a subject, logo, or text that must be outside the editable boundary?
- Can the prompt name a credible continuation of each visible plane (floor, wall, sky, water, road)?
- Is the desired empty space explicit?
- Is a staged extension safer than one extreme expansion?

Continue with [[GPT Image 2 Reframe Iteration and QA]] before accepting a result.
