---
title: "AVTok — Unified 1D Tokenization for Audio-Video Generation"
category: concept
summary: "Dual-stream transformer with shared encoder-decoder that tokenizes audio-video pairs into a compact 1D latent representation via unified codebook. Eliminates modal representation gap without separate branch training. Enables audio-to-video, video-to-audio, and joint generation downstream."
tags: [audio-video, tokenization, multimodal, unified-representation, diffusion]
sources: 1
source_path: arXiv (submitted 2026-06-29)
updated: 2026-07-02
---

# AVTok — Unified Audio-Video Tokenization

## Problem

Audio-video generation methods typically use dual-branch designs with separate tokenizers per modality. This creates a representation gap and requires intensive compute for training both branches independently.

## Approach

Inspired by 1D visual tokenization advances, AVTok uses:

1. **Dual-stream transformer**: Shared encoder-decoder architecture with modal-specific learnable queries
2. **Unified codebook**: Audio and video encoded into the same 1D latent space
3. **Hierarchical training**: Progressive reconstruction capabilities per modality before joint fine-tuning

## Design Choices

- Single codebook instead of two separate vocabularies — reduces vocabulary mismatch errors
- Modal-specific queries handle heterogeneous information imbalance (audio is lower-dimensional than video)

## Downstream Applications

When integrated into generation pipelines:
- **Audio-to-video**: Music/sound drives visual generation with tight synchronization
- **Video-to-audio**: Generate soundtracks or foley from existing footage
- **Joint audio-video generation**: Simultaneous synthesis with native alignment

For [[ComfyUI]] workflows, this replaces the current approach of running separate audio and video models and trying to post-align them.

## Related Work

- [[Suno v5 Prompt Engineering Best Practices]] — covers AI music generation; AVTok provides a technical bridge between music models like [[Magma RT2]] and video diffusion pipelines
- [[DramaDirector]] — multi-shot narrative video with audio context; unified tokenization makes audio conditioning more natural
- [[ComfyUI MCP Agent Panel]] — if agents orchestrate both modalities, unified tokenization simplifies the control flow
