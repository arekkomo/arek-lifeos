---
title: "Physics Question Scene Graph (PQSG): Fine-Grained Evaluation of Physical Plausibility in Generated Video"
category: source
summary: Hierarchical VLM-driven evaluation pipeline that checks generated videos for object faithfulness, action accuracy, and physical law adherence via a graph-based question structure. Benchmarked against Sora 2, Veo 3, and Wan 2.1 on the new FinePhyEval dataset with human annotations. Closed-source models score higher than Wan 2.1 on physical realism.
tags: [ai-video, evaluation-benchmarks, physics-grounding, vision-language-models, video-quality, sora, veo, wan-models]
sources: 3
source_path: https://arxiv.org/abs/2606.25306
source_date: 2026-06
authors: [PQSG authors (cs.CV submission)]
ingested: 2026-06-25
---

# Physics Question Scene Graph (PQSG)

## Overview

Video generation models produce increasingly realistic content but still violate basic physical laws — objects float, gravity is inconsistent, materials deform unrealistically. Existing evaluation methods treat video quality as a single scalar or coarse category. PQSG introduces fine-grained, hierarchical evaluation via vision-language model (VLM)-generated question graphs that decompose physical plausibility into verifiable sub-queries about objects, actions, and physics constraints.

## Method: Graph-Based Question Hierarchy

Rather than flat questioning (e.g., "Does this video look physically plausible?"), PQSG represents questions as a directed graph where nodes are specific queries and edges encode logical dependencies:

- Only ask "Did the glass break?" if "Was the glass dropped?" is true
- Only evaluate gravitational acceleration if an object was actually in freefall
- Questions at one level gate access to dependent child questions, preventing logically invalid evaluation paths
- VLM generates questions guided by high-quality in-context examples that ensure consistent questioning style

### Three Evaluation Dimensions

PQSG assesses faithfulness across:

1. **Object faithfulness** — are the correct objects present with accurate properties (mass, material, size)?
2. **Action accuracy** — are the described events/actions depicted correctly?
3. **Physical law adherence** — do motions follow gravity, momentum conservation, fluid dynamics, collision physics?

## FinePhyEval Dataset & Results

A benchmark created specifically to validate PQSG:

- Contains prompt-to-video pairs from three models: Sora v2 (OpenAI), Veo 3 (Google), and Wan 2.1 (Alibaba)
- Each video annotated across multiple physical categories by human reviewers
- PQSG scores correlated with human judgments, outperforming prior evaluation methods on correlation metrics
- **Finding:** Both Sora 2 and Veo 3 rank higher than Wan 2.1 on physical realism under PQSG evaluation

### VLM Subtask Benchmark

FinePhyEval annotations also serve as a benchmark for two VLM capabilities:

- **Question generation** — models produce structurally similar questions to humans
- **Question answering/evaluation** — models still fall noticeably short of human accuracy, especially on subtle physics violations

This gap means automated evaluation pipelines still require careful calibration before fully replacing human review.

## Practical Significance for AI Video Production

- **Quality gate for generated footage** — PQSG can flag physically implausible clips before they reach compositing stages in [[davinci-resolve]] workflows
- **Model selection criteria** — the PQSG ranking of Sora 2 > Veo 3 > Wan 2.1 on physical plausibility provides a concrete metric for choosing video generation backends when physics accuracy matters (e.g., action sequences, stunts, product simulations)
- **Automated review integration** — could be integrated into [[agentic-creative-pipelines]] as an evaluation node that scores generated clips and routes low-scoring outputs for re-generation with modified prompts

### Limitations

VLM-based evaluation still lags behind human judgment on nuanced physics assessments. Use PQSG as a pre-screening filter rather than a final quality gate — any clip passing PQSG should still receive human review before entering the edit.

## Related Work

PQSG represents an evolution from scalar video quality metrics toward structured, interpretable evaluation. Compare with earlier approaches that used single VLM scores or human panel ratings without granular physical-category breakdowns.

> **Status:** ArXiv preprint (June 2026). FinePhyEval dataset and PQSG pipeline details are available in the paper; independent code release timing TBD. The three-model comparison (Sora 2, Veo 3, Wan 2.1) is notable as one of the few head-to-head physical plausibility benchmarks in current literature.
