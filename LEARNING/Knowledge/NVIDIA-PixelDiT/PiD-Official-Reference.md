---
title: "NVIDIA PiD — Official Technical Reference"
category: source
summary: "Verified reference for NVIDIA's PiD pixel diffusion decoder: its compatible backbones, 4-step distilled checkpoints, decode targets, and official inference interfaces."
tags: [nvidia, pid, pixeldit, pixel-diffusion-decoder, super-resolution, flux, image-upscaling]
sources: 4
updated: 2026-08-09
source_path: "https://github.com/nv-tlabs/PiD"
source_date: 2026-08
authors: [NVIDIA]
ingested: 2026-08-09
---

# NVIDIA PiD — Official Technical Reference

[[nv-tlabs-pid|PiD]] (Pixel Diffusion Decoder) is NVIDIA's decoder for turning a compatible model latent into a high-resolution pixel image. It is a decoder/upscaler stage, not a generic pixel-image upscaler: the official `from_clean` path first encodes an input through the compatible backbone's VAE, then asks PiD to decode that latent at the requested target size.[1][3]

## What the released checkpoints support

- NVIDIA's released distilled PiD checkpoints are **4-step** checkpoints.[2]
- The FLUX, FLUX.2, SD3, SDXL, Qwen Image, Z-Image, and DINOv2 variants are documented as **4×** upscalers; the SigLIP variant is documented as 8×.[2]
- `2k` checkpoints decode at 2K resolution; `2kto4k` / `2kto4k_v1pt5` checkpoints target the 2K-to-4K range. The v1.5 2K-to-4K variants are the current official option for FLUX, FLUX.2, Qwen Image (WAN2.1 VAE), Z-Image, and related compatible backbones.[1][2]
- PiD's 4-step count is the **decoder** sampling count. Do not confuse it with the source image-generation model's denoising steps.[1]

## Prompting implication

PiD requires a text caption for its batch. In NVIDIA's clean-image interface, that caption comes from the per-image manifest `prompt` field or the global `--prompt`; the program errors when neither is supplied.[3] The practical prompting guidance and interface caveat are maintained in [[PiD-4-Step-Upscale-Prompting|PiD 4-Step Upscale Prompting]].

## Related

- [[PiD-4-Step-Upscale-Prompting|PiD 4-Step Upscale Prompting]] — production prompt contract for 2×/4× wrappers
- [[PiD-4-Step-Upscale-Workflow|PiD 4-Step Upscale Workflow]] — checkpoint, scale, and review decisions
- [[PiD-ComfyUI-Integration|PiD ComfyUI Integration]] — current core-conditioning constraints
- [[PixelDiT]] — companion NVIDIA pixel-space DiT in the existing AI Image library
- [[ComfyUI Compendium]] — native PiD/PixelDiT support record

## Sources

[1] NVIDIA, [PiD official repository](https://github.com/nv-tlabs/PiD).
[2] NVIDIA, [PiD checkpoint reference](https://github.com/nv-tlabs/PiD/blob/main/docs/checkpoints.md).
[3] NVIDIA, [`from_clean` inference implementation](https://github.com/nv-tlabs/PiD/blob/main/pid/_src/inference/from_clean.py).
[4] ComfyUI, [PiD conditioning node](https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_pid.py).
