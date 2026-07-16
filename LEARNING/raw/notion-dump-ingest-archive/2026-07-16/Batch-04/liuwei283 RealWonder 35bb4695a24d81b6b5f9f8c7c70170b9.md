# liuwei283/RealWonder

Tags: AI Video, Github
Description: Real-time physical action-conditioned video generation from a single image using physics simulation — 13.2 FPS at 480×832.
URL: https://github.com/liuwei283/RealWonder
Date Added: May 9, 2026 4:37 PM
Type: Github
Archive: No
Spark: No

## About

RealWonder is the first real-time system for action-conditioned video generation from a single image. It bridges physics simulation and video generation by converting forces and actions into optical flow + RGB representations that video models understand. Runs at 13.2 FPS at 480×832 with only 4 diffusion steps.

**GitHub:** [https://github.com/liuwei283/RealWonder](https://github.com/liuwei283/RealWonder)

**Paper:** [https://arxiv.org/abs/2603.05449](https://arxiv.org/abs/2603.05449)

**Project Page:** [https://liuwei283.github.io/RealWonder/](https://liuwei283.github.io/RealWonder/)

## Capabilities

- Real-time video generation from a single image at 13.2 FPS
- Action conditioning: forces, robot manipulation, camera controls
- Supports rigid objects, deformable bodies, fluids, granular materials
- 3D reconstruction + physics sim + distilled video generator (4 diffusion steps)
- Interactive web UI

## VFX / Filmmaking Use Cases

- Physics-accurate previsualization from a single photo before building sets or assets
- Interactive shot prototyping with real-time force/camera exploration
- Fluid and destruction simulation preview without full VFX pipeline
- On-set look-development: feed a still and interactively explore how elements would move

## Requirements

- CUDA 12.1, NVIDIA H200 for real-time performance
- Submodules: SAM 3D Objects, SAM 2, Genesis physics engine
- Models: Realwonder-Distilled-AR-I2V-Flow, Wan2.1-Fun-V1.1-1.3B-InP

## How to Run

```
conda env create -f default.yml && conda activate realwonder
cd demo_web && python app.py --demo_data demo_data/lamp
```

## Notes

Three-stage pipeline: 3D reconstruction → physics sim → distilled video generator. Physics sim converts actions to visual representations video models already understand — no retraining. Built on Wan2.1-Fun-V1.1-1.3B-InP. Stanford + USC.