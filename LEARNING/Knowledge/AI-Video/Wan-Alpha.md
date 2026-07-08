---
title: Wan-Alpha
category: entity
summary: WeChatCV text-to-video model generating RGBA (transparent-bg) videos via diffusion transformer — direct VFX compositing use-case
tags: [ai-video, transparency, vfx, wan, rgba, compositing]
sources: 1
updated: 2026-07-04
---

# Wan-Alpha

WeChatCV's text-to-video framework that produces **RGBA videos** (transparency-ready) using a joint RGB+Alpha diffusion transformer architecture. Unlike standard T2V models, Wan-Alpha outputs semi-transparent pixels natively — hair strands, smoke, glass refraction, sparks without manual rotoscoping.

## Key Features
- Text-to-video with alpha transparency channel per frame
- Joint RGB + Alpha DIT architecture (not post-hoc matte extraction)
- ComfyUI workflow integration available
- Pretrained: Wan2.1-T2V-14B, LightX2V variants

## VFX Relevance
Direct drop-in replacement for green-screen/rotoscope workflows in AI-assisted filmmaking. Transparent output composited over live-action backgrounds without additional matting pipelines.

> ⚠️ Cross-domain note: RGBA video generation eliminates a key compositing step — see `[[SAM2Matting]]` on contrast if you need frame-by-frame refinement later.

## Installation
- Clone repo, Python ≥ 3.11, install deps from requirements.txt
- Download pretrained weights, run text prompt generation scripts
- ComfyUI nodes available for integration

> [[source: dtb Knowledge dump, 2025-11-16]] | [GitHub](https://github.com/WeChatCV/Wan-Alpha)

```
## [2026-07-04] ingest | Wan-Alpha
Created entity page from Notion dump — RGBA compositable video model. Source: raw/dtb_export_archive_2026-07-04/Wan-Alpha.md
```
