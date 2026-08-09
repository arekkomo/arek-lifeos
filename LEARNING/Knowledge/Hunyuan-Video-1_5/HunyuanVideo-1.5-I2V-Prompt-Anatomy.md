---
title: HunyuanVideo 1.5 I2V Prompt Anatomy
category: concept
summary: Official I2V prompt structure: subject motion, scene motion, and optional camera movement.
tags: [hunyuanvideo-1.5, i2v, prompting, motion]
sources: 2
updated: 2026-08-09
---

# HunyuanVideo 1.5 I2V Prompt Anatomy

HunyuanVideo 1.5 treats the uploaded image as the first frame; the text directs the later frames. Its official I2V formula is:

> **Subject motion dynamics + scene motion dynamics + [camera movement]**.
> — [[HunyuanVideo 1.5 I2V — Official Source Guide]] ([Prompt Handbook](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/assets/HunyuanVideo_1_5_Prompt_Handbook_EN.md))

## Write in three layers

1. **Subject motion:** Name the pictured subject and describe one primary action with observable mechanics: posture, direction, speed, limbs, gaze, or material response.
2. **Scene motion:** Add only background or environmental motion that supports the subject: grass bending, dust lifting, waves moving, traffic passing, cloth fluttering.
3. **Camera movement (optional):** State a single intentional move and what it follows or reveals.

The official rewriter converts static intent into a small time sequence, uses explicit transitions such as “then” and “meanwhile,” and prefers concrete subject–action–detail descriptions over abstract emotional labels. It also asks for precise screen position and direction when spatial relations matter. [[HunyuanVideo 1.5 I2V — Official Source Guide]] ([I2V rewrite specification](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/hyvideo/utils/rewrite/i2v_prompt.py))

## Working template

`[Named subject] [performs one observable action]. [A body/clothing/material detail reacts]. [Background element] [moves in a compatible way]. [Optional: camera move] [follows/reveals a specific target].`

**Production recommendation:** Begin with a one-beat action. Add a second beat only after the first produces stable identity and motion; this keeps the test interpretable.

## Related pages

- [[HunyuanVideo 1.5 Reference Image and Motion]]
- [[HunyuanVideo 1.5 Camera Direction]]
- [[HunyuanVideo 1.5 I2V Production Workflow]]
