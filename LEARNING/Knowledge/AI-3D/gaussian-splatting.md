---
title: Gaussian Splatting (Radiance Fields)
category: concept
summary: Real-time 3D scene representation technique using 3D Gaussians as primitives; enables high-fidelity novel view synthesis from photographs or video at render speeds far exceeding NeRF.
tags: [vfx, 3d-reconstruction, radiance-fields, nerf, gaussian-splatting, virtual-production]
sources: 1
updated: 2026-04-19
---

# Gaussian Splatting (Radiance Fields)

**Gaussian Splatting** (formally: 3D Gaussian Splatting, 3DGS) is a real-time radiance field rendering technique. It represents scenes as a cloud of 3D Gaussians rather than a neural network (as in NeRF), enabling real-time novel view synthesis.

## How it works

1. Input: multiple photographs or video frames of a scene
2. Structure from Motion (SfM) recovers camera positions
3. 3D Gaussians are placed and optimized to reproduce the input views
4. Rendering: Gaussians are splatted (projected and alpha-composited) onto the image plane in real time

## Why it matters for VFX/production

- **Real-time rendering** — unlike NeRF (seconds per frame), 3DGS renders at interactive rates
- **High fidelity** — competitive with or exceeding NeRF quality in many scenes
- **Consumer-to-professional pipeline** — iPhone video → Gaussian Splat → VFX asset
- **Location scanning** — capture real environments cheaply for set extensions, virtual production

## Tools using Gaussian Splatting

- [[volinga]] — professional desktop suite for VFX/TV/entertainment
- [[lyra]] — iPhone video to 3D reconstruction

## Relationship to NeRF

| | NeRF | Gaussian Splatting |
|---|---|---|
| Representation | Neural network | Explicit 3D Gaussians |
| Render speed | Slow (seconds/frame) | Real-time |
| Training speed | Slow | Faster |
| Editability | Hard | More accessible |

## Related pages

- [[volinga]]
- [[lyra]]
- [[dejavu]]
- [[Synthesis/filmmaking-production-overview]]
- [[notion-export-filmmaking-vfx-editing]]
