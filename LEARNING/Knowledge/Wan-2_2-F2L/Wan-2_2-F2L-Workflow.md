---
title: Wan 2.2 F2L Workflow
category: concept
summary: Native ComfyUI first-to-last-frame setup for Wan 2.2 I2V denoisers, with version-safe configuration boundaries.
tags: [wan-2.2, flf2v, first-last-frame, comfyui, i2v]
sources: 3
updated: 2026-08-09
---

# Wan 2.2 F2L Workflow

> Source ledger: [[Wan 2.2 F2L Sources]].

## What the workflow does

The native ComfyUI workflow bridges a supplied `start_image` and `end_image` with `WanFirstLastFrameToVideo`; one positive prompt and one negative prompt condition the whole generated interval. [1][3] The official guide says to define the two endpoints, adjust the node size, and write the prompt according to both frames. [1]

## Canonical graph

1. Load **two endpoint images**: first into `start_image`, second into `end_image`.
2. Load **both** `wan2.2_i2v_high_noise_14B_fp8_scaled` and `wan2.2_i2v_low_noise_14B_fp8_scaled`; each receives its own sampling-shift node in the official template. [3]
3. Encode one positive and one negative text condition, then connect these, VAE and the two images to `WanFirstLastFrameToVideo`. [3]
4. Sample, decode, then encode frames to video. The template’s default output rate is 16 fps. [3]

The downloadable official template defaults to 640×640 and 81 frames; its guide characterizes that as a low-VRAM starting size and suggests around 720P when VRAM permits. [1][3]

## Do not conflate these paths

- **Wan2.2 I2V**: official upstream I2V-A14B release; one-image I2V is the directly named upstream task. [2]
- **Wan2.2 F2L in ComfyUI**: first+last frame workflow that uses those Wan2.2 I2V denoisers via the native F2L latent node. [1][3]
- **Wan2.1-FLF2V**: an earlier separately named Diffusers pipeline/checkpoint path with `image` and `last_image`; it is useful as a behavioral precedent, but not a license to substitute model files in the Wan2.2 ComfyUI workflow. [4]

> ⚠️ Contradiction: Some references call endpoint video generation “Wan FLF2V” without naming a version. For reproducibility, record the exact workflow and model files: native ComfyUI `WanFirstLastFrameToVideo` plus the two `wan2.2_i2v_*_14B` denoisers. [[Wan 2.2 F2L Sources]]

## Related pages

- [[Wan 2.2 F2L Prompting]]
- [[Wan 2.2 F2L Endpoint Design]]
- [[ComfyUI Compendium]]
- [[Wan 2.1]]
