---
title: Qwen Image Edit 2511 — Source Summary
category: source
summary: Primary-source digest for Qwen Image Edit 2511, its official edit-prompt enhancer, and Diffusers pipeline behavior.
tags: [qwen-image-edit, image-editing, prompting, diffusers, source]
sources: 4
updated: 2026-08-09
source_path: external/official-qwen-image-edit-2511
source_date: 2025-12
authors: [Qwen Team, Hugging Face]
ingested: 2026-08-09
---

# Qwen Image Edit 2511 — Source Summary

## What the release changes
Qwen Image Edit 2511 is the December 2025 edit-model release, positioned as an improvement over 2509 for reduced image drift, character consistency, integrated community-LoRA capabilities, industrial-design work, and geometric reasoning.[5] The official examples cover portrait identity preservation, multi-person fusion from separate images, lighting, viewpoint changes, material replacement, and construction-line generation.[5]

## What is authoritative for prompting
The strongest usable prompting guidance is Qwen's own `polish_edit_prompt` system prompt. It says an edit instruction should be direct and specific, preserve the user's core intent, make only visually feasible additions, and keep additions consistent with the source image's scene logic and style.[8] Its task-specific rules are distilled in [[Qwen Image Edit 2511 Edit Instructions]].

## Runtime facts that matter to prompts
The release uses `QwenImageEditPlusPipeline`, accepts a list of input images, and its official quick start uses 40 inference steps, `true_cfg_scale: 4.0`, `guidance_scale: 1.0`, and a blank negative prompt.[5] In current Diffusers documentation, `guidance_scale` is ineffective for ordinary Qwen pipelines; CFG is instead activated with `true_cfg_scale` plus a negative prompt, including a blank one.[9]

## Limits of this knowledge base
There is no separate official prose “prompting guide” for 2511 beyond examples and the upstream edit-prompt enhancer. The templates in this folder are therefore operational distillations of Qwen's enhancer rules, not claims about a hidden model syntax.

## Related pages
- [[Qwen Image Edit 2511 Edit Instructions]]
- [[Qwen Image Edit 2511 Task Patterns]]
- [[Qwen Image Edit 2511 Multi-Image and Identity]]
- [[Qwen Image Edit 2511 Validation and Recovery]]

## Sources
[4] https://github.com/QwenLM/Qwen-Image
[5] https://huggingface.co/Qwen/Qwen-Image-Edit-2511
[8] https://github.com/QwenLM/Qwen-Image/blob/main/src/examples/tools/prompt_utils.py
[9] https://huggingface.co/docs/diffusers/api/pipelines/qwenimage
