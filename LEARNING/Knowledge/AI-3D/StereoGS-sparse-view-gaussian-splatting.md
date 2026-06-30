---
title: "StereoGS — Sparse-View 3D Gaussian Splatting via Stereo Priors"
category: source
summary: Sparse-view 3DGS framework using stereo depth regularization with virtual stereo pairs and a foundation stereo model for absolute scale. Includes gradient-aware opacity decay and consistency-aware initialization. State-of-the-art on LLFF, DTU, Mip-NeRF360.
tags: [3dgs, gaussian-splatting, sparse-view, stereo-priors, novel-view-synthesis, depth-regularization]
sources: 1
source_path: "arXiv 2606.30545"
source_date: "2026-06"
authors: ["Wenhao Yuan", "Yiyuan Ge", "Deli Cai"]
ingested: "2026-06-30"
updated: "2026-06-30"
---

# StereoGS: Sparse-View 3D Gaussian Splatting via Stereo Priors

## Overview

[StereoGS](https://stringerywh00.github.io/StereoGS_project_page/) addresses overfitting in [[3D Gaussian Splatting]] under sparse-view conditions. Existing monocular depth priors suffer from scale ambiguity and cross-view inconsistency. StereoGS replaces monocular constraints with binocular stereo regularizations for reliable geometry.

## Three Core Contributions

### 1. Stereo Depth Regularization

Constructs virtual stereo pairs during optimization. Uses a foundation stereo model (e.g., MiDaStereo, ZOE) to predict disparity maps from these pairs. Enforces absolute scale and binocular-consistent structure in the 3D Gaussian primitive placement. Unlike monocular depth which only provides relative ordering, stereo priors give metric-scale geometry constraints.

### 2. Gradient-Aware Opacity Decay

Dynamic pruning criterion that penalizes Gaussians based on opacity gradient magnitude distribution:

- High-gradient Gaussians (sharp opacity transitions) are structural and preserved
- Low-gradient Gaussians (flat opacity regions) represent redundant primitives and decay faster
- Adaptive threshold updates each optimization iteration

Reduces overfitting while preserving fine geometric detail.

### 3. Consistency-Aware Dense Initialization

Zero-shot multi-view depth estimation initializes Gaussian positions on consistent scene surfaces rather than random sparse points. Multi-view depth maps are fused via voting to anchor primitives before optimization begins. This reduces early-stage instability that causes ghosting in sparse settings.

## Evaluation Results

Tested across four sparse-view benchmarks:

| Dataset | Method | PSNR | SSIM | LPIPS |
|---------|--------|------|------|-------|
| LLFF (3 views) | StereoGS | **state-of-the-art** | **SOTA** | **lowest** |
| DTU (4 views) | StereoGS | **SOTA** | **SOTA** | **lowest** |
| Mip-NeRF360 (8 views) | StereoGS | **SOTA** | — | — |
| Blender (5 views) | StereoGS | **improvement over baseline 3DGS** | — | — |

Zero additional inference overhead at test time. All regularization is training-only.

## Relevance to Current Workflows

Builds directly on [[3D Gaussian Splatting]] foundations. Related to [[OrbitForge]]'s reconstruction-anchored approach for text-to-3D via video — both address sparse-view geometry anchoring. The stereo prior technique could transfer to [[ComfyUI]] 3DGS pipelines where limited input views are the norm for real-world captures.

## Key Differences from Monocular Approaches

Monocular depth priors (e.g., MiDaS, DepthAnything) only provide relative ordering — scale is ambiguous up to a global factor. StereoGS virtual pairs provide binocular parallax, resolving absolute geometry. This distinction matters most when fewer than 8 views are available, which is the typical sparse-view scenario in practical capture setups.

---

*Source: https://arxiv.org/abs/2606.30545 | Project: https://stringerywh00.github.io/StereoGS_project_page/*
