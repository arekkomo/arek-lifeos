---
title: "Vega — Unified Video Understanding and Generation Framework"
category: concept
summary: "Hybrid autoregressive + diffusion architecture that jointly models video understanding (compact semantic tokens) and generation (dense visual frames). Shares vocabulary across text and visual representations, achieving strong performance on both VBench generation and VideoMME understanding benchmarks."
tags: [video-generation, video-understanding, unified-modeling, hybrid-architecture, autoregressive, diffusion]
source_path: arXiv (submitted 2026-07-01)
sources: 1
updated: 2026-07-02
---

# Vega — Unified Video Understanding and Generation

## Problem

Video understanding favors compact, discriminative semantic representations; video generation requires dense signals preserving visual detail. Unifying both in one model is architecturally challenging — similar to the [[Cross-Space Distillation via Bridge]] challenge but bidirectional.

## Architecture

Vega bridges both regimes with a hybrid approach:

1. **Shared vocabulary**: Text and visual representations use a unified token space
2. **AR component**: Predicts semantically meaningful visual tokens for keyframes (structure, semantics)
3. **Diffusion component**: Renders dense, high-resolution frames from the AR- predicted skeleton

This separates *what* to render from *how* to render it — echoing [[World Narrative Model]]'s philosophical framing but implemented within a single model rather than an agent-driven pipeline.

## Results

- Strong on VBench generation benchmarks
- Competitive on VideoMME understanding benchmarks
- Single model replaces cascaded architectures (understanding VLM + generation T2V)

## Practical Implications

For AI video workflows in [[ComfyUI]]:
- Eliminates need for separate vision encoder + generation model pipeline
- Reduces VRAM footprint by sharing backbone between understanding and generation passes
- Potential for iterative refine-generate cycles within a single model context

## Related Work

- [[Infinite-Length Video]] — also combines AR structure with diffusion detail, but focused on sequence length rather than multimodal unification
- [[Shell-LCC]] — models manifold structure of SFT data for reward signals; Vega's shared vocabulary implicitly addresses the same representation alignment problem
- [[FreeStory]] — character consistency via entity feature grounding; unifying understanding+generation makes this kind of cross-modal coherence more natural
