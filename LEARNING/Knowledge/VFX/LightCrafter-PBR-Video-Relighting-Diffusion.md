---
title: "LightCrafter — PBR-Conditioned Video Relighting via Diffusion"
category: concept
summary: Replaces direct video-to-video relighting with PBR-proxy translation pipeline, combining physically-based rendering with diffusion post-training for temporal consistency.
tags: [relighting, PBR, inverse-rendering, diffusion-refinement, CogVideoX, compositing]
sources: 1
updated: 2026-07-10
---

# LightCrafter — PBR-Conditioned Video Relighting

## Overview

Video relighting requires long-form temporal consistency and physically grounded understanding of light transport. Current methods either reconstruct intrinsic scene properties via inverse rendering (noisy, fails on global illumination) or treat it as generative video-to-video translation (limited control, unstable over long sequences).

LightCrafter (arXiv 2026-07) reformulates relighting as translation of a PBR proxy rather than the source video directly. This hybrid approach bakes illumination targets into the PBR render before diffusion sees them.

## Two Paradigms It Bridges

**Inverse Rendering + Forward Rendering**
Reconstruct materials, geometry, and illumination from video. Then forward-render under new lighting. Physically accurate but reconstruction noise compounds across frames. Fails on effects like indirect bounces (global illumination).

**Generative Video-to-Video Translation**
Condition diffusion model on target environment maps or text. Limited control over specific lighting variables. Diffusion models struggle with temporal stability on long-form translation tasks.

LightCrafter replaces direct video translation with proxy-mediated translation: PBR render of the input under target illumination becomes the source for the diffusion post-training model instead of the raw video.

## Pipeline

1. Inverse rendering estimates geometry, materials, and lighting from the source video
2. Forward-render under target illumination → produces a PBR proxy video
3. Post-trained CogVideoX translates PBR proxy → final photorealistic target

The key insight: PBR alone already outperforms some prior art but lacks global illumination effects. A diffusion model trained on synthetic pairs (PBR render → relit photo) captures precisely those missing non-photorealistic effects rather than learning an entire physical simulation.

## Results

Outperforms SOTA on real-world relighting benchmarks. Synthetic benchmark contributions enable controlled analysis of global illumination vs. directional components. Code, dataset, and metrics released.

## Practical ComfyUI Relevance

Direct relevance to VFX compositing pipelines where lighting matches between AI-generated plates and live-action footage is a bottleneck. LightCrafter offers physically grounded control over temporal-consistent relighting — useful for integrating [[LTX-2.3]] or [[Wan2]] generated backgrounds with on-set talent under matching illumination conditions.

> ⚠️ Limitation: Requires inverse rendering quality sufficient to produce clean PBR intermediates. Complex scenes (transparent materials, reflections) degrade the proxy and downstream translation quality. Post-training on CogVideoX means it is backend-specific rather than architecture-agnostic.

## Related

- [[SAM2Matting]] (extracts alpha mattes for compositing; relighting complements keying)
- [[Wan2]] (tested as diffusion backbone in some experiments)
- [[ComfyUI-OCIO-Nuke-Style-Color-Management]] (color pipeline integration point)
