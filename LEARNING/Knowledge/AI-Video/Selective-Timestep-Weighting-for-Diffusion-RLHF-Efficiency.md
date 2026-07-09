---
title: Selective Timestep Weighting for Diffusion RLHF Efficiency
category: concept
summary: Sample-efficient diffusion RLHF via timestep-weighted rewards and advantage-based trajectory replay to reduce feedback bottleneck.
tags: [diffusion, reinforcement-learning, rlhf, sample-efficiency, timesteps]
sources: 1
source_path: https://arxiv.org/abs/2607.07693v1
source_date: "2026-07"
updated: "2026-07-08"
---

## What It Is

Reinforcement learning from human feedback for diffusion models
wastes compute because not every denoising timestep contributes equally.

This paper identifies that reward signal density varies across the trajectory
and proposes two mechanisms that cut required feedback by up to 4x while
matching alignment quality of full-timestep baselines.

> ⚠️ Contradiction: [[Miles LLM RL Post-Training]] assumes uniform
timestep value during PPO rollouts for language models, which may not
transfer cleanly to diffusion where denoising trajectory dynamics differ
substantially from autoregressive token-by-token generation.

---

## Core Observations

**Observation 1 — Uneven Reward Distribution.** Empirical analysis of
reward model outputs across timesteps shows that early denoising steps
(high noise) contribute disproportionately less to gradient quality than
mid-to-late steps where structure emerges.

Standard diffusion RLHF treats all timesteps as equally valuable,
leading to waste.

**Observation 2 — Redundant Replay.** Trajectories sampled during training
are replayed indiscriminately regardless of whether their reward signal
provides new information.

Low-advantage trajectories that reinforce existing policy gradients add
minimal signal beyond the first pass.

---

## Proposed Mechanisms

### Selective Timestep Weighting (STW)

- Assigns learnable weights $w_t$ per timestep based on expected gradient magnitude
- High-noise timesteps down-weighted, mid-late timesteps up-weighted
- Weights are trained jointly with the reward model head via a lightweight meta-optimizer

### Advantage-Based Replay Buffer (ABR)

- Stores trajectories sorted by advantage estimate $A(s,a) = Q - V$ 
- Sampling probability proportional to absolute advantage magnitude
- Clips extreme advantages to prevent mode collapse on outlier trajectories

---

## Key Results

On [[Wan 2.1]] and [[CogVideoX]] benchmarks:

| Method | Reward Calls | Alignment Score | FVD |
|--------|:------------:|:---------------:|:---:|
| Uniform sampling baseline | — | 0.87 | 34.2 |
| STW alone | 58% fewer | 0.86 | 35.1 |
| ABR alone | 73% fewer | 0.84 | 36.8 |
| STW + ABR combined | ~78% fewer | **0.88** | **33.9** |

Combined approach achieves highest alignment score with roughly 1/4 the feedback budget. No degradation in FVD (Fréchet Video Distance).

---

## Pipeline Integration Notes

- Drop-in compatible with existing [[ComfyUI]] inference loops once reward model is mounted
- Tested on both text-to-video and image-to-video workflows
- Memory overhead <2% for timestep weight cache; replay buffer scales linearly with batch size
- Requires no modification to the diffusion backbone itself — operates entirely at the RL optimization layer

---

## Related Entries

- [[Miles LLM RL Post-Training]] — RL post-training infrastructure (contrast: language models)
- [[Wan 2.1 Family]] — diffusion model tested against in this work
- [[CogVideoX]] — additional test subject for cross-architecture generalization