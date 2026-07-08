---
title: MrFlow — Multi-Resolution Flow Matching Diffusion Acceleration
category: concept
summary: Training-free multi-resolution acceleration strategy for flow-matching diffusion models achieving 10x end-to-end speedup via low-to-high staged pipeline with GAN-based super-resolution and pixel-space refinement. Tested on FLUX.1-dev and Qwen-Image with <1% OneIG gap.
tags: ["diffusion-acceleration", "flow-matching", "training-free", "multi-resolution", "comfyui", "flux", "super-resolution"]
sources: 1
source_path: arxiv.org/abs/2607.01642
source_date: 2026-07
authors: [Xingyu Zheng, Xianglong Liu, Yifu Ding, Weilun Feng, Junqing Lin, Jinyang Guo, Haotong Qin]
ingested: 2026-07-03
updated: 2026-07-03
---

# MrFlow — Training-Free Multi-Resolution Diffusion Acceleration

Hardware-agnostic diffusion acceleration via staged low-to-high-resolution sampling,
eliminating the blurring and artifacts typical of latent-space upsampling methods.

## Core mechanism

MrFlow builds a four-stage pipeline that exploits quadratic token reduction at
low resolution:

1. Low-res generation — Rapidly synthesize the main structural composition at
   reduced resolution. Quadratic token savings in self-attention means fewer
   compute steps for the coarse pass.

2. Pixel-space super-resolution — A lightweight pretrained GAN-upscaler converts
   the low-res output to high resolution. Operating in pixel space rather than
   latent space avoids artifacts from selective region modification.

3. Low-strength noise injection — Adds controlled stochasticity to enable
   high-frequency resampling without distorting the structural foundation from
   stage 1, bridging pixel-space GAN features back to the diffusion prior.

4. High-res diffusion refinement — Flow-matching steps refine the super-resolved
   image at full resolution, recovering details while preserving overall structure.

## Results and benchmarks

- 10x end-to-end acceleration on [[Flux]] (FLUX.1-dev) and Qwen-Image models
- OneIG (one-sample image generation quality metric) within 1% of baseline,
  meaning perceptual quality is nearly indistinguishable from full-resolution runs
- Composable with timestep distillation strategies for up to 25x total speedup when
  combined orthogonally with pre-trained acceleration methods

## Practical implications for workflows

Directly applicable to [[ComfyUI]] text-to-image generation pipelines. The training-free
nature means no model retraining or checkpoint swapping — just a sampling pipeline
replacement. Particularly valuable for:

- Iterative design workflows where rapid preview at lower fidelity matters more than
  pixel-perfect output per iteration
- Batch image generation tasks (concept art, storyboarding) where throughput beats
  marginal quality gains
- Local inference on limited GPU hardware where full-resolution sampling is prohibitively slow

## Comparison with related approaches

Different from [[NaviCache]] which caches test-time features in temporal diffusion, and
[[DiffRGD]] which manipulates guidance optimization manifolds. MrFlow addresses the
resolution-compute tradeoff head-on via staged scaling rather than step-skipping or cache reuse.

The GAN-based super-resolution step is what differentiates MrFlow from prior multi-res
methods that blur at boundaries because they upsample in latent space instead of pixel space.

## References

- arXiv: 2607.01642v1 (2026-07-02)
- Code: https://github.com/Xingyu-Zheng/MrFlow
