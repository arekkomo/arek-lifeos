---
title: "NaviCache — Test-Time Self-Calibration Caching for Video Diffusion"
category: source
summary: Plug-and-play acceleration method that models video diffusion feature evolution as an inertial navigation system, enabling error-bounded computation skipping without offline calibration data. Tested on HunyuanVideo, Wan, Open-Sora series.
tags: [video-diffusion, acceleration-feature-caching, computational-efficiency, hunyuanvideo, wan, open-sora]
sources: 1
source_path: https://arxiv.org/abs/2606.26795
source_date: 2026-06-25
authors: [anonymous arXiv submission]
ingested: 2026-06-27
updated: 2026-06-27
---

# NaviCache: Test-Time Self-Calibration Caching for Video Generation

## Core Idea

Video diffusion models (VDMs) require immense compute per frame. Existing acceleration methods fall into two camps with different failure modes:

**Offline calibration-based methods:** Require separate calibration datasets, have long setup duration, and break under distribution shifts across prompts.

**Offline calibration-free methods:** Use instantaneous zero-order approximations where the input-to-output mapping varies in real-time, making them noise-sensitive and momentum-blind.

NaviCache proposes a path that avoids both by modeling feature evolution as an [[Inertial Navigation System]] (INS) problem — tracking dynamic state rather than assuming stationarity.

## Architecture

The system treats the mapping between input changes and output changes during diffusion steps as a dynamic coupling, estimated test-time via two states:

1. **Feature change ratio** — how much encoder/decoder features shift per step
2. **Latent drift** — accumulated deviation from the ideal trajectory

These are tracked adaptively using:

### Initial Alignment Phase
- Specialized warmup that establishes baseline covariance estimates
- Eliminates the need for offline calibration data

### Dual-State Estimation
- Predicts feature evolution using physics-inspired INS formulation
- Bridges domain gap between stationary and non-stationary diffusion dynamics

### Measurement Update Mechanism
- Integrates time-dependent noise schedule with uncertainty-aware updates
- Provides theoretical error bounds on which steps can be safely skipped
- High confidence = skip computation; high uncertainty = run full inference

## Results

Evaluated across three model families:

- **HunyuanVideo** — more accurate error judgment than prior caching methods
- **Wan series** — outstanding comprehensive performance metrics
- **Open-Sora** — robust acceleration with bounded quality degradation

The key advantage over prior feature caching is error-bounded guarantees rather than heuristic thresholds.

## Relevance to Workflow

This approach directly applies to ComfyUI video generation pipelines where inference time is the bottleneck. The plug-and-play nature means it can be integrated as a node that wraps existing diffusion blocks without model retraining. For workflows using [[Wan 2.1]] or [[HunyuanVideo]], this cuts inference cost with provable quality bounds.

## Practical Application

In ComfyUI, this would manifest as an optional wrapper node around the sampler that tracks feature momentum internally and dynamically decides per-step whether to cache-reuse or recompute. No additional VRAM for calibration storage, unlike batch-prompt caching methods.

> Note: Works at inference time only — no training overhead. Compatible with any diffusion transformer backbone that exposes intermediate features.
