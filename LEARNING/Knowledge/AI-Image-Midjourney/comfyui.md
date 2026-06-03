---
title: ComfyUI
category: entity
summary: Node-based UI for running Stable Diffusion and diffusion model pipelines locally; the standard interface for advanced AI image workflows.
tags: [comfyui, stable-diffusion, ai-images, node-based, local-ai]
sources: 1
updated: 2026-04-19
---

# ComfyUI

Node-based graphical interface for running Stable Diffusion and other diffusion model pipelines locally. The de facto standard for advanced, customizable AI image and video workflows outside of cloud platforms like Midjourney.

## Why it matters

ComfyUI exposes the full diffusion pipeline as a visual node graph, enabling:
- Custom model loading (checkpoints, LoRA, ControlNet)
- Precise control over sampling, conditioning, and post-processing
- Integration of custom models (e.g. Lucy Edit for instruction-guided editing)
- Reproducible, shareable workflows (JSON-based)

## Key integrations

- **Stable Diffusion** (all versions) — primary backend
- **LoRA models** — style/character fine-tunes via kohya_ss training
- **ControlNet** — structural conditioning (pose, depth, canny edge)
- **Lucy Edit (Lucy-Edit-ComfyUI)** — instruction-guided image and video editing model within ComfyUI
- Custom node ecosystem — hundreds of community extensions

## Compared to alternatives

| | ComfyUI | Automatic1111 (WebUI) | Invoke AI |
|---|---|---|---|
| Interface | Node graph | Form-based | Hybrid |
| Flexibility | Maximum | Moderate | Moderate |
| Learning curve | High | Low | Medium |
| Custom pipelines | Yes | Limited | Yes |

## Open questions

- Which ComfyUI workflows produce the best results for video generation (AnimateDiff, SVD)?
- What are the best community node packs for production workflows?

## Appears in

- [[notion-export-ai-image-midjourney]] — ComfyUI section; Lucy-Edit-ComfyUI integration

## Related pages

- [[stability-ai]]
- [[diffusion-model-fine-tuning]]
- [[ai-image-generation]]
