---
title: "PiD ComfyUI Integration"
category: note
summary: "Current ComfyUI core PiD conditioning attaches positive conditioning, a latent, and degrade_sigma; negative conditioning is not exposed by the core PiD conditioning node."
tags: [comfyui, nvidia, pid, pixeldit, conditioning, workflows, negative-prompt]
sources: 2
updated: 2026-08-09
---

# PiD ComfyUI Integration

ComfyUI's current core `PiDConditioning` node is registered under `model/conditioning`. Its stated function is to attach a latent and a `degrade_sigma` scalar to a conditioning object for PiD decoding/upscaling.[4]

## Inputs verified in core

| Input | Role |
|---|---|
| `positive` | The text conditioning passed into PiD conditioning.[4] |
| `latent` | A latent from `VAEEncode` or a `KSampler`.[4] |
| `degrade_sigma` | Scalar controlling the degradation/noise value attached for PiD decoding.[4] |

The current node schema does not expose a `negative` conditioning input.[4] This aligns with NVIDIA's clean-image reference interface, which requires a caption but does not define a negative-prompt flag.[[PiD-Official-Reference|PiD Official Reference]][3]

## Implication for `pid-upscale`

A downstream skill or product schema may accept `negativePrompt`, but it must distinguish two cases:

- **Supported wrapper:** the specific surrounding pipeline has a documented negative-conditioning control; forward the field using that pipeline's contract.
- **Core PiD path:** retain the field as optional metadata or omit it from execution; do not wire it into `PiDConditioning` as if the core node accepted it.

This is a capability boundary, not an argument against keeping a UX-level negative prompt field. It avoids promising a parameter that the underlying official node does not declare.

## Related

- [[PiD-4-Step-Upscale-Prompting|PiD 4-Step Upscale Prompting]]
- [[PiD-4-Step-Upscale-Workflow|PiD 4-Step Upscale Workflow]]
- [[PiD-Official-Reference|PiD Official Reference]]
- [[ComfyUI Compendium]]

## Sources

[3] NVIDIA, [`from_clean` inference implementation](https://github.com/nv-tlabs/PiD/blob/main/pid/_src/inference/from_clean.py).
[4] ComfyUI, [PiD conditioning node](https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_pid.py).
