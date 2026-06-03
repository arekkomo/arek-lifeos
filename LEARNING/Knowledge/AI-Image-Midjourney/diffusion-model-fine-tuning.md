---
title: Diffusion Model Fine-Tuning
category: concept
summary: Adapting pre-trained diffusion models (Stable Diffusion) to specific characters, objects, or styles using LoRA, DreamBooth, and similar methods; kohya_ss is the standard GUI.
tags: [diffusion-models, lora, dreambooth, fine-tuning, kohya, stable-diffusion, ai-images]
sources: 1
updated: 2026-04-19
---

# Diffusion Model Fine-Tuning

## Definition

Adapting a pre-trained diffusion model (typically Stable Diffusion) to generate images of a specific subject, style, or character by training on a small custom dataset. Fine-tuning is the primary method for achieving **consistent characters, product shots, or brand aesthetics** that base models cannot produce reliably from prompts alone.

## Key methods

### LoRA (Low-Rank Adaptation)
Trains a small adapter on top of the frozen base model rather than modifying all weights. Fast to train, small file size (~50-200MB), composable (multiple LoRAs can stack). The dominant approach for community fine-tunes.

### DreamBooth
Fine-tunes the full model (or a subset of weights) on 5-30 images of a subject. Higher quality than LoRA for precise subject fidelity, but slower to train and larger output files.

### Textual Inversion
Trains only a new text embedding ("token") while keeping model weights frozen. Lightest approach; useful for style rather than identity.

## Tooling

### kohya_ss
Standard GUI for LoRA and DreamBooth training on custom images.
- GitHub: bmaltais/kohya_ss
- **Requires: CUDA 11.8 toolkit** — GPU dependency, Linux/Windows only
- Supports SD 1.x, SD 2.x, SDXL
- Source: [[notion-export-ai-image-midjourney]]

### ComfyUI
After training, LoRA models are loaded into [[comfyui]] for inference. ComfyUI supports composing multiple LoRAs and ControlNet conditioning.

## Typical workflow

1. Collect 10-30 images of subject (consistent lighting, varied angles)
2. Caption images (BLIP2 or manual)
3. Train LoRA with kohya_ss (~30-60 min on RTX 3090)
4. Load LoRA in ComfyUI or Automatic1111
5. Prompt with the trigger token

## Open questions

- How many images are needed for reliable face/character consistency?
- Does SDXL-based LoRA outperform SD 1.5 LoRA for character work?
- Can LoRA fine-tunes be used with Flux effectively?

## Used in

- [[comfyui]]
- [[stability-ai]]
- [[ai-image-generation]]

## Key claims from sources

- kohya_ss requires CUDA 11.8 toolkit — [[notion-export-ai-image-midjourney]]
- LoRA/DreamBooth enables fine-tuning diffusion models on custom images — [[notion-export-ai-image-midjourney]]
