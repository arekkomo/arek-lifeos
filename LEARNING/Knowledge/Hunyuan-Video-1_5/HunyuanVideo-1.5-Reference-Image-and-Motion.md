---
title: HunyuanVideo 1.5 Reference Image and Motion
category: concept
summary: Reference-image anchoring and motion-description rules for HunyuanVideo 1.5 I2V.
tags: [hunyuanvideo-1.5, i2v, reference-image, motion, continuity]
sources: 2
updated: 2026-08-09
---

# HunyuanVideo 1.5 Reference Image and Motion

## The image anchors frame one; the prompt animates forward

The official handbook specifies that an I2V upload supplies the first video frame and that subsequent content is generated from the text prompt. Therefore, use the prompt to state **what changes**, not to redundantly redescribe every static detail already visible. [[HunyuanVideo 1.5 I2V — Official Source Guide]] ([Prompt Handbook](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/assets/HunyuanVideo_1_5_Prompt_Handbook_EN.md))

## Preserve reference logic

Tencent’s I2V rewriting specification requires the rewrite to interpret the reference image and user scope together. It explicitly preserves subjects, count, direction, and event order; it replaces vague pronouns with clear entities; and it uses screen-space language when a new object enters or moves. [[HunyuanVideo 1.5 I2V — Official Source Guide]] ([I2V rewrite specification](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/blob/main/hyvideo/utils/rewrite/i2v_prompt.py))

Use this continuity check before generation:

- **Subject:** Who in the reference moves? Name them distinctly if there is more than one.
- **Starting state:** What pose, eyeline, object relationship, or direction is already established?
- **Change:** What moves first, and where does it end?
- **Secondary motion:** What nearby material or environment responds?
- **Scope:** Does “they,” “it,” or “the object” refer to every relevant item or one specific item?

## Example transformation

Weak: `She turns and the camera moves.`

Anchored: `The woman in the foreground turns her head toward screen right. Her earrings sway slightly. The camera pans right with her eyeline, revealing the carved window beside her.`

The latter follows the official pattern of named subject, observable action, spatial direction, and a camera move tied to a reveal. It does not invent a new story event.

> ⚠️ Contradiction: The official rewriter encourages necessary, restrained detail expansion but forbids inventing key events, changes in subject/count/direction/order, or unrequested lighting. Do not treat “make it cinematic” as permission to rewrite the shot’s action. [[HunyuanVideo 1.5 I2V — Official Source Guide]]

## Related pages

- [[HunyuanVideo 1.5 I2V Prompt Anatomy]]
- [[HunyuanVideo 1.5 Camera Direction]]
- [[AI Video Scene Packet]]
