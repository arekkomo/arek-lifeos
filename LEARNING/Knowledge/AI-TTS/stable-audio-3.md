---
title: Stable Audio 3
category: entity
summary: Stability AI's third-generation audio synthesis model family -- text-to-audio pipeline covering music, sound effects, and environmental audio with optimized variants for specific domains.
tags: [stable-audio, stability-ai, text-to-audio, diffusion, music-generation, sound-effects]
sources: 2
updated: 2026-06-24
---

# Stable Audio 3

Stability AI's latest audio synthesis model family (arXiv: 2605.17991), released June 2026. Covers music generation, sound effects, and environmental audio via text prompts using diffusion-based architecture.

## Model variants

| Model | Purpose | Size | Released | Downloads |
|-------|---------|------|----------|-----------|
| stable-audio-3-medium | General audio / SFX | Medium | 2026-06-16 | 61,463 |
| stable-audio-3-medium-base | Base checkpoint | Medium | 2026-06-16 | 21 |
| stable-audio-3-small-music-base | Music-specific | Small | 2026-05-20 | 2,031 |
| stable-audio-3-optimized | Optimized inference | N/A | 2026-06-03 | 17 |

## Architecture

- **Diffusion-based text-to-audio** pipeline (consistent with [[stable-audio-open]] v2)
- **Specialization strategy** -- separate checkpoints for general audio vs. music-specific generation, rather than one monolithic model
- **Optimized variant** suggests distillation or architectural changes for inference efficiency

## Practical impact

- **Aiah Syn relevance** -- Music-specific base model provides raw audio stems that can be mixed/mastered in [[daw|DaVinci Resolve]] for Aiah Syn content without relying on Suno/Udio APIs
- **Sound design** -- General-purpose SFX variant reduces need for royalty-free sound libraries in video production pipelines
- **ComfyUI integration** -- Text-to-audio pipeline format enables ComfyUI node support; check for community nodes when `text-to-audio` diffusers adapters are released

## Limitations vs. dedicated music tools

| Feature | Stable Audio 3 | [[suno]] / Udio |
|---------|----------------|-----------------|
| Training data openness | Closed ("other" license) | Closed |
| Commercial rights | Unspecified | Plan-dependent |
| Instrument separation | No (full mix only) | Varies |
| Length limit | Depends on variant | ~3-4 min typical |

## Related pages

- [[stability-ai]]
- [[higgs-audio-v3]]
- [[suno]]
- [[notion-export-ai-agents-automation-n8n]]
- [[aiah-syn-style]]
