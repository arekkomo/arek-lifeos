---
title: "PiD 4-Step Upscale Workflow"
category: concept
summary: "Decision guide for using NVIDIA PiD's released 4-step decoder checkpoints: select a compatible VAE/backbone, describe the source image faithfully, choose the documented 4× checkpoint/target, and review for drift before delivery."
tags: [nvidia, pid, pixeldit, workflow, super-resolution, flux, 4k, quality-control]
sources: 3
updated: 2026-08-09
---

# PiD 4-Step Upscale Workflow

## Preflight

1. **Match the checkpoint to the backbone/VAE.** PiD is paired with compatible backbone encoders (such as FLUX, FLUX.2, SD3, SDXL, Qwen Image, or Z-Image); it is not documented as an arbitrary RGB upscaler.[[PiD-Official-Reference|PiD Official Reference]][1]
2. **Select the output band.** Use `2k` for 2K decoding or `2kto4k` / `2kto4k_v1pt5` when a 2K-to-4K target is needed. The public checkpoints described for these decoder variants are 4× upscalers.[[PiD-Official-Reference|PiD Official Reference]][2]
3. **Prepare a faithful caption.** Use the recipe in [[PiD-4-Step-Upscale-Prompting|PiD 4-Step Upscale Prompting]].
4. **Preserve the 4-step decoder default.** NVIDIA documents released distilled checkpoints as 4-step; changing the count needs workflow-specific testing, not a prompt change.[[PiD-Official-Reference|PiD Official Reference]][2]

## 2× versus 4× in a product wrapper

The public NVIDIA checkpoint table documents 4× decoder checkpoints, not a dedicated 2× PiD checkpoint.[[PiD-Official-Reference|PiD Official Reference]][2] A UI may offer a 2× export, but that is a **delivery-scale choice** unless its backend explicitly supplies a validated 2× PiD path.

- **4×:** direct use of a documented PiD 4× checkpoint/target; appropriate when the compatible latent and VRAM budget support it.
- **2×:** use only when the invoking workflow proves how it maps to PiD. It may be an intermediate target, resize after a 4× decode, or a separate implementation decision—not a claim about a released dedicated 2× checkpoint.

> ⚠️ Contradiction: a generic “2×/4× PiD upscaler” label can imply two native PiD scale models. NVIDIA's current checkpoint reference instead documents 4× (and one 8× SigLIP) decoder scales.[[PiD-Official-Reference|PiD Official Reference]][2]

## Review gate

Compare the output to the source at 100% before delivery:

- **Identity:** face, text, product geometry, and distinctive markings unchanged.
- **Composition:** crop, pose, object count, and perspective unchanged.
- **Texture:** inspect skin, hair, fabric, foliage, and gradients for hallucinated detail or tiling.
- **Typography/logos:** re-check manually; captions do not guarantee exact text reconstruction.
- **Semantics:** if a new object/style appears, shorten the caption and remove any non-visible adjectives before retrying.

## ComfyUI note

Current ComfyUI core support provides a PiD conditioning node that attaches a latent and `degrade_sigma` to **positive** conditioning. Confirm a workflow's loader/decode nodes and exact model files before promising end-to-end 2× or negative-prompt behavior.[[PiD-ComfyUI-Integration|PiD ComfyUI Integration]][4]

## Related

- [[PiD-Official-Reference|PiD Official Reference]]
- [[PiD-4-Step-Upscale-Prompting|PiD 4-Step Upscale Prompting]]
- [[PiD-ComfyUI-Integration|PiD ComfyUI Integration]]
- [[ComfyUI Compendium]]

## Sources

[1] NVIDIA, [PiD official repository](https://github.com/nv-tlabs/PiD).
[2] NVIDIA, [PiD checkpoint reference](https://github.com/nv-tlabs/PiD/blob/main/docs/checkpoints.md).
[4] ComfyUI, [PiD conditioning node](https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_pid.py).
