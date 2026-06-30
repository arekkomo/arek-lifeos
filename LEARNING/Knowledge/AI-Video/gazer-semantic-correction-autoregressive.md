---
title: "Gazer — Training-Free Semantic Correction for Autoregressive Visual Models"
category: source
summary: Framework that integrates VLM feedback into autoregressive visual model sampling to diagnose and correct semantic errors mid-generation via reflective diagnosis + trajectory rewinding. No additional training required.
tags: [semantic-correction, video-synthesis, autoregressive-models, vlm-feedback, training-free]
sources: 1
source_path: arxiv.org/abs/2606.22550
source_date: 2026-06
authors: [Junhao Chen, Chanyu Zhu, Zheqi Lv, Keting Yin, Shengyu Zhang]
ingested: 2026-06-29
updated: 2026-06-29
---

# Gazer — Training-Free Semantic Correction for AVMs

**arXiv:** [2606.22550](https://arxiv.org/abs/2606.22550)
**Published:** 2026-06-21 | **Categories:** cs.CV, cs.AI, cs.CL, cs.MM
**Authors:** Junhao Chen et al.

## Problem Statement

Autoregressive visual models (AVMs) decompose generation into discrete scales via next-scale prediction. Semantic errors are hard to detect until the final output. Training-based correction methods incur substantial compute cost. Existing training-free tools neglect intermediate states, letting errors accumulate across scales.

## Method

Gazer inserts a VLM feedback loop directly into the AVM sampling process between scales. Two cooperating stages:

**Reflective Diagnosis Stage:**
- VLM inspects each intermediate generation state
- Identifies semantic mismatches against target prompt before error propagates to next scale
- Outputs structured diagnostic tokens indicating which regions/scales deviate

**Semantic Correction Stage:**
- Rewinds generation trajectory at identified scales
- Rectifies latent directions toward prompt-aligned distribution
- Resumes sampling from corrected state rather than corrupted intermediate

## Key Properties

- Zero additional model training required — plug-and-play at inference time
- Works across multiple AVM architectures (evaluated on compositional image and video benchmarks)
- Improves both semantic alignment and compositional accuracy
- Overhead is one VLM call per scale step vs. one forward pass

## Practical Relevance

Directly addresses a common failure mode in [[ai-video-generation]] pipelines: outputs that look locally correct but miss prompt semantics globally. Applicable to any AVM-based ComfyUI workflow — wrap the Gazer module around diffusion sampling nodes for mid-process semantic validation. Particularly useful for prompt adherence in character-consistent generation ([[freestory-character-consistency]]) and multi-concept composition ([[disco-lora-multi-concept-video]]).

## Related Work

- [[domainshuttle-s2v-source]] — Cross-domain flexibility in subject-driven T2V, related consistency problem
- [[feature-self-guidance-flow-diversity]] — Training-free improvement for flow models via feature manipulation during inference
- [[lisa-likelihood-score-alignment-source]] — Likelihood regularization for conditional generation quality

## References

1. Junhao Chen, Chanyu Zhu, Zheqi Lv, Keting Yin, Shengyu Zhang. "Training-Free Semantic Correction for Autoregressive Visual Models." arXiv:2606.22550, 2026-06-21.
