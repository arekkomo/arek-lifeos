---
title: "Notion Export — AI Image Generation & Midjourney"
category: source
summary: Curated Notion database export covering Midjourney prompting and techniques, AI image tools (Flux, OmniGen, NVIDIA Edify), 3D generation (Tripo AI, Step1X-3D), diffusion tooling (ComfyUI, kohya_ss), and research on compositional/drag-based/world generation.
tags: [ai-images, midjourney, diffusion-models, comfyui, prompting, 3d-generation, stable-diffusion]
source_path: raw/notion-export/ai-image-midjourney.md
source_date: 2026-04-19
authors: [Arek Komorowski (curator)]
ingested: 2026-04-19
updated: 2026-04-19
---

# Notion Export — AI Image Generation & Midjourney

## TL;DR

A personal knowledge base export from the dtb Knowledge Notion database covering Midjourney workflows, competing AI image platforms, 3D generation tools, diffusion model fine-tuning tooling, and research on compositional generation, spatial editing, and world generation from single images.

## Key claims

1. **Midjourney character consistency** — the Pan/VR method generates a character sheet (multiple poses in a single image), solving the consistency problem across generations.
2. **Midjourney Describe tool** — enables image-to-prompt reverse engineering and color palette extraction from existing images.
3. **Midjourney new features** — supports building on foundational images (photo or MJ-generated) for iterative creative workflows.
4. **Vector art generation** — Midjourney can produce vector-style artwork via color prompts ("cool colors", "radioactive colors") and flat design guidance.
5. **Flux** — AI image generation model with editing and customization; direct competitor to Midjourney and Stable Diffusion.
6. **OmniGen** — prompt-based object replacement ("replace cake with pasta"); intuitive AI image editor.
7. **NVIDIA Edify** — enterprise AI image/3D generator with clean quad topology, 4K PBR texture support, and customization via AI Foundry.
8. **Tripo AI** — text and image to 3D model in seconds; generates interactive 3D environments from single images and doodles.
9. **kohya_ss** — standard LoRA/DreamBooth training GUI for fine-tuning diffusion models on custom images; requires CUDA 11.8.
10. **StableDrag** — edit images by dragging content spatially rather than prompting; removes need for complex prompt engineering for spatial edits.
11. **World generation** — generating full 3D worlds from a single input image (panoramic world generation, backside anchor removal technique); framed as a step toward spatial intelligence.
12. **Ethical AI image generation** — artist collaboration models emerging alongside active copyright litigation (Getty vs Stable Diffusion).

## Methods / source structure

Notion database export with categorized entries across:
- Midjourney tutorials and technique guides (YouTube, articles)
- AI Image Tools & Platforms (product pages, GitHub repos)
- Prompting guides (Nano Banana multi-model patterns)
- Research (StableDrag, Omost compositional generation, world generation, Generating Worlds)
- ComfyUI tooling (Lucy Edit)

## Surprises / contradictions

- No contradictions with existing wiki pages detected.
- The "ethical AI image generation" angle (artist collaboration, Getty lawsuit) is notable: legal/IP infrastructure is a real gap in the current wiki's AI creative tools coverage.

## Connections

- Extends [[midjourney]] — techniques, tools, consistency methods
- Extends [[stability-ai]] — adds Stable Artisan (Discord interface) and Getty lawsuit context
- Extends [[ai-image-generation]] — top-level concept page
- New: [[flux]], [[nvidia-edify]], [[tripo-ai]], [[comfyui]]
- New: [[diffusion-model-fine-tuning]], [[ai-3d-generation]]
- Related: [[Synthesis/ai-creative-tools-overview]]

## Where it's cited

- [[midjourney]]
- [[stability-ai]]
- [[flux]]
- [[nvidia-edify]]
- [[tripo-ai]]
- [[comfyui]]
- [[ai-image-generation]]
- [[diffusion-model-fine-tuning]]
- [[ai-3d-generation]]
- [[Synthesis/ai-creative-tools-overview]]
