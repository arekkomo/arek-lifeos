---
title: "HyperVAttention — Efficient Sparse Attention for Video Diffusion"
category: concept
summary: Training-time sparse attention with spatio-temporal token clustering achieves 2-3x speedup in video diffusion models without quality loss by addressing CTA irregular block utilization
tags: [video-diffusion, inference-optimization, sparse-attention, performance, vdiT]
sources: 1
updated: 2026-07-07
source_path: arxiv.org/abs/2607.03012
source_date: "2026-07"
authors: [Dongyeun Lee, Amir Zandieh, Vahab Mirrokni, Junmo Kim]
ingested: 2026-07-07
---

## What It Does

Video Diffusion Transformers (VDiTs) suffer from quadratic attention complexity across all frames. HyperVAttention targets the two bottlenecks of prior clustering methods: clustering overhead and poor GPU utilization from irregular block shapes. Result: **2.1-3.4× speedup** on [[CogVideoX]] 5B and [[HunyuanVideo]].

## How It Works

1. **Spatio-Temporal Clustering** — Tokens grouped by spatial proximity AND temporal coherence simultaneously (not sequential or separate). Adjacent frames sharing similar content cluster together into rectangular blocks
2. **Regular Block Shapes** — Instead of arbitrary cluster sizes, clusters are constrained to 2^K × 2^L dimensions that match GPU CTA (Cooperative Thread Array) warp boundaries. Eliminates padding waste and warp divergence
3. **Training-Time Integration** — Unlike inference-only sparse attention (e.g., [[AdaCluster]]), HyperVAttention is trained end-to-end so the model adapts to cluster boundaries rather than being retrofitted

## Key Technical Details

- Power-of-two block constraints: 16×16, 32×32, 64×32 etc. for optimal tensor core alignment
- Cluster assignment layer is lightweight: 79 parameters per attention head learned via soft-differentiable routing
- Memory reduction: 40% lower peak VRAM on HunyuanVideo compared to full attention

## Relevance Pipeline: Where It Fits

- **ComfyUI**: Requires a HyperVAttention-aware model checkpoint. Drop-in replacement for models trained with this attention mechanism. Not compatible with base checkpoints without fine-tuning
- **DGX Spark / Cloud Inference**: Significant throughput improvement for batch video generation or long sequences
- **Inference Optimization**: Addresses the same problem as [[NaviCache]] and [[AdaCluster]] but through a different (training-aware) approach

> **Adjacent to**: [[AdaCluster]], [[NaviCache]], [[CogVideoX]], [[HunyuanVideo]], [[ISPA]]

## Limitations

- Requires retraining; cannot retroactively apply to existing checkpoints
- Cluster topology learned during training may not generalize to drastically different video lengths or resolutions
- Speedup is at training time; inference benefit depends on whether clustering overhead is cached per checkpoint
