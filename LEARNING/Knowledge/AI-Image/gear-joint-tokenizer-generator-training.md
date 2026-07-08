---
title: "GEAR — Guided End-to-End AutoRegression for Image Synthesis"
category: concept
summary: Joint tokenizer-generator training eliminates decoupling gap in autoregressive image models
tags: [autoregressive, image-synthesis, tokenizer, joint-training, diffusion-alternative]
sources: 1
source_path: arXiv 2606.32039
source_date: 2026-06
ingested: 2026-07-01
updated: 2026-07-01
---

## Core Problem

Current autoregressive image models train tokenizers separately from generators. The tokenizer optimizes for reconstruction fidelity while the generator sees only discrete indices. This decoupling means the tokenizer cannot learn which patterns are easy or hard for the generator to model, leading to inefficient information compression and degraded generation quality.

## Key Insight

Joint end-to-end training aligns the tokenizer's compression strategy with the generator's modeling capacity. The tokenizer learns to produce representations that maximally benefit the autoregressive predictor, rather than minimizing pure reconstruction loss. This closes the gap between representation learning and generation objectives.

## Technical Details

- Replaces the separate VAE/tokenizer pretraining stage
- Joint optimization via gradient flow through both tokenizer and generator
- Tested on discrete tokenization (ViT/VQVAE-style) and continuous latent spaces
- Compatible with existing autoregressive architectures like [[DiT]] backbones

## Practical Implications

For [[ComfyUI]] workflows, GEAR-trained models should produce sharper outputs at equivalent FLOP budgets since the tokenizer-generator pipeline is end-to-end optimized. The architecture applies to image synthesis pipelines that currently rely on pretrained VAEs like SDXL's VAE or Flux.1's latent encoder. No workflow changes needed beyond swapping in a jointly trained model checkpoint.

## Related Work

- [[Cross-Space Distillation via Bridge]] also bridges tokenizer-generator gaps but through distillation rather than joint training
- [[FLUX.2 Klein Architecture]] uses a separate VAE pipeline that would benefit from GEAR-style alignment
