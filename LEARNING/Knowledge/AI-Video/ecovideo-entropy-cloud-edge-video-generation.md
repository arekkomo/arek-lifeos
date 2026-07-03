---
title: "EcoVideo — Entropy-Orchestrated Cloud-Edge Video Generation"
category: concept
summary: "Training-free framework that uses self-attention entropy to estimate frame-wise information density, selecting keyframes for cloud GPU denoising while edge devices reconstruct remaining frames via motion-aware interpolation. Adapts to real-time bandwidth and compute constraints, achieving up to 2.9x end-to-end speedup."
tags: [video-generation, inference-optimization, cloud-edge, entropy, diT, acceleration]
sources: 1
source_path: arXiv (submitted 2026-06-29)
updated: 2026-07-02
---

# EcoVideo — Entropy-Orchestrated Video Generation

## Problem

DiT video generation is latency-intensive due to iterative full-frame denoising. Static cloud-edge methods can't leverage inter-frame similarity or adapt to dynamic resource constraints.

## Approach

Entropy-orchestrated *dynamic* inter-frame decoupling:

1. **Keyframe selection**: Early-stage self-attention entropy estimates frame-wise information density — high entropy = high visual complexity = denoise on cloud GPU
2. **Cloud processing**: Large model denoises only the sparse set of high-entropy keyframes
3. **Edge reconstruction**: Lightweight model reconstructs remaining frames via motion-aware interpolation with stability refinement

The framework adapts keyframe budget and edge refinement depth to real-time bandwidth/compute availability.

## Results

- Training-free (no fine-tuning required)
- Up to **2.9x end-to-end speedup** in low-bandwidth, compute-limited settings
- Tested on representative DiT video generators
- Code available: https://github.com/IF-LAB-PKU/EcoVideo

## Practical Implications

For [[ComfyUI]] deployments with constrained local GPU:
- Offload only high-complexity frames to cloud while generating simpler frames locally
- Reduces bandwidth vs. full-frame-cloud approaches
- Complements [[NaviCache]] (feature-level caching) and [[ISPA]] (KV cache compression) for different optimization layers

## Related Work

- [[SSM-Meets-Video-Diffusion]] — linear scaling via Mamba blocks; EcoVideo tackles efficiency through frame-level decoupling rather than architectural replacement
- [[Helion]] — auto-generated inference kernels; EcoVideo's frame selection could run on top of Helion-optimized backends for compounded speedup
