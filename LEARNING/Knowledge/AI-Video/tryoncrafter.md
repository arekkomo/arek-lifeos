---
title: "TryOnCrafter – Camera-Controllable Video Virtual Try-on via 4D Proxy"
category: concept
summary: Unified DiT framework for camera-controllable video virtual try-on using a renderable 4D Gaussian Splatting proxy (2026-06)
tags: [virtual-try-on, video-synthesis, gaussian-splatting, dit, 4d-avatar, smpl-x]
sources: 1
source_path: "https://arxiv.org/abs/2606.26092"
source_date: "2026-06"
authors: [Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan]
ingested: "2026-06-25"
updated: "2026-06-25"
---

# TryOnCrafter – Camera-Controllable Video Virtual Try-on via 4D Proxy

## Overview

First unified [[diffusion transformer]] framework for camera-controllable
video virtual try-on (CaM-VVT). Uses a renderable 4D Gaussian Splatting
proxy to decouple human subject from environment, enabling arbitrary
camera movement and viewpoint control.

Paper: [[arXiv:2606.26092]]

## Problem

Existing video virtual try-on methods depend on source camera trajectories.
Users cannot freely explore viewpoints around the try-on subject. Two gaps:

- Texture hallucination at novel viewpoints (no training data there)
- Structural synchronization between non-rigid human dynamics
  and background under unconstrained camera movement

This paper defines Camera-controllable VVT (CaM-VVT) as a new task.

## Architecture

```
2D try-on priors
    |
    v
[3D Gaussian Splatting clothed avatar]
    |
    + SMPL-X animation sequences
    |
    v
[Background point cloud reconstruction]
    |
    v
Proxy-Anchored Video DiT (45. Diffusion Transformer backbone
conditioned on the 4D proxy as geometric anchor.

### Key Components

- **Renderable 4D Try-on Proxy:** Explicitly decouples human from
  background using [[3D Gaussian Splatting]] for clothed avatar,
  animated via SMPL-X sequences and metric-aligned to background.
- **Proxy-Anchored Video DiT:** Leverages the 4D proxy as primary
  geometric anchor. Synthesized videos constrained by prescribed
  trajectories and physically plausible deformations.

### Pipeline

1. Distill high-fidelity 2D try-on priors into clothed 3DGS avatar
2. Animate via [[SMPL-X]] pose sequences
3. Metric-align avatar to reconstructed background point cloud
4. Feed proxy to Video DiT for photorealistic video synthesis

## Results

The proxy establishes superior texture density and motion integrity
over implicit pixel-space manipulation methods. Enables:

- Human relocalization tasks
- Bullet time effects (frozen subject, moving camera)
- 360-degree orbital viewing around try-on subject

## Practical Relevance

For filmmaking workflows, the 4D proxy approach enables compositing
techniques similar to green-screen but with AI-generated avatars.
[[DaVinci Resolve]] timelines could integrate generated outputs for
virtual production pipelines.

The 3DGS avatar + DiT pipeline could be adapted for [[ComfyUI]] custom
nodes handling character animation or virtual try-on scenes.

## Related Work

- [[4D-GS]] Gaussian-based novel-view synthesis
- Try-on methods in [[AI video generation]] workflows
- Virtual production techniques for film VFX
