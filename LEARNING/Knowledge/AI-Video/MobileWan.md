---
title: MobileWan — 5B Video Diffusion Transformer on Mobile Hardware
category: concept
summary: Recurrence distillation and structured compression make Wan2.2-5B deployable on commercial mobile GPUs at 16 FPS with SOTA VBench scores
tags: ["mobile-deployment", "recurrence-distillation", "video-diffusion", "attention-pruning", "Wan2.2", "qualcomm"]
sources: 1
updated: 2026-07-08
---

## Overview

MobileWan (arXiv 2607.06173) demonstrates that server-scale video diffusion
models can run efficiently on memory-constrained mobile hardware through
algorithmic reformulation rather than model shrinking. Starting from the
5B-parameter Wan2.2, it achieves 16 FPS generation on commercial mobile
GPUs while maintaining state-of-the-art quality metrics.

Published: 2026-07-07 by Mohsen Ghafoorian et al. (Qualcomm AI Research, cs.CV)

Key insight: the bottleneck is not model size but attention memory; reformulating
attention operations enables large models to fit within mobile VRAM budgets.

## Core Techniques

### Recurrence Distillation

The central innovation converts [[Wan 2.1]]-style parallel video diffusion
into a chunk-wise autoregressive process with constant-memory attention. The
model operates as an RNN at inference time — each temporal chunk is processed
with causal linear attention that only retains compressed state from prior
chunks, not the full KV cache.

This eliminates the O(seq_len) memory growth of standard DiT video diffusion,
making 5B-parameter models viable on devices with <8 GB VRAM.

### Causal Linear Attention

Standard multi-head attention grows quadratically with sequence length.
MobileWan replaces temporal attention layers with causal linear attention
approximations that maintain O(1) memory per chunk while preserving
cross-chunk temporal coherence through the recurrent state buffer.

### Learnable Attention Head Pruning

A novel binary gating mechanism prunes unnecessary attention heads end-to-end:

- Per-head binary gates (keep/drop) are learned during distillation
- Noise-biased sparsity objective ensures only genuinely redundant heads
  are pruned, not heads that matter under distribution shift
- Distillation-based fine-tuning transfers quality from the unpruned teacher
  to the pruned student

This achieves effective model compression without quantization artifacts,
since the pruning is learned rather than heuristic.

### Sampling-Step and VAE Decoding Optimization

Additional optimizations for mobile inference:

- Step distillation reduces denoising steps while maintaining output quality
- Memory-optimized VAE decoding batches tiles to fit GPU memory constraints
- Combined latency of 20 seconds end-to-end for 5s/480x832 video at 16 FPS

## Performance Metrics

| Metric | Score |
|--------|-------|
| VBench overall | 83.79 (new SOTA for mobile) |
| End-to-end latency (5s video on mobile) | 20 seconds |
| Output resolution | 480x832 at 16 FPS |
| Model parameters | 5B (full Wan2.2-5B, not distilled size) |

## Practical Relevance

For field production and edge workflows:

- On-set preview generation without cloud dependency — generate reference
  video shots directly on mobile workstation hardware
- Complementary to [[ComfyUI]] deployment on DGX Spark for studio-scale
  pipelines; MobileWan covers the mobile/edge use case with the same
  Wan model family backbone
- The recurrence distillation framework is applicable to other large
  diffusion models beyond video — any DiT with long temporal dimensions

The head-pruning approach (learnable binary gates optimized via distillation)
could be adapted for pruning over-provisioned custom nodes in [[ComfyUI]]
workflows running on mid-range GPUs.

## Related Work

- [[Wan 2.1]] — the base model family; MobileWan uses Wan2.2-5B as its teacher
- [[ISPA]] — instance-specific parametric absorption for KV cache reduction;
  different approach (weight distillation vs. recurrent reformulation)
- [[NaviCache]] — adaptive computation skipping via inertial state estimation;
  complementary latency optimization strategy
