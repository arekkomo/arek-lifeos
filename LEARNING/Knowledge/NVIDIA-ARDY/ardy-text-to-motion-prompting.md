---
title: "ARDY Text-to-Motion Prompting"
aliases: ["ARDY Text-to-Motion Prompting"]
category: concept
summary: A body-first prompting method for ARDY: action, direction or body part, optional qualitative manner, then an ordered next beat.
tags: [ardy, prompt-engineering, text-to-motion, human-motion, action-sequences]
sources: 1
updated: 2026-08-09
---

# ARDY Text-to-Motion Prompting

ARDY’s official examples are compact action descriptions, not cinematic paragraphs. The recommended working syntax below is an operational abstraction of those examples; see [[NVIDIA ARDY — Official Source Summary]] for the primary-source evidence.

## Prompt grammar

`[Performer] + [primary action] + [direction / limb / target] + [optional manner] + [optional ordered next action]`

- **Performer:** usually `A person` or `A dancer`.
- **Primary action:** a visible full-body verb: walk, step, turn, bow, jump, kick, wave, stand.
- **Direction / limb / target:** `backwards`, `to the right`, `with their right leg`, `forward`.
- **Manner:** use sparingly for physically legible gait quality, e.g. `elegantly`.
- **Sequence:** join only the next clear beat with `then`.

## Strong patterns

- `A person side steps to the right.`
- `A person kicks with their right leg.`
- `A person bows down and then stands upright.`
- `A dancer walks forward elegantly, then turns to the left.`

## Keep out of the text prompt

Do not spend the prompt on camera, lens, lighting, colour, production design, character identity, or editorial instructions. ARDY generates skeletal motion, so these are not documented control channels. If the requirement is a path, precise pose, hand/foot placement, orientation, or speed/direction, route it to [[ARDY Streaming Prompt and Constraint Workflow]] rather than padding the text.

## Prompt-change rule

For a new motion beat, replace the active prompt at the intended timeline point instead of accumulating a long description. The demo applies the updated prompt from the current frame onward; preserving continuity is an autoregressive context/constraint problem, not a reason to make prose more cinematic. [[NVIDIA ARDY — Official Source Summary]]

## Related

- [[ARDY Prompt Pattern Library]]
- [[ARDY Motion Quality Review]]
- [[Interactive-Kinematic-Motion-Generation]]
