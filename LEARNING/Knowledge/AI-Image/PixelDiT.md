---
title: "PixelDiT — NVIDIA Pixel-Space Text-to-Image DiT"
category: entity
summary: NVIDIA 1.3B text-to-image PixelDiT model with native ComfyUI core support since merged PR #14103; distributed through Comfy-Org under the NSCLv1 model license.
tags: [pixeldit, text-to-image, diffusion-transformer, comfyui-core, nvidia, pixel-space]
sources: 2
updated: 2026-07-19
---

# PixelDiT — NVIDIA Pixel-Space Text-to-Image DiT

**Model:** [nvidia/PixelDiT-1300M-1024px](https://huggingface.co/nvidia/PixelDiT-1300M-1024px) · **ComfyUI weights:** [Comfy-Org/PixelDiT](https://huggingface.co/Comfy-Org/PixelDiT)

## Library status

ComfyUI PR [#14103](https://github.com/Comfy-Org/ComfyUI/pull/14103), by Kijai, was merged June 4, 2026. It adds **core** (not custom-node) PixelDiT support alongside PiD support.

## What to remember

- PixelDiT is an NVIDIA text-to-image diffusion transformer, released at 1.3B parameters for 1024px image generation.
- Core integration means model detection, text encoding, loading, and relevant latent/model paths are part of ComfyUI itself.
- The model is **not Apache/MIT**: PR documentation identifies the model weights as **NSCLv1**. Review that license before any commercial use.

## Related

- [[PiD]] — the companion NVIDIA diffusion decoder; ComfyUI core support landed in the same PR
- [[ComfyUI Compendium]] — local installation/status reference
- [[Lucida]] — downstream alpha-matte extraction for generated images
