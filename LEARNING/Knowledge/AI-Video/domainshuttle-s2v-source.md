---
title: "DomainShuttle — Subject-Driven Text-to-Video with Cross-Domain Flexibility"
category: source
summary: Method that bridges in-domain (high subject fidelity) and cross-domain (style/attribute editing) text-to-video personalization via Domain-MoT, DualRoPE, and Cross-Pair Consistent Loss. Enables freeform open domain video customization without per-subject fine-tuning.
tags: [text-to-video, subject-driven, personalization, cross-domain, rope, adaln]
sources: 1
source_path: https://arxiv.org/abs/2606.26058
source_date: 2026-06-24
authors: [anonymous arXiv submission]
ingested: 2026-06-27
updated: 2026-06-27
---

# DomainShuttle: Freeform Open Domain Subject-driven Text-to-video Generation

## Core Idea

Subject-driven text-to-video (S2V) has two competing requirements:

**In-domain:** Reference subject features preserved as-is (high fidelity). Existing methods optimize for this exclusively.

**Cross-domain:** Intrinsic subject identity kept while style, attributes, and semantic combos vary per prompt. Existing methods fail here due to over-fitting the reference.

DomainShuttle bridges both regimes via three architectural innovations.

## Architecture

### Domain-MoT (Mixture-of-Transformers)
Decouples video tokens from reference image features into separate processing streams. Introduces domain-aware [[AdaLN]] modulation that switches between fidelity mode and flexibility mode based on prompt signals rather than requiring separate model instances.

### Video-Reference DualRoPE
Places reference image tokens and video tokens in independent [[Rotary Position Embedding]] spaces. This prevents the model from conflating reference spatial relationships with generated video spatial relationships, achieving precise subject-level geometry modeling without cross-contamination.

Practical implication: The same subject can appear at different scales, angles, and compositions across frames while maintaining identity coherence.

### Cross-Pair Consistent Loss
A regularization term that extracts intrinsic subject features by explicitly penalizing feature variation caused by irrelevant reference properties (background, lighting, pose). Trains the encoder to be invariant to domain noise while sensitive to identity signals.

## Results

- Significant improvements over prior S2V methods across both in-domain and cross-domain benchmarks
- Handles novel style transfers, semantic recombination, and attribute swapping without degradation
- Zero-shot generalization to unseen subject categories

## Relevance to Workflow

This is directly applicable to character-consistent video generation — a key blocker for narrative content creation. Instead of tuning a LoRA per character, DomainShuttle's dual-space approach means you drop a reference image into the pipeline and get faithful reproduction *or* creative variation, controlled by prompt intensity.

For [[ComfyUI]] workflows, this maps cleanly to the subject-driven generation node architecture where reference inputs are decoupled from the main video latent stream.

> Works with any transformer-based text-to-video backbone that supports conditional RoPE injection. No per-subject training required.
