---
title: "ComfyUI v0.27 — Native int8 Support and Partner Nodes Expansion"
category: entity
summary: ComfyUI release adding native int8 convrot model support, Turing GPU compatibility, HappyHorse 1.1 / SeeDance 2.0-Grok partner nodes, bounding box canvas, and memory leak fixes — released 2026-06-30.
tags: [ComfyUI, int8, video-generation, release-notes, diffusion]
sources: 1
updated: 2026-07-04
---

# ComfyUI v0.27 Release Notes

## Key Feature: Native int8 Support

Major architectural improvement — native support for **int8 convrot (convolution + rotation) models**, enabling lower VRAM usage for large diffusion backbones without external quantization libraries like [[OrbitQuant]].

### What Changed

- Full int8 inference pipeline for compatible checkpoints
- **Faster int8 kernels** — follow-up optimizations to initial int8 support
- **int8 on Turing GPUs** (RTX 20xx series) — previously limited to Ampere+ architecture
- **Fixed memory leak** in int8 path (PR #14697) — critical for long batch jobs
- **Improved LoRA + int8 interaction** — offloaded LoRA weights no longer skip matrix multiply when int8 is active

### Practical Impact

Works synergistically with [[OrbitQuant]]: OrbitQuant reduces model weights to ultra-low precision (W2A4) but requires custom rotation kernels. ComfyUI v0.27 provides a native path for moderately quantized models (int8) with broader hardware support including older Turing GPUs. Both approaches useful depending on GPU tier.

| Aspect | int8 (v0.27) | OrbitQuant W2A4 |
|--------|-------------|-----------------|
| VRAM savings | ~50% | ~75% |
| Hardware reqs | Turing+ | Ampere+ |
| Calibration needed | None | None (data-agnostic) |
| Quality drop | Minimal | Higher but usable |

## Partner Nodes Added

- **Alibaba HappyHorse 1.1** — image generation model node
- **Grok Image** — now supports 1080p resolution
- **ByteDance SeeDance 2.0** — 4K video generation; includes SeeDance-2.0-Mini variant for lower-cost inference
- **Google Nano Banana 2 Lite** — text-to-image
- **Gemini Video Omni** — multimodal video generation

## Other Notable Changes

- **Bounding box canvas node** (CORE-292) — visual tool for region-aware prompting/composition
- **Ideogram JSON prompt support** — structured prompt input alongside natural language
- **Seed node** — explicit seed control as a native graph node (CORE-295)
- **Krea 2 model merging** — advanced checkpoint blending via dedicated node
- **GLSL node uses ANGLE library** instead of system OpenGL for better cross-platform compatibility
- Workflow templates bumped to v0.11.1

## Version Comparison

Released: 2026-06-30 | 41 reactions (16 👍, 9 ❤️)
Previous: v0.26.x → Current: v0.27.0
[Full changelog](https://github.com/Comfy-Org/ComfyUI/compare/v0.26.0...v0.27.0)

## Relationship to Vault Content

- Follows [[ComfyUI-OCIO]] (color management integration) — int8 support enables OCIO workflows with larger models on consumer hardware
- Complements all AI-Video entries since ComfyUI is the primary runtime for local video generation pipelines
- int8 path means [[Wan 2.1]], [[CogVideoX]], [[FLUX.1]] backbones now fit in smaller VRAM footprints without OrbitQuant's overhead
