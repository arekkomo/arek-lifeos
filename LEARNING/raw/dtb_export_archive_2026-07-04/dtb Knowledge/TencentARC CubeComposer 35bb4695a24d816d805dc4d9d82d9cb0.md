# TencentARC/CubeComposer

Tags: AI Video, Github
Description: Converts perspective videos to native 4K 360° equirectangular video using spatio-temporal cubemap-face autoregressive generation — no memory blow-up, no upscaling. CVPR 2026.
URL: https://github.com/TencentARC/CubeComposer
Date Added: May 9, 2026 4:36 PM
Type: Github
Archive: No
Spark: No

## About

CubeComposer converts a normal perspective video into native 4K 360° equirectangular video. It autoregressively generates one cubemap face over a fixed temporal window at a time, enabling native 2K/3K/4K output without upscaling or memory blow-up. Built on Wan2.2.

**GitHub:** [https://github.com/TencentARC/CubeComposer](https://github.com/TencentARC/CubeComposer)

**Paper:** [https://arxiv.org/abs/2603.04291](https://arxiv.org/abs/2603.04291)

**Models:** [https://huggingface.co/TencentARC/CubeComposer](https://huggingface.co/TencentARC/CubeComposer)

**Project:** [https://lg-li.github.io/project/cubecomposer/](https://lg-li.github.io/project/cubecomposer/)

## Capabilities

- Perspective video → native 4K 360° equirectangular video
- Spatio-temporal autoregressive cubemap face generation
- Native 2K, 3K, and 4K output modes
- No memory blow-up from full-panorama generation
- Custom camera trajectory control (rotation, FOV, waypoints)
- Based on Wan2.2 (diffsynth backend)

## VFX / Filmmaking Use Cases

- 360° pre-visualization from standard flat footage for VR or LED wall review
- Environment map generation from perspective clips for CG lighting
- Virtual production 360° background plates for LED volumes
- Repurpose B-roll as 360° content without reshooting
- Scene extension to full spherical environment for reflections and environment passes

## Models

| Variant | Cubemap Size | Temporal Window | Output |
| --- | --- | --- | --- |
| cubecomposer-3k | 768px | 9 frames | 2K / 3K |
| cubecomposer-4k | 960px | 5 frames | 4K |

## Requirements

- Python 3.10, CUDA 12.4 (Linux), ffmpeg in PATH
- Wan2.2 base model (auto-downloads via diffsynth cache)
- CubeComposer checkpoint from HuggingFace

## How to Run

```
conda create -n cubecomposer python=3.10 && conda activate cubecomposer
pip install -r requirements.txt
bash run.sh
```

## Notes

Embeds modified diffsynth and equilib — no separate install needed. Trajectory files control camera path. CVPR 2026.