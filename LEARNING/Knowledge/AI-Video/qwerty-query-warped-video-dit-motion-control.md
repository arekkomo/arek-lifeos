---
title: "QWERTY: Training-Free Motion Control via Query-Warped Video Diffusion Transformers"
category: concept
summary: Training-free motion control for image-to-video DiTs using spatial warping of query tokens in 3D full attention layers, enabling object trajectory and optical flow control without fine-tuning.
tags: [video-generation, motion-control, diffusion-transformer, training-free, ComfyUI, i2v]
sources: 1
updated: 2026-07-04
---

# QWERTY: Query-Warped Video Diffusion Transformers

## Overview

QWERTY is a training-free motion control framework that works with pretrained image-to-video diffusion transformers (DiTs). Instead of fine-tuning with spatial prompts like bounding boxes, it manipulates the 3D full attention mechanism directly by warping frame-invariant semantic queries.

**Key insight:** The noise predicted by query-warped DiTs naturally guides the diffusion trajectory toward desired motion patterns.

## Technical Approach

### Query Warping in Attention Layers

DiT architectures use 3D attention over spatial (H×W) and temporal (T) dimensions simultaneously. QWERTY operates on the frame-invariant semantic subspace of queries:

1. Extract query embeddings from the DiT attention layers
2. Apply user-defined spatial warps (object trajectories, optical flow fields) to these query positions
3. The warped queries shift predicted noise toward motion-consistent denoising directions

### Self-Guidance via Latent Optimization

QWERTY uses the query-warped noise prediction as self-guidance signal:

- First pass: standard DiT denoising produces a baseline latent
- Second pass: query-warped attention refines motion direction of that latent
- Combined guidance stabilizes control without degrading visual quality

### Performance vs. Fine-Tuning

Experiments show QWERTY achieves competitive performance against fine-tuned methods with additional spatial conditioning, while requiring zero training data or compute beyond the pretrained model weights.

## Practical Applications

- **ComfyUI integration:** Drop-in workflow for motion-directed i2v generation — feed trajectory JSON or optical flow maps as conditioning alongside standard prompt + seed
- **Filmmaking previs:** Control object movement in generated video without retraining models
- **DaVinci Resolve pipeline:** Pre-generate controlled motion clips that align with storyboards

## Relationship to Existing Work

Extends [[WorldDirector]] — uses different control mechanism. WorldDirector relies on an LLM to coordinate trajectories; QWERTY applies warping directly in the DiT attention space, which is lower latency since no LLM coordination step is needed.

Complement [[TempAct]]. TempAct handles high-level prompt decomposition and temporal planning for autoregressive generation. QWERTY targets low-frame motion control within individual chunks.

Contrasts with [[PointDiT]] — PointDiT estimates geometry from single images. QWERTY controls motion in video generation, but both operate on 3D attention/geometry representations.

---

## References

- arXiv: 2607.xxxx (QWERTY paper, published 2026-07-02)
- Targets pretrained i2v DiT backbones including [[CogVideoX]] and [[Wan 2.1]] families
