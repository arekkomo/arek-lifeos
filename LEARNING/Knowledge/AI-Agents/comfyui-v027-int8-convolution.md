---
title: "ComfyUI v0.27 — Native int8 Convolution Support and Partner Node Updates"
category: entity
summary: "Major ComfyUI release adding native int8 convolution model support with progressive optimizations (faster int8, Turing GPU compatibility, memory leak fixes). Partner node updates include HappyHorse 1.1, SeeDance 2.0-Mini, Krea 2 advanced merging, and Nano Banana 2 Lite."
tags: [comfyui, inference-optimization, int8-quantization, partner-nodes, diffusion]
sources: 1
source_path: GitHub release (published 2026-06-30)
updated: 2026-07-02
---

# ComfyUI v0.27.0

## Release Date
2026-06-30

## Major Changes

### Native int8 Convolution Support

First-class support for int8 convolution models across multiple PR iterations:

1. **Core int8 inference** — Basic int8 matmul support for offloaded weights
2. **Performance pass** — Faster int8 kernel path avoiding quantize-dequantize overhead
3. **Lora compatibility fix** — Correct requantization when lora weights applied with wrong settings
4. **Turing GPU support** — int8 works on older Turing architecture (RTX 20-series)
5. **Memory leak fix** — Resolved int8-related memory accumulation issues

**Impact**: VRAM reduction of ~50% for compatible models, enabling larger checkpoints or higher batch sizes on constrained hardware like DGX Spark.

### Partner Node Updates

- **Alibaba HappyHorse 1.1** — New model variant added to partner node
- **ByteDance SeeDance 2.0 + Mini** — Dance video generation with 4K resolution support; Mini variant for lower-resource inference
- **Google Nano Banana 2 Lite** — Lightweight image model via Google partner integration
- **Grok Image** — 1080p resolution added

### New Core Features

- **Seed node** — Explicit seed control as a core node (CORE-295)
- **Bounding box canvas + Ideogram JSON prompt** — Structured prompt injection for controlled layout composition
- **Advanced Krea 2 model merging node** — Multi-model blending for effect synthesis
- **ConditioningMultiply node** — Additional conditioning adjustment alongside existing nodes
- **GLSL node updated** — Uses ANGLE library (CORE-162)

## Practical Implications

This release is the most performance-focused since v0.24. The int8 support chain alone represents a significant upgrade for local diffusion inference:

- [[ComfyUI v0.26 + Kling V3-Turbo]] was partner-node focused; v0.27 shifts toward core infrastructure optimization
- Compatible with existing workflows — no node graph changes required for int8 activation
- Paired with [[NaviCache]] or [[ISPA]], enables multi-layer inference acceleration

## Version History

| Version | Date | Focus |
|---------|------|-------|
| v0.27.0 | 2026-06-30 | int8 conv, partner nodes, seed node |
| v0.26.0 | ~2026-06-24 | Partner node architecture, Kling V3-Turbo |
| v0.25.1 | ~2026-06-17 | Bug fixes |
