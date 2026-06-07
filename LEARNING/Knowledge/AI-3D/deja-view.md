---
title: Deja View
category: entity
summary: Efficient 3D reconstruction from multiple images using Gaussian splats — 117M-parameter looping transformer from NVIDIA Research.
tags: [ai-3d, 3d-reconstruction, gaussian-splats, nvidia-research, multi-view]
sources: 1
updated: 2026-06-07
---

# Déjà View

**By:** Alessandro Burzio, Tobias Fischer, Sven Elflein, Qunjie Zhou, Riccardo de Lutio, Jiawei Ren, Jiahui Huang, Shengyu Huang, Marc Pollefeys, Laura Leal-Taixé, Zan Gojcic, Haithem Turki (NVIDIA Research, University of Modena, Univ of Toronto, ETH Zürich)
**Released:** 2026
**GitHub:** https://github.com/nv-tlabs/dvlt
**Paper:** https://arxiv.org/abs/2605.30215
**Project Page:** https://research.nvidia.com/labs/dvl/projects/dvlt/

---

## What It Is

Efficient 3D reconstruction model that creates Gaussian splats from multiple images. Uses a 117M-parameter looping transformer that matches or beats >1B-parameter feed-forward baselines. Exposes inference compute as a slider for trading off speed vs quality.

---

## Key Architecture

- **117M-parameter looping transformer**: Much more parameter-efficient than feed-forward baselines
- **Multiple-view input**: Processes image sets for coherent 3D reconstruction
- **Gaussian splat output**: Standard 3D representation compatible with most rendering pipelines
- **Compute slider**: Adjust inference compute for different latency/quality requirements
- **Multi-source**: NVIDIA Research + University partnerships

---

## Capabilities

- Multi-image input → 3D Gaussian splat output
- Parameter-efficient (117M params vs >1B for comparable models)
- Tunable inference compute for speed/quality trade-offs
- Compatible with standard Gaussian splat rendering

---

## VFX / Filmmaking Applications

- **Rapid environment capture**: Convert photo sets into 3D environments for virtual production
- **Photo-to-scene pipeline**: Use archival photos/scans as 3D scene assets
- **VR/AR content creation**: Efficiently produce 3D assets from multi-view photography
- **Location scouting replacement**: Build digital twins of real locations from photos

---

## Requirements

- Standard transformer compute (model is ~117M params, lighter than most competitors)
- Multi-view image input set

---
