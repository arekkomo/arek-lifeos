---
title: TempAct — Planner-Executor RL for Autoregressive Video Generation
category: concept
summary: Addresses temporal ambiguity in chunk-wise autoregressive video diffusion via a Planner-Executor RL framework that enforces correct prompt-transition ordering and sub-event sequencing per video chunk. Trained with step-level reward signals to eliminate delayed reactions, blended semantics, and error propagation across transitions.
tags: ["autoregressive-video", "video-diffusion", "reinforcement-learning", "temporal-coherence", "chunk-wise-generation", "prompt-following"]
sources: 1
source_path: arxiv.org/abs/2606.28016
source_date: 2026-07
authors: [arXiv anonymous (v2 replacement)]
ingested: 2026-07-03
updated: 2026-07-03
---

# TempAct — Advancing Temporal Plausibility in AR Video Generation

Temporal coherence fix for autoregressive (AR) video diffusion models where chunk-by-chunk
generation creates ambiguity in which sub-event belongs to which time segment.

## The problem

AR video models synthesize videos incrementally, processing one temporal chunk at a time with
cached visual context from previous chunks. This enables streaming/real-time generation but
introduces three structural failures:

1. **Delayed reactions**: Model processes a prompt instruction too late, causing the action to
   appear after its intended start point in the timeline.

2. **Blended step semantics**: When switching between consecutive prompt segments (e.g.,
   "woman walks" → "woman sits"), the model blends both instructions rather than executing
   them sequentially in their respective chunks.

3. **Error propagation**: Mistakes in early chunk transitions compound through later chunks,
   degrading temporal quality as the video progresses.

Standard SFT (supervised fine-tuning) cannot fix this reliably due to exposure bias during
training-time vs. inference-time generation mismatch. Rollout-based distillation targets
low-level denoising rather than structural action ordering.

## TempAct approach

Planner-Executor RL architecture with two key innovations:

**LLM Planner**: An LLM-based planner decomposes multi-step prompts into *span-aware step*
prompts — per-chunk instructions that are executable by the video diffusion model. Rather
than a single global prompt, the LLM generates structured sub-event assignments mapped to
temporal positions in the chunk sequence.

**AR Diffusion Executor**: Trained under RL to follow the planner's step prompts while
conditioning on its own generated visual history (auto-regressive execution). The executor
learns from rollouts where it generates continuations conditioned on past frames, closing
the SFT exposure-gap that plagues fine-tuning approaches.

**Hierarchical group exploration**: Candidate plans are grouped into planning groups, and each plan generates an execution group of multiple continuations from a shared visual context. This structure enables two levels of credit assignment — plan-level for long-horizon temporal outcomes, executor-level for immediate denoising quality. Hierarchical grouping lets the RL policy learn that *which* plan leads to temporally coherent outputs even when individual executions vary in pixel fidelity.

## Why this matters

Directly relevant to [[WanStreamer]] and [[LiveEdit]]-style streaming video pipelines where
temporal coherence across chunks is the bottleneck — not generation speed or image quality.
The Planner-Executor separation also opens the path for human-in-the-loop planning where a
user could modify the chunk-by-chunk action plan mid-generation.

## Comparison with related work

Unlike [[Shell-LCC]] which optimizes reward via manifold scoring on final frames (offline), and
[[Delta Forcing]] which steers diffusion via trust-region guidance at inference time, TempAct
operates at the structural level of *which* prompt maps to *which* chunk — orthogonal to
sampling-level acceleration or quality improvement.

Different from [[Freestory]] consistency technique too: Freestory preserves character identity
across freeform storytelling, while TempAct ensures temporal instruction sequencing inside a
single multi-event prompt.

## References

- arXiv: 2606.28016v2 (replacement)
- Category: cs.CV (Computer Vision and Pattern Recognition)
