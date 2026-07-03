---
title: "ISPA — Instance-Specific Parametric Absorption for AR Video Cache Compression"
category: concept
summary: "Shifts KV cache compression from token dropping to weight-space distillation via closed-form least-squares. Removes up to 50% of KV cache with near-lossless quality in autoregressive video generation, preventing temporal flickering and identity loss while enabling longer sequences without memory explosion."
tags: [video-generation, autoregressive, kv-cache, memory-efficiency, inference-optimization, transformer]
sources: 1
source_path: arXiv (submitted 2026-07-01)
updated: 2026-07-02
---

# ISPA — Instance-Specific Parametric Absorption

## Problem

Autoregressive (AR) streaming video models suffer from linearly growing KV cache. Token dropping causes temporal flickering and identity loss by breaking long-range dependencies.

## Approach

Instead of discarding tokens, ISPA *distills* context into the model's weights:

1. **Layer transition**: Monitor output discrepancy between global (full) attention and local (windowed) attention during a warmup phase
2. **Parametric absorption**: At the transition point, solve a closed-form least-squares problem to compute instance-specific weight modulation that compensates for missing history
3. **Layer conversion**: Transition selected layers from Full-Attention (F-Layers) to memory-efficient Local-Attention (L-Layers)

The key insight is that historical context can be encoded as weight perturbations rather than external tokens.

## Results

- **Up to 50% KV cache removal** with near-lossless visual quality
- Tested across architectures from 1.3B to 14B parameters
- Eliminates temporal flickering that plagueS token-dropping compression methods
- No additional training required — operates at inference time

## Practical Implications

[[ComfyUI]] workflows with video generation nodes benefit directly:
- Longer sequences on constrained VRAM (important for local DGX Spark deployments)
- Compatible with [[Wan-Streamer v0.1]] and other autoregressive video backends
- Alternative to [[NaviCache]] which uses INS-inspired caching — ISPA targets weight-space while NaviCache operates at the feature-evaluation level

## Related Work

- [[SSM-Meets-Video-Diffusion]] also targets memory scaling (linear via Mamba blocks, ISPA targets cache compression)
- [[Infinite-Length Video]] tackles sequence length with causal-bidirectional attention + KV caching — complementary approach to ISPA
