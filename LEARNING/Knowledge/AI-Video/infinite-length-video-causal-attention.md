---
title: "Infinite-Length Video Generation — Error-Free Long Video via Causal Attention and KV Caching"
category: source
summary: Framework for minute-level video synthesis using hybrid causal-bidirectional attention across clips, KV caching for constant memory, and truncation-rectified flow (T-RFlow) to suppress error accumulation in long sequences.
tags: [long-video, video-generation, causal-attention, kv-caching, diffusion]
sources: 1
source_path: arxiv.org/abs/2606.22370
source_date: 2026-06
authors: [Shuning Chang, Weihua Chen, Jiasheng Tang, Hao Xu, Zeyu Zhang]
ingested: 2026-06-29
updated: 2026-06-29
---

# Infinite-Length Video Generation Framework

**arXiv:** [2606.22370](https://arxiv.org/abs/2606.22370)
**Published:** 2026-06-21 | **Categories:** cs.CV
**Authors:** Shuning Chang et al.

## Problem Statement

Video generation has reached minute-level synthesis capability but hits three hard limits on duration: error accumulation across frames, attribute drift (character identity, lighting, style slowly change), and data scarcity for long training clips. Most pipelines generate short clips then concatenate — seams are obvious.

## Architecture

Framework builds a video extension model via two-stage fine-tuning:

1. **Short-video extension fine-tune** — Diffusion model trained on large-scale short videos to autoregressively produce coherent clips
2. **Long-video causal attention fine-tune** — Same model further trained on long video data with hybrid attention: bidirectional within each clip, unidirectional (causal) between clips

The hybrid attention design borrows from [[llm-architecture]] principles for sequence modeling. Within-clip tokens get full context; across-clip tokens only see prior history, preventing lookahead artifacts while preserving temporal coherence.

## Technical Components

**KV Caching:**
- Maintains constant key-value memory budget regardless of clip count
- Enables theoretically infinite-length generation without OOM errors
- Constant memory footprint enables sustained real-time generation

**Truncation-Rectified Flow (T-RFlow):**
- Suppresses error accumulation by correcting flow trajectories at truncation boundaries
- Applied at each clip boundary to prevent drift from previous segments
- Complements KV caching by ensuring cached representations stay aligned with target distribution

## Practical Relevance

Addresses one of the most requested capabilities in [[ai-video-generation]]: generating continuous footage without visible seams or identity collapse. The hybrid attention pattern (bidirectional-intra, causal-inter) maps directly to ComfyUI batch processing — each clip becomes a node invocation that reads from shared KV cache state. Useful for filmmaking previsualization where minute-level takes are standard. Compatible with [[wan-streamer-v01-realtime]] streaming architecture since both use block-causal attention patterns.

## Related Work

- [[navicache-test-time-caching-source]] — Test-time caching for video diffusion, adjacent memory-efficiency approach
- [[freestory-character-consistency]] — Character consistency methods relevant to attribute drift problem
- [[disco-lora-multi-concept-video]] — Multi-concept composition also faces coherence challenges across duration

## References

1. Shuning Chang, Weihua Chen, Jiasheng Tang, Hao Xu, Zeyu Zhang. "Towards Error-Free Long Video Generation." arXiv:2606.22370, 2026-06-21.
