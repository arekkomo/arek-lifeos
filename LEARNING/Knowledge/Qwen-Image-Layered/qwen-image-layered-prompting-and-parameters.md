---
title: Qwen-Image-Layered Prompting and Parameters
category: concept
summary: Prompt and parameter contract for Qwen-Image-Layered, separating supported decomposition prompting from limited text-to-layered-image use.
tags: [qwen-image-layered, prompting, negative-prompt, rgba, diffusers]
sources: 3
updated: 2026-08-09
---

# Qwen-Image-Layered Prompting and Parameters

## Prompt contract
For image decomposition, write one concise caption of the **entire intended composite**: subject(s), setting, salient objects, visible text, and meaningful occluded content. This is the supported use of the text condition; do not phrase it as a numbered list of desired layer contents, because Qwen explicitly says the prompt is not intended to control individual layers.[[qwen-image-layered-source]]

**Reliable decomposition prompt shape:**
`[overall scene and style]. [foreground subject/object], [midground objects], [background/environment]. [Visible or occluded text that must be understood].`

Use only facts that are present in, or intentionally clarify, the input image. A detail prompt can help the automatic captioning route, but it cannot guarantee a particular semantic allocation across RGBA outputs.[[qwen-image-layered-source]]

## `negativePrompt` / `negative_prompt`
The official Diffusers example exposes `negative_prompt` and passes a single blank space. The official README provides no Qwen-specific negative-prompt vocabulary or evidence that long exclusion lists improve layer assignment; therefore the safe baseline is blank/neutral unless a tested host workflow establishes its own behavior.[[qwen-image-layered-source]]

Use `negativePrompt` only as a conservative quality exclusion field, for example: `watermark, UI text, duplicated subject, unwanted border`. Do **not** use it as the primary mechanism for saying “put X on layer 2”; that is outside the documented prompt contract.[[qwen-image-layered-source]]

## Parameter baseline
| Parameter | Starting value | Why |
|---|---:|---|
| `layers` | 3–5 | The model supports variable counts; start with the fewest independently editable elements needed, then recursively decompose a layer if necessary.[[qwen-image-layered-source]] |
| `resolution` | 640 | Qwen recommends the 640 bucket for this release; 1024 is also named as a bucket option.[[qwen-image-layered-source]] |
| `true_cfg_scale` | 4.0 | Official example baseline.[[qwen-image-layered-source]] |
| `num_inference_steps` | 50 | Official example baseline.[[qwen-image-layered-source]] |
| `cfg_normalize` | enabled | Official example baseline.[[qwen-image-layered-source]] |
| `use_en_prompt` | enabled when no caption is supplied | Official automatic-caption option.[[qwen-image-layered-source]] |

## Text-to-layered-image mode: experimental
The paper describes a text-to-multi-RGBA training stage, but Qwen’s released-weights README says the release is fine-tuned specifically for image-to-multi-RGBA and that text-to-multi-RGBA performance is limited. Treat t2i layered generation as an exploratory option, not a production promise.[[qwen-image-layered-source]]

For an exploratory t2i prompt, describe the final composited scene rather than trying to dictate exact per-layer membership. Inspect the result, then use normal RGBA editing or re-decomposition to obtain a usable layer structure.[[qwen-image-layered-source]]

Related: [[layer-decomposition-and-edit-workflow]] · [[qwen-image-layered-production-guardrails]]
