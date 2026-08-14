---
title: Story-to-Storyboard Prompting for LTX 2.3
category: concept
summary: Previz-first prompt workflow for converting a short story and base image into a 3×3 board, then turning one selected panel into a compliant LTX 2.3 single-shot prompt.
tags: [ltx-2, ltx-2.3, prompting, storyboard, i2v, keyframe, continuity]
sources: 1
updated: 2026-08-13
---

# Story-to-Storyboard Prompting for LTX 2.3

The 3×3 storyboard method is useful **before** LTX prompting: it gives the director coverage options and a chosen keyframe. It does not replace LTX’s single-shot prompt grammar.

> **Source:** [[Storytelling Prompts — Notion Source Capture]]

## Two-stage workflow

### Stage A — Story to board

Given a short story beat and a base image:

1. Interpret the beat in one sentence.
2. Extract and lock a continuity ledger: subject identity, costume, hair, key props, environment, time/weather, light direction, and grade.
3. Draft nine distinct still-frame prompts using [[Storyboard Coverage Grid]].
4. Ask the director to select one panel (`x.y`) as the hero keyframe.

### Stage B — Selected board panel to LTX shot

Take only the selected frame and create a 130–160 word LTX prompt using the seven-part [[prompting-guide]] structure:

1. One main action.
2. Specific movement and gesture.
3. Appearance locked to the selected still.
4. Foreground → midground → background environment.
5. One camera position/movement.
6. Lighting and color temperature retained from the still.
7. One temporal change within the shot.

## Agent rule

**Never animate the whole 3×3 board in one LTX prompt.** A board is coverage planning. LTX receives one selected reference frame, one continuous action, and one intelligible camera path.

## Copyable internal meta-prompt

```text
Do not generate an image. Given the user’s base image and one short story beat, write a single 3×3 cinematic storyboard image prompt. First preserve a continuity ledger from the base image: subject appearance, wardrobe, hair, props, environment, weather, lighting direction, and grade. Then describe nine distinct panels: ELS, LS, medium-long, medium, MCU, CU, ECU, low angle, and high angle. Each panel must advance a visual or emotional question while keeping the same story world and subject continuity. Finish with: “Extract still [panel]” so the director can select one keyframe for a separate single-shot LTX generation.
```

## Quality check before handoff

- Board panel is visually coherent as a standalone keyframe.
- Identity, costume, prop, environment, light, and grade match the board ledger.
- The LTX prompt contains no other shots, cut instructions, or competing camera paths.
- LTX action and camera movement extend naturally from the selected still.

## Related

- [[Story-to-Storyboard 3×3 Workflow]]
- [[Storyboard Coverage Grid]]
- [[prompting-guide]]
