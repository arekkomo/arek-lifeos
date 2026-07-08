---
title: AI Image Generation
category: concept
summary: The field of generating images from text prompts, reference images, or hybrid inputs using diffusion models and related architectures.
tags: [ai-images, diffusion-models, generative-ai, text-to-image, stable-diffusion, midjourney]
sources: 1
updated: 2026-04-19
---

# AI Image Generation

## Definition

AI image generation encompasses systems that produce raster or vector images from text prompts, image references, sketches, or combinations thereof. The dominant paradigm is **diffusion models** (Stable Diffusion, DALL-E, Midjourney's backend), which iteratively denoise a random latent into a coherent image conditioned on a text or image embedding.

## Major platforms (as of 2026)

| Platform | Type | Strength |
|---|---|---|
| [[midjourney]] | Hosted | Aesthetic quality; prompting culture; character consistency (Pan/VR method) |
| [[flux]] | API/integration | Editing + generation; customization |
| [[stability-ai]] Stable Diffusion | Open-source | Ecosystem (ComfyUI, LoRA, ControlNet); self-hostable |
| DALL-E 3 (OpenAI) | Hosted | Instruction following; long text rendering |
| Imagen (Google) | Hosted | Photorealism |
| [[nvidia-edify]] | Enterprise | 3D + image; professional topology; 4K PBR |

## Key techniques

### Prompting
- **Describe tool** (Midjourney) — reverse image-to-prompt for style extraction
- **Color prompting** — "cool colors", "radioactive colors" drive palette
- **Style references** — `--sref` in Midjourney; LoRA models in SD
- **Compositional generation** — Omost (lllyasviel) structures complex scenes with characters, settings, and styles

### Fine-tuning
- **LoRA / DreamBooth** — adapt a base model to specific characters, objects, or styles using custom image datasets
- See [[diffusion-model-fine-tuning]]

### Editing
- **Inpainting** — replace masked regions with prompt-driven content
- **Drag-based editing** — StableDrag enables spatial content manipulation by dragging rather than prompting
- **Object replacement** — OmniGen: "replace cake with pasta" from a single prompt

### Consistency
- **Character sheets** (Midjourney Pan/VR method) — anchor consistency across generations
- **Image-to-image** — use existing generation as foundation for next

## Legal / ethical landscape

Active copyright litigation (Getty Images vs [[stability-ai]]) is defining the IP framework for the field. "Ethical AI image generators" built on artist-collaboration models are emerging as an alternative to models trained on scraped internet data.

## Open questions

- Will drag-based editing (StableDrag) displace prompt-based editing for spatial tasks?
- How will copyright litigation reshape training data practices across all major providers?
- When does ComfyUI + local SD outperform cloud platforms for production use?

## Used in

- [[Synthesis/ai-creative-tools-overview]]
- [[midjourney]]
- [[flux]]
- [[stability-ai]]
- [[comfyui]]
- [[nvidia-edify]]

## Key claims from sources

- Midjourney Describe tool enables color palette reverse-engineering — [[notion-export-ai-image-midjourney]]
- Flux offers editing + generation in one model — [[notion-export-ai-image-midjourney]]
- Getty lawsuit is a landmark case for AI training data IP — [[notion-export-ai-image-midjourney]]
