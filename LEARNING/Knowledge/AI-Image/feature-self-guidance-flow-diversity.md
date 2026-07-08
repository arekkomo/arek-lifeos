---
title: Feature Self-Guidance — Mitigating Diversity Collapse in Pretrained Flow Models
category: concept
summary: Training-free plug-and-play method that mitigates diversity collapse in flow-model generation by dispersing internal features during batch inference and projecting them back onto the data manifold via regularization. Works across T2I, depth-to-image, and reference-guided generation.
tags: [flow-matching, diversity-collapse, training-free, inference-time, text-to-image, generative-ai, self-guidance]
sources: 1
source_path: arxiv/2606.27371
source_date: "2026-06"
authors: [Pradhaan S Bhat, Rishubh Parihar, Abhijnya Bhat, R. Venkatesh Babu]
ingested: "2026-06-25"
updated: "2026-06-25"
---

# Feature Self-Guidance for Flow Model Diversity

**arXiv:** 2606.27371 | **Published:** June 25, 2026
**Authors:** Pradhaan S Bhat et al.

## Problem statement

State-of-the-art flow models produce high-fidelity images under the same conditioning prompt but suffer from *diversity collapse* — multiple samples look nearly identical despite random seeds. This limits creative control in workflows where variation matters (e.g., generating multiple concept variations of the same scene).

Existing solutions:
- **Latent guidance** — Limited effectiveness; often produces blurry or distorted outputs
- **Sample selection** — Requires external reward models, adding inference-time overhead

## Core method

A training-free self-guidance mechanism that operates entirely at inference time with minimal overhead. Two stages per batch:

### Stage 1: Feature dispersion

During batch generation, internal features of the flow model are actively *dispersed* (pushed apart) across samples in the same batch. This prevents all trajectories from converging to the same mode in latent space.

### Stage 2: Manifold regularization

To keep dispersed features close to valid image regions, a *manifold regularization* step projects the perturbed features back onto the data manifold. This ensures diversity without sacrificing alignment with input conditions (text prompts, depth maps, reference images).

## Key properties

- **Training-free** — No fine-tuning; works as a drop-in module on pretrained models
- **Minimal overhead** — Marginal cost in inference latency
- **Plug-and-play** — Integrates into existing pipelines without architecture changes
- **Cross-task compatibility** — Validated on text-to-image (multi-step and few-step), depth-to-image, and reference image generation

## Results

Significant improvement in diversity metrics across several conditional flow models while preserving fidelity scores. Works with both multi-step (high quality) and few-step (fast inference) sampling regimes.

## Practical implications for ComfyUI workflows

For [[comfyui]] users generating multiple iterations of the same prompt, this method provides a pathway to genuine variation without:
- Prompt engineering hacks
- External CLIP-based reward scoring
- Training new LoRA adapters

Since it is training-free and plug-and-play, a ComfyUI custom node implementation would require only modifying the internal feature tensor during the denoising loop.

## Relation to existing knowledge

> ⚠️ Contradiction: [[danceopd-flow-distillation]] describes diversity/composition issues at *training* time (capability interference). This paper addresses diversity at *inference* time (mode collapse). Both point to mode-seeking behavior in flow models but operate at different stages of the pipeline.

Compatible with [[flux-2-klein-architecture]] since the Klein family uses flow-matching under the hood. The self-guidance module would apply directly to FLUX.2 checkpoints.

## Code availability

Paper states code will be released. Check arXiv 2606.27371 for updates.

## Related pages

- [[danceopd-flow-distillation]]
- [[flux-2-klein-architecture]]
- [[comfyui]]
- [[ai-image-generation]]
- [[stable-layers]]
