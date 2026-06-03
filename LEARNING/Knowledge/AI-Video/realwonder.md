---
title: RealWonder
category: entity
summary: Real-time physical action-conditioned video generation from a single image, using physics simulation as an intermediate bridge.
tags: [ai-video, physics-simulation, image-to-video, real-time, diffusion-models, github]
sources: 1
updated: 2026-05-09
---

# RealWonder

**By:** Stanford University, University of Southern California (Wei Liu, Ziyu Chen, Zizhang Li, Yue Wang, Hong-Xing Yu, Jiajun Wu)
**Released:** 2026-03
**GitHub:** https://github.com/liuwei283/RealWonder
**Paper:** https://arxiv.org/abs/2603.05449
**Demo:** https://liuwei283.github.io/RealWonder/

---

## What It Is

RealWonder is the first real-time system for action-conditioned video generation from a single image. Instead of encoding continuous actions directly, it routes them through physics simulation, converting forces and robotic manipulations into optical flow and RGB representations that video models can process. A distilled video generator (4 diffusion steps) produces 13.2 FPS at 480×832 resolution.

---

## Capabilities

- Real-time interactive video generation from a single image at 13.2 FPS (480×832)
- Action conditioning via physics simulation: forces, robot actions, camera controls
- Supports rigid objects, deformable bodies, fluids, and granular materials
- 3D reconstruction from single images + physics sim + distilled video generator pipeline
- Interactive web UI for real-time exploration

---

## VFX / Filmmaking Use Cases

- **Physics-accurate previsualization**: Input a photo of a scene, apply forces, and preview how objects would behave — before building a single set or asset
- **Interactive shot prototyping**: Explore camera control and object interaction in real-time from a single reference image
- **Fluid and destruction simulation preview**: Test how fluids, cloth, and granular materials respond to actions without running full VFX sims
- **On-set look-development**: Feed a still from set and interactively explore how elements would move under different force conditions
- **Concept validation**: Quickly test if a physically-driven shot is achievable before committing to full simulation

---

## Requirements

- CUDA 12.1, NVIDIA H200 GPU tested (for real-time performance)
- Python via conda (`default.yml`)
- Multiple submodule installs: SAM 3D Objects, SAM 2, Genesis physics engine
- Model checkpoints: `Realwonder-Distilled-AR-I2V-Flow`, `Wan2.1-Fun-V1.1-1.3B-InP`

---

## Quick Start

```bash
conda env create -f default.yml
conda activate realwonder
# Install submodules (SAM 3D, SAM 2, Genesis)
# Download checkpoints
cd demo_web
python app.py --demo_data demo_data/lamp --checkpoint_path /path/to/checkpoint.pt
```

---

## Notes

Three-stage architecture: 3D reconstruction → physics simulation → distilled video generator. The physics sim converts actions to visual representations (optical flow + RGB) that existing video models understand — a clever bridge that avoids retraining video models on physics data. 4 diffusion steps only. Built on top of Wan2.1-Fun-V1.1-1.3B-InP.
