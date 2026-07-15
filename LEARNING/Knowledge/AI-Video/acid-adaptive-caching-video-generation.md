---
title: "ACID — Adaptive Caching for Video Generation"
category: concept
summary: Per-step adaptive threshold replaces fixed caching thresholds, eliminating the speed-quality tradeoff in video diffusion acceleration. Works with TeaCache/EasyCache/DiCache families. Tested on Wan 2.1 and CogVideoX.
tags: ["video-diffusion", "acceleration", "caching", "comfyui", "inference-optimization"]
sources: 1
updated: 2026-07-15
---

# ACID — Adaptive Caching for Video Generation

**arXiv:** 2607.12358 | **Published:** 2026-07-14
**Authors:** Om Agrawal, Saurabh Agarwal, Aditya Akella
**Venue:** cs.CV

## Overview

Video diffusion models are slow at inference because each denoising step requires
a full forward pass through the transformer. Caching-based acceleration methods
like [[NaviCache]], TeaCache, EasyCache, and DiCache address this by reusing
intermediate model outputs when a drift signal stays below a fixed threshold.

ACID shows that holding the skip-threshold constant creates an artificial
speed-quality tradeoff. Some timesteps are "critical" — drift changes rapidly
and skipping them hurts quality disproportionately. Other timesteps are benign
and can be skipped aggressively without visible degradation.

## Method

Per-step adaptive threshold: instead of one global `tau`, ACID computes the
local curvature of the accumulated-drift signal at each denoising step. High-curvature regions get a tighter skip-threshold (fewer skips), low-curvature regions get a looser threshold (more skips). No architecture change, no retraining required.

The key insight is that not all skipped steps are equal: missing a skip
decision at t=300 hurts quality 5x more than missing one at t=800 for the same drift magnitude. The adaptive threshold redistributes computational budget toward steps where caching matters most.

## Results

Tested on Wan 2.1 and CogVideoX. ACID achieves the same visual quality as
fixed-threshold caching at 1.6-2.3x more skips, or equivalently, reaches
the same skip-rate with 15-22% lower FVD degradation vs. TeaCache/EasyCache.

The method is model-agnostic and plugs into any diffusion pipeline that uses
drift-based caching. Both Wan and CogVideoX showed comparable per-step
curvature patterns despite very不同 architectures.

## Practical Relevance for ComfyUI Workflows

Direct relevance: [[comfyui-v027-int8-support-release]] and other recent
ComfyUI releases focus on inference acceleration. ACID is a sampler-level
optimization that could be implemented as a custom node without touching
model weights. Combined with int8 convolution support in ComfyUI v0.27,
adaptive caching could push practical video generation closer to real-time
on consumer-grade GPUs for shorter clip lengths.

Also complements [[delta-forcing-trust-region-steering-ar-video]] which
optimizes a different part of the same problem: AR trajectory quality vs.
computational cost. ACID handles denoising-speed; Delta Forcing handles
temporal-coherence-speed in chunked generation.

## Connections

- [[navicache-test-time-caching-source]] — Earlier caching approach with fixed thresholds
- [[cycle-world-temporal-reversibility-long-video]] — Long-horizon quality preservation
- [[infinite-length-video-causal-attention]] — Extended sequence optimization