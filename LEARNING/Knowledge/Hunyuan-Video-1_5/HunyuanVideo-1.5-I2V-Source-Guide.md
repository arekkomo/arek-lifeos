---
title: HunyuanVideo 1.5 I2V — Official Source Guide
category: source
summary: Primary-source map for HunyuanVideo 1.5 image-to-video prompting, rewriting, ComfyUI use, and model capabilities.
tags: [hunyuanvideo-1.5, i2v, prompting, ai-video, source]
sources: 5
updated: 2026-08-09
source_path: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5
source_date: 2025-11
authors: [Tencent Hunyuan]
ingested: 2026-08-09
---

# HunyuanVideo 1.5 I2V — Official Source Guide

## Primary sources

- [Official repository](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5) — model releases, I2V inference, prompt-rewrite integration, and ComfyUI entry points.
- [Official Prompt Handbook](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/assets/HunyuanVideo_1_5_Prompt_Handbook_EN.md) — the authoritative I2V prompt formula, examples, camera vocabulary, style, and lighting controls.
- [Official I2V rewrite prompt](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/hyvideo/utils/rewrite/i2v_prompt.py) — the operational specification for turning a short intent plus reference image into a detailed motion description.
- [Official ComfyUI guide](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/ComfyUI/README.md) — templates and the supported I2V inference configurations.
- [Technical report](https://arxiv.org/abs/2511.18870) — model context: 8.3B parameters, consumer-GPU positioning, motion coherence, bilingual text understanding, and SSTA architecture.

## What is official versus inferred

The actionable prompting guidance in this folder is grounded in the first four sources. Workflow advice labelled **production recommendation** is an operational interpretation, not a Tencent benchmark claim.

## Related pages

- [[HunyuanVideo 1.5 I2V Prompt Anatomy]]
- [[HunyuanVideo 1.5 Reference Image and Motion]]
- [[HunyuanVideo 1.5 Camera Direction]]
- [[HunyuanVideo 1.5 I2V Production Workflow]]
- [[HunyuanVideo-1.5]] — earlier sparse model card in the legacy AI-Image-Midjourney folder.
- [[Hunyuan Video 1.5 — Camera Movement Prompting]] — earlier sparse bookmark card in AI-Video.
