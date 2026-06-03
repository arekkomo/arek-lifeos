---
title: Utonia
category: entity
summary: Universal cross-domain pre-trained encoder for 3D point clouds, built on Point Transformer V3, covering indoor, outdoor, and object-scale data.
tags: [ai-3d, point-cloud, 3d-understanding, pre-training, github]
sources: 1
updated: 2026-05-09
---

# Utonia

**By:** Pointcept (Xiaoyang Wu et al.)
**Released:** 2026-02
**GitHub:** https://github.com/Pointcept/Utonia
**Paper:** https://arxiv.org/abs/2603.03283
**Models:** https://huggingface.co/Pointcept/Utonia
**Demo:** https://pointcept.github.io/Utonia/

---

## What It Is

Utonia is a cross-domain pre-trained Point Transformer V3 (PTv3) encoder that works across indoor, outdoor LiDAR, and object-scale point clouds — all from a single checkpoint. It extends Sonata and Concerto, providing semantic features, segmentation, and PCA visualizations from arbitrary 3D point cloud data without task-specific pre-training.

---

## Capabilities

- Single encoder for indoor scenes, outdoor LiDAR, and object-scale 3D data
- Pre-trained on diverse cross-domain 3D datasets
- Outputs hierarchical point features mappable back to original scale
- Visualization demos: PCA, semantic segmentation, similarity heatmaps
- Video lifting support via VGGT integration (3D from video)
- Standalone inference or package mode integration into custom codebases

---

## VFX / Filmmaking Use Cases

- **Scene understanding from scans**: Feed a 3D scan or photogrammetry point cloud through Utonia to get semantic segmentation for automated object classification
- **LiDAR-to-semantic**: Convert LIDAR data from on-set scanning into semantically labelled point clouds for layout and depth passes
- **Video-to-3D-to-semantic**: Use VGGT to lift a video to 3D, then run Utonia for scene understanding — useful for environment reconstruction
- **Asset similarity search**: Use the similarity heatmap feature to find matching surface regions across 3D assets
- **Automated scene labelling**: Leverage the pre-trained semantic understanding to auto-label 3D capture data without per-scene fine-tuning

---

## Requirements

- CUDA 12.4, PyTorch 2.5.0 (conda environment via `environment.yml`)
- FlashAttention required
- `open3d`, `gradio`, `scipy`, `trimesh` for demo visualization
- Optional: VGGT for video-to-3D lifting

---

## Quick Start

```bash
conda env create -f environment.yml --verbose
conda activate utonia
export PYTHONPATH=./
python demo/0_pca_indoor.py
```

---

## Notes

Encoder-only architecture (no decoder). Features are extracted hierarchically and can be mapped back to original point cloud scale using the pooling inverse mechanism. Scale parameter in the transform pipeline controls granularity — higher scale = more fine-grained. Modified from Sonata (Meta) and Concerto (Pointcept).
