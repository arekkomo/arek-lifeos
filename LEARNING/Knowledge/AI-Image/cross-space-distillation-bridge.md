---
title: Cross-Space Distillation via Bridge Interface
category: concept
summary: Lightweight latent-space Bridge enables distillation from high-capacity diffusion teachers like Flux into compact SD 1.5 students despite VAE and latent resolution mismatch.
tags: [diffusion, distillation, flux, sd-1.5, bridge-interface, one-step-inference]
sources: 1
updated: 2026-07-01
source_path: arxiv/2606.32020
source_date: 2026-06
authors: [Anh Nguyen, Ngan Nguyen, Duc Vu, Trung Dao]
ingested: 2026-07-01
---

# Cross-Space Distillation (Bridge)

One-step diffusion models use timestep distillation for speed.
Most methods assume teacher and student share the same latent space.

## The Constraint

High-capacity teachers like [[Flux]] or SD 3.5
have different VAE parameterizations from backbones like SD 1.5.
This blocks knowledge transfer between them.

The gap has two parts:

- **Latent resolution mismatch** - different latent dimensions
- **VAE space mismatch** - different encoder/decoder weights

## The Bridge Solution

A lightweight latent interface maps student latents
into teacher space without modifying the student backbone.

Design components:

- Frozen student VAE decoder as spatial prior
- Compact learnable projector (trainable only)
- Latent reconstruction objective for pixel fidelity
- Attention fidelity for feature alignment across spaces

## Results

SD 1.5 improved from 5.4 to 9.4 on HPSv3 score.
One-step inference is preserved with low latency.

> Works via SD 1.5, which has broad [[ComfyUI]] ecosystem support.
Related to [[Stability AI]] fine-tuning in [[Diffusion Model Fine-Tuning]].
Distillation approach parallels [[DanceOPD - Flow Distillation]].

> Contradiction check: No contradiction with existing vault knowledge.
