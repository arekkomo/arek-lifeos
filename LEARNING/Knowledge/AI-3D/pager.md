---
title: PaGeR — Panoramic Geometry Estimation Engine
category: source
summary: 360-degree panoramic geometry estimation via multi-view foundation models. ETH Zurich approach for unified panoramic scene understanding of any camera input — including single-image and video inputs.
tags: [panoramic-geometry, 360-view, 3dgs, virtual-production, eth-zurich, scene-understanding]
sources: 1
updated: 2026-07-01
ingested: 2026-07-01
source_url: https://github.com/prs-eth/PaGeR
---

# PaGeR — Panoramic Geometry Estimation Engine

> 360-degree panoramic geometry estimation via multi-view foundation models. ETH Zurich approach for unified panoramic scene understanding of any camera input.

**URL:** [prs-eth/PaGeR](https://github.com/prs-eth/PaGeR) · [Paper: arXiv 2403.18858](https://arxiv.org/abs/2403.18858)

**Type:** Github | **Tags:** VFX

## About

Unified 360 scene perception via panorama-aware geometry models built by ETH Zurich's Physical Reasoning Systems group. Enables single-image panoramic geometry estimation without camera calibration, supporting both still and video panoramic inputs.

## Capabilities

- Unified 360 scene perception via panorama-aware geometry models
- Single-image panoramic geometry estimation without camera calibration
- Robust depth, surface normal, and camera pose estimation for spherical panoramas
- Panoramic video understanding and panorama-to-video synthesis

## VFX / Filmmaking Use Cases

- Generate 360 scene geometry from single reference photos for virtual production
- Rapid panoramic environment mapping for CG scene matching
- Extract geometry from 360 captures for real-time scene replacement
- Create seamless panoramic assets for volumetric content pipelines

## Cross-Domain Connections

**→ [[VirtualProduction]]:** PaGeR's capacity to extract full 3D geometry from a single reference image could eliminate days of photogrammetry work in virtual production pre-vis.

**→ [[3DGS|360GaussianSplatting]]:** Complements sparse-view GS approaches — while [[StereoGS]] handles sparse viewpoints for static scenes, PaGeR specializes in the panoramic domain for real-world geometry extraction.

**→ [[DaVinci-Resolve-Workflows]]:** The 360 environment assets generated could feed directly into Resolve's HDR/fusion workspace for volumetric scene replacement in post.

**→ Cinematic VR content pipelines:** For Aiah Syn or immersive music content where the audience experiences spatial video, PaGeR provides the geometry foundation before any rendering step.

## How to Run

Implementation details on [GitHub](https://github.com/prs-eth/PaGeR).

---
*Ingested from [[Notion-dtb_Knowledge|Notion dtb Knowledge]] source, batch 01.*
