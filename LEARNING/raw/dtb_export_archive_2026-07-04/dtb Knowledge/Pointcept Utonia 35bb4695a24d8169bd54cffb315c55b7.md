# Pointcept/Utonia

Tags: AI 3D Model, Github
Description: Universal cross-domain pre-trained encoder for 3D point clouds (Point Transformer V3) covering indoor, outdoor LiDAR, and object-scale data from a single checkpoint.
URL: https://github.com/Pointcept/Utonia
Date Added: May 9, 2026 4:37 PM
Type: Github
Archive: No
Spark: No

## About

Utonia is a cross-domain pre-trained Point Transformer V3 encoder that works across indoor scenes, outdoor LiDAR, and object-scale point clouds from one checkpoint. Provides semantic features, segmentation, and PCA visualizations without domain-specific pre-training.

**GitHub:** [https://github.com/Pointcept/Utonia](https://github.com/Pointcept/Utonia)

**Paper:** [https://arxiv.org/abs/2603.03283](https://arxiv.org/abs/2603.03283)

**Models:** [https://huggingface.co/Pointcept/Utonia](https://huggingface.co/Pointcept/Utonia)

**Project:** [https://pointcept.github.io/Utonia/](https://pointcept.github.io/Utonia/)

## Capabilities

- Single encoder for indoor, outdoor LiDAR, and object-scale 3D data
- PCA visualization, semantic segmentation, similarity heatmaps
- Video lifting via VGGT integration (video → 3D → semantic)
- Standalone inference or package-mode integration into custom codebases
- Hierarchical feature extraction mappable back to original point cloud scale

## VFX / Filmmaking Use Cases

- Semantic segmentation of photogrammetry or scan data for automated object classification
- LIDAR → semantic labels for layout and depth passes
- Video-to-3D-to-semantic pipeline for environment reconstruction
- Asset similarity search across 3D capture data

## Requirements

- CUDA 12.4, PyTorch 2.5.0 via conda, FlashAttention required
- open3d, gradio, scipy, trimesh for demo visualization

## How to Run

```
conda env create -f environment.yml && conda activate utonia
export PYTHONPATH=./ && python demo/0_pca_indoor.py
```

## Notes

Encoder-only (no decoder). Features extracted hierarchically and mapped back via pooling inverse. Scale parameter controls granularity. Modified from Meta Sonata and Pointcept Concerto.