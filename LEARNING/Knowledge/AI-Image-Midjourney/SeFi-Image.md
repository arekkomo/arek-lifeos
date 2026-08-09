---
title: "SeFi-Image — Semantic-First Image Diffusion"
category: entity
summary: Text-to-image model family (1B/2B/5B, Base+Turbo variants) that separates semantic and texture latent streams, denoising semantic structure slightly ahead of texture for cleaner structural anchors.
tags: [text-to-image, diffusion, dual-stream, semantic-first, turbo-inference, ai-image]
sources: 2
updated: 2026-08-09
---

# SeFi-Image — Semantic-First Image Diffusion

## Overview

SeFi-Image is a text-to-image model family built on **Semantic-First Diffusion** — it separates image representation into two decoupled latent streams and denoises the semantic structure slightly ahead of texture details. This gives the texture stream a cleaner structural anchor during generation, reducing the common failure mode where fine textures appear before coherent composition is established.

## Architecture

### Dual-Stream Design

Standard diffusion models jointly denoise all latents simultaneously. SeFi-Image splits this:

1. **Semantic latent stream** — captures high-level structure, object placement, spatial relationships. Denoised first to provide a clean scaffold.
2. **Texture latent stream** — captures material appearance, fine detail, color. Receives its guidance from the already-cleaned semantic stream.

This separation means texture generation doesn't have to compete with structural convergence — it can focus on quality details once composition is stable.

## Model Zoo

| Family | Model | Size | Default Steps | Guidance Scale | Use Case |
|--------|-------|------|--------------|----------------|----------|
| Base | SeFi-Image-1B-Base | 1B params | 50 | 4.0 | Standard T2I, fast |
| Base | SeFi-Image-2B-Base | 2B params | 50 | 4.0 | Balanced quality/speed |
| Base | SeFi-Image-5B-Base | 5B params | 50 | 4.0 | Highest fidelity |
| RL | SeFi-Image-5B-RL | 5B params | 50 | 4.0 | Reward-aligned, likely style-tuned |
| Turbo | SeFi-Image-1B-Turbo | 1B params | 4 | 1.0 | Ultra-fast generation at ~2.5s |
| Turbo | SeFi-Image-2B-Turbo | 4-step model | 4 | 1.0 | Medium-speed, better quality |
| Turbo | SeFi-Image-5B-Turbo | 5B params | 4 | 1.0 | Best speed/fidelity balance |

## Key Design Decisions

- **Training efficiency**: The 5B model reaches strong benchmark performance with ~125K A800 GPU hours — competitive for a dual-stream architecture
- **Turbo variant**: 4-step generation at guidance scale 1.0 enables interactive use (storyboarding, rapid prototyping)
- **Compositional benefit**: Semantic-first design is particularly advantageous for complex prompts with multiple objects/specific layouts

## Connections

- Complementary to [[LongForcing]] thinking: both emphasize structural coherence before detail refinement
- Turbo variants (4-step) compete with Wan2.2-Lightning's acceleration approach but in the image domain
- [[SeFi-Image 5B Turbo — Source Summary]] distinguishes verified runtime facts from working prompt practice.
- [[SeFi-Image 5B Turbo — Prompting Guide]] and [[SeFi-Image 5B Turbo — Storyboard Still Prompt Grammar]] translate Turbo use into repeatable storyboard-still prompts.
