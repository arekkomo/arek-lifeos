---
title: "LatSearch — Latent Reward-Guided Search for Inference-Time Scaling"
category: source
summary: Video diffusion inference-time scaling via a latent reward model that scores partially denoised latents at arbitrary timesteps, enabling efficient resampling and pruning without decoding full video frames.
tags: [video-diffusion, inference-scaling, reward-model, search, wan21, benchmark]
sources: 1
source_date: "2026-03"
updated: "2026-07-01"
---

# LatSearch — Inference-Time Scaling for Video Diffusion

**arXiv:** [2603.14526](https://arxiv.org/abs/2603.14526) (v2)
**Tested on:** Wan2.1 model, VBench-2.0 benchmark

## Motivation

Inference-time scaling works for LLMs. The same principle could unlock quality gains in video diffusion — but existing attempts hit three blockers:

1. **Prior-based methods** only optimize initial noise (no mid-denoising correction)
2. **Reward-on-decoded-video** is extremely expensive (encode→denoise→decode→evaluate = full pipeline each iteration)
3. Error accumulation from early-stage decisions compounds through the denoising trajectory

## Core Contribution: Latent Reward Model

A separate reward model that scores *partially denoised latents* (not decoded video frames) at arbitrary timesteps along three dimensions:

- **Visual quality** — spatial coherence, artifact absence
- **Motion quality** — temporal smoothness, consistency
- **Text alignment** — prompt fidelity

Scoring in latent space is orders of magnitude cheaper than decoding + evaluating full video.

## LatSearch Mechanism: RGRP

**Reward-Guided Resampling & Pruning:**

1. **Resampling stage**: Candidates sampled proportional to reward-normalized probabilities (not raw rewards), reducing over-reliance on any single reward model
2. **Pruning stage**: At final scheduled step, only the candidate with highest *cumulative* reward is retained

Both stages operate in latent space — no video decoding needed during search.

## Results

Evaluated on VBench-2.0 benchmark with Wan2.1 as baseline. LatSearch consistently improves generation quality across multiple evaluation dimensions while keeping inference overhead manageable (since scoring happens in latent space, not pixel space).

## Relevance to Pipeline

Directly applicable to Wan2.1 ComfyUI workflows — the paper explicitly tests on Wan2.1 which is already installed on DGX Spark. A LatSearch node could add an inference-time quality boost to existing generations, trading compute for quality in a controlled way. Particularly valuable for high-stakes renders (client work, portfolio pieces) where you want confidence in temporal consistency before committing to a full decode.

## Caveats

- Requires training/tuning the latent reward model for each base diffusion model
- Added inference cost, though significantly less than naive approaches
- VBench is an academic benchmark — real-world creative quality gains need empirical validation
