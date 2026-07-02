---
title: "TrajLoc — Trajectory-Attention Localization for Multi-Object Motion Control"
category: concept
summary: Per-object spatial constraints via attention-layer Gaussian heatmaps for multi-object I2V motion control, tested on CogVideoX 5B and Wan 2.1 14B with up to 20 simultaneous objects.
tags: ["video-generation", "image-to-video", "motion-control", "attention-modification", "vfx-compositing"]
sources: 1
updated: "2026-07-02"
---

# TrajLoc

> arXiv **2607.00861** — Published July 1, 2026

## Overview

Controlling multiple objects in image-to-video generation requires maintaining separate identities while enforcing distinct trajectories. Existing methods entangle all trajectories within a shared dense conditioning signal, causing identity confusion as objects intersect or occlude each other.

TrajLoc departs from that paradigm by enforcing strict per-object spatial constraints directly inside the attention layers of diffusion transformers.

## Method

- Replaces cross-attention weights for each object token with a Gaussian heatmap centered on its target location at every frame
- Per-object tokens carry trajectory and depth information through learned embeddings
- First-frame appearance replaces abstract object tokens to preserve identity across frames
- Applied as a drop-in module to architecturally distinct backbones: CogVideoX 5B and Wan 2.1 14B

## Results

Evaluated across six datasets, including scenes with up to 20 simultaneously controlled objects:

- +4.3 dB PSNR average gain over strongest baselines
- 51% reduction in trajectory endpoint error
- Maintains control quality in out-of-distribution real-world scenes with intersections and occlusions

## Practical Implications

TrajLoc's per-object attention isolation maps directly to VFX compositing workflows where multiple elements need independent motion paths. In ComfyUI workflows, this approach could enable node-level trajectory assignment rather than whole-scene prompting, giving editorial control at the layer level already used in node-based compositing tools.

The method works on both CogVideoX and Wan backbones, both of which have active ComfyUI implementations. Integration would require modifying cross-attention layers during inference rather than retraining.

## Related Work

- [[RayPE — Ray-Space Positional Encoding]] also modifies attention for camera control, but operates at the positional embedding level rather than per-token spatial constraints
- [[SAM2Matting]] handles temporal consistency via tracking; TrajLoc handles precise trajectory enforcement
- [[FreeStory]] maintains character consistency through feature reuse; TrajLoc enforces spatial constraints directly in attention weights
- [[Goku — Million-Scale Video Editing]] provides structural control but at the scene-graph level rather than per-frame attention

## Links

- arXiv: <https://arxiv.org/abs/2607.00861>
- Project page: <https://sela-omer.github.io/traj-loc/>
