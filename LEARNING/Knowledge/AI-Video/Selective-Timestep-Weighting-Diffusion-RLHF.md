---
title: Selective Timestep Weighting for Diffusion RLHF
category: concept
summary: Improves diffusion RLHF efficiency via timestep weighting and advantage-based replay, targeting uneven reward distribution across denoising steps.
tags: [diffusion-rlhf, reinforcement-learning, sample-efficiency]
sources: 1
source_path: https://arxiv.org/abs/2607.07693
source_date: "2026-07"
authors: [Eric Zhu, Abhinav Shrivastava, Soumik Mukhopadhyay]
ingested: "2026-07-09"
updated: "2026-07-09"
---

## What It Is

Sample-efficient RLHF for diffusion models. Two strategies target
uneven reward distribution across denoising timesteps directly.

> ⚠️ Note: [[Shell-LCC]] uses manifold-reward signals with zero
feedback cost. This paper assumes rewards exist and optimizes
which timesteps benefit from them most. Complementary approach.

---

## Core Insight

Late timesteps carry more structural information than early ones.
Most diffusion RLHF methods treat all steps as equal-value targets
for reward evaluation, wasting compute on low-signal timesteps.

---

## Strategy 1: Timestep Weighting

Assigns learnable importance weights per denoising step.
High-information steps get amplified, noisy ones down-weighted.
Cuts evaluation budget ~40% while maintaining alignment gains.

---

## Strategy 2: Advantage-Based Replay

Buffers trajectories with large reward-vs-baseline divergence
and reuses them across training iterations. Low-advantage
trajectories discard after single use instead of cycling.
Convergence speedup ~2x in reported experiments.

---

## Benchmarks

Tested on [[Wan 2.1]] and [[CogVideoX]]. Evaluated:
reward calls per epoch, alignment quality on held-out prompts,
and generalization vs overfitting to seen rewards. Both strategies
show sustained performance with fewer reward model calls.

---

## Practical Use

Drop-in modification of existing diffusion RLHF training loops.
Sampler-level only — no architecture changes required. Relevant
for fine-tuning [[ComfyUI]] backends with custom reward signals.

---

## Related Work

- [[Shell-LCC]] — manifold-based rewards instead of external feedback
- [[LocalDPO]] — region-level preference optimization for T2V alignment
- [[Miles LLM RL Post-Training]] — RL infrastructure (different domain)
