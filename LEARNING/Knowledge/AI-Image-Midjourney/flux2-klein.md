---
title: FLUX.2 Klein Architecture
category: entity
summary: Black Forest Labs' FLUX.2 release series featuring the new Klein architecture -- a compact family of diffusion models optimized for image generation and editing with significantly reduced parameter counts.
tags: [flux, black-forest-labs, diffusion, text-to-image, kv-cache, inference-optimization]
sources: 3
updated: 2026-06-24
---

# FLUX.2 Klein Architecture

Black Forest Labs' second major iteration of [[flux]], introducing the **Klein** architecture -- a family of compact diffusion models designed for efficient image generation and editing at fraction of the original parameter count.

## Release timeline

| Model | Size | Params | Released | License | Downloads |
|-------|------|--------|----------|---------|-----------|
| FLUX.2-klein-base-4b-fp8 | 4B FP8 | ~4B | 2026-02-24 | Apache 2.0 | 56,387 |
| FLUX.2-klein-9b-kv | 9B KV-cache | ~9B | 2026-03-12 | Proprietary | 10,265 |
| FLUX.2-small-decoder | Decoder-only | N/A | 2026-04-07 | Apache 2.0 | 208,146 |

## Architecture changes

**Klein name** -- Named after Felix Klein (mathematician), referencing the topology and geometry of the model's latent space design. The Klein architecture uses a key-value (KV) cache mechanism to reduce per-step computation.

Key architectural differences from FLUX.1:
- **KV-cache optimization** -- 9B variant caches attention keys/values across diffusion steps, reducing redundant re-computation
- **FP8 support** -- Base-4b runs in mixed precision with maintained output quality
- **Small decoder variant** -- Standalone decoder module decouples the bottleneck from the core transformer, enabling modular fine-tuning

## Practical impact for workflows

- **ComfyUI compatible** -- All FLUX.2 variants are supported via [[comfyui]] through diffusion-single-file format and diffusers pipeline (`Flux2KleinPipeline`)
- **Lower VRAM requirements** -- 4B FP8 variant runs on consumer GPUs where full FLUX models require 24GB+ VRAM
- **Image editing** -- All variants support `image-to-image` pipelines, enabling in-painting and structural edits without regenerating entire frames

## Relation to video workflow

While Klein is image-focused, the KV-cache + small decoder design represents a clear optimization path that BFL will likely extend to video diffusion. Efficient per-frame generation via cached intermediates directly applies to [[ai-video-generation]] pipelines where frame-to-frame coherence matters.

> ⚠️ Contradiction: Existing [[flux]] page describes Flux as having "editing and customization" capabilities without any mention of the Klein architecture or FLUX.2 release series. That page is now outdated — FLUX.2 replaces the FLUX.1 architecture entirely. Update needed on [[flux]].

## Licensing note

Base-4b-fp8 and small-decoder are Apache 2.0 (commercial use permitted). The 9B KV-cache variant uses "other" license -- likely similar terms to FLUX.1 commercial license.

## Related pages

- [[flux]]
- [[stability-ai]]
- [[comfyui]]
- [[ai-image-generation]]
- [[notion-export-ai-image-midjourney]]
