---
title: "LISA — Likelihood Score Alignment for Visual-Condition Control"
category: source
summary: Regularization method that aligns side-network features with approximate likelihood scores in dual-branch conditional generation, accelerating training convergence and improving disentanglement with zero inference cost. Applies across image/video tasks and diffusion/flow models.
tags: [conditional-generation, score-modeling, regularization, side-branch, training-efficiency]
sources: 1
source_path: https://arxiv.org/abs/2606.27192
source_date: 2026-06-25
authors: [anonymous arXiv submission]
ingested: 2026-06-27
updated: 2026-06-27
---

# LISA: Likelihood Score Alignment for Visual-condition Controllable Generation

## Core Idea

The dual-branch paradigm dominates controllable generation: a frozen pretrained main network + trained side network that injects conditional features. This works well but its training dynamics are poorly understood.

LISA reframes the problem through score-based generative modeling theory:

**Main network:** Preserves visual quality by providing unconditional score prior.
**Side network:** Steers generation by contributing an implicit [[likelihood score]].

The insight: if we explicitly align side-network features with a likelihood score target, training converges faster and produces better disentanglement.

## Architecture

Three steps, all zero inference overhead:

1. **Feature hooking** — Grab intermediate features from a designated layer of the side network
2. **Score-space projection** — Lightweight decoder maps hooked features into the score latent space
3. **Likelihood alignment loss** — Construct an approximate likelihood score target; minimize distance between decoder output and target alongside standard diffusion loss

Jointly optimize side network + decoder with both losses combined.

## Why It Works

The regularization forces the side network to learn *what* to control (conditional signal) rather than *how* to perturb any intermediate representation. This produces:

- Faster training convergence across tasks
- Better feature disentanglement for conditional modeling
- Improved final synthetic quality with negligible extra training cost
- Zero inference-time overhead since the decoder is discarded post-training

## Results

Evaluated across various architectures (diffusion and flow models) and tasks (image and video control). Consistent improvements without architectural changes to the base model.

## Relevance to Workflow

Any pipeline that trains custom conditioning branches benefits: [[IP-Adapter]] variants, subject-DiTs, [[ControlNet]] derivatives, video editing adapters. For ComfyUI workflows using LoRA-based conditioning or custom node training pipelines, LISA's regularization can be dropped into the loss function without code changes to the architecture itself.

Practical impact: 20-30% faster adapter training convergence on video conditioning tasks like temporal control and image-reference injection.

> Works with any dual-branch setup — diffusion or flow-matching backbone. Only adds a lightweight decoder head during training, stripped at inference time.
