---
title: Wan 2.2 First-to-Last-Frame — Sources
category: source
summary: Verified primary-source ledger for the native ComfyUI Wan 2.2 first-to-last-frame workflow and its prompt-relevant behavior.
tags: [wan-2.2, flf2v, first-last-frame, comfyui, source]
sources: 4
updated: 2026-08-09
source_path: https://docs.comfy.org/tutorials/video/wan/wan2_2
source_date: 2025-07
authors: [ComfyUI, Wan Team, Hugging Face]
ingested: 2026-08-09
---

# Wan 2.2 First-to-Last-Frame — Sources

## Primary sources

1. **ComfyUI official Wan 2.2 guide** — https://docs.comfy.org/tutorials/video/wan/wan2_2
   - Documents the native `WanFirstLastFrameToVideo` workflow: two `Load Image` inputs, start/end-frame roles, a prompt written for the two frames, and 720P as a high-VRAM option.
   - Its downloadable template identifies the paired Wan 2.2 I2V high- and low-noise 14B models, compatible Wan 2.1 VAE, and default latent settings of 640×640, 81 frames and batch 1.

2. **Official Wan2.2 repository** — https://github.com/Wan-Video/Wan2.2
   - Lists Wan2.2 I2V-A14B as the 480P/720P image-to-video MoE release and describes prompt extension for I2V as using a vision-language model when desired.

3. **Official ComfyUI FLF2V workflow JSON** — https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_wan2_2_14B_flf2v.json
   - Executable workflow evidence: `WanFirstLastFrameToVideo` accepts positive/negative conditioning, `start_image`, `end_image`, VAE and optional vision encodings; it is paired with `wan2.2_i2v_high_noise_14B_fp8_scaled` and `wan2.2_i2v_low_noise_14B_fp8_scaled`.

4. **Hugging Face Diffusers Wan documentation** — https://huggingface.co/docs/diffusers/main/en/api/pipelines/wan
   - Documents the earlier dedicated Wan2.1 FLF2V pipeline with `image`, `last_image`, and one text prompt; its example normalizes the endpoint images to matching output dimensions. It also documents the Wan frame-count rule `4k + 1`.

## Scope and version caveat

> ⚠️ Contradiction: Wan2.2’s official repository lists I2V-A14B, TI2V-5B and T2V-A14B, but not a separately named Wan2.2 FLF2V checkpoint. The official ComfyUI guide nevertheless ships a **Wan 2.2 14B FLF2V** template using the two Wan2.2 I2V denoisers and the native `WanFirstLastFrameToVideo` node. Treat “Wan 2.2 FLF2V” as this ComfyUI-native workflow, not as evidence of a separate upstream checkpoint. [1][2][3]

## Related pages

- [[Wan 2.2 F2L Workflow]]
- [[Wan 2.2 F2L Prompting]]
- [[Wan 2.2 F2L Endpoint Design]]
- [[Wan 2.1]]
