---
title: "RefAlign — Representation Alignment for Reference-to-Video Generation"
category: source
summary: Explicit alignment of DiT reference-branch features to a visual foundation model semantic space, improving identity consistency in reference-to-video generation with zero inference overhead.
tags: [reference-to-video, r2v, dit, identity-consistency, representation-alignment, training-loss]
sources: 1
source_date: "2026-03"
updated: "2026-07-01"
---

# RefAlign — For Reference-to-Video Generation

**arXiv:** [2603.25743](https://arxiv.org/abs/2603.25743) (v2)
**Evaluated on:** OpenS2V-Eval benchmark, TotalScore metric

## Problem: Modality Mismatch in R2V

Reference-to-video generation uses reference images to constrain video synthesis alongside text prompts (personalized ads, virtual try-on, character-driven narrative). Current approaches stack multiple features into the DiT:

- VAE latent of the reference image
- High-level semantic features from vision encoders
- Cross-modal embeddings

These heterogeneous representations are *implicitly* aligned through joint training. But implicit alignment leaves two persistent artifacts: **copy-paste** (reference appearance bleeds incorrectly into unrelated regions) and **multi-subject confusion** (when multiple subjects appear, identity features get scrambled).

## Approach: Explicit Reference Alignment Loss

RefAlign pulls reference-branch DiT features toward the semantic space of a frozen visual foundation model (VFM):

- **Pull**: Features of the *same* subject in reference branch and VFM are attracted
- **Push**: Features of *different* subjects are repulsed

This contrastive-style loss enhances both identity consistency and semantic discriminability.

### Key Properties

- **Training-only** — zero inference-time overhead
- Simple to add to any R2V pipeline (single loss term)
- Applied only to the reference branch, not the generation branch
- Better balance between text controllability and reference fidelity

## Results

RefAlign outperforms current SOTA methods on TotalScore in OpenS2V-Eval. The gains are most pronounced on multi-subject scenes where existing methods typically fail.

## Relevance to Pipeline

Directly applicable if building or fine-tuning reference-driven video workflows in ComfyUI (character consistency, product shot generation). Any T2V node that accepts a reference image could benefit from this alignment strategy. Particularly valuable for narrative video where maintaining character/subject identity across shots is critical.

## Caveats

- Training-time technique — not applicable to pretrained models without fine-tuning
- OpenS2V-Eval focuses on synthetic/product scenarios; creative/narrative applicability needs testing
- Performance gains may saturate if the base DiT already has strong reference conditioning
