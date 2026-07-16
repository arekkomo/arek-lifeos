---
title: henry123-boy/SpaTracker: [CVPR 2024 Highlight] Official PyTorch implementation of SpatialTracker: Tracking Any 2D Pixels in 3D Space
category: note
summary: Preserved substantive Notion export for henry123-boy/SpaTracker: [CVPR 2024 Highlight] Official PyTorch implementation of SpatialTracker: Tracking Any 2D Pixels in 3D Space.
tags: [notion-import, source-preservation]
sources: 1
updated: 2026-07-16
source_path: raw/notion-dump-ingest-archive/2026-07-16/Batch-04/henry123-boy SpaTracker [CVPR 2024 Highlight] Offi f6f09df40e764bbca6f635cef79754b4.md
ingested: 2026-07-16
---

# henry123-boy/SpaTracker: [CVPR 2024 Highlight] Official PyTorch implementation of SpatialTracker: Tracking Any 2D Pixels in 3D Space

**Ingest batch:** [[Notion-Dump-Ingest-Batch-04]]  
**Original export:** `raw/notion-dump-ingest-archive/2026-07-16/Batch-04/henry123-boy SpaTracker [CVPR 2024 Highlight] Offi f6f09df40e764bbca6f635cef79754b4.md`

---

# henry123-boy/SpaTracker: [CVPR 2024 Highlight] Official PyTorch implementation of SpatialTracker: Tracking Any 2D Pixels in 3D Space

Tags: AI Video
Description: [CVPR 2024 Highlight] Official PyTorch implementation of SpatialTracker: Tracking Any 2D Pixels in 3D Space - henry123-boy/SpaTracker
URL: https://github.com/henry123-boy/SpaTracker
Date Added: January 11, 2025 10:28 AM
Type: Github
Archive: No
Spark: No

![](henry123-boy%20SpaTracker%20%5BCVPR%202024%20Highlight%5D%20Offi/stn-RXAc1iN0XlyNYS4OSDpt0QSNjWt7NIpGykwLt2Rz.jpeg)

[](https://camo.githubusercontent.com/bbadae02346be284215d393a0faaf8137375c6e9f6661ae538263b417a8ac07b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f61725869762d537061547261636b65722d726564)

# SpatialTracker: Tracking Any 2D Pixels in 3D Space

![](https://github.com/henry123-boy/SpaTracker/raw/main/assets/dance-twirl.gif)

[**SpatialTracker: Tracking Any 2D Pixels in 3D Space**](https://henry123-boy.github.io/SpaTracker/),
Yuxi Xiao*, Qianqian Wang*, Shangzhan Zhang, Nan Xue, Sida Peng, Yujun Shen, Xiaowei Zhou,
CVPR 2024, Highlight *Paper at [arxiv](https://arxiv.org/abs/2404.04319)*

## News and ToDo

- Release SpatialTracker-v2 (coming).
- Release SpatialTracker inference code and checkpoints.
- `05.04.2024`: SpatialTracker is selected as Highlight Paper!
- `26.02.2024`: SpatialTracker is accepted at CVPR 2024!

## Requirements

The inference code was tested on

- Ubuntu 20.04
- Python 3.10
- [PyTorch](https://pytorch.org/) 2.1.1
- 1 NVIDIA GPU (RTX A6000) with CUDA version 11.8. (Other GPUs are also suitable, and 22GB GPU memory is sufficient for dense tracking (~10k points) with our code.)

### Setup an environment

conda create -n SpaTrack python==3.10
conda activate SpaTrack

### Install PyTorch

pip install torch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 --index-url https://download.pytorch.org/whl/cu118

### Other Dependencies

pip install -r requirements.txt

Note: Please follow the version of the dependencies in `requirements.txt` to avoid potential conflicts.

## Depth Estimator

In our default setting, monocular depth estimator is needed to acquire the metric depths from video input. There are several models for options ([ZoeDepth](https://github.com/isl-org/ZoeDepth), [Metric3D](https://github.com/YvanYin/Metric3D), [UniDepth](https://github.com/lpiccinelli-eth/UniDepth) and [DepthAnything](https://github.com/LiheYoung/Depth-Anything)). We take ZoeDepth as default model. **Download** `dpt_beit_large_384.pt`, `ZoeD_M12_K.pt`, `ZoeD_M12_NK.pt` into `models/monoD/zoeDepth/ckpts`.

## Data

Our method supports **`RGB`** or **`RGBD`** videos input. We provide the `checkpoints` and `example_data` at the [Goolge Drive](https://drive.google.com/drive/folders/1UtzUJLPhJdUg2XvemXXz1oe6KUQKVjsZ?usp=sharing). Please download the `spaT_final.pth` and put it into `./checkpoints/`.

### RGB Videos

For `example_data`, we provide the `butterfly.mp4` and `butterfly_mask.png` as an example. Download the `butterfly.mp4` and `butterfly_mask.png` into `./assets/`. And run the following command:

python demo.py --model spatracker --downsample 1 --vid_name butterfly --len_track 1 --fps_vis 15  --fps 1 --grid_size 40 --gpu ${GPU_id}

### RGBD Videos

we provide the `sintel_bandage.mp4`, `sintel_bandage.png` and `sintel_bandage/` in `example_data`. `sintel_bandage/` includes the depth map of the `sintel_bandage.mp4`. Download the `sintel_bandage.mp4`, `sintel_bandage.png` and `sintel_bandage/` into `./assets/`. And run the following command:

python demo.py --model spatracker --downsample 1 --vid_name sintel_bandage --len_track 1 --fps_vis 15  --fps 1 --grid_size 60 --gpu ${GPU_id} --point_size 1 --rgbd # --vis_support (optional to visualize all the points)

## Visualization 3D Trajectories

Firstly, please make sure that you have installed [blender](https://www.blender.org/). We provide the visualization code for blender:

/Applications/Blender.app/Contents/MacOS/Blender -P create.py -- --input ./vis_results/sintel_bandage_3d.npy

For example, the `sintel_bandage` looked like 

![](https://github.com/henry123-boy/SpaTracker/raw/main/assets/sintel.gif)

## Citation

If you find our work useful in your research, please consider citing:

@inproceedings{SpatialTracker,
title={SpatialTracker: Tracking Any 2D Pixels in 3D Space},
author={Xiao, Yuxi and Wang, Qianqian and Zhang, Shangzhan and Xue, Nan and Peng, Sida and Shen, Yujun and Zhou, Xiaowei},
booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
year={2024}
}

## Acknowledgement

Spatialtracker is built on top of [Cotracker](https://github.com/henry123-boy/SpaTracker/blob/main/co-tracker.github.io) codebase. We appreciate the authors for their greate work and follow the License of Cotracker.
