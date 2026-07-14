---
title: "SparkVSR — Interactive Video Super-Resolution via Sparse Keyframe Propagation"
category: source
summary: Novel interactive video super-resolution framework that uses sparse keyframes as control signals to propagate HR details across entire sequences. Two-stage cross-space propagation (LR video latents + sparsely encoded HR keyframe latents) learned robust feature alignment. Supports flexible keyframe selection, reference-free guidance for blind restoration balance, and generalizes to old-film restoration and style transfer without retraining. ECCV 2026 accepted.
tags: [video-super-resolution, VSR, keyframe-propagation, interactive-control, video-processing, eccv-2026, comfui-compat]
sources: 2
source_path: https://github.com/taco-group/SparkVSR + arXiv 2603.16864
source_date: 2026-03
authors: [Jiongze Yu, Xiangbo Gao, Pooja Verlani (YouTube), Akshay Gadde (YouTube), Yilin Wang (YouTube), Balu Adsumilli (YouTube), Zhengzhong Tu]
ingested: 2026-07-13
updated: 2026-07-13
---

# SparkVSR — Interactive Video Super-Resolution via Sparse Keyframe Propagation

## TL;DR

SparkVSR is an **interactive, keyframe-conditioned video processing framework** that lets users control VSR quality by specifying sparse HR keyframes — the model then propagates those details to the entire sequence while respecting motion in the LR input. No black-box single-pass restoration: users can correct artifacts on key frames and get consistent output everywhere.

## Architecture

### Two-Stage Cross-Space Training Pipeline

1. **Keyframe conditioning:** A user selects (or auto-extracts) sparse keyframes from the LR video input and enhances them using *any* off-the-shelf image SR model
2. **Cross-space propagation:** SparkVSR fuses:
   - **LR video latents** (motion/temporal continuity source)
   - **Sparsely encoded HR keyframe latents** (quality/detail signal)
   to learn a mapping that propagates details while staying grounded in LR motion
3. **Reference-free guidance:** During inference, continuously balances between:
   - Keyframe adherence (faithfulness to user-specified high-quality frames)
   - Blind restoration quality on non-keyframe sections

### Keyframe Selection Modes

| Mode | Description | Best For |
|------|-------------|----------|
| Manual specification | User picks which frames to enhance | Precise control over artifact correction |
| Codec I-frame extraction | Auto-extract keyframes from compressed video | Practical pipeline deployment |
| Random sampling | Uniformly distributed reference frames | Quick baseline improvement without user input |

## Performance

SparkVSR surpasses VSR baselines on three evaluation metrics:
- **CLIP-IQA:** +24.6%
- **DOVER:** +21.8%
- **MUSIQ:** +5.6%

These improvements are across multiple standard benchmarks, indicating strong generalization.

## Generic Task Applicability

The architecture is intentionally task-agnostic — it works out of the box on:
1. **Standard VSR** (LR → HR video)
2. **Old-film restoration** (apply to degraded archival footage)
3. **Video style transfer** (keyframes carry style, propagated across entire sequence without retraining)

This is a significant design advantage over specialized SR models that need per-task retraining.

## ComfyUI Integration

**ComfyUI-SparkVSR extension released May 2026.** Available as a standard ComfyUI custom node. Compatible with the existing DGX Spark setup (PyTorch 2.5+, CUDA 12.4). Could serve as:
- A post-processing step in any video pipeline to boost output quality from AI video generators
- An artifact-reduction step when using models that produce frame-inconsistent results (e.g., early-stage diffusion video)
- A targeted detail enhancement tool for specific shots without re-running the entire generation

## Connections

- `Diffusion-Video-Models` — can combine with any diffusion-based video generator as a refinement step
- `AI-Image-Midjourney` — the ISR component for keyframe enhancement could use SeFi-Image's Turbo variant for speed
- Traditional VFX pipeline: equivalent to "detail pass" or "texture bake" steps, but automated via keyframe specification

## Release Status

- Code: ✅ Released (GitHub)
- Pre-trained models: ✅ Available on HuggingFace
- Training code: ✅ Released
- ComfyUI extension: ✅ Released (May 2026)
- Community deployments: RunningHub.ai, CNAPS.ai (June 2026)
