---
title: Z-Image Official Source Summary
category: source
summary: Primary-source record for Tongyi-MAI’s Z-Image family, its documented T2I parameters and Diffusers API.
tags: [z-image, text-to-image, prompting, diffusion, source]
sources: 4
updated: 2026-08-09
source_path: https://github.com/Tongyi-MAI/Z-Image
source_date: 2025-11
authors: [Z-Image Team, Tongyi-MAI]
ingested: 2026-08-09
---

# Z-Image Official Source Summary

## Source set

1. **Tongyi-MAI Z-Image repository** — canonical model-family description, variant table, prompt examples, and recommended base-model parameters. [GitHub](https://github.com/Tongyi-MAI/Z-Image)
2. **Tongyi-MAI/Z-Image-Turbo model card** — Turbo checkpoint, its eight-forward inference example, and documented zero-CFG setting. [Hugging Face](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)
3. **Z-Image technical report** — model-family research record. [arXiv:2511.22699](https://arxiv.org/abs/2511.22699)
4. **Hugging Face Diffusers Z-Image API** — current pipeline inputs including prompt, negative prompt, dimensions, steps, CFG controls, seed generator and maximum sequence length. [Documentation](https://huggingface.co/docs/diffusers/api/pipelines/z_image)

## Confirmed operating facts

- Z-Image is a 6B-parameter model family; the standard **Z-Image** checkpoint is the controllable, higher-diversity option, while **Z-Image-Turbo** is a distilled eight-forward T2I checkpoint. [1][2]
- The official examples use plain natural-language, attribute-rich descriptive prompts rather than a special tag grammar. [1][2]
- For standard Z-Image, Tongyi-MAI recommends 512–2048 px total dimensions, 28–50 steps, CFG 3–5, and says negative prompts are strongly recommended; CFG normalization is documented as `False` for general stylism and `True` for realism. [1]
- For Z-Image-Turbo, the official example uses nine scheduler steps (eight DiT forwards) and `guidance_scale=0.0`; the model table marks Turbo as no-CFG. [1][2]
- Diffusers exposes both `negative_prompt` and seed-generator inputs for the standard pipeline, so negative-control experiments and repeatable boards are supported at the API level. [4]

## Evidence boundary

No primary source found in this research set specifies a proprietary word order, token weighting syntax, or a model-specific storyboard prompt formula. The reusable prompt structures in [[Z-Image T2I Prompting]] and [[Z-Image Storyboard Stills]] are therefore production heuristics: they combine the official descriptive examples and documented controls with the vault’s directing workflow, rather than presenting community convention as official model behavior.

## Related pages

- [[Z-Image]]
- [[Z-Image T2I Prompting]]
- [[Z-Image Generation Settings]]
- [[Z-Image Storyboard Stills]]
