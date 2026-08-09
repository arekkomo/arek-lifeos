---
title: GPT Image 2 Restore Sources
category: source
summary: Primary-source ledger for GPT Image 2 image editing, prompting, masks, and restoration-oriented workflows.
tags: [gpt-image-2, openai, image-editing, photo-restoration, colorization, prompting]
sources: 3
updated: 2026-08-09
source_url: https://platform.openai.com/docs/guides/image-generation
source_date: 2026-08
authors: [OpenAI]
ingested: 2026-08-09
---

# GPT Image 2 Restore Sources

## Primary sources

1. [OpenAI Image generation guide](https://platform.openai.com/docs/guides/image-generation) — GPT Image 2 image generation/editing API guidance, image and mask requirements, fidelity controls, and error guidance.
2. [OpenAI image-model prompting guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide) — OpenAI cookbook with documented production prompting patterns for edits, photorealism, identity-sensitive work, compositing, and iterative refinement.
3. [OpenAI Images API reference](https://platform.openai.com/docs/api-reference/images) — endpoint and parameter reference for image generation and edits.

## Evidence used in this knowledge set

- GPT Image 2 supports iterative, prompt-directed image edits; input images can be supplied as edit references. [1]
- Masks guide the edit rather than guaranteeing an exact boundary. The base image and mask must use the same dimensions/format, the mask must contain alpha, and the uploaded files must be under 50 MB. [1]
- In edit prompts, OpenAI recommends explicit invariants and a narrow change instruction: state “change only X,” “keep everything else the same,” and repeat the preserve list on later iterations to limit drift. [2]
- OpenAI’s cookbook recommends a stable prompt order—scene, subject, details, constraints—and short labeled segments for complex work. [2]
- Restoration/colorization recommendations in this folder are operational adaptations of those documented edit-control patterns; they are not a claim that OpenAI publishes a dedicated restoration model or automatic historical-color ground truth. [1][2]

## Scope and confidence

**High confidence:** API/model behaviour and prompting mechanics directly described by OpenAI. **Medium confidence:** restoration-specific templates, which translate the official editing patterns into an archival-photo workflow. **Do not infer:** real historical colours, lost facial detail, or scene facts from a generated result without independent source evidence.

## Related pages

- [[GPT Image 2 Restoration Workflow]]
- [[GPT Image 2 Restoration Prompting]]
- [[GPT Image 2 Colorization Control]]
- [[FireRed-Image-Edit]]
- [[Stable Layers]]
