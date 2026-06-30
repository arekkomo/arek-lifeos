---
title: "SSM-Meets-Video-Diffusion — Structured State Spaces for Long-Term Video Generation"
category: source
summary: Bidirectional SSMs (Mamba) replace attention layers as temporal feature extractors in video diffusion models, achieving linear-time computation vs quadratic attention while maintaining or improving FVD at comparable GPU memory usage.
tags: [video-diffusion, ssm, mamba, long-video, temporal-modeling, inference-efficiency]
sources: 1
source_date: "2026-03"
updated: "2026-07-01"
---

# SSM-Meets-Video-Diffusion Models

**arXiv:** [2403.07711](https://arxiv.org/abs/2403.07711) (v5)
**Authors:** shim0114 + collaborators
**Code:** https://github.com/shim0114/SSM-Meets-Video-Diffusion-Models

## Core Idea

Attention layers in video diffusion transformers scale quadratically with sequence length. SSMs (state-space models, e.g., Mamba) scale linearly — making them attractive temporal feature extractors for long-sequence diffusion.

Key finding: **bidirectional** SSMs outperform unidirectional ones for temporal feature capture in video generation (consistent with prior results showing bidirectional SSMs help spatial features in image gen).

## Architecture Changes

- Replace attention-based temporal layers with bidirectional SSM blocks
- Test across multiple model sizes
- Memory usage per-frame drops significantly vs attention baseline
- Evaluated on MineRL Navigate and other long-term video datasets

## Key Results

| Metric | Attention Baseline | SSM Variant |
|--------|-------------------|-------------|
| FVD (256 frames) | X | ≤ X (same or better) |
| GPU Memory | Higher | Lower for same quality |
| Sequence Length Scaling | O(n²) | O(n) |

- For sequences up to 256 frames, SSM models require less memory for equal FVD
- SSM variants often deliver *better* performance at comparable GPU memory usage
- Linear scaling enables generation of much longer video clips without memory explosion

## Relevance to Pipeline

Direct applicability to ComfyUI workflows: any diffusion-based video node could theoretically swap attention temporal layers for SSM blocks, enabling longer generations without VRAM increase. Particularly relevant for Wan2.1 or HunyuanVideo pipelines where sequence length is a bottleneck.

## Caveats

- Paper focuses on MineRL datasets (robotic navigation), not photorealistic creative video
- Translation to text-to-video DiTs needs additional work
- Code available but integration path unclear without T2V-specific benchmarks
