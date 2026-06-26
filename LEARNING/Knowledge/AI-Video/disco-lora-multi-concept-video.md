---
title: Disco-LoRA — Disentangled Content, Style, and Motion LoRA Composition
category: concept
summary: Multi-concept video customization framework that disentangles content, style, and motion via iterative dual-LoRA with Z-score regularization for composable LoRA mixing in T2V models.
tags: [ai-video, lora, text-to-video, video-customization, comfyui-relevant]
sources: 1
source_path: arxiv.org/abs/2606.26668
source_date: 2026-06
authors: [Xuancheng Xu, Gengyun Jia, Bing-Kun Bao]
ingested: 2026-06-26
updated: 2026-06-26
---

# Disco-LoRA — Disentangled Multi-Concept Video Customization

Method that decomposes video customization into two sub-tasks (Content-Style and Content-Motion) using iterative dual-LoRA disentanglement, then recombines via Z-score statistical regularization.

## Core mechanism

Two stages:

1. **Iterative Dual-LoRA Disentanglement**: Each training task is solved with a specialized LoRA pair that isolates one concept (e.g., style vs content). The framework alternates optimization between LoRAs assigned to different concepts, progressively disengaging shared parameters.

2. **Z-Score Composition Regularization**: Authors identify that layer-wise weight trends encode LoRA identity, while weight magnitudes control composability. A Z-score normalization aligns distributions across LoRAs, preserving patterns while minimizing interference at merge time.

## Why it works

- Layer-wise attention patterns of each LoRA determine what concept is being encoded
- Weight magnitude is the primary source of cross-LoRA interference
- Normalizing to zero mean per layer removes the interference channel without distorting identity

## Use cases

- Custom style transfer onto arbitrary content with controllable motion
- Multi-character video consistency where each character needs a separate LoRA
- Combining pre-trained motion LoRAs with new subject LoRAs in [[ai-video-generation]] pipelines
- Potentially integrable into ComfyUI custom node workflows for modular video generation

## Benchmarks

Disco-LoRA tested on comprehensive multi-concept video benchmark. Outperforms existing methods across joint content-style-motion control tasks. Preserves source appearance, style transfer fidelity, and motion pattern accuracy simultaneously.

## Related pages

- [[ai-video-generation]]
- [[free-story-character-consistency]]
- [[comfyui-v026-kling-v3-turbo]]
- [[mvtrack4gen]]
- [[danceopd-flow-distillation]]
