---
title: Cinematic Shooting
category: concept
summary: Practical principles for shooting footage that grades well in post — covering the cinematic triangle, picture profiles, and the shooting-to-grade pipeline.
tags: [filmmaking, cinematography, davinci-resolve, color-grading, iso, picture-profile]
sources: 1
updated: 2026-04-19
---

# Cinematic Shooting

Practical framework for capturing footage that is intentionally designed for post-production color grading — not shooting for a "finished look" in camera.

## The Cinematic Triangle

Three interdependent camera settings that control exposure and motion rendering:

| Setting | Cinematic principle | Common rule |
|---|---|---|
| **ISO** | Keep low to minimize noise | ISO 100–800; protect highlights |
| **Shutter speed** | 180° rule for natural motion blur | 2× the frame rate (24fps → 1/50s) |
| **Aperture** | Controls depth of field | Open for shallow DoF; close for sharp |

Balance these three to achieve correct exposure without sacrificing any one element.

## Picture Profile 8 (Flat/Log)

Shooting in a flat or log picture profile (e.g., Sony's S-Log, Canon's C-Log, Blackmagic Film) retains more dynamic range by compressing highlights and shadows. The footage looks desaturated and flat in-camera but carries more information for grading.

- **Low ISO + flat profile** = maximum retained dynamic range
- Post: apply LUT or one-click preset to restore color; fine-tune on top

## Shooting-to-grade pipeline

```
Shoot flat/log → Import into DaVinci Resolve → Apply base LUT/preset → Refine nodes → Deliver
```

This pipeline is referenced in the "Guide to Filming Cinematic Videos" Notion entry and aligns with standard professional color science workflows.

## DaVinci Resolve one-click presets

One-click color grading presets apply a starting look to flat footage, enabling rapid stylistic consistency across a project. DaVinci Resolve's PowerGrades and LUTs are the primary vehicles.

## Related pages

- [[davinci-resolve]]
- [[Synthesis/filmmaking-production-overview]]
- [[notion-export-filmmaking-vfx-editing]]
