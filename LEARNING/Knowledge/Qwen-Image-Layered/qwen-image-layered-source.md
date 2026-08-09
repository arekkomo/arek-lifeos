---
title: Qwen-Image-Layered — Source Summary
category: source
summary: Primary-source reference for Qwen’s RGBA-layer decomposition model, its supported parameters, production workflow, and current limits.
tags: [qwen-image-layered, rgba, layer-decomposition, image-editing, comfyui]
sources: 4
updated: 2026-08-09
source_path: https://github.com/QwenLM/Qwen-Image-Layered
source_date: 2025-12
authors: [Shengming Yin, Zekai Zhang, Zecheng Tang, Kaiyuan Gao, Xiao Xu, Kun Yan, Jiahao Li, Yilei Chen, Yuxiang Chen, Heung-Yeung Shum, Lionel M. Ni, Jingren Zhou, Junyang Lin, Chenfei Wu]
ingested: 2026-08-09
---

# Qwen-Image-Layered — Source Summary

## What it is
Qwen-Image-Layered is an Apache-2.0 Qwen model that decomposes one RGB/RGBA input into a variable number of semantically disentangled RGBA layers, enabling downstream edits to a selected layer without regenerating the whole flattened image.[[qwen-image-layered-source#Sources]]

## Official operating facts
- The release is specifically fine-tuned for **image-to-multi-RGBA decomposition**; it accepts a text condition, but its text-to-multi-RGBA generation quality is explicitly described by Qwen as limited.[[qwen-image-layered-source#Sources]]
- In the official Diffusers example, the decomposition defaults are a supplied RGBA image, `layers=4`, `resolution=640`, `true_cfg_scale=4.0`, 50 steps, `cfg_normalize=True`, `use_en_prompt=True`, and a blank `negative_prompt`.[[qwen-image-layered-source#Sources]]
- The text condition describes the **complete input composition**, including content occluded by foreground objects; Qwen states that it is not a per-layer semantic-control language.[[qwen-image-layered-source#Sources]]
- Qwen documents flexible layer counts and recursive decomposition; the research system was trained with a maximum of 20 layers, while a practical first pass should request only the separations that are useful for a planned edit.[[qwen-image-layered-source]]

## Operational map
1. Use [[layer-decomposition-and-edit-workflow]] for supplied-image decomposition and post-decomposition edits.
2. Use [[qwen-image-layered-prompting-and-parameters]] for the prompt, `negativePrompt`, layer-count, and generation-mode guardrails.
3. Use [[qwen-image-layered-comfyui-output-handling]] when running the current ComfyUI workflow: discard the regenerated input slot before treating outputs as editable layers.
4. Use [[qwen-image-layered-production-guardrails]] for scope, verification, and quality limits.

## Sources
1. [QwenLM/Qwen-Image-Layered README](https://github.com/QwenLM/Qwen-Image-Layered) — official usage, prompt note, parameter example, layer editing/compositing workflow, release date, and license.
2. [Qwen/Qwen-Image-Layered model card](https://huggingface.co/Qwen/Qwen-Image-Layered) — official model distribution and matching Diffusers example.
3. [Yin et al., “Qwen-Image-Layered: Towards Inherent Editability via Layer Decomposition” (arXiv:2512.15603)](https://arxiv.org/abs/2512.15603) — model design, variable-layer capability, training maximum, and edit rationale.
4. [Comfy-Org workflow_templates PR #1092](https://github.com/Comfy-Org/workflow_templates/pull/1092) — merged template correction for the regenerated-input output slot.
