---
title: "PiD 4-Step Upscale Prompting"
category: concept
summary: "A prompt contract for PiD 4-step upscale/edit workflows: use a concise faithful caption of visible content, preserve scene identity, and treat negativePrompt as wrapper-level control rather than an official PiD requirement."
tags: [nvidia, pid, pixeldit, prompting, upscaling, image-editing, negative-prompt, comfyui]
sources: 4
updated: 2026-08-09
---

# PiD 4-Step Upscale Prompting

## Core rule

For PiD upscale/edit runs, write the **positive prompt as a concise, faithful description of the supplied image**. Name the subject, essential action/pose, setting, lighting, and only the visual qualities that are already materially present. PiD consumes a required caption alongside the image/latent; it is not documented as a text-to-image redesign pass.[[PiD-Official-Reference|PiD Official Reference]][3]

**Good:** `Close portrait of a woman in a black leather jacket, looking into camera, soft window light, shallow depth of field.`

**Too generative:** `A glamorous cyberpunk queen in a neon future city, intricate chrome costume, dramatic rain, cinematic masterpiece.`

The second prompt introduces a new identity, costume, setting, and mood that may compete with the image being decoded. Treat the caption as an **identity-and-content anchor**, not a chance to add embellishment.

## Positive prompt recipe

Use one sentence or two short clauses:

1. **Subject and count:** who/what is visible.
2. **Defining attributes:** only stable, salient features (wardrobe, material, colour, age class, species).
3. **Pose/action and composition:** only if visually clear.
4. **Environment and lighting:** only if they materially define the shot.
5. **Existing finish:** e.g. `photograph`, `soft film grain`, or `clean product render`—never a requested replacement style.

Prefer concrete nouns over adjective piles. If an attribute is uncertain or absent in the source, omit it. Keep text density low enough that the image remains the primary instruction.

## `negativePrompt` contract

The requested `negativePrompt` should be kept as a **short defect-suppression list** in a wrapper/UI contract, for example: `blurry, low resolution, jpeg artifacts, distorted face, extra fingers, text, watermark`.

> ⚠️ Implementation distinction: NVIDIA's public PiD clean-image interface exposes a required positive caption and CFG scale, but its documented command and current implementation do **not** expose a negative-prompt argument.[[PiD-Official-Reference|PiD Official Reference]][3] Current ComfyUI core PiD conditioning similarly accepts `positive`, a latent, and `degrade_sigma`, not negative conditioning.[[PiD-ComfyUI-Integration|PiD ComfyUI Integration]][4]

Therefore, a `negativePrompt` field in `pid-upscale` should be passed only where the actual surrounding workflow supports it. Do not represent it as an official PiD checkpoint control without validating the target node/API.

## Recommended defaults

| Field | Default | Why |
|---|---|---|
| Positive prompt | One concise faithful caption | Meets PiD's required-caption contract while minimizing semantic drift.[[PiD-Official-Reference|PiD Official Reference]][3] |
| `negativePrompt` | Short, defect-oriented list | Useful wrapper-level hygiene; not verified as an official PiD input.[[PiD-ComfyUI-Integration|PiD ComfyUI Integration]][4] |
| PiD inference steps | `4` | Matches NVIDIA's released distilled checkpoints.[[PiD-Official-Reference|PiD Official Reference]][2] |
| CFG | `1` unless the specific wrapper documents otherwise | NVIDIA's clean-image example uses `--cfg_scale 1`.[[PiD-Official-Reference|PiD Official Reference]][1] |

## Prompt examples

| Source image | Positive prompt | `negativePrompt` |
|---|---|---|
| Beauty close-up | `Close beauty portrait of a woman with long dark hair, neutral expression, soft studio key light, shallow depth of field.` | `blurry, low resolution, distorted face, extra fingers, text, watermark` |
| Product still | `Matte black running shoe on a pale concrete pedestal, side view, soft daylight, clean product photography.` | `blurry, warped product, duplicate object, text, logo distortion, watermark` |
| Landscape | `Wide mountain lake at sunrise, pine forest and reflected orange sky, natural atmospheric haze.` | `blurry, oversharpened, banding, artifacts, text, watermark` |

## Related

- [[PiD-Official-Reference|PiD Official Reference]]
- [[PiD-4-Step-Upscale-Workflow|PiD 4-Step Upscale Workflow]]
- [[PiD-ComfyUI-Integration|PiD ComfyUI Integration]]
- [[PixelDiT]]

## Sources

[1] NVIDIA, [PiD official repository](https://github.com/nv-tlabs/PiD).
[2] NVIDIA, [PiD checkpoint reference](https://github.com/nv-tlabs/PiD/blob/main/docs/checkpoints.md).
[3] NVIDIA, [`from_clean` inference implementation](https://github.com/nv-tlabs/PiD/blob/main/pid/_src/inference/from_clean.py).
[4] ComfyUI, [PiD conditioning node](https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_pid.py).
