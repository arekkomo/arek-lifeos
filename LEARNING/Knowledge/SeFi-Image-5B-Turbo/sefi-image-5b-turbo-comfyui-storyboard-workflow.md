---
title: "SeFi-Image 5B Turbo — ComfyUI Storyboard Workflow"
category: concept
summary: "Evidence-bounded ComfyUI workflow notes for generating and recording SeFi-Image 5B Turbo storyboard stills."
tags: [sefi-image, comfyui, storyboard, t2i, turbo, workflow]
sources: 2
updated: 2026-08-09
---

# SeFi-Image 5B Turbo — ComfyUI Storyboard Workflow

A community node pack supports SeFi-Image 5B Base and Turbo in ComfyUI, with the transformer, Qwen3-VL text encoder, and SeFi VAE supplied as separate files.[4] It states that the SeFi VAE is required rather than a generic FLUX.2 VAE, and its sampler exposes prompt, steps, guidance, size, and seed.[4]

## Minimal graph intent

`SeFi Loader → SeFi Sampler → Save Image`

Use the Turbo model family, the matching SeFi VAE, and the matching text encoder. Set the sampler to 4 steps and guidance 1.0 for the first board pass—the same baseline documented by the official inference repository.[1]

## Board-pass workflow

1. Lock an aspect ratio and create a shot list using [[SeFi-Image 5B Turbo — Storyboard Still Prompt Grammar]].
2. Run 4-step Turbo prompt variants while recording seed, dimensions, prompt revision, and selected frame.
3. For chosen frames, reuse the seed and raise only steps to 8 or 10 if the comparison is useful.
4. Save selected stills with shot identifiers (for example, `S03_SH04_master_seed-1234.png`) and retain the prompt record beside them.
5. Convert selected images into the continuity packet in [[AI Video Scene Packet]] before moving them into I2V tests.

## Boundaries and risks

The ComfyUI node is community-maintained, so treat its VRAM, timing, and offload notes as environment-specific—not model-team guarantees.[4] The official repository describes the released model as research use rather than direct product/service deployment; model weights may have a separate license, so verify both before commercial use.[1]

> ⚠️ Contradiction: The official repository's code is MIT licensed, while a project issue and the community node documentation identify the released weights as CC BY-NC 4.0. The code license does not establish commercial rights for the weights.[1][4]

## Sources

[1] https://github.com/jmliu206/SeFi-Image — SeFi-Image official inference repository
[4] https://github.com/RealRebelAI/ComfyUI_Rebels_SeFi — ComfyUI Rebels SeFi custom node
