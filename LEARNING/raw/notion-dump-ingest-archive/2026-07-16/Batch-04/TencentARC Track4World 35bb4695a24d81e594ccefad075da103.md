# TencentARC/Track4World

Tags: AI 3D Model, AI Tracking, Github, VFX
Description: Feedforward dense 3D tracking of every pixel in a monocular video, in world-centric coordinates with scene flow estimation.
URL: https://github.com/TencentARC/Track4World
Date Added: May 9, 2026 4:26 PM
Type: Github
Archive: No
Spark: No

## About

Feedforward dense 3D tracking of every pixel in a monocular video, outputting world-centric 3D scene flow, camera poses, and 4D trajectories. Separates camera movement from object motion without any special rig or markers.

- **GitHub:** [https://github.com/TencentARC/Track4World](https://github.com/TencentARC/Track4World)
- **Paper:** [https://arxiv.org/abs/2603.02573](https://arxiv.org/abs/2603.02573)
- **Project:** [https://jiah-cloud.github.io/Track4World.github.io/](https://jiah-cloud.github.io/Track4World.github.io/)
- **Models:** [https://huggingface.co/TencentARC/Track4World](https://huggingface.co/TencentARC/Track4World)
- **By:** HKUST + ARC Lab, Tencent PCG (2026)

## Capabilities

- Dense 3D tracking of every pixel across all frames (not just sparse points)
- World-centric coordinate output — separates camera pose from object motion
- Three modes: 2D tracking, first-frame 3D, and every-pixel-every-frame 3D
- Metric-scale output (meters) with DepthAnythingV3 backbone
- Automatic foreground/background separation via Grounded-SAM-2 + DINO
- Multiple backbones: DepthAnythingV3, MoGe, Pi3
- Outputs: 3D point clouds, scene flow, camera poses, dense trajectories (PLY)

## VFX / Filmmaking Use Cases

- **Object extraction without greenscreen** — world-centric tracking + SAM2 segmentation isolates moving subjects from handheld shots
- **Camera solve from monocular footage** — recover camera poses for matchmove without tracking markers or SynthEyes
- **Dense point cloud generation** — turn any video into a dense 4D scene reconstruction for compositing reference
- **Rotoscoping assist** — foreground/background masks as a byproduct of the tracking pipeline
- **Depth/parallax effects** — feed 3D tracks into depth warp for 2D-to-3D workflows

## Requirements

- Python 3.11, CUDA 12.1, PyTorch 2.5.1
- Dependencies: Grounded-SAM-2, Grounding DINO, MoGe, Pi3, DepthAnythingV3
- 3 model weight variants (DA3, Pi3, MoGe) + SAM2 large

## How to Run

```bash
git clone --recursive https://github.com/TencentARC/Track4World.git
conda create -n track4world python=3.11 && conda activate track4world
pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt

# Dense world-centric tracking
python demo.py \
    --mp4_path demo_data/cat.mp4 \
    --coordinate world_depthanythingv3 \
    --mode 3d_efep \
    --ckpt_init checkpoints/track4world_da3.pth \
    --save_base_dir results/cat
```

## Notes

- Feedforward = single pass, no iterative optimization — fast inference
- Pi3 and MoGe backbones are relative scale only; DA3 gives metric scale
- Built on MoGe, AllTracker, Pi3, and Depth Anything 3
- Tencent license — check before commercial use
- One of the first feedforward world-centric dense pixel trackers (2026)