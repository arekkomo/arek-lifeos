---
title: "SeFi-Image 5B Turbo — Prompting Guide"
category: concept
summary: "Evidence-bounded T2I prompting and iteration guide for fast storyboard stills with SeFi-Image 5B Turbo."
tags: [sefi-image, text-to-image, prompting, storyboard, t2i, turbo]
sources: 1
updated: 2026-08-09
---

# SeFi-Image 5B Turbo — Prompting Guide

[[SeFi-Image 5B Turbo — Source Summary]] establishes the hard model limits: 4, 8, or 10 Turbo steps and guidance 1.0.[1] Start at four steps for storyboard exploration; use 8 or 10 only when a selected composition needs a comparison, not as a substitute for a clearer brief.

## Prompt as a shot brief

Use one compact, declarative description of the image you want. Put decisions in this order so each pass can be diagnosed:

1. **Frame intent:** storyboard still, aspect/frame priority, shot size.
2. **Subject anchor:** who or what, appearance, wardrobe/props, pose.
3. **Dramatic action:** one readable instant, not a sequence of events.
4. **World:** location, time/weather, spatial relation to the subject.
5. **Camera:** angle, lens character, composition, depth relationship.
6. **Light and finish:** key light, contrast, palette, material/medium.

Recommended template:

`[shot size / composition] storyboard still of [subject anchor], [single dramatic action], in [location and spatial relation], [camera / lens / angle], [lighting], [palette / material / finish].`

Example:

`Wide 2.39:1 storyboard still of a rain-soaked detective in a charcoal overcoat, pausing beneath a flickering motel sign, empty highway receding behind her, low eye-level 35mm lens, strong cyan and sodium-vapor practicals, wet asphalt reflections, restrained neo-noir production-design realism.`

## Working rules

- Make the subject, action, and staging unambiguous before adding mood words.
- Describe a single decisive frame; split distinct beats or camera angles into separate prompts.
- Use concrete spatial language: `foreground`, `behind`, `screen left`, `through a doorway`, `silhouette against`.
- When output drifts, change one prompt layer at a time—first staging, then camera, then light/finish.
- State desired qualities positively. There is no verified project guidance here on negative-prompt syntax or weighting, so do not make them a dependency.[1]

For a repeatable hierarchy of prompt components, use [[SeFi-Image 5B Turbo — Storyboard Still Prompt Grammar]]. For controlled comparisons, use [[SeFi-Image 5B Turbo — Iteration and Parameter Control]].

## Sources

[1] https://github.com/jmliu206/SeFi-Image — SeFi-Image official inference repository
