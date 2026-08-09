---
title: HunyuanVideo 1.5 Camera Direction
category: concept
summary: Official camera vocabulary and shot-direction rules for HunyuanVideo 1.5 image-to-video prompts.
tags: [hunyuanvideo-1.5, i2v, camera, cinematography, prompting]
sources: 2
updated: 2026-08-09
---

# HunyuanVideo 1.5 Camera Direction

The official handbook recommends standard camera-movement language to improve cinematic control. Its library includes vertical movement (crane/pedestal), lateral movement (truck/tracking), dolly in/out, tilt, pan, orbit, 360-degree rotation, follow, and static camera. [[HunyuanVideo 1.5 I2V — Official Source Guide]] ([Prompt Handbook](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/assets/HunyuanVideo_1_5_Prompt_Handbook_EN.md))

## Direction pattern

`The camera [one movement] [in relation to subject], [revealing / keeping / following] [specific result].`

Examples:

- `The camera follows the runner from the side, keeping her face in frame.`
- `The camera slowly dollies back, revealing the convoy behind the motorcycle.`
- `The camera pans right with his gaze, revealing the window.`
- `The camera remains static as the curtains move in the wind.`

## Control rules from the official rewriter

- Normalize a stated move to a conventional description where possible.
- Retain a user’s unusual move if no standard label captures it.
- Do **not** add camera movement the user did not request.
- Do **not** add “static camera” unless that is explicitly requested.

These rules come from Tencent’s I2V rewrite system prompt, not from an informal community convention. [[HunyuanVideo 1.5 I2V — Official Source Guide]] ([I2V rewrite specification](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/hyvideo/utils/rewrite/i2v_prompt.py))

**Production recommendation:** Use one camera instruction per test. If a shot needs a compound move, establish the first move in a successful generation before attempting the full move.

## Related pages

- [[HunyuanVideo 1.5 I2V Prompt Anatomy]]
- [[HunyuanVideo 1.5 Reference Image and Motion]]
- [[Purposeful Shot Lists]]
