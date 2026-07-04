---
title: "AdaCluster — Adaptive Query-Key Clustering for Sparse Attention in Video DiTs"
category: concept
summary: AdaCluster is a training-free adaptive clustering framework that accelerates video diffusion transformer inference by 1.67–4.31× while preserving quality. It clusters query vectors with angle-similarity-preserving compression and key vectors with euclidean-similarity-preserving methods, adapting cluster counts per layer based on token distribution heterogeneity. Tested on CogVideoX-2B, HunyuanVideo, and Wan 2.1 on a single A40 GPU.
tags: [sparse_attention, diffusion_transformer, inference_acceleration, training_free, video_generation]
sources: 1
updated: 2026-07-03
---

## Overview

Video diffusion transformers suffer from quadratic attention complexity.

The cost grows with frame count and spatial resolution together.

Full self-attention scales as O(N²). Minute-long generation costs a lot.

AdaCluster reduces this cost without distillation or retraining.

It clusters Q/K projections at inference time per layer.

## Method

### Angle-Preserving Query Clustering

Query vectors encode what each token searches for. AdaCluster uses angular similarity for clustering instead of euclidean distance. Relative importance survives aggressive compression of redundant heads.

### Euclidean Key Clustering

Key vectors carry position and content features. Position matters, so euclidean distance fits better. A threshold-wiser selection keeps the top-k clusters by query weight. The rest get discarded entirely. Early layers keep more clusters. Late layers use fewer for compression.

### Critical Cluster Selection

Not every cluster contributes equally to attention output. AdaCluster scores each one by total incoming query mass. Below-threshold clusters get pruned per head and per layer. Selective pruning drives the largest speedups without quality loss.

## Results

Tests ran on three models: CogVideoX-2B, HunyuanVideo, Wan 2.1. All on a single A40 GPU.

- Up to 4.31× speedup on Wan 2.1 at high resolutions
- Minimum 1.67× on CogVideoX-2B with negligible PSNR loss
- Drop-in compatible with existing diffusion pipelines

## Practical Implications

It sits alongside [[NaviCache]] and [[SSM-Meets-Video-Diffusion]] for inference optimization.

Unlike [[NaviCache]], it modifies attention within each step rather than skipping steps entirely. AdaCluster reduces per-step cost while NaviCache reduces step count. The two are complementary.

## Contradictions and Caveats

> Note: Speedup was measured on a single A40 GPU. Multi-GPU setups may show different scaling due to kernel overhead.

No contradiction with existing entries. The angle-vs-euclidean split for Q vs K is novel. Prior sparse attention methods use one distance metric for both.

## Related Work

- [[CogVideoX]]: Tested backbone; 2.6B variant used in experiments
- [[Wan 2.1]]: Largest tested model at 14B parameters
- [[ComfyUI]]: Native integration path through attention override hooks
- [[NaviCache]]: Step-skipping acceleration (complementary approach)
- [[SSM-Meets-Video-Diffusion]]: Architectural replacement of attention blocks
- [[ISPA]]: KV cache distillation rather than sparse attention
