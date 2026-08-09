---
title: Wan 2.2 F2L Endpoint Design
category: concept
summary: Endpoint-pairing rules that turn first and last images into solvable continuity and transition constraints for Wan 2.2 F2L.
tags: [wan-2.2, flf2v, endpoints, continuity, preproduction]
sources: 2
updated: 2026-08-09
---

# Wan 2.2 F2L Endpoint Design

> Source ledger: [[Wan 2.2 F2L Sources]].

## Endpoint pair = a shot brief

The native node accepts independent start and end images alongside one global text condition. [3] Treat the pair as the hard visual brief and the prompt as the intended path between them. F2L is strongest when the transition can be explained as a single shot rather than an edit between unrelated scenes.

## Compatibility checklist

Before generation, compare the two images:

| Constraint | Preserve or motivate |
|---|---|
| Subject identity | Face, body type, wardrobe and hero prop should match unless transformation is the single explicit event. |
| Screen geography | Keep a plausible direction of travel and camera-side relationship. |
| Lens / framing | Prefer adjacent focal-length and shot-scale choices, or explicitly motivate a push/pull/orbit. |
| Lighting / time | Preserve direction and palette, or prompt one visible motivated change such as a sign turning on or a cloud break. |
| Environment | Preserve anchors—door, skyline, furniture, horizon—unless the shot’s action changes location. |
| Action delta | One legible change: turn, walk, reveal, transform, approach, depart, or settle. |

This checklist is production guidance derived from how the endpoint-conditioned native workflow is structured, rather than a vendor performance guarantee. [[Wan 2.2 F2L Sources]]

## Image preparation

The earlier official FLF2V Diffusers example resizes the first frame to a model-valid area and center-crops/resizes the last frame to the matching dimensions; it also documents Wan frame counts as `4k + 1`. [4] For Wan2.2 native ComfyUI, use matching aspect ratio and deliberately composed endpoint images to avoid asking the model to resolve accidental crop, lens or geometry discontinuities. The ComfyUI template’s default is 81 frames, which fits that frame-count rule. [3][4]

> ⚠️ Contradiction: The Diffusers resize code is for a Wan2.1 FLF2V pipeline, not an official Wan2.2 preprocessing prescription. Reuse its dimensional-consistency principle; do not copy its pipeline identifier or assume its exact preprocessing is required in ComfyUI. [[Wan 2.2 F2L Sources]]

## Shot-design patterns

- **Reveal:** same scene, a camera move exposes a person/object already plausibly off-frame.
- **Approach/departure:** subject’s start and end positions show one direction of travel.
- **Pose resolution:** a subtle shift between two compatible poses; retain wardrobe, lens and lighting.
- **Motivated transformation:** preserve camera and scene while one named physical change produces the end state.
- **Match-move transition:** keep the principal subject anchored while a single camera movement re-frames the end composition.

## Related pages

- [[Wan 2.2 F2L Prompting]]
- [[Wan 2.2 F2L Workflow]]
- [[Script to Scene Analysis]]
- [[AI Video Scene Packet]]
