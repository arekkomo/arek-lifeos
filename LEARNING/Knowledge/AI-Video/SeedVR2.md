---
title: SeedVR2
category: entity
summary: Video upscaling/restoration tool from ICEclear — increases resolution and enhances existing video content with AI super-resolution
tags: [ai-video, upscaling, post-production, restoration]
sources: 1
updated: 2026-07-04
---

# SeedVR2

AI video upscaling and restoration system. Takes lower-resolution content (from any generation source) and enhances it with super-resolution — useful bridge between AI model output limitations and production quality requirements.

## Key Features
- AI-powered video resolution enhancement
- Temporal consistency across frames (no flickering during upscale)
- Works on existing footage, not just generated content
- Restores details lost in low-res generation

## Use Cases
Post-hoc enhancement of generated clips from models like Wan2 or SkyReels that output at lower base resolutions. Critical for getting production-ready resolution without re-generating entire sequences.

> ⚠️ Compare: `[[FastVideo]]` optimizes inference speed; SeedVR2 optimizes output quality. Used in different pipeline stages — first accelerate (FastVideo), then enhance (SeedVR2).

## Access
[Project Page](https://iceclear.github.io/projects/seedvr2/) | [GitHub](https://github.com/iceclear/SeedVR2)

```
## [2026-07-04] ingest | SeedVR2
Created entity page from Notion dump — video upscaling and restoration tool. Source: raw/dtb_export_archive_2026-07-04/SeedVR2.md
```
