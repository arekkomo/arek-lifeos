---
title: Track4World
category: entity
summary: Feedforward dense 3D tracking of every pixel in a monocular video, in world-centric coordinates with scene flow estimation.
tags: [ai-3d, ai-tracking, vfx, scene-flow, point-cloud, github]
sources: 1
updated: 2026-05-09
---

# Track4World

**By:** Jiahao Lu, Jiayi Xu, Wenbo Hu, Ruijie Zhu, Chengfeng Zhao, Sai-Kit Yeung, Ying Shan, Yuan Liu — HKUST + ARC Lab, Tencent PCG
**Released:** 2026
**GitHub:** https://github.com/TencentARC/Track4World
**Paper:** https://arxiv.org/abs/2603.02573
**Project:** https://jiah-cloud.github.io/Track4World.github.io/
**Models:** https://huggingface.co/TencentARC/Track4World

---

## What It Is

Track4World estimates dense 3D scene flow for every pixel between arbitrary frame pairs in a monocular video, operating in a global feedforward (single-pass) manner. Unlike most trackers that work in camera-centric space, it reconstructs motion in a world-centric coordinate system — meaning it separates camera movement from object movement. It supports 2D tracking, camera-centric 3D tracking, and full world-centric 3D tracking with foreground/background separation using DINO + SAM2 segmentation.

---

## Capabilities

- Dense 3D tracking of **every pixel** across all frames (not just sparse keypoints)
- World-centric coordinate output — separates camera pose from object motion
- Three tracking modes: `2d`, `3d_ff` (first frame geometry), `3d_efep` (every pixel, every frame)
- Metric-scale output (meter-level) with the DA3 backbone
- Automatic foreground/background separation via Grounded-SAM-2 + DINO
- Multiple backbone options: DepthAnythingV3, MoGe, Pi3
- Outputs: 3D point clouds, scene flow vectors, camera poses, dense trajectories (PLY format)
- Evaluation benchmarks: Sintel, KITTI, Kubric

---

## VFX / Filmmaking Use Cases

- **Object extraction without greenscreen** — use world-centric tracking + foreground segmentation to isolate moving subjects (actors, vehicles) from a handheld shot with no special rig
- **Camera solve from monocular footage** — recover camera poses from any video clip for matchmove, without dedicated tracking markers or a dedicated app like SynthEyes
- **Dense point cloud generation** — turn any video into a dense 4D scene reconstruction for compositing reference or environment rebuild in DaVinci / Resolve Fusion
- **Scene flow for VFX reference** — understand exactly how every pixel is moving in 3D, useful for planning CG integration or verifying depth
- **Rotoscoping assist** — foreground/background separation with SAM2 gives per-frame masks as a byproduct of the tracking pipeline
- **AI animation depth and parallax** — feed output 3D tracks into a parallax/depth warp for 2D-to-3D depth effect workflows

---

## Requirements

- Python 3.11
- CUDA 12.1
- PyTorch 2.5.1
- Dependencies: Grounded-SAM-2, Grounding DINO, MoGe, Pi3, DepthAnythingV3, utils3d
- Model weights: ~3 checkpoints (DA3, Pi3, MoGe variants) + SAM2 large

---

## Quick Start

```bash
git clone --recursive https://github.com/TencentARC/Track4World.git
cd Track4World
conda create -n track4world python=3.11
conda activate track4world
pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt

# Download weights
wget https://huggingface.co/TencentARC/Track4World/resolve/main/track4world_da3.pth -O ./checkpoints/track4world_da3.pth

# Run dense world-centric tracking
python demo.py \
    --mp4_path demo_data/cat.mp4 \
    --coordinate world_depthanythingv3 \
    --mode 3d_efep \
    --Ts -1 \
    --ckpt_init checkpoints/track4world_da3.pth \
    --save_base_dir results/cat
```

---

## Notes

- Feedforward = single pass, no iterative optimization — much faster than NeRF-based or optimization-based scene flow
- The Pi3 and MoGe backbones output in relative scale; only DA3 gives metric (meter) scale
- Built on top of MoGe, AllTracker, Pi3, and Depth Anything 3 — essentially combining state-of-the-art monocular depth with dense optical flow in 3D
- Tencent license — check before commercial use
- Paper from 2026, one of the first feedforward world-centric dense trackers
