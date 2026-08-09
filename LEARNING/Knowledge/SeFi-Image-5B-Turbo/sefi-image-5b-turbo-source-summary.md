---
title: "SeFi-Image 5B Turbo — Source Summary"
category: source
summary: "Verified source ledger for SeFi-Image 5B Turbo prompting, sampling limits, architecture, and ComfyUI integration."
tags: [sefi-image, text-to-image, turbo, prompting, storyboard, source]
sources: 4
updated: 2026-08-09
source_path: "https://github.com/jmliu206/SeFi-Image"
source_date: 2026-06
authors: [Ruoyu Feng, Jinming Liu, Yuqi Wang, Xin Cheng, Boyuan Liu, Shanglin Li, Hanshen Zhu, Wenfeng Lin, Mingyu Guo, Xin Jin]
ingested: 2026-08-09
---

# SeFi-Image 5B Turbo — Source Summary

## What is confirmed

SeFi-Image is a text-to-image family built on semantic-first diffusion: semantic and texture latent streams are denoised at staggered times, with the semantic stream intended to establish structure before texture detail.[1][2] The 5B Turbo checkpoint is the few-step variant intended for rapid generation.[1][2]

The official inference repository specifies the 5B Turbo checkpoint, a default of four denoising steps, and guidance scale 1.0. Its runtime accepts only 4, 8, or 10 Turbo steps and rejects a guidance scale other than 1.0.[1] Output defaults to 1024×1024; height, width, seed, image count, and prompt-file batching are exposed by the CLI.[1]

## Prompting evidence boundary

The official README supplies short natural-language prompts (for example, an object, surface, and setting) and runtime controls, but it does **not** publish a model-specific prompt grammar, token limit, negative-prompt recipe, or validated keyword/style-weight syntax.[1] The storyboard prompt structure in [[SeFi-Image 5B Turbo — Storyboard Still Prompt Grammar]] is therefore an operational convention for controllable stills, not an official SeFi claim.

## Implementation and ecosystem notes

A Diffusers contribution describes Qwen3-VL prompt encoding, SeFi dual-time denoising, Turbo step validation, and CPU offload; treat it as an implementation-status source rather than the model team's prompt guidance.[3] A community ComfyUI node pack documents Base/Turbo loading, its own sampler defaults, and a model-specific VAE requirement. It is useful operational evidence, not official prompting guidance.[4]

## Sources

[1] https://github.com/jmliu206/SeFi-Image — SeFi-Image official inference repository
[2] https://arxiv.org/abs/2606.22568 — SeFi-Image technical report
[3] https://github.com/huggingface/diffusers/pull/14084 — Diffusers SeFi-Image pipeline PR
[4] https://github.com/RealRebelAI/ComfyUI_Rebels_SeFi — ComfyUI Rebels SeFi custom node
