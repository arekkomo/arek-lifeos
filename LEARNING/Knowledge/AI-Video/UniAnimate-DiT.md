---
title: UniAnimate-DiT (Alibaba)
category: entity
summary: Alibaba's DiT-based universal animate model for character-consistent video generation from single reference images
tags: [ai-video, animation, di-t, alibaba, character-consistency]
sources: 1
updated: 2026-07-04
---

# UniAnimate-DiT

Alibaba's diffusion transformer model for generating animated sequences conditioned on **single reference images**. Produces coherent motion from static character references with strong temporal consistency.

## Key Features
- Single image → video animation pipeline
- DiT-based architecture for efficient token processing
- Character-preserving across frames
- Open research release, supports custom avatars

## Use Cases
Quickly bringing concept art or reference photos to life as short clips — useful for pre-vis, mood tests, and AI-character pipelines. More direct than `[[VACE-Alibaba]]` for single-shot animation.

> ⚠️ Synergy: Combine output with `[[FilmPort]]` pipeline for full production workflow. For audio-driven motion, add `[[SkyReels-A2]]` lip-sync pass.

## Access
[GitHub](https://github.com/ali-vilab/UniAnimate). Research release from Alibaba Vision Lab.

```
## [2026-07-04] ingest | UniAnimate-DiT Alibaba
Created entity page from Notion dump — single-reference animation model. Source: raw/dtb_export_archive_2026-07-04/UniAnimate.md
```
