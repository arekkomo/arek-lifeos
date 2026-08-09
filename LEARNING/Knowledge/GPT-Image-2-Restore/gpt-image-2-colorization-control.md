---
title: GPT Image 2 Colorization Control
category: concept
summary: Historically cautious prompt and review method for colorizing restored photographs while preserving source evidence.
tags: [gpt-image-2, colorization, photo-restoration, prompting, archival]
sources: 1
updated: 2026-08-09
---

# GPT Image 2 Colorization Control

Colorization is a **creative reconstruction layer**, not evidence recovery. Treat it as separate from damage repair so a clean monochrome restoration remains available. This separation follows the general edit-control principle of limiting each pass to one change and explicitly preserving all other image properties. [[GPT Image 2 Restore Sources]]

## Before colorization

- Lock an accepted monochrome restoration and keep it as the reference/master.
- Record confirmed colour evidence: surviving print tint, uniform/service records, product references, location research, or family testimony.
- Divide assumptions into **confirmed**, **probable**, and **unknown**. Only confirmed/probable colours should be directed; unknown areas should remain restrained.

> ⚠️ Contradiction: saturated or emotionally “right” colour can make an image feel more historical while making it less defensible. Prefer low-saturation, period-plausible colour when evidence is weak. [[GPT Image 2 Restore Sources]]

## Controlled colorization template

```text
Task: colorize this restored photograph conservatively.
Confirmed colours: [list only documented colours].
Probable colours: [list with restrained alternatives].
Unknown areas: use subdued, period-plausible neutral tones; do not imply certainty.
Preserve exactly: people and identity, facial detail, clothing cut, object geometry, composition, camera angle, lighting direction, tonal hierarchy, grain, and all text.
Do not: modernize the scene, increase saturation, add cinematic teal/orange grading, change skin tone or ethnicity, alter fabric/material detail, add objects, or change the crop.
Output: natural, restrained colour consistent with the original light and photographic material.
```

## Pass order

1. **Global palette:** only white balance and a restrained overall palette.
2. **High-evidence anchors:** uniforms, known products, flags, signage, or architectural colours with documentary support.
3. **People:** preserve identity and avoid cosmetics/skin smoothing; use evidence where available.
4. **Material check:** verify foliage, sky, skin, metal, fabric and shadows remain coherent under the original lighting direction.

When needed, use a mask for a local intervention. The mask must match the base image in dimensions/format and include alpha; OpenAI documents masks as guidance rather than a pixel-exact hard boundary. [[GPT Image 2 Restore Sources]]

## Acceptance checklist

- Compare colour result, monochrome restoration, and original side by side.
- Ask whether every strong colour has evidence or is visibly marked as an interpretation.
- Reject selective saturation, glowing skin, inconsistent shadow colours, and colour bleed at object boundaries.
- Export both `restored-mono` and `restored-colour-interpreted` versions; never overwrite the master.

## Related pages

- [[GPT Image 2 Restoration Workflow]]
- [[GPT Image 2 Restoration Prompting]]
- [[GPT Image 2 Restore Sources]]
