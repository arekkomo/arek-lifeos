---
title: PixWorld — Unified Pixel-Space 3D Generation and Reconstruction
category: concept
summary: Single model unifying 3D scene generation and reconstruction in pixel space via diffusion, eliminating VAE dependency and adding geometry perception loss.
tags: [3d-generation, 3d-reconstruction, pixel-space-diffusion, unified-model, geometry-perception]
sources: 1
source_path: arxiv/2607.05373
source_date: 2026-07
authors: []
ingested: 2026-07-07
updated: 2026-07-07
---

# PixWorld — Pixel-Space Diffusion for Unified 3D Tasks

## What It Is

**PixWorld** unifies 3D scene generation and reconstruction via a single model. Instead of defining the diffusion objective on compressed latent features, supervision operates directly on rendered images. This aligns optimization with actual 3D scene fidelity rather than [[VAE]] reconstructions.

## The Problem with Latent-Space Unification

Recent works attempt to unify generation and reconstruction in latent space. They suffer from three issues:

1. Information loss from encoding through the VAE bottleneck
2. Misaligned optimization — diffusion operates on latents that may not match 3D quality
3. Separate autoencoder dependency constrains the unified model capacity

PixWorld avoids all three by working directly in pixel space.

## Architecture

### Pixel-Space Diffusion

Diffusion supervises rendered multi-view images rather than latent codes. Generation quality maps directly to 3D structure without VAE distortion. Reconstruction and generation share the same training objective. No separate autoencoder required.

### Geometry Perception Loss

Beyond standard photometric and perceptual losses at the 2D level, PixWorld adds a **geometry perception loss**. This aligns rendered views with ground truth in the feature space of a pretrained 3D foundation model. Structural supervision during training adds no parameters to the diffusion backbone.

| Loss Component | Level | Purpose |
|---|---|---|
| Photometric | 2D pixel | Raw image fidelity |
| Perceptual | 2D feature | High-level visual quality |
| Geometry Perception | 3D-aware feature | Structural 3D consistency |

## Results

Outperforms prior latent-space generation methods across benchmarks. Matches SOTA reconstruction methods on standard tasks. A unified pixel-space approach proves superior to splitting into separate models.

## Practical Relevance

Applicable to VFX pipelines where both asset creation and scene capture are needed. Eliminates pipeline bifurcation.

Compatible with [[ComfyUI]] workflows via rendered-image supervision. Useful alongside [[Gaussian Splatting]] methods where GS optimization is impractical.

## Related Work

- [[SynCity 3000]] — Scene-scale 3D diffusion (different scale focus)
- [[Pano2World]] — Single panorama to Gaussian Splatting (unifies capture to 3D in fewer steps)
- [[OrbitForge]] — Video-to-3D via Gaussian Splatting proxy (coherent 3D from imperfect inputs)
