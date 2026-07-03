---
title: ComfyUI-WhiteRabbit Video Frame Nodes
category: entity
summary: ComfyUI custom node suite for video frame manipulation including batch scaling, framerate resampling, seamless loops and watermark compositing.
tags: [comfyui, video-compositing, post-production, DaVinci-Resolve]
sources: 1
source_path: GitHub Artificial-Sweetener/comfyui-WhiteRabbit
updated: 2026-07-03
---

# ComfyUI-WhiteRabbit

## Overview

Custom node pack for [[ComfyUI]] focused on video frame manipulation. Bridges AI-generated footage and VFX-ready timelines with batch processing and loop generation.

## Capabilities

**Batch Scaling** — Resize clips using Lanczos/EWA resamplers over naive bilinear interpolation. Forces output dimensions for node chaining.

**Framerate Resampling** — Swap 24/30/60 fps via optical flow interpolation. Motion-adaptive blending reduces judder on inconsistent model outputs.

**Seamless Loops** — Crossfade loop stitching for background plates and ambient elements. Saves work in [[DaVinci Resolve]] compositing.

**Batch Watermarking** — Per-frame protection overlays with configurable position, opacity, and blend mode.

## Technical Notes

Python nodes using only the host GPU. Pairs with [[comfyui-ocio-color-management]] for managed EXR workflows. 75 stars on GitHub as of scan date.

## Pipeline Steps

1. Generate footage in ComfyUI
2. WhiteRabbit resamples to target fps
3. Scale frames to delivery resolution
4. Composite via OCIO grading nodes
5. Export plates for [[DaVinci Resolve]]

## Related Work

- [[SAM2Matting]] — Video matting for rotoscoping
- [[LTX-Video-2-3-Prompting-Guide]] — Generation feeds these nodes