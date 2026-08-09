---
title: Wan 2.2 F2L Prompting
category: concept
summary: Endpoint-aware prompt grammar for directing one continuous action between first and last frames in Wan 2.2 F2L.
tags: [wan-2.2, flf2v, prompting, i2v, directing]
sources: 2
updated: 2026-08-09
---

# Wan 2.2 F2L Prompting

> Source ledger: [[Wan 2.2 F2L Sources]].

## Prompting principle

F2L has **one prompt for the interval**, not one prompt per endpoint. The official ComfyUI guide explicitly instructs the user to write an appropriate prompt *according to the first and last frames*. [1] Therefore, use text to specify the **causal bridge**—the action, camera move and visual continuity that make the end frame a credible consequence of the start—while letting the images anchor appearance and composition.

## House grammar for `FRAME MODE: first|last`

Write one compact paragraph in this order:

`[shot + continuous camera move]. [same subject / identity anchor] [single irreversible action] from [start-state] to [end-state]. [environment continuity]. [lighting / palette continuity]. [texture, speed, physical behavior].`

**Example**

> A locked medium-wide shot slowly pushes in as the same silver-haired woman in a black coat crosses the rain-soaked plaza, turning from profile toward camera; she raises a red umbrella and stops beneath the neon arcade, ending in the posed three-quarter view. Continuous wet pavement reflections, blue-magenta neon, light rain, realistic fabric and hair motion, restrained cinematic movement.

This is a directing template, not an official quoted prompt. It operationalizes the official requirement that the prompt account for both endpoints. [[Wan 2.2 F2L Sources]]

## Prompt rules

- **Describe a transition, not two disconnected tableaux.** Use one subject and one main action so the interval has a coherent path to solve. [[Wan 2.2 F2L Sources]]
- **Make camera intent singular.** “Static”, “slow push-in”, “gentle orbit” or “tracking left” gives a clear geometric bridge; do not ask for competing moves in a short shot. This is a production constraint, not a model guarantee. [[Wan 2.2 F2L Sources]]
- **State invariants only when they matter**: identity, wardrobe, prop, location, time of day and colour logic. The endpoints already carry visual information; redundant object inventories make the desired change less legible. This is a practical house policy. [[Wan 2.2 F2L Sources]]
- **Name the arrival condition in action language**: “ends facing camera”, “comes to rest beside the doorway”, “reveals the skyline”. Do not merely say “transition to the final image.” [[Wan 2.2 F2L Sources]]
- **Use negative conditioning for failure classes, not for plot.** The official template includes a negative conditioning branch; reserve it for artifacts such as text, watermark, extra limbs, blur, deformation, or unintended stillness. [3]

## Prompt revision order

1. Fix endpoint incompatibility in the images.
2. Simplify to one action and one camera move.
3. Clarify the final physical state.
4. Add only the continuity details required for the shot.
5. Then test seed and sampler settings; do not compensate for incompatible endpoints with longer prose.

## Related pages

- [[Wan 2.2 F2L Endpoint Design]]
- [[Wan 2.2 F2L Workflow]]
- [[AI Video Scene Packet]]
- [[Purposeful Shot Lists]]
