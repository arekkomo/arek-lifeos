---
title: Midjourney
category: entity
summary: AI image generation service known for artistic quality and stylistic control via Discord and web interface.
tags: [ai-images, midjourney, generative-ai, text-to-image]
sources: 1
updated: 2026-04-19
---

# Midjourney

AI image generation platform by Midjourney Inc. Known for high aesthetic quality and a strong community-driven prompting culture. Operates via Discord and a web interface.

## Key techniques

### Character consistency — Pan / VR method
The core consistency challenge in Midjourney is generating the same character across multiple scenes. The **Pan & VR method** solves this by creating a character sheet: a single image containing the character in multiple poses. This sheet then serves as a visual anchor for subsequent generations.
- Source: [[notion-export-ai-image-midjourney]]

### Describe tool
Image-to-prompt reverse engineering. Upload an existing image and Midjourney generates candidate prompts that would produce a similar result. Key applications:
- Extract the "prompt DNA" of any image
- Color palette extraction and reverse-engineering of style choices
- Source: [[notion-export-ai-image-midjourney]]

### Building on foundational images
New feature allowing iterative refinement: use a photo or previously generated MJ image as the starting point for further generation. Enables compounding creative exploration rather than one-shot generation.
- Source: [[notion-export-ai-image-midjourney]]

### Vector art generation
Midjourney can produce vector-style artwork via prompt-based color and style guidance:
- Color terms like "cool colors" or "radioactive colors" drive palette
- Style terms for flat design, graphic design, and icon-style output
- Source: [[notion-export-ai-image-midjourney]]

## 3D video workflow
Midjourney images used as base frames for 3D video production. Full production workflow: MJ image → 3D conversion → video. See also [[tripo-ai]] for text/image-to-3D.
- Source: [[notion-export-ai-image-midjourney]]

## Key parameters

_`--ar`, `--style`, `--chaos`, `--weird`, `--sref`, etc. — populate from tutorials and experimentation._

## Open questions

- Which `--sref` (style reference) patterns work best for character consistency vs. the Pan/VR method?
- How does Midjourney's Describe tool compare to FLUX's reverse-prompt capabilities?

## Appears in

- [[notion-export-ai-image-midjourney]] — techniques, tools, consistency methods, 3D workflow

## Related pages

- [[Synthesis/ai-creative-tools-overview]]
- [[ai-image-generation]]
- [[flux]] — competitor
