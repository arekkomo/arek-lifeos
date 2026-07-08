---
title: "iRDM One-Step Image Generation via Representation Distribution Matching"
category: source
summary: One-step image generation via feature distribution matching under frozen encoders uses MMD as primary comparison across 14 encoder 
representations at batch sizes above 2048. Post-trains FLUX.2 from four-step to one-step, improving GenEval (0.826 vs 0.794) and PickScore while 
eliminating denoising loops that dominate diffusion inference cost. Distribution-matching approach makes local training impractical on consumer 
hardware but demonstrates sampling-reduction as viable strategy beyond caching or quantization.
tags: [one-step-generation, diffusion-acceleration, mmd, distribution-matching, imagenet-synthesis]
sources: 1
updated: "2026-07-04"
source_path: https://arxiv.org/abs/2607.02375
source_date: "2026-07-02"
authors: ["Lan Feng", "Wuyang Li", "Eloi Zablocki", "Matthieu Cord"]
ingested: "2026-07-04"
---

# Representation Distribution Matching for One-Step Generation (iRDM)

**Source:** arXiv 2607.02375v1 (July 2, 2026) | Alan Lab, EPFL/CNRS/HSE

## Problem and Core Idea

Video diffusion inference cost is dominated by denoising loops, where each
timestep recomputes transformer attention across all spatial-temporal tokens.
RDM eliminates the loop entirely: if a single forward pass produces images
whose feature distributions match real image features from multiple encoders,
multi-step sampling becomes unnecessary.

The training objective operates on encoder representations rather than pixel or
latent space reconstruction. A frozen set of pre-trained encoders extracts
features from both generated and reference images; the generator learns to align
its output distribution with real data by minimizing a distance metric between
these feature sets under those encoders. Two design axes structure RDM: which
statistical test compares distributions, and which representations are compared.

## Two Design Axes and Three Findings

- **MMD scales with estimator quality.** Maximum Mean Discrepancy is a two-sample
  test that could not train convincing generators a decade ago due to poor batch
  estimation. Modern implementations with larger batches make MMD strong and
  scalable. The paper adopts it as the primary distribution comparison mechanism
  for feature alignment between generated and real distributions.

- **Batch size above 2048 required for stability.** Generated batch size drives
  estimation accuracy, with optimal behavior above 2048 samples -- far beyond
  customary diffusion training pipelines where GPU memory constrains effective
  batch sizes. Smaller batches fail to represent the learned distribution
  adequately, leading to mode collapse and degenerate outputs.

- **Single-encoder gaming is real but solvable.** Any individual encoder can be
  driven below real distance score while generated images remain visibly fake
  and structurally incoherent. Solution: a battery of 14 encoders with evaluation
  via SW_r14 (Sliced-Wasserstein), independent of training loss and resistant to
  gaming on any single encoder weakness through multi-representation ensemble.

## Performance Results at Scale

- One-step state of the art on ImageNet at SW_r14 score of 1.30, surpassing all prior single-forward-pass generators by a measurable margin 
across human-preference proxy metrics
- PickScore (human-preference proxy NOT optimized during training) prefers iRDM over prior one-step generator on 71.2% of matched samples, 
indicating genuine quality improvement rather than test-set gaming
- Post-trains four-step FLUX.2 into a one-step generator while improving GenEval (0.826 vs original 0.794) and PickScore (22.76 vs 22.58), 
trained in approximately 90 H200 GPU-hours

## Relevance to Video Diffusion Pipelines

Collapsing diffusion from multi-step to one-step eliminates the dominant
inference cost in ComfyUI serving workflows. The batch-size requirement makes
local training on DGX Spark hardware impractical, but post-training a smaller
checkpoint with pre-distilled features could integrate through [[ComfyUI v0.27]]
workflows since the framework now supports efficient memory management for large-
model serving backends with reduced latency overhead per inference request.

[[FLUX.2 Klein Architecture]] describes the diffusion family that serves as iRDM's primary teacher model for one-step post-training. Converting 
FLUX.2 from four-step to one-step while improving GenEval demonstrates distribution matching replaces sampling overhead without quality 
regression, relevant for any pipeline where FLUX.2 serves as backbone in image-to-video compositing or LoRA fine-tuning workflows.

[[NaviCache test-time caching]] accelerates diffusion through state estimation by predicting which denoising steps can be safely skipped via 
dual-state tracking of feature evolution and latent drift. RDM attacks the problem from architecture (no steps needed) while NaviCache operates 
at inference time on production checkpoints, combining both yields compounding reduction in per-image latency beyond either method alone.

[[UltraImageGen]] targets ultra-high-resolution generation with hierarchical local attention replacing quadratic global attention for a 10x 
speedup through resolution scaling rather than timestep reduction. Combined with one-step generation, both methods address different bottleneck 
dimensions and compound multiplicatively: UltraImageGen handles spatial efficiently while iRDM removes temporal denoising overhead entirely from 
the inference graph.

[[Cross-Space Distillation]] transfers knowledge across latent spaces via a bridge interface from high-capacity teachers to compact students. 
Distribution matching and cross-space distillation both operate on internal representations rather than pixels but through different mechanisms: 
MMD alignment versus feature bridging between source and target spaces. [[SpheRoPE]] replaces position embeddings with spherical priors for 
native 360 panorama generation, confirming representation-level modification as a general pattern for training-free capability extension without 
full architecture surgery.

> **Contradiction:** The paper emphasizes MMD's success at large batch sizes while
reporting the practical requirement for >2048 generated samples per optimization step. This tension means smaller batches produce degenerate 
distributions, and training on consumer-grade hardware (e.g., 8x H100 with approximately 320 GB total VRAM) requires aggressive checkpointing or 
gradient accumulation that adds wall-clock overhead proportional to batch scaling factor. The claimed 90 GPU-hours for FLUX.2 post-training 
assumed large-scale infrastructure; smaller clusters would need proportionally more time to accumulate equivalent batch statistics.
