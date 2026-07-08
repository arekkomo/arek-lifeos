---
title: Wan2 (Open Version)
category: entity
summary: Tencent's open Wan large-scale video model family — foundational text-to-video generator that powers subsequent variants like Lightning, Alpha, and others
tags: [ai-video, wan, base-model, tencent]
sources: 1
updated: 2026-07-04
---

# Wan2 (Open Version)

Tencent's open-source large-scale video generation model family. Serves as the **foundation** for downstream variants (Wan-Alpha for RGBA, Wan2.2-Lightning for speed). Unlike closed models like Kling, Wan provides full weight access for self-hosting and fine-tuning.

## Key Features
- Large-scale diffusion transformer architecture
- Text-to-video and image-to-video modes
- Full model weights available
- Base for ecosystem of specialized variants (see `[[Wan-Alpha]]`, `[[Wan2.2-Lightning]]`)

## Model Versions
- Wan2.1: Initial release, strong T2V quality
- Wan2.2: Improved temporal coherence; Lightning variant = 4-step distilled (20x speed)
- LightX2V variants for different VRAM constraints

> ⚠️ Priority model in AI video space — multiple downstream tools build directly on it. See also `[[Vision-Language]]` framework overview for the vision-language foundation used.

## Access
[HuggingFace](https://huggingface.co/Wan-Video) and [GitHub](https://github.com/Wan-Video). Requires substantial VRAM (≥40GB recommended for 14B model).

```
## [2026-07-04] ingest | Wan2
Created entity page from Notion dump — foundation open T2V model family. Source: raw/dtb_export_archive_2026-07-04/Wan-Video.md
```
