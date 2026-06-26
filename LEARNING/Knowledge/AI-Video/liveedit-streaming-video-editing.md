---
title: LiveEdit — Real-Time Diffusion-Based Streaming Video Editing
category: concept
summary: Streaming video editing framework with three-stage distillation from bidirectional to unidirectional model, achieving 12.66 FPS causal frame-by-frame editing with content preservation for AR and interactive VFX workflows.
tags: [ai-video, streaming-video, real-time-editing, diffusion, vfx, ar]
sources: 1
source_path: arxiv.org/abs/2606.26740
source_date: 2026-06
authors: [Xinyu Wang, Chongbo Zhao, Fangneng Zhan, Yue Ma]
ingested: 2026-06-26
updated: 2026-06-26
---

# LiveEdit — Real-Time Streaming Video Editing

Framework that enables causal, frame-by-frame video editing with strong background preservation and real-time latency targets for AR deployment.

## Core mechanism

Three-stage distillation pipeline:

1. Bidirectional foundation editor (teacher model) → trains on offline editing tasks with full context
2. Progressive compression to streaming-compatible architecture with causal/temporal constraints
3. Unidirectional streaming editor that processes frames sequentially, maintaining state for consistency

**AR-oriented mask cache**: Reuses region-related computation across consecutive frames. Since masks change slowly in editing tasks, the framework caches and re-adapts mask tensors instead of recomputing them each frame.

## Key design choices

- Causal processing: Each frame only depends on its own input and cached state from past frames
- Content preservation: Non-edited regions are protected via explicit preservation loss during distillation
- Latency target: 12.66 FPS measured, targeting interactive/AR use cases where sub-80ms response matters

## Why it matters for VFX workflows

Current video generation models require the full video to be encoded before editing begins. LiveEdit flips this — edits propagate frame-by-frame in real time, enabling:

- Interactive compositing during filming (see-through AR with AI-generated overlays)
- Real-time green screen replacement with generated backgrounds
- On-set VFX preview without waiting for post-processing

## Connection to existing tools

- Complements [[comfyui-v026-kling-v3-turbo]] style node-based video workflows by adding real-time feedback
- Related to [[ai-video-generation]] infrastructure as a deployment optimization rather than a new architecture
- Shares streaming paradigm with [[wan-streamer-v01-realtime]] but focused on editing rather than generation

## Related pages

- [[ai-video-generation]]
- [[comfyui-v026-kling-v3-turbo]]
- [[wan-streamer-v01-realtime]]
- [[vpa-guard-image-to-video-safety]]
- [[daveinci-resolve-reddit-workflow-tips]]
