---
title: Dynamic-in-Few-Step — Dynamic Computation with Few-Step Distillation for Video Diffusion Acceleration
category: concept
summary: >-
  Joint optimization of denoising steps and structural sparsity transforms a
  pretrained video diffusion model into step-specific Mixture-of-Models,
  achieving 30x real-time speedup on Wan-14B while preserving quality.
tags: ["video-diffusion", "acceleration", "distillation", "MoM", "structural-sparsity", "Wan-14B", "inference-optimization"]
sources: 1
updated: 2026-07-09
---

## Overview

Dynamic-in-Few-Step (arXiv 2607.06631) addresses the prohibitive compute cost
of video diffusion models by jointly optimizing denoising steps and architectural
sparsity. Unlike standard post-hoc pruning that compresses a fixed pipeline, it
transforms each step of a pretrained model into a custom mixture-of-models (MoM),
where the active sub-network adapts per-timestep.

Published: 2026-07-07 by Yu Cheng et al., Fudan University (cs.CV, cs.AI, cs.LG).
Preprint: https://arxiv.org/abs/2607.06631

## Core Insight

Few-step distillation accelerates video diffusion by reducing 50+ steps to 4--8,
but existing approaches use a static architecture at every step. In practice,
early denoising stages carry more representational weight than late-stage
refinement — wasting compute on redundant capacity.

Dynamic-in-Few-Step exploits this asymmetry: rather than pruning uniformly, the
model learns step-specific sparse structures. Each timestep activates only
the layers/sub-blocks needed at that noise level, forming a Mixture-of-Models
(MoM) over time.

## Architecture

### Step-Specific MoM Construction

Given a pretrained VDM with L transformer blocks, the method creates B binary
gates per block. At each distillation step t, gates decide which attention heads
and FFN paths to activate — removing ~24 per-step FLOPs beyond base 4-step
distillation on top of Wan-14B.

Gating is differentiable via straight-through estimator (STE) with a sparsity
objective that pushes activation patterns below a target density threshold.

### Progressive Training Strategy

Joint optimization of distillation objectives and architectural decisions causes
training instability: both signal pathways move simultaneously. The paper solves
this with:

1. **Phase 1** — Freeze gates, distill knowledge transfer from teacher to student
2. **Phase 2** — Unlock gates, learn sparse activation patterns under fixed
   denoising weights
3. **Phase 3** — Joint fine-tuning of both gates and denoising parameters

### Output Rollout Mechanism

To ensure sparsity decisions remain coherent (i.e., timesteps do not collapse
to identical structures), the rollout mechanism enforces diversity by comparing
intermediate latent outputs between adjacent steps and penalizing redundancy.

## Results

**Wan-14B benchmark:**

| Metric | 50-Step Teacher | 4-Step Baseline | Dynamic-in-Few-Step |
|---|---|---|---|
| FLOPs/step | 100% | ~20% | ~15.2% |
| Wall-clock | 1x | 8.3x | 10x (combined with MoM) |
| Speedup over teacher | — | 8.3x | **30x total** |
| Visual quality (VBench) | Baseline | Competitive | Slight improvement over baseline |

Key finding: 30x speedup from combined few-step reduction and step-specific
pruning, with no significant measurable visual quality loss on standard benchmarks.

## Practical Relevance

For ComfyUI workflows using high-parameter backbones like [[Wan 2.1]]:

- Reduces VRAM requirement per generation batch (fewer active parameters at each
  step allows larger resolution or longer clips)
- Compatible with existing KSampler nodes — MoM structure is baked into weights,
  no custom node needed after conversion
- Orthogonal to [[FlowMo]]'s flow-scheduling acceleration; can stack both methods
  for multiplicative gains
- Alternative pathway to [[Wan2.2-Lightning]] speed without separate distillation
  training cycle — post-training method works on any pretrained VDM

## Limitations

- Post-training only: requires a dedicated distillation phase before deployment
- Gate inference adds minimal overhead; paper reports the specialized runtime
  engine is needed to actually extract FLOP savings
- Tested exclusively on Wang2.1/14B; generalization to CogVideoX or HunyuanVideo
  unverified

## Related Work

[[Wan2.2-Lightning]] uses step-distillation alone (no architecture changes).
[[FlowMo]] rewrites token scheduling rather than model topology.
[[Selective-Timestep-Weighting-for-Diffusion-RLHF-Efficiency]] targets RLHF feedback
efficiency in diffusion models with a different sparsification mechanism.
