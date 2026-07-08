---
title: Wan2.2-Lightning
category: entity
summary: Distilled 4-step variant of Wan2.2 T2V - up to 20x speed gain with LoRA quantized variants for smaller GPUs
tags: [ai-video, wan, acceleration, diffusion, lightning, lora]
sources: 1
updated: 2026-07-04
---

# Wan2.2-Lightning

Distilled version of Tencent's Wan2.2 by the LightX2V team (Sept 2025). Produces text-to-video and image-to-video with **only 4 inference steps** — up to 20x speed gain vs base model while maintaining fidelity.

## Key Features
- 4-step diffusion pipeline (typically 100+ steps)
- Output: 480P–720P with temporal stability improvements
- LoRA variants for GPU-limited deployment (~80GB VRAM baseline for full model)
- ComfyUI compatible

## Use Cases
- Rapid cinematic generation/prototyping
- Real-time storyboarding in AI filmmaking pipelines  
- Previewing compositions before heavy generation runs

> ⚠️ Cross-domain: For production-grade output after Lightning pass, see `[[GenFocus]]` on post-hoc enhancement.

## Installation
Access via Hugging Face; use with diffusers or ComfyUI nodes. LoRA/quantized variants for smaller GPUs available.

> [[source: dtb Knowledge dump, 2025-11-16]] | [HuggingFace](https://huggingface.co/lightx2v/Wan2.2-Lightning)

```
## [2026-07-04] ingest | Wan2.2-Lightning
Created entity page from Notion dump — distilled 4-step T2V model. Source: raw/dtb_export_archive_2026-07-04/Wan2.2-Lightning.md
```
