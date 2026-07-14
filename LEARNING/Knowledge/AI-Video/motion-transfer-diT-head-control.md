---
title: "Controlling Motion Transfer in DiTs via Attention Heads"
category: concept
summary: >
  Training-free motion transfer framework for video diffusion transformers based on identifying and manipulating distinct attention heads specialized for motion vs spatial structure, enabling controllable character animation without parameter updates.
tags: ["motion-transfer", "attention-head-analysis", "training-free-control", "video-diffusion", "DiT-mechanistic"]
sources: 1
updated: "2026-07-14"
arxiv_id: "2607.11081"
---

# Motion Transfer in DiTs via Attention Heads

## What It Is

A training-free framework for controllable motion transfer in video Diffusion Transformers that operates at the individual attention-head level rather than full model fine-tuning. The core finding is that video DiTs naturally develop distinct attention heads specialized for encoding motion information versus preserving spatial structure -- and these can be independently manipulated to control transfer quality without updating any model parameters.

## Method

**Attention Head Analysis:** The authors systematically probe video DiT architectures at the head level and identify separate clusters: motion-specialized heads that encode temporal dynamics and pose trajectories, and structure-specialized heads that maintain spatial layout, object identity, and compositional arrangement.

**Head-Aware Transfer Pipeline:** Motion cues from motion-specialized heads are refined via semantic correspondence guidance to ensure target-prompt alignment. Structural fidelity is preserved through selective feature injection into the structure-specialized heads. Both operations require zero training -- they work by reading and modifying attention maps during inference.

## Results

- Enables accurate motion transfer that follows reference motion while respecting target prompts
- Provides interpretable control since users can reason about which heads govern which aspect of generation
- Competitive with fine-tuned methods on standard motion transfer tasks despite being parameter-frozen
- Tested across multiple video DiT backbones including Wan and CogVideoX variants

## Relevance to Your Workflows

This directly enables a class of controllable video generation that was previously only accessible through per-subject LoRA training or ControlNet-style conditioning. For [[ComfyUI]] workflows, this could manifest as an optional pre-processing step on KSampler outputs that selectively rewinds motion-specialized attention heads before final denoising. Particularly useful for character animation pipelines where you need to transfer reference performance (from body-mocap clips, dancer footage) onto different characters while maintaining the target prompt's styling -- relevant to [[DreamO-ByteDance]] and [[VACE]] style workflows but without custom training overhead.

Related to [[FlowMo]] for flow-mapped gesture control and [[QWERTY]] for query-warped spatial motion trajectories, but operates at a fundamentally different level: direct attention manipulation rather than embedding or conditioning modification.

> ✅ Verified against arXiv 2607.11081v1, published 2026-07-13. Authors: Jung, Sunyoung et al. (KAIST). Categories: cs.CV, cs.AI. Evaluated on motion transfer benchmarks across Wan and CogVideoX diffusion transformer backbones with zero parameter updates.
