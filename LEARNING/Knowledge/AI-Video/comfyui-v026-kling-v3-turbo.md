---
title: ComfyUI v0.26 Release — Partner Nodes, LTX2 Context Windows, Krea2
category: update
summary: ComfyUI v0.26.0 (June 23) adds partner node SDK architecture with Kling V3-Turbo integration, LTX2 context window sampling with IC-LoRa guides, Krea2 and Boogu-Image model support, and SCAIL-2 multireference subject consistency.
tags: [comfyui, kling, ltx2, krea2, scaill, ai-video, workflow]
sources: 2
updated: 2026-06-28
---

# ComfyUI v0.26 Release — Partner Nodes, LTX2 Context Windows, Krea2

ComfyUI reached **v0.26.0** on June 23, 2026. This release ships the Partner Nodes SDK architecture, native model integrations (Kling V3-Turbo, Krea2, Boogu-Image), and LTX2 context window sampling with [[ic-lora|IC-LoRa]] conditioning guides. Release cadence accelerated to ~48h cycles.

## Partner Node SDK system

- **What it is** -- Official distribution channel where partner orgs (e.g., [[kling-ai]], Runway, [[minimax]]) publish ComfyUI nodes with guaranteed API support
- **Version-pinned SDKs** -- Community nodes previously reverse-engineered endpoints and broke on every API change. Partner nodes ship SDK manifests tied to specific API versions
- **First releases in v0.26** -- Kling V3-Turbo (PR #14528), Luma Rays 3.2 (PR #14540), HappyHorse 1.1 (Alibaba, PR #14581), Grok Image 1080p (PR #14597)
- **Retry header compliance** -- Partner nodes now respect `Retry-After` HTTP headers for rate-limited APIs (PR #14234)

## LTX2 Context Windows + IC-LoRa guides

- **Context windows sampling** -- LTX2 models now support configurable context window sizes, enabling longer video generation without full recomputation
- **IC-LoRa conditioning** -- Instance-Conditioned LoRa adapters guide generation within sliding windows, preserving temporal coherence across frame boundaries
- **PR #13325** by @drozbay (CORE-3). Enables multi-reference subject consistency in LTX2 pipelines

## Krea2 integration

- **Krea AI v2** -- New model support with accurate VRAM usage factor calculation (PR #14589, #14594)
- Text-to-image generation node with native ComfyUI workflow integration
- Memory-efficient inference via optimized attention allocation

## SCAIL-2 Multireference

- **Subject consistency** -- SCAIL-2 enables multi-reference image conditioning for character-consistent generation (PR #14509 by @kijai)
- Combines IP-Adapter-style reference images with flow-matching guidance
- Applicable to storyboarding and sequence art workflows in [[ai-video-generation]]

## Boogu-Image + Text Encoder updates

- **Boogu-Image** support added (PR #14523) with negative prompt input and min_images=0 for edit-only pipelines
- **Qwen3-VL as Flux2 Klein text encoder** -- Qwen3-VL can serve as a text encoder for [[flux2-klein|FLUX.2 Klein]] models (PR #14526), enabling vision-language prompting in image generation workflows

## Other v0.26 changes

- int8 quantization support on Turing GPUs (PR #14662)
- SDPoseDrawKeypoints checkbox for head drawing toggle
- Load3DAdvanced node for mesh import (PR #14316)
- Output socket added to save nodes for pipeline chaining
- Telemetry CLI flag (`--enable_telemetry`)

## Release timeline

| Version | Date | Highlights |
|---------|------|------------|
| v0.26.0 | 2026-06-23 | Partner node SDK, Kling V3-Turbo, LTX2 context windows + IC-LoRa, Krea2, Boogu-Image, SCAIL-2 multireference |
| v0.25.1 | 2026-06-18 | Companion update for partner node infrastructure |
| v0.25.0 | 2026-06-16 | Partner nodes framework foundation |

## Practical workflow impact

- **Kling V3-Turbo in ComfyUI** -- Direct text-to-video and video-to-video from within ComfyUI, no external API calls
- **Multi-model comparison** -- Kling, MiniMax, Open-Sora as parallel nodes enables side-by-side quality testing
- **LTX2 + IC-LoRa** -- Longer videos with consistent characters via context window sampling
- **SCAIL-2** -- Training-free subject consistency for storyboard and sequence workflows

## Architecture note

Partner SDKs signal ComfyUI's shift from prototype to production workflow engine. Stable API contracts enable pre-built workflow templates. Alignment with DGX Spark hosting capabilities is direct.

## Related pages

- [[comfyui]]
- [[kling-ai]]
- [[minimax]]
- [[runway-ml]]
- [[ai-video-generation]]
- [[flux2-klein]]
- [[agentic-creative-pipelines]]
- [[notion-export-ai-video-animation]]
