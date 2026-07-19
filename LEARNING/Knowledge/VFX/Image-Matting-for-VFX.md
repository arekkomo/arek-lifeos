---
title: "Image Matting for VFX"
category: concept
summary: Extracting an alpha matte for compositing, with tool choice determined by whether the asset is a single image or a temporally coherent video sequence.
tags: [image-matting, alpha-matte, vfx-compositing, background-removal, rgba]
sources: 1
updated: 2026-07-19
---

# Image Matting for VFX

Matting preserves fractional transparency at object boundaries; it is more precise than a binary segmentation mask for hair, glass, glow, smoke, soft shadows, and anti-aliased graphics.

## Tool selection

| Need | Relevant library tool |
|---|---|
| Difficult **single image**: glass, camouflage, typography, glow, illustrations | [[Lucida]] |
| Temporally coherent **video** alpha matte / rotoscoping | [[SAM2Matting]] |
| Native RGBA video generation | [[Wan-Alpha]] |
| Semantic layer decomposition, not necessarily a precise foreground matte | [[Stable Layers]] |

## Pipeline note

A reliable compositing pass should retain the resulting RGBA/alpha output and perform color decontamination when foreground edge colors were contaminated by the original background.
