---
title: SpheRoPE - Zero-Shot 360 Panorama Gen with Spherical RoPE
category: concept
summary: Training-free framework that injects spherical priors into diffusion transformers via modified rotary position embeddings for native 360 panorama and video generation.
tags: [panorama, 360, spherope, position-encoding, flux, ltx-video, zero-shot]
sources: 1
updated: 2026-07-01
source_path: arxiv/2606.32033
source_date: 2026-06
authors: [Or Hirschorn, Aaron Olender, Eli Alshan, Ianir Ideses]
ingested: 2026-07-01
---

# SpheRoPE - Spherical RoPE for Panorama Generation

Training-free approach for 360 panoramic image and video generation.
Injects spherical priors into pre-trained diffusion transformers.

## The Problem

Existing panorama methods either fine-tune on scarce 360 data
or use multi-step optimization with high latency.
Pre-trained models have some panoramic priors but fail
to satisfy equirectangular projection (ERP) constraints.

## How Spherical RoPE Works

Replaces standard rotary position embeddings (RoPE):

- Low-frequency channels as 3D Cartesian coordinates
  for spherical manifold encoding
- High-frequency channels harmonically quantized
  for exact periodicity at map boundaries
- Semantic Distortion CFG steers geometry at inference

## Key Properties

- Zero-shot: no training or fine-tuning required
- Optimization-free: works at inference time only
- Drop-in replacement for RoPE in diffusion backbones

> Demonstrated on [[Flux]] 1, Flux 2, and [[LTX-Video]].
Compatible with [[ComfyUI]] custom node workflows.
Relates to [[RayPE - Ray-Space Positional Encoding]]
for geometry-aware position encoding in vision models.
Also connects to [[NaviCache - Test-Time Caching]] principles.

> Contradiction check: SpheRoPE uses spherical RoPE for panorama.
Distinct from [[RayPE - Ray-Space Positional Encoding]] ray encoding.
No contradiction with existing knowledge.
