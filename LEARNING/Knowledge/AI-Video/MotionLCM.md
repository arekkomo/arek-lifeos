---
title: MotionLCM
category: entity
summary: Real-time controllable motion generation via Latent Consistency Model — 1-step inference at ~30ms/sample for text-to-motion and pose-controlled output
tags: [ai-video, motion-control, real-time, consistency-model, human-animation]
sources: 1
updated: 2026-07-04
---

# MotionLCM

ECCV 2024 paper from Tsinghua/Shanghai AI Lab proposing a **latent diffusion model for controllable motion** with real-time inference (~30ms/sample, ~1-step or few-step). Extends MLD architecture to produce text-conditioned and pose-controlled motion sequences.

## Key Features
- Text-to-motion: text prompt → human motion data (skeleton-based)
- Pose control via ControlNet in latent space (dense/sparse pelvis signals)
- 1-step inference at ~30ms/sample on GPU
- Works across diverse motion types: walking, dancing, jumping, etc.

## Architecture Notes
Builds on MLD (Motion Latent Diffusion). Uses motion ControlNet for control signals, enabling both text-driven and signal-driven generation with a single model — crucial for choreographic precision in AI-assisted animation pipelines.

> ⚠️ Cross-domain: For full-body video from motion data, chain output through `[[VACE-Alibaba]]` or `[[DreamO-ByteDance]]`. For voice → face animation, see `[[SkyReels-A2]]` which handles the speaking avatar aspect.

## Related
- [[ARDY]] is a newer interactive motion system built around autoregressive diffusion and live kinematic constraints (paths, waypoints, joints); MotionLCM instead prioritizes very low-latency latent-consistency inference.

## Access
[Project Page](https://dai-wenxun.github.io/MotionLCM-page/) | [arXiv](https://arxiv.org/abs/2404.19759) | [GitHub](https://github.com/Dai-Wenxun/MotionLCM)

```
## [2026-07-04] ingest | MotionLCM
Created entity page from Notion dump — real-time controllable motion model (ECCV 2024). Source: raw/dtb_export_archive_2026-07-04/MotionLCM-full.md
```
