---
title: PACR-Video — Prompt-Adapter Context Routing for Multi-Shot Long Video Extrapolation
category: concept
summary: >-
  Parameter-efficient LoRA-style adapters with recursive prompt routing
  preserve identity and style across multi-shot video without full fine-tuning.
tags: ["video-extrapolation", "parameter-efficient", "temporal-adapters", "long-video", "consistency", "shot-control"]
sources: 1
updated: 2026-07-08
---

## Overview

PACR-Video (arXiv 2607.06481) addresses the problem of extrapolating long,
multi-shot video sequences from a text-to-video diffusion transformer while
preserving entity consistency, visual style, and narrative coherence across
shot boundaries.

Instead of fine-tuning the full generator — which is expensive and causes
distribution shift — PACR-Video keeps the base model frozen and adds
lightweight parameter-efficient components:

- Low-rank temporal adapters on attention layers (similar to [[LoRA]] patterns)
- Learned shot-role prompt tokens that gate adapter activation per shot
- A recursive prompt bank storing entity, location, action, and style
  descriptions from prior shots

Published: 2026-07-07 by Anna Córdoba, Adam Puente Tercero et al. (cs.CV, cs.AI)

## Architecture

### Temporal Adapters with Prompt Routing

The framework augments a frozen text-to-video diffusion transformer (tested
on [[CogVideoX]] and [[Wan 2.1]]) with low-rank adapters on the temporal
attention layers of each transformer block.

Each adapter is gated by learned prompt tokens that encode shot-level roles
(e.g., protagonist, background object, environmental detail). These gates
determine how much each adapter contributes during generation of a given shot,
enabling fine-grained control without retraining base weights.

### Recursive Prompt Bank

After generating each shot, the system distills compact prompts describing:

- Entity descriptions (character appearance, clothing, props)
- Spatial locations within the scene
- Actions and motion trajectories performed
- Visual style tokens (color palette, lighting, camera treatment)

These stored prompts are then routed through adapter gates for the next shot
based on predicted narrative dependencies. This is analogous to what [[TempAct]]
does at the planning layer but here it operates at the adapter-routing level
instead of prompt orchestration.

### Training Objective: Shot-Local / Story-Global

The composite loss combines three terms:

1. Next-shot reconstruction fidelity (shot-level quality)
2. Cross-shot identity contrast (same entity should look consistent across
   shots; different entities should stay distinct)
3. Prompt sparsity regularization (keep stored prompts compact, avoiding
   bloated context banks in long sequences)

An adapter composition schedule balances early-shot visual consistency with
later-shot event progression and viewpoint change, addressing the common
problem where long-video models degrade toward the end of a sequence.

## Results

Tested across six multi-shot and long-video benchmarks:

- Outperforms text-to-video baselines on distributional quality (FVD/FID)
- Better semantic alignment than tuning-based methods (prompt fidelity)
- Higher identity consistency scores than memory-augmented streaming models
- Improved temporal smoothness and motion stability over clip boundaries
- Wins human preference evaluation across transition coherence

Key finding: lightweight prompt routing + adapter composition provides
sufficient controllable capacity for stable long-horizon extrapolation,
eliminating the need for expensive full-model fine-tuning.

## Practical Relevance

For filmmaking workflows in [[ComfyUI]], this approach translates to:

- Maintaining character consistency across scene cuts without per-scene LoRA
  training — simply accumulate prompt bank entries during generation
- Integrating with [[Wan 2.1]] or [[CogVideoX]] backends via adapter injection
  nodes (the architecture is model-agnostic given a DiT backbone)
- Complementing [[FreeStory]]'s entity-grounded feature reuse approach, though
  PACR works at the adapter level rather than latent KV cache injection

This fills a gap in multi-shot generation pipelines where current methods
either require full fine-tuning (expensive) or lack identity tracking across
shots (quality degradation).

## Related Work

- [[TempAct]] — LLM planner-executor for autoregressive video generation;
  PACR handles the same coherence problem at the diffusion adapter level
- [[FreeStory]] — training-free character consistency via feature reuse;
  PACR takes a parametric approach with learned routing instead
- [[Disco-LoRA]] — disentangled multi-concept customization via iterative
  dual-LoRA isolation; shares the LoRA-mixing philosophy for composable control
