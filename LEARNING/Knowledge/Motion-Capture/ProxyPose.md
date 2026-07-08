---
title: ProxyPose: 6-DoF Pose Tracking via Video-to-Video Translation
category: concept
summary: Tracks six-degree-of-freedom pose of objects from monocular video alone, using the video diffusion model as a spatial consistency constraint through v2v translation
tags: [pose-tracking, motion-capture, VFX, video-to-video, 6DoF]
sources: 1
updated: 2026-07-08
---

# ProxyPose (2607.06555)

**Authors:** Ruihang Zhang, Felix Taubner, Pooja Ravi, Kiriakos N Kutulakos, David B Lindell
**Published:** 2026-07-07 
**Categories:** cs.CV
**Source:** arXiv: [2607.06555](https://arxiv.org/abs/2607.06555)

## Overview

Monocular 6-DoF pose tracking typically requires supplementary inputs beyond video: 3D object models, depth maps, segmentation masks, or task-specific learned features. ProxyPose eliminates those requirements by treating v2v translation as a spatial consistency constraint that implicitly solves for camera pose over time.

## Key Approach

Instead of explicit optimization of camera parameters, the method leverages a diffusion model's understanding of 3D structure:

- Renders a synthetic target view from an estimated pose
- The video diffusion model measures how consistent the rendered view is with the actual observed video through translation loss
- Gradient signal backpropagates through the diffusion prior to refine pose estimates iteratively
- No 3D mesh, no depth estimator -- raw RGB video and a candidate object proxy are the only inputs

## Practical Relevance

- **VFX compositing:** Automatic camera tracking from plate footage without LiDAR or stereo rig. Works where conventional SfM fails (featureless surfaces, repetitive textures).
- **Motion capture pipeline drop-in:** Replaces marker-based or IMU-free pose estimation with a purely monocular solution that still estimates full 6-DoF trajectories.
- **ComfyUI integration path:** V2V node can be wired as a tracking preprocessor before compositing stages in [[LTX Video]] or [[Flux]] workflows.

## Technical Details

- Uses video diffusion models ( CogVideoX, HunyuanVideo tested) for their implicit 3D prior
- Iterative refinement: pose estimate → synthetic render → v2v consistency check → gradient update
- Tested on monocular video sequences with no supplementary data requirements

## Limitations

- Iterative gradient-based approach means per-frame optimization rather than real-time inference
- Quality depends on how well the diffusion model's internal 3D prior matches the real-world object geometry
- Currently requires a candidate object proxy (simple geometric approximation or rough mesh) for initialization

## Related Work

- Fills a gap between pure visual object tracking and marker-based motion capture systems like Move AI
- Compared to [[CineMaster]] which requires explicit bbox + camera trajectory control as input. ProxyPose's v2v consistency loop also complements [[PointDiT]] by using video diffusion rather than single-image depth for full pose estimation
- Complements motion-capture tooling like Move AI by providing an all-vision alternative for environments where physical sensors are impractical
