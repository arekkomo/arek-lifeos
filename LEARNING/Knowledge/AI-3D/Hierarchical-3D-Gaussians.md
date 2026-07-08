---
title: Hierarchical 3D Gaussians (HUGS)
category: concept
summary: Meuleman et al / SIGGRAPH 2024 — divide-and-conquer approach to training very large scenes as independent chunks consolidated into a hierarchy; enables real-time rendering of km-scale captures with efficient LOD and sparse-coverage regularization
tags: [3dgs, gaussian-splatting, large-scenes, novel-view-synthesis, hierarchical, chunk-training]
sources: 2
updated: 2026-07-04
---

# Hierarchical 3D Gaussians (HUGS)

**SIGGRAPH 2024** extension of 3D Gaussian Splatting. Solves the critical limitation that 3DGS cannot scale to very large scenes because individual Gaussian clouds grow enormous and exhaust memory/bandwidth.

## Core idea
A hierarchy of coarse-to-fine Gaussians enables multi-resolution scene representation that adapts rendering detail based on camera position and available resources.

## Technical contributions
1. **Divide-and-conquer training:** Very large scenes split into independent chunks, each trained separately, then consolidated into a hierarchy
2. **Efficient LOD (Level-of-Detail):** Distant content rendered from coarser levels with smooth transitions between LODs
3. **Sparse-coverage regularization:** Training and optimization adapted for sparse camera coverage — common when capturing km-scale scenes with simple affordable rigs
4. **Chunk merge optimization:** Gaussians merged into intermediate nodes are further optimized to recover visual quality lost during consolidation

## Scale achieved
- Tens of thousands of input images
- Several kilometer trajectory coverage
- Up to one-hour capture durations
- Real-time rendering on consumer hardware

## Relationship to 3DGS and StereoGS
StereoGS (previous KB entry) improves _per-scene_ accuracy via stereo depth priors for sparse views. HUGS improves _scene size scalability_ via hierarchical representation — these are complementary approaches that could be combined for both large-scale and sparse-view reconstruction at production quality.

Also related to Mega-NeRF, Mip-NeRF 360 (neural radiance field precursors) and standard Instant Gaussian Splatting (Kerbl et al. 2023 — the original 3DGS paper).

## Reference
[Paper](https://repo-sam.inria.fr/fungraph/hierarchical-3d-gaussians/) · [Code](https://github.com/graphdeco-inria/hierarchical-3d-gaussians) · [Datasets](https://repo-sam.inria.fr/fungraph/hierarchical-3d-gaussians/datasets/)