---
title: "Flex4DHuman — Multi-View Video Diffusion for 4D Human Reconstruction"
category: concept
summary: Flex4DHuman converts monocular or sparse multi-view video of a moving subject into synchronized dense multi-view videos using only relative camera-pose conditioning, with no explicit geometry priors. Built on Wan 2.1 1.3B text-to-video backbone, it encodes view information through five-axis positional encoding that extends spatio-temporal RoPE with SE(3) camera geometry. The generated video feeds directly to 4D Gaussian Splatting pipelines for dynamic scene reconstruction.
tags: [four_d_reconstruction, gaussian_splatting, multi_view, video_diffusion, camera_pose, wan]
sources: 1
updated: 2026-07-03
---

## Overview

Human-centric 4D reconstruction typically needs a skeleton or depth map. Flex4DHuman removes all explicit geometry requirements. It conditions only on relative camera poses encoded as embeddings.

The output feeds directly to [[Gaussian Splatting]] reconstruction.

## Architecture

### Five-Axis Positional Encoding

Video DiTs use spatio-temporal RoPE for position encoding. Flex4DHuman extends this to five axes total. Width, height, and frame index join continuous SE(3) camera parameters. The view embedding starts zero-initialized during early training.

### Three-Stage Curriculum Training

1. **Pose Following**: Generates target-view frames from a reference and a pose delta.
2. **Flexible Reference**: Any sparse input becomes valid as source.
3. **Temporal Rollout**: Cleans historical tokens for geometry-consistent motion across frames.

### Camera-Aware Conditioning

Relative pose is computed at training time via standard multiview geometry. At inference, any camera trajectory works with SE(3) poses. This gives full control over virtual camera positions.

## Results

Evaluated on DNA-Rendering and ActorsHQ datasets. It beats methods that use explicit skeleton or depth cues despite having fewer requirements. The method generalizes to animal categories after mixed training.

## Practical Implications

It bridges casual monocular capture to dynamic 3D assets for gaming or compositing in DaVinci Resolve. Capture video, generate multi-view expansion, feed into [[Gaussian Splatting]].

Compared to [[OrbitForge]], the focus differs. OrbitForge targets static scenes from single-video input via SDS optimization. Flex4DHuman produces animation-ready assets for moving subjects.

## Contradictions and Caveats

> Note: Input video should be clean with minimal occlusion. Heavy motion blur degrades multi-view coherence in the downstream reconstruction stage.

No contradiction with vault entries. The camera-pose-only approach fills a gap between heavy methods like [[Align4D]] and pure text-conditioned generators.

## Related Work

- [[Gaussian Splatting]]: Downstream reconstruction target
- [[OrbitForge]]: Text-to-3D via video prior (different scope)
- [[Wan 2.1]]: Backbone diffusion model (1.3B variant)
- [[RayPE]]: Extends positional encoding with ray-space geometry
- [[PhysiFormer]]: 4D motion prediction via diffusion, different conditioning
- [[Ink3D]]: Video-to-texture synthesis, shares video-prior philosophy
