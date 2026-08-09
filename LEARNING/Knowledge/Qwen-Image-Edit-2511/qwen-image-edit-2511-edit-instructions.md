---
title: Qwen Image Edit 2511 — Edit Instructions
category: concept
summary: A natural-language instruction grammar for precise, minimal Qwen Image Edit 2511 transformations.
tags: [qwen-image-edit, prompting, instruction-following, image-editing]
sources: 2
updated: 2026-08-09
---

# Qwen Image Edit 2511 — Edit Instructions

Use **edit instructions**, not a fresh scene-description prompt. State the operation, the exact target, the requested result, and only the preservation constraints needed to bound drift. This follows Qwen's official enhancer: direct and specific, core intent unchanged, edits visually feasible, and additions coherent with the input scene.[8]

## Base grammar
`<operation> <target> <new state>. Keep <protected attributes> unchanged.`

- **Operation:** add, remove, replace, change, restore, extend, or perform inpainting.
- **Target:** name one unambiguous subject/object; use “the woman in the foreground,” not “it.”
- **New state:** give only attributes that determine the edit: material, color, pose, placement, expression, or text.
- **Protected attributes:** identity, wardrobe, pose, framing, lighting, background, or composition — only those that must survive.

The model card's own multi-image example is an instruction: place named subjects in named left/right positions, facing each other in a named setting.[5]

## Good instruction shapes
- `Replace the brass desk lamp with a matte-black anglepoise lamp. Keep the desk, window light, and camera framing unchanged.`
- `Change the jacket to deep red leather. Preserve her face, hairstyle, expression, pose, and the original background.`
- `Remove the parked car at the far right. Reconstruct the road, curb, and shadows naturally.`
- `Add “ONE MORE” in white condensed capitals on the storefront sign, centered on the existing sign panel.`

## Specific official rules to preserve
- For a clear add/delete/replace request, refine grammar only; for a vague request, add the minimum useful details such as category, color, size, orientation, or placement.[8]
- Write replacement as “Replace Y with X,” including the key visual features of X.[8]
- Put literal text in English double quotes and preserve its language and capitalization.[8]
- For identity edits, explicitly protect core traits; beauty/makeup/expression changes should be natural and subtle.[8]
- Keep a style conversion concise and put it after other edits; name the target object to avoid global unintended stylization.[8]

## Avoid
- Re-describing every visible part of the image; it increases opportunities for drift.
- “Make it better,” “more cinematic,” or “change the vibe” without a target and observable result.
- Contradictory constraints such as “remove all trees but keep all trees.” Qwen's enhancer resolves contradictions, but a clean instruction is more controllable.[8]

See [[Qwen Image Edit 2511 Task Patterns]] for operation-specific templates and [[Qwen Image Edit 2511 Validation and Recovery]] for iteration.

Source: [[Qwen Image Edit 2511 — Source Summary]]

## Sources
[5] https://huggingface.co/Qwen/Qwen-Image-Edit-2511
[8] https://github.com/QwenLM/Qwen-Image/blob/main/src/examples/tools/prompt_utils.py
