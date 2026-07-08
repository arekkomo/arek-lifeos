---
title: DreamO (ByteDance)
category: entity
summary: ByteDance image-to-video model for generating character-consistent videos from reference photos — style transfer with pose animation
tags: [ai-video, byte-dance, reference-animation]
sources: 1
updated: 2026-07-04
---

# DreamO (ByteDance)

ByteDance's image conditioning approach for video generation. Uses reference photos of characters or objects to generate animated sequences while preserving visual identity across frames and transferring styles between subjects.

## Key Features
- Reference character animation with pose control
- Style transfer across different subjects in video format
- Maintains identity consistency through temporal space
- Handles multiple reference images simultaneously

## Use Cases
Taking static character designs (concept art, portraits) and animating them consistently — faster than training custom LoRA models for individual characters. Good for storyboarding animated content from still references.

> ⚠️ Cross-domain: `[[VACE-Alibaba]]` also does reference-based generation but with different architecture; DreamO focuses on image-conditioned rather than video-conditioned input. For character consistency beyond video, see `[[ConsistentCharactersMJ]]` in Image domain.

## Installation
Access via [ByteDance GitHub](https://github.com/bytedance/DreamO). Follow setup guide for available configurations.

> [[source: dtb Knowledge dump, 2025-06-05]] | [GitHub](https://github.com/bytedance/DreamO)

```
## [2026-07-04] ingest | DreamO ByteDance
Created entity page from Notion dump — reference-based video animation. Source: raw/dtb_export_archive_2026-07-04/bytedance_DreamO.md
```
