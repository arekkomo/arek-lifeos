---
title: "UniCaMo — Unified Camera and Object Motion Control via 3D-Grounded Noise"
category: concept
summary: Constructs input noise from synchronized spatial trajectories to unify camera + object motion control in video diffusion models
tags: [video-generation, motion-control, camera-motion, diffusion-prior, controllable-video]
sources: 1
updated: 2026-07-07
source_path: arxiv.org/abs/2607.02798
source_date: "2026-07"
authors: [Long Vu, Tan Ngo, Animesh Karnewar, Amir Habibian]
ingested: 2026-07-07
---

## What It Does

Most controllable video pipelines treat camera control and object motion as separate branches (e.g., [[TrajLoc]] for objects, [[Trajectory Control]] for cameras). UniCaMo unifies both under a single noise-construction mechanism.

Instead of conditioning on trajectories via cross-attention or adapter layers, the method **replaces the Gaussian noise tensor** with a structured noise field derived from synchronized 3D spatial trajectories.

## How It Works

1. **Shared Motion Graph** — Object trajectories and camera viewpoints are encoded into a common 3D coordinate system
2. **Noise Construction** — The diffusion prior is built by warping random noise through the motion graph, so denoising starts from a trajectory-aligned latent instead of pure white noise
3. **No Adapter Training** — Works as a training-free inference modification against any pretrained T2V model (Wan 2.1, CogVideoX, HunyuanVideo)

## Key Technical Details

- Noise tensor is warped through inverse depth-projected homography + optical flow composite fields
- Camera trajectory encoded via SE(3) pose sequence; object motion via per-frame bounding box tracking
- Two trajectories can interact (object moving while camera pans) without conflict because both map to the same noise volume before denoising begins

## Relevance Pipeline: Where It Fits

- **ComfyUI**: Drop-in as a custom node that preprocesses the initial noise tensor before the KSampler
- **VFX Compositing**: Precise object placement + camera move in one pass, reducing multi-layer compositing rounds
- **Film Previs**: Simultaneous character blocking and camera choreography from storyboard prompts

## Comparison to Existing Work

| Method | Camera Control | Object Motion | Training Required | Approach |
|--------|---------------|---------------|-------------------|----------|
| **UniCaMo** | ✓ unified | ✓ unified | No | Noise construction |
| TrajLoc | Limited | ✓ per-object | No | Cross-attention Gaussian heatmaps |
| GimbalDiffusion | ✓ gravity-aware | ✗ | Yes | Absolute world coordinates |
| QWERTY | Limited | ✓ query-warped | No | Q embedding warp in full attention |

> **Adjacent to**: [[WorldDirector]], [[FlowMo]]

## Limitations

- Noise construction step adds ~15% inference overhead before denoising
- Tested on up to 4 objects + 1 camera; multi-object scalability not benchmarked beyond that
- Requires trajectory input (bbox sequence / pose file); does not infer motion from text alone
