---
title: Story-to-Storyboard 3×3 Workflow
category: concept
summary: Reference-image-first method for turning a short story beat into a continuity-controlled nine-shot cinematic storyboard and selecting one production still.
tags: [storytelling, storyboard, prompt-engineering, reference-image, previz, filmmaking]
sources: 1
updated: 2026-08-13
---

# Story-to-Storyboard 3×3 Workflow

A short synopsis is too broad to send directly to an image or video model. First convert it to a **nine-shot coverage board** that locks identity, wardrobe, world, light, and grade. Then choose one panel as the hero still/keyframe for a downstream image or video pass.

> **Source:** [[Storytelling Prompts — Notion Source Capture]]

## Input contract

- **Base image:** the visual authority for identity, wardrobe, materials, palette, and world details.
- **Story beat:** one concise dramatic event, not a multi-scene treatment.
- **Requested look:** add only if it does not contradict the base image.

## Board prompt procedure

1. Interpret the synopsis in one sentence: subject, objective, obstacle/change, and emotional beat.
2. Extract a continuity ledger from the base image: appearance, costume, key props, environment, lighting, weather, and grade.
3. Write a 3×3 board that uses the nine standard coverage positions in [[Storyboard Coverage Grid]].
4. Make each panel narratively useful: establish place → orient action → reveal emotion → isolate the detail → vary power/spatial perspective.
5. End with an extract marker for the selected panel; use that still as a new, explicit reference in the next generation stage.

## Guardrails

- Never vary the character’s wardrobe, hairstyle, signature prop, time of day, weather, or grade between panels unless the story explicitly contains that transition.
- Do not create nine unrelated beauty shots. Every frame needs a distinct editorial purpose.
- Do not ask the downstream video model to animate the entire board. Select one still and generate **one continuous shot** from it.
- Treat the board as an exploration asset, not a canonical shot list, until the director picks the production frame.

## Prompter handoff

For LTX, a selected board panel becomes the I2V/keyframe reference. The LTX prompt should preserve the panel’s composition and continuity ledger while adding only the on-screen action, camera behavior, and temporal change required for that one shot. See [[Story-to-Storyboard Prompting for LTX 2.3]] and [[prompting-guide]].

## Related

- [[Storyboard Coverage Grid]]
- [[visual-storytelling]]
- [[Storytelling Prompts — Notion Source Capture]]
