---
title: "Score Accuracy Does Not Certify Numerical Stability in Diffusion Sampling"
category: concept
summary: Theoretical proof that small forward-marginal score matching error does not guarantee numerical stability of Euler-Maruyama discretizations in reverse-time diffusion sampling, with denoiser projection as a practical stabilization technique.
tags: [diffusion-theory, numerical-stability, sampler-analysis, euler-maruyama, classifier-free-guidance]
sources: 1
source_path: "arXiv:2607.08757"
source_date: 2026-07
authors: [Numerical Analysis Group]
ingested: 2026-07-10
updated: 2026-07-10
---

## Overview

This paper proves a counterintuitive result about diffusion model samplers: **small training error (forward-marginal \\(L^2\\) accuracy) does not guarantee that the discretized reverse-time sampler produces stable samples**. Specifically, Euler-Maruyama discretizations converge in probability but every \\(W_p\\) Wasserstein distance diverges for bounded, globally Lipschitz denoisers. The failure occurs even within a single fixed neural architecture.

The paper simultaneously provides a constructive fix: **projecting the learned denoiser onto a known bounded convex set** containing the data support restores moment bounds and yields Wasserstein convergence under mild local regularity.

## Key Results

### The Negative Result (Main Theorem)
- A smooth score field can have arbitrarily small forward-marginal \\(L^2\\) error while its Euler-Maruyama discretization diverges in every \\(W_p\\) for \\(p \\geq 1\\)
- Weak convergence holds, but moments of every order diverge along rare numerical trajectories
- Constructed within one fixed finite neural architecture — not a degenerate asymptotic artifact

### The Positive Result (Corollary)
For compactly supported data:
- Projecting the denoiser onto a bounded closed convex set containing support preserves pointwise accuracy
- Gives grid-uniform moment bounds across all trajectories
- Yields Wasserstein convergence under mild local regularity conditions

Empirical validation with a small fixed DiT-style network confirms: rare trajectories cause large numerical growth, which **denoiser projection suppresses** while overall trajectory errors remain small.

## Practical Relevance for ComfyUI / Sampler Tuning

### Direct Implications
This paper explains why certain samplers in ComfyUI (Euler, Euler-Maruyama variants) produce sporadically degraded samples despite otherwise good training metrics. The "rare trajectory divergence" predicts:

- **Batch-of-many consistency issues** — Most of a batch generates fine; occasional samples blow up due to rare trajectory convergence failures
- **High-guidance instability** — Increasing guidance weight (CFG scale) amplifies the Lipschitz constant effect, increasing probability of hitting divergent trajectories
- **Sampler selection matters more than previously understood** — The gap between weak convergence and Wasserstein convergence means some samplers appear fine on aggregate metrics while failing on individual samples

### Connection to Vault Entries
[[Guidance-Breaks-Fitted-Operator-CFG-Repair]] showed that CFG destroys the fitted-operator property of DDIM at high guidance. This paper shows a different failure mode: even with perfect score estimation, discretization error alone can cause divergence. Together, they paint a picture where **no sampler is universally stable** — Euler methods fail due to trajectory divergence (this paper), while DDIM fails due to stiffness from CFG (the fitted operator paper).

| Paper | Failure Mode | Sampler Affected | Fix |
|-------|-------------|-----------------|-----|
| Score Accuracy Does Not Certify Stability | Trajectory divergence (rare but severe) | Euler, EM variants | Denoiser projection |
| [[Guidance-Breaks-Fitted-Operator-CFG-Repair]] | Stiffness from high CFG weight | DDIM, DDPM | Modified guidance coefficient |

## Limitations

- Theoretical results assume bounded, globally Lipschitz denoisers — real DiT/ViT denoisers may not satisfy these conditions uniformly
- Denoiser projection requires knowing the data support a priori (trivial for image space [0,1] or standard normal latents, but non-trivial for custom latent spaces)
- No benchmark comparison against alternative samplers like DPM-Solver or FlowMatch schedulers like [[FlowMo]]
- DiT validation uses a small reference network; scaling to Wan2.2 or Flux-class models untested

## References

[[Guidance-Breaks-Fitted-Operator-CFG-Repair]], [[Wan2.2-Lightning]], [[Dynamic-in-Few-Step]], [[FlowMo]], [[Stable Layers]]
