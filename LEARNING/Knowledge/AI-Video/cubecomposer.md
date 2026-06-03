---
title: CubeComposer
category: entity
summary: Converts perspective videos to native 4K 360° videos using spatio-temporal cubemap-face autoregressive generation — no memory blow-up, no upscaling.
tags: [ai-video, 360-video, panoramic, video-generation, diffusion-models, github]
sources: 1
updated: 2026-05-09
---

# CubeComposer

**By:** TencentARC (Lingen Li, Guangzhi Wang, Xiaoyu Li, Zhaoyang Zhang, Qi Dou, Jinwei Gu, Tianfan Xue, Ying Shan)
**Released:** CVPR 2026
**GitHub:** https://github.com/TencentARC/CubeComposer
**Paper:** https://arxiv.org/abs/2603.04291
**Models:** https://huggingface.co/TencentARC/CubeComposer
**Demo:** https://lg-li.github.io/project/cubecomposer/

---

## What It Is

CubeComposer takes a perspective (normal) video and generates a native 4K 360° video in equirectangular format. Instead of generating the full panorama at once (which blows up memory), it autoregressively generates one cubemap face over a fixed temporal window at a time. This enables native 2K/3K/4K output without the resolution degradation of low-res-then-upscale approaches. Built on Wan2.2 base model.

---

## Capabilities

- Perspective video → native 4K 360° equirectangular video
- Spatio-temporal autoregressive cubemap face generation (one face per time window)
- Native 2K, 3K, and 4K output modes
- No memory blow-up from full-panorama generation
- Custom camera trajectory control (rotation, FOV, waypoints)
- Outputs: equirectangular video, cubemap faces, generation info JSON
- Based on Wan2.2 (diffsynth backend)

---

## VFX / Filmmaking Use Cases

- **360° pre-visualization from standard footage**: Turn any flat reference video into a 360° environment for VR review or virtual production LED walls
- **Environment map generation for lighting**: Generate 360° HDRi-style video environments from a perspective reference clip for use in CG lighting
- **Virtual production background plates**: Create immersive 360° plate content from standard camera footage for LED volume backgrounds
- **360° content from existing B-roll**: Repurpose existing flat footage into 360° deliverables without reshooting
- **Scene extension for compositing**: Expand a perspective shot into a full spherical environment for reflections and environment passes
- **Post-production world-building**: Generate surrounding 360° context from a hero perspective shot for VR storytelling

---

## Requirements

- Python 3.10, CUDA 12.4 (Linux)
- `ffmpeg` in PATH (for video saving)
- Wan2.2 base model weights (auto-downloads via diffsynth cache)
- CubeComposer checkpoint: `cubecomposer-3k` (2K/3K) or `cubecomposer-4k` (4K)
- ODVista360 dataset for testing; 4K360Vid dataset on HuggingFace

---

## Quick Start

```bash
conda create -n cubecomposer python=3.10
conda activate cubecomposer
pip install -r requirements.txt
# Edit run.sh: set BASE_MODEL_PATH, ODV_ROOT_DIR, TEST_OUTPUT_DIR, TEST_MODE
bash run.sh
```

---

## Notes

Two model variants: `cubecomposer-3k` (cubemap 768px, 9-frame temporal window) and `cubecomposer-4k` (cubemap 960px, 5-frame window). Embeds modified versions of `diffsynth` and `equilib` — no separate install needed. Trajectory files control camera path; includes rotation trajectory JSON with 2-waypoint example. 4K360Vid dataset provides face-wise captions and YouTube video IDs (no raw files).
