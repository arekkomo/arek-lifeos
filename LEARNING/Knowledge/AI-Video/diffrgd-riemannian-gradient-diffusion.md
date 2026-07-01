---
title: "DiffRGD — Riemannian Gradient Descent for Diffusion Guidance"
category: concept
summary: Inference-time diffusion guidance via spherical manifold optimization.
tags: ["diffusion-guidance", "inference-time", "riemannian", "sampler"]
sources: 1
updated: 2026-07-01
---

# DiffRGD — Riemannian Optimization for Diffusion Guidance

**Paper:** arXiv 2606.28417 (June 25, 2026)
**Authors:** Jia-Wei Liao et al.
**Categories:** cs.CV
**Code:** https://github.com/jwliao1209/DiffRGD

## Core Claim

Inference-time guidance methods steer latents via external loss
functions. Standard Euclidean gradients push samples away from the
Gaussian prior, causing distributional drift and visual artifacts.

DiffRGD formulates each sampling step as constrained optimization
on a spherical manifold. This preserves latent radial structure
while still enabling conditional steering of generation paths.

## Background

Inference-time guidance avoids costly pretraining or fine-tuning
by optimizing over partially-denoised latents. Approaches include
classifier-free guidance, prompt-to-prompt editing, and methods
like null-text inversion applied at inference time.

These share one weakness: optimization trajectories leave the
manifold of valid Gaussian samples. After enough steps this causes
over-saturation, color distortion, and structural incoherence.

## Method

DiffRGD reinterprets each denoising step through Riemannian geometry.
Latent space follows an approximately spherical Gaussian distribution.

Standard Euclidean gradients push latents radially outward or inward.
This breaks the implicit radius constraint enforced by the sampler,
creating out-of-distribution samples with visible artifacts.

DiffRGD performs optimization on the manifold surface:

1. Map each latent to a point on a unit sphere
2. Project guidance gradients onto tangent space
3. Update via exponential map retractions
4. Re-normalize radius to target timestep distribution

This preserves isotropic structure while optimizing conditional
objectives like identity preservation or structural alignment.

## Results

DiffRGD outperforms previous guidance methods across:

- Image restoration: deblurring, inpainting tasks
- Conditional generation: class-conditioned sampling quality
- Distributional stability: KL divergence stays near zero

The method is plug-and-play with no base-model retraining required.
Compatible with any score-based or flow-matching sampler pipeline.

## Practical Relevance

For [[ComfyUI]] workflows that use inference-time conditioning:
control nets, prompt-strength sliders, IP-Adapter nodes, and custom
text-guidance samplers all benefit from geodesically constrained steps.

Current ComfyUI implementations of CFG do not enforce Gaussian
constraints. Long sampling runs with high CFG weights produce
over-saturation artifacts that DiffRGD addresses at root cause level.

Integration path: a sampler-customization node that replaces the
standard Euler or Heun step with spherical manifold update logic.
Minimal overhead, one normalization plus projection per denoising step.

See also [[liveedit-streaming-video-editing]] — real-time video editing
where distributional stability matters as a correctness constraint.

Compared to [[latsearch-latent-reward-guided-search-video-diffusion]],
which uses explicit reward models on partially-denoised latents,
DiffRGD uses mathematical structure instead of learned scores.

## Related Work

- [[lisa-likelihood-score-alignment-source]] — dual-branch conditional generation
- [[physics-question-scene-graph-eval]] — fine-grained physics evaluation for video
