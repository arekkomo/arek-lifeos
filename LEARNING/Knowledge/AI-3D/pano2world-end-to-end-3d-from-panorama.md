---
title: "Pano2World: End-to-End 3D Scene Generation from a Single Panorama"
category: source
summary: Takes a single indoor panorama and generates a persistent, explorable 3D Gaussian Splatting scene via unified multi-view joint denoising with View-Aware Attention Routing.
tags: [3d-generation, gaussian-splatting, panorama, novel-view-synthesis, diffusion-models]
sources: 1
source_path: arXiv:2607.00832v1
source_date: 2026-07
authors: [Zhenjia Li, Jinrang Jia, Yifeng Shi]
ingested: 2026-07-02
---

# Pano2World: End-to-End 3D Generation via Unified Multi-View Sequences

## Overview

Pano2World bridges the gap between looking around a static panorama and freely exploring a true 3D scene. Given **one indoor panoramic image** as input, it outputs a fully explorable [[gaussian-splatting]] scene — multiple poses, free camera movement, no iterative inpainting loops.

**Core approach:** Reconstruct a coarse 3D Gaussian proxy from the panorama, render it at adaptively sampled nearby poses for geometrically aligned guidance, then use a panoramic diffusion model to jointly denoise all target views via **View-Aware Attention Routing**.

## Key Technical Contributions

### View-Aware Attention Routing (VAAR)
- During joint denoising of all target views simultaneously, each view receives two parallel attention streams:
  - **Geometric constraints** from its corresponding guidance panorama (rendered from the coarse proxy)
  - **Global semantic guidance** from the original source panorama
- Naturally enforces cross-view consistency without post-hoc alignment or iterative refinement

### Latent Feature Adapter (LFA)
- Standard approaches decode multi-view hidden features back to pixel space via VAE, losing geometry information
- LFA skips this lossy bottleneck — a geometry-aware bridge module directly distills joint-denoising features into a scene latent, then decodes straight into the final 3D Gaussian representation

### Adaptive Multi-Pose Sampling
- Coarse proxy rendered at poses chosen adaptively based on scene complexity (more sampling in structurally dense areas)
- Single-shot pipeline: no iterative per-view completion that propagates inpainting error

## Why This Matters for VFX/Production

- **One panorama → explorable 3D in one pass.** No multi-stage pipeline, no accumulated error from iterative inpainting
- Useful for rapid virtual location scouting: take a single 360° photo of a real location and get an explorable scene
- Complements [[spherope-spherical-rope-panorama]] (which handles spherical positional encoding for T2I) by adding true depth navigation on top of panorama generation

## Evaluation Results

- Significantly outperforms existing methods on multi-position panoramic novel-view synthesis benchmarks
- Produces sharper geometry and more consistent textures across viewpoints compared to iterative-completion baselines
- Zero error accumulation (single-shot vs. N-step pipelines where each step compounds artifacts)

## Relationship to Existing Vault Content

| Related Entry | Connection |
|---|---|
| [[gaussian-splatting]] | Uses GS for final scene representation |
| [[spherope-spherical-rope-panorama]] | Shares 360° panorama input paradigm but adds true 3D output |
| [[tripo-ai]] | Similar text/image-to-3D goal, but Pano2World uses panoramas instead of multi-camera captures |

## Limitations

- Currently evaluated on indoor scenes only; outdoor/generalization not demonstrated
- Quality depends on the initial coarse proxy — poor panorama → poor proxy → poor guidance → degraded final scene
- Not yet publicly released as a runnable tool (paper-only at time of writing)

## Links

- arXiv: [2607.00832](https://arxiv.org/abs/2607.00832)
- Related: [[ai-3d-generation]], [[gaussian-splatting]]
