---
title: FastVideo
category: entity
summary: Unified inference and post-training framework for accelerated video generation — optimization layer for diffusion-based T2V models
tags: [ai-video, acceleration, inference-optimization, diffusion]
sources: 1
updated: 2026-07-04
---

<!-- NOTE: Sparse bookmark entry. FastVideo is the Hao-AI-Lab acceleration framework. -->

# FastVideo

Unified framework by Hao-AI-Lab for **accelerating video generation** across diffusion-based models. Provides both inference optimization and post-training distillation — essentially an acceleration layer you can drop between your pipeline and any base T2V model.

## Key Features
- Unified interface across multiple base models (SD, Wan, etc.)
- Post-training distillation for faster inference
- Inference-time optimization (attention cutting, KV caching)
- Compatible with existing ComfyUI workflows

## Use Cases
Speeding up generation when working with large models on limited hardware. Critical for iterative creative work where prompt iteration speed matters more than peak pixel quality.

> ⚠️ Synergy: `[[Wan2.2-Lightning]]` provides distilled models; FastVideo extends this across multiple base architectures.

## Installation
Clone [GitHub](https://github.com/hao-ai-lab/FastVideo). Install dependencies and configure for your target model.

> [[source: dtb Knowledge dump, 2025-08-29]] | [GitHub](https://github.com/hao-ai-lab/FastVideo)

```
## [2026-07-04] ingest | FastVideo
Created entity page from Notion dump — video generation acceleration framework. Source: raw/dtb_export_archive_2026-07-04/FastVideo.md
```
