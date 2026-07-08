---
title: Meta 3D AssetGen (PBR Text-to-Mesh)
category: entity
summary: Meta/NeurIPS 2024 framework producing high-fidelity textured meshes with full PBR materials from text or image input — uses dual-stage text-to-image → mesh reconstruction pipeline with deferred shading loss for PBR supervision, SDF-based shape representation, and UV-space texture refiner
tags: [ai-3d, pbr, text-to-3d, diffusion-model, nvidia, meta-research]
sources: 1
updated: 2026-07-04
---

# Meta 3D AssetGen (PBR Text-to-Mesh)

**Meta/NeurIPS 2024** — text/image-to-mesh generation producing meshes with physically-based rendering materials, relightability, and high-resolution UV-space texture detail.

## Architecture
- **Stage 1 (Text → Image):** predicts a 6-channel image for 4 object views — shaded colors + albedo channels separated
- **Stage 2a (Image → 3D):** MetaILRM 3D reconstructor outputs triplanar-supported SDF field → textured mesh with PBR materials
- **Stage 2b (Texture refinement):** UV-space transformer recovers missing sharpness and detail from input views

## Key results
- **+17% Chamfer Distance** over best concurrent work
- **+40% LPIPS** improvement on few-view reconstruction
- **72% human preference** over best industry competitors of comparable speed (including PBR-supporting tools)
- Generates geometry + albedo/metalness/roughness for realistic environment relighting

## Technical novelties
- Deferred shading loss for efficient PBR supervision
- SDF shape representation with direct shape loss
- Fused kernels for high memory efficiency
- UV-space texture transformer as post-hoc refiner

## Compared to (from source)
- Gaussian Reconstruction Model, InstantMesh, MeshLRM (concurrent methods)
- Instant3D (pioneering text-to-mesh)
- LightplaneLRM (splatting enhancements)
- Luma AI Genie + Meshy 3 (commercial text-to-3D tools)

## Reference
[Paper](https://assetgen.github.io/static/AssetGen.pdf) · [Code](https://github.com/MetaGLM/AssetGen) · [Video](https://www.youtube.com/watch?v=xY_2jAEcBa0)