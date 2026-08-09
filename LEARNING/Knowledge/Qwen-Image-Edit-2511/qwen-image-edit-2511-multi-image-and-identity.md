---
title: Qwen Image Edit 2511 — Multi-Image and Identity
category: concept
summary: How to name sources, assign roles, and preserve identity when combining multiple Qwen Image Edit references.
tags: [qwen-image-edit, multi-image, character-consistency, reference-images]
sources: 3
updated: 2026-08-09
---

# Qwen Image Edit 2511 — Multi-Image and Identity

Qwen Image Edit 2511 accepts multiple image inputs through `QwenImageEditPlusPipeline`.[5] Diffusers likewise documents multiple reference images for that pipeline.[9] Its release materials specifically claim improved portrait identity and multi-person fusion consistency versus earlier versions.[5]

## Role-first instruction grammar
`Use [subject/object] from Image 1 and [subject/object] from Image 2. Place them [relationship/position] in [destination setting]. Preserve [identity or source property] from each image.`

Always establish source identity before describing the composite. Use numbered image references consistently; do not switch between “first image,” “reference,” and “the woman” mid-instruction.

## Character continuity
For each person, protect the traits that make the result usable across shots:
- identity: face, approximate age, ethnicity, hairstyle;
- continuity: wardrobe, accessories, pose when required;
- shot design: which source supplies setting, framing, lighting, or style.

Example: `Place the woman from Image 1 beside the man from Image 2 in a café interior. Keep her face, short black hair, and gray jacket from Image 1; keep his face, tan coat, and glasses from Image 2. Match both subjects to the café lighting.`

This maps directly to Qwen's enhancer guidance: multi-image prompts must identify which image provides the edited element; styling should preserve source visual content while describing the reference style.[8]

## Do not overconstrain
Request only the traits that matter. Full descriptions of both images can conflict with the composite request and create drift. If roles are unclear, split work: first produce a clean two-person composite; then do wardrobe, lighting, or viewpoint changes in later edits.

> ⚠️ Capability boundary: improved consistency is not a guarantee of exact identity, geometry, or text reproduction. Treat every output as a visual take and evaluate it against protected traits before using it downstream.

See [[Qwen Image Edit 2511 Edit Instructions]] for preservation clauses and [[Qwen Image Edit 2511 Validation and Recovery]] for a repeatable quality gate.

Source: [[Qwen Image Edit 2511 — Source Summary]]

## Sources
[5] https://huggingface.co/Qwen/Qwen-Image-Edit-2511
[8] https://github.com/QwenLM/Qwen-Image/blob/main/src/examples/tools/prompt_utils.py
[9] https://huggingface.co/docs/diffusers/api/pipelines/qwenimage
