---
title: "UltraImageGen: Ultra-High-Resolution Image Generation with Hierarchical Local Attention"
category: source
summary: Framework enabling text-to-image generation at 8K+ resolution by replacing global attention with hierarchical local windows guided by low-res semantics.
tags: [text-to-image, diffusion-models, high-resolution, flux, hierarchical-attention, loora]
sources: 1
source_path: arXiv:2510.16325v4
source_date: 2025-10
authors: [Yuyao Zhang, Yu-Wing Tai]
ingested: 2026-07-02
---

# UltraImageGen: Efficient Ultra-High-Resolution Image Generation

## Overview

UltraImageGen solves a fundamental bottleneck in text-to-image diffusion models: the quadratic attention complexity that caps practical resolution at ~1K×2K (sub-2MP). Models like [[flux]] and Stable Diffusion 3 simply run out of VRAM before they can handle ultra-high-resolution latents.

**Core innovation:** Replace global self-attention with **hierarchical local attention** — dividing high-resolution latents into fixed-size GPU-aligned windows while using a low-resolution latent as a semantic anchor. Attention complexity drops from O(N²) to near-linear, enabling resolutions beyond 8K with a **10× speedup**.

## Key Technical Components

### Hierarchical Local Attention Windows
- High-res latents divided into fixed-size local windows → reduces attention from quadratic to near-linear
- A parallel low-resolution latent equipped with scaled positional embeddings injects global semantics as an anchor

### LoRA Bridge Between Global and Local Pathways
- Lightweight LoRA adapts pretrained models to bridge the structural gap between global-attention training data and local-window inference
- Ensures cross-window semantic consistency (e.g., matching skin tones, lighting direction) across structure and detail levels

### Token Repermutation for GPU Efficiency
- Tokens re-permuted in "window-first" order so that dense local blocks in attention computation align with fixed-size 2D windows regardless of output resolution
- Makes the same computation kernel work identically at 1K, 4K, or 8K — no architecture changes needed per resolution

## Practical Significance for ComfyUI/Workflow Users

- **Drop-in compatible** with pretrained Flux/SD3 models via LoRA — no full model retraining required
- Opens the door to print-resolution image generation (billboard quality, large-format poster rendering) from ComfyUI workflows
- The 10× speedup means 8K inference runs in roughly the same time a global-attention model would need for 2K

## Performance Metrics

| Resolution | Speed vs. Full Attention | VRAM Usage | Quality (FID) |
|---|---|---|---|
| 4K | ~3× faster | ~60% of baseline | Competitive |
| 8K | ~10× faster | ~45% of baseline | Superior to upscaling |

> **Comparison:** Unlike [[flux2-klein]] which targets high-res through architectural scaling, UltraImageGen achieves its gains purely through attention redistribution — making it applicable to any DiT-based model.

## Limitations

- Cross-window seam artifacts at very low LoRA ranks; requires ≥4 rank for clean transitions
- Currently demonstrated on DiT architectures; adapting to UNet-based models (SDXL) is non-trivial
- Low-res global anchor means overall composition quality depends partly on the low-res model's prompt adherence

## Links

- arXiv: [2510.16325](https://arxiv.org/abs/2510.16325)
- Related: [[flux]], [[comfyui]], [[ai-image-generation]]
