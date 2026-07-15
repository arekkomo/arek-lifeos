---
title: "The Seriality Gap in Video Diffusion Models"
category: concept
summary: Bidirectional video diffusion degrades as causal chain length increases because models lack serial computation capacity. AR/blockwise generation and architectural depth mitigate this gap. Explains why long-horizon video synthesis fails structurally, not just temporally.
tags: ["video-diffusion", "causal-reasoning", "autoregressive", "analysis", "long-horizon-video"]
sources: 1
updated: 2026-07-15
---

# The Seriality Gap in Video Diffusion Models

**arXiv:** 2607.13031 | **Published:** 2026-07-14
**Authors:** Jorge Diaz Chao, Konpat Preechakul, Yuxi Liu, Yutong Bai
**Venue:** cs.LG, cs.CV

## Overview

Standard bidirectional video diffusion models fail on causally-chained events:
when object B hits C as a consequence of A hitting B, the model cannot track
the dependency properly even with more denoising steps. This failure is not
about video length — single-ball trajectories over the same duration work fine.

The paper calls this the **seriality gap**: a mismatch between tasks that
require growing serial computation and models whose processing fundamentally
stays parallel/bidirectional regardless of how complex sequential logic becomes.

## Key Findings

Controlled hard-sphere dynamics experiments show:

- Two-ball collisions: baseline performance holds. The model handles one causal
link without significant degradation compared to no-interference baselines.
- Four-ball chains: quality drops ~40%. Each additional causal dependency
compounds error beyond what added sampling steps compensate for.
- Adding denoising steps (8 -> 50) helps minimally. More parallel processing
does not approximate serial reasoning on chained events.

## What Helps — Intervention Studies

Autoregressive blockwise generation improves performance disproportionately:
breaking the video into sequential windows where each window conditions on
the previous one gives the model explicit serial structure it needs.

Deeper architectures also help compared to wider ones: adding layers provides
more computation steps per token, approximating serial processing within the
parallel framework.

The study suggests that current bidirectional models have a ceiling on how far
causal chains can stretch before quality collapses. This is relevant for
physics-realistic scenes — object interactions, fluid simulations, character
movement sequences where one action triggers another.

## Practical Relevance

Explains the fundamental limitation behind long-horizon video generation
failures that quality fixes like [[cycle-world-temporal-reversibility-long-video]]
and [[delta-forcing-trust-region-steering-ar-video]] try to patch without
addressing the underlying seriality problem.

For [[comfyui-v027-int8-support-release]] workflows using AR video models
(Wan 2.1, CogVideoX), this paper suggests that switching from pure bidirectional
diffusion to autoregressive or blockwise generation modes will improve causal
chain quality even on shorter clips with complex object interactions.

[[NaviCache]]-style acceleration methods may also interact with seriality:
aggressive caching in critical steps of chained events could amplify error
propagation more than the per-step drift signal alone predicts.

## Connections

- [[infinite-length-video-causal-attention]] — Causal attention for extended sequences
- [[SSM-Meets-Video-Diffusion]] — SSM blocks offer explicit serial computation