---
title: "SeFi-Image 5B Turbo — Iteration and Parameter Control"
category: concept
summary: "A seed-locked storyboard iteration protocol using SeFi-Image 5B Turbo's supported sampler settings."
tags: [sefi-image, turbo, seed, iteration, storyboard, t2i]
sources: 1
updated: 2026-08-09
---

# SeFi-Image 5B Turbo — Iteration and Parameter Control

SeFi Turbo supports only 4, 8, or 10 denoising steps and should use guidance scale 1.0; 4 is the official default.[1] The official CLI also exposes seed, dimensions, prompt-file input, batch size, and images-per-prompt.[1]

## Recommended control protocol

| Phase | Keep fixed | Change | Goal |
|---|---|---|---|
| Explore | 4 steps, guidance 1.0, target aspect | seed across a small batch | Find promising composition families |
| Compose | seed, 4 steps, guidance 1.0 | subject / beat / geography wording | Solve staging before styling |
| Direct | seed, core staging | camera and shot-size wording | Select the emotional point of view |
| Finish test | selected seed and prompt | 8 or 10 steps | Compare detail stability against the 4-step candidate |
| Lock | seed, dimensions, prompt, model, steps | nothing | Preserve a reproducible board still |

## Parameter rules

- **Seed is the continuity handle.** Record it with every selected still. Change it when you need alternate compositions; keep it when you need to isolate a prompt edit.
- **Dimensions are the framing handle.** Establish the delivery aspect before shot selection. Do not compare a wide frame and square frame as though they were prompt-only variants.
- **Steps are the speed/detail trade-off.** Four steps is the rapid storyboard baseline. An 8- or 10-step result is a controlled confirmation pass, not proof that the prompt was good.
- **Guidance stays at 1.0.** Do not tune classifier-free guidance as an ordinary creative dial for Turbo: the official runtime enforces 1.0.[1]
- **One variable per round.** If the action is wrong, do not simultaneously alter lens, palette, wardrobe, and seed.

## Minimal record

Store: `model=SeFi-Image-5B-turbo | steps | guidance=1.0 | width×height | seed | prompt revision | selected/rejected + reason`.

The official pipeline writes a manifest for the run and supports one prompt per line for batch generation, which makes a named prompt matrix practical.[1] For image-language structure, see [[SeFi-Image 5B Turbo — Prompting Guide]].

## Sources

[1] https://github.com/jmliu206/SeFi-Image — SeFi-Image official inference repository
