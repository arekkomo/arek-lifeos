---
title: GPT Image 2 Outpaint Continuity Controls
category: concept
summary: A continuity-control framework for reframing and outpainting without drifting from the supplied source plate.
tags: [gpt-image-2, outpainting, continuity, cinematography, vfx]
sources: 3
updated: 2026-08-09
---

# GPT Image 2 Outpaint Continuity Controls

Source basis: [[GPT Image 2 Reframe — Source Summary]]. Use this page after [[GPT Image 2 Reframe Prompt Architecture]] to turn a general extension into a controllable plate.

## Continuity stack

Specify only the controls that are visually load-bearing for the extension:

| Layer | State explicitly when it matters | Example language |
|---|---|---|
| Geometry | horizon, vanishing direction, camera height, ground/wall planes | "Continue the pavement toward the same vanishing point; horizon stays below the window line." |
| Lens | focal-length feel, perspective strength, distortion | "Match the existing 35 mm perspective and natural edge falloff." |
| Light | key direction, softness, color temperature, practical sources | "Continue the warm key from camera-right and cool dusk fill from the open sky." |
| Atmosphere | weather, haze, grain, smoke, depth falloff | "Keep the same light rain, wet speculars, and distant haze." |
| Design | material, era, palette, set dressing density | "Extend the same worn concrete facade and sparse 1990s street furniture." |
| Protected plate | identity-critical existing pixels/concepts | "Keep the performer, face, costume, and original sign lettering unchanged." |

## Negative space is content

For a widescreen or poster reframe, explicitly describe the empty area you need: "leave uncluttered shadowed wall and diffuse haze on camera-left for title placement." Without that instruction, an extension often fills the new space with visually plausible but editorially unusable detail.

## Boundary strategy

The official guide treats masks as control inputs but warns that boundary behavior need not be pixel-perfect. [OpenAI Image generation guide](https://platform.openai.com/docs/guides/image-generation) Keep the protected image comfortably inside the original canvas, avoid placing a critical face/text/logo exactly on a mask edge, and inspect the seam at 100% after every edit.

## Failure diagnosis

| Symptom | Likely missing control | Repair prompt addition |
|---|---|---|
| New architecture tilts or scales wrongly | geometry/camera height | Name horizon, vanishing direction, and the plane to continue. |
| Light flips or reflections disagree | key/fill/practical description | State source direction, color, softness, and what surface must reflect it. |
| Subject mutates | narrow lock list absent or edit region too broad | Protect the subject by mask/canvas and name the 2–4 identity facts that matter. |
| Extension feels pasted on | lens, grain, atmosphere omitted | Match perspective, depth falloff, grain, and atmospheric density. |
| Frame is unusably busy | negative space undescribed | State where and how much uncluttered space must remain. |

> **VFX connection:** This is the generative equivalent of a set extension brief: camera match and lighting continuity are constraints; newly revealed geometry and dressing are the creative payload. See [[GPT Image 2 Canvas and Mask Preparation]] and [[Stable Layers]].
