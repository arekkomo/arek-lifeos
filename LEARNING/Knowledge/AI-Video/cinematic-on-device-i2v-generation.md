---
title: "CineMobile — On-Device Image-to-Video Diffusion for Cinematic Camera Motion"
category: concept
summary: Three-fold optimization (distillation pruning, efficient sampling, mobile kernel) enables cinematic I2V generation on smartphone hardware with bullet-time and dolly-zoom effects
tags: [video-generation, image-to-video, mobile-inference, diffusion-optimization, camera-motion]
sources: 1
updated: 2026-07-07
source_path: arxiv.org/abs/2607.03803
source_date: "2026-07"
authors: [Xuyao Huang, Zelai Deng, Xu Wang, Xizhong Xiao]
ingested: 2026-07-07
---

## What It Does

Diffusion Transformers (DiTs) produce excellent video but require server-grade GPUs. CineMobile targets **real-time I2V generation on phone SoCs** by combining distillation-guided pruning, efficient sampling, and hardware-aware kernel optimization. Focus: cinematic camera effects (bullet time, dolly zoom, slow motion, crane shots).

## How It Works

1. **Distillation-Guided Pruning** — A distilled student model's gradients identify redundant layers in the teacher DiT. Only layers with high pruning-sensitivity scores are retained, reducing parameters by 4-6× while preserving motion quality
2. **Two-Stage Efficient Sampling** — High-level scene composition uses a compact 0.5B backbone (fewer steps). Refinement passes use selective full-model attention only on spatial regions requiring detail (motion boundaries, texture-heavy areas)
3. **Mobile Kernel Optimization** — Custom convolutions and attention kernels tuned for ARM Mali/Adreno GPU architectures. Uses INT8 weight caching + block-sparse computation patterns

## Key Technical Details

- Achieves ~7 FPS I2V at 480p on flagship Android SoC (骁龙 Gen 3)
- Supports 16-frame sequences with bullet-time, dolly-zoom, slow-mo, crane, and pan effects via motion-prompt tokens
- Trained as a distilled adapter on top of existing DiT checkpoints (no full retraining from scratch)

## Relevance Pipeline: Where It Fits

- **ComfyUI**: Not directly applicable (server-side tool), but the pruning methodology informs which modules matter for video quality — useful when selecting LoRAs or sub-modules for [[HunyuanVideo]] workflows
- **Content Creation**: On-device means no network latency or privacy concern for quick storyboarding
- **Comparison**: Similar motivation to [[NaviCache]] (test-time acceleration) but targets different hardware tier

> **Adjacent to**: [[NaviCache]], [[HunyuanVideo]], [[Wan2.1]], [[ISPA]]

## Limitations

- 480p resolution; not production quality for final output
- Tested on single SoC class (骁龙 Gen 3); porting to iOS or mid-range chips unproven
- Distillation-pruning is one-time per teacher model; adapting requires re-running the sensitivity analysis pipeline
