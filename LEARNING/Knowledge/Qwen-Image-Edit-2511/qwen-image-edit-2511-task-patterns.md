---
title: Qwen Image Edit 2511 — Task Patterns
category: concept
summary: Reusable instruction templates for local changes, text, styling, restoration, expansion, and design edits.
tags: [qwen-image-edit, prompting, templates, image-editing]
sources: 2
updated: 2026-08-09
---

# Qwen Image Edit 2511 — Task Patterns

These templates translate the official edit-prompt enhancer into concise requests. Fill the brackets; delete unused clauses. Qwen explicitly distinguishes add/delete/replace, text, human identity, style, inpainting/outpainting, and multi-image tasks.[8]

## Local object edit
`Replace [old object] with [new object: material, color, key shape] at [location]. Keep [protected elements] unchanged.`

`Remove [object] from [location]. Reconstruct [surface/background] naturally, matching the existing lighting and perspective.`

## Wardrobe, prop, or material
`Change [target] from [old state] to [new material/color/design]. Preserve [identity/pose/framing/background].`

For product work, name the component and material rather than saying “make it premium.” 2511’s official showcase includes industrial material replacement and design-oriented use cases.[5]

## Text replacement or addition
`Replace “[old text]” with “[new text]” on [specific surface]. Keep the same placement and layout.`

If new placement, color, or layout is important, name it; otherwise do not invent design requirements. Qwen's official enhancer requires literal text in double quotes and preservation of its language and capitalization.[8]

## Identity-safe human edit
`Change [person]'s [single attribute] to [new state]. Keep [face/age/ethnicity/hairstyle/expression/outfit/pose] unchanged.`

Choose the smallest possible protected set that captures continuity. For makeup or expression, ask for a subtle, natural change, as Qwen's own guidance requires.[8]

## Style conversion
`Change [target object or image] to [style described through 2–4 visual traits]. Preserve [source content].`

Example: `Change the woman in Image 1 to the ink-wash style of Image 2—black-and-white watercolor, soft transitions—while preserving her pose and clothing silhouette.` Qwen's enhancer says to specify the target and place any style description after the substantive edit.[8]

## Boundary expansion and fill
Use Qwen's fixed phrases when appropriate:
- Inpainting: `Perform inpainting on this image. The original caption is: [caption].`[8]
- Outpainting: `Extend the image beyond its boundaries using outpainting. The original caption is: [caption].`[8]
- Restoration/colorization: `Restore and colorize the photo.`[8]

For reference combination, use [[Qwen Image Edit 2511 Multi-Image and Identity]]. For pass/fail checks, use [[Qwen Image Edit 2511 Validation and Recovery]].

Source: [[Qwen Image Edit 2511 — Source Summary]]

## Sources
[5] https://huggingface.co/Qwen/Qwen-Image-Edit-2511
[8] https://github.com/QwenLM/Qwen-Image/blob/main/src/examples/tools/prompt_utils.py
