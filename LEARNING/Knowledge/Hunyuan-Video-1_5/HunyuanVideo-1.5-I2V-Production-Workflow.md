---
title: HunyuanVideo 1.5 I2V Production Workflow
category: concept
summary: Practical HunyuanVideo 1.5 I2V prompting and ComfyUI iteration workflow grounded in official templates and settings.
tags: [hunyuanvideo-1.5, i2v, comfyui, prompting, workflow]
sources: 3
updated: 2026-08-09
---

# HunyuanVideo 1.5 I2V Production Workflow

## 1. Build the first-frame brief

Choose a reference image with a readable subject, direction, and staging. Write a one-beat prompt using the official sequence: subject motion + scene motion + optional camera move. [[HunyuanVideo 1.5 I2V Prompt Anatomy]]

## 2. Use the official I2V path

Tencent publishes a [720p I2V ComfyUI workflow template](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_hunyuan_video_1.5_720p_i2v.json). Its guide advises using the latest templates, detailed descriptive prompts, and explicit camera/style/lighting information where desired. [[HunyuanVideo 1.5 I2V — Official Source Guide]] ([ComfyUI guide](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/ComfyUI/README.md))

## 3. Match settings to the checkpoint

Official best-quality settings are checkpoint-specific: 480p I2V uses CFG 6, flow shift 5, and 50 steps; 720p I2V uses CFG 6, flow shift 7, and 50 steps. CFG-distilled I2V variants use CFG 1 and 50 steps. The 480p I2V step-distilled model uses CFG 1, flow shift 7, and recommends 8 or 12 steps. [[HunyuanVideo 1.5 I2V — Official Source Guide]] ([ComfyUI guide](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/ComfyUI/README.md))

## 4. Iterate one variable at a time

**Production recommendation:** Lock seed, image, checkpoint, and settings while testing the prompt. Then change only one of: subject action, scene motion, or camera direction. This creates a useful comparison set rather than an opaque prompt rewrite.

## 5. Escalate deliberately

The repository exposes I2V prompt rewriting and recommends a vision-language model for that task when configured; rewriting is enabled by default in its source-code path but the pipeline can run without a remote rewriter. [[HunyuanVideo 1.5 I2V — Official Source Guide]] ([official repository](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5))

Use rewriting after a clear human-authored brief exists. Check the rewritten result against the reference image for subject identity, count, direction, action order, and camera intent before generation.

## Related pages

- [[HunyuanVideo 1.5 Reference Image and Motion]]
- [[HunyuanVideo 1.5 Camera Direction]]
- [[ComfyUI Compendium]]
