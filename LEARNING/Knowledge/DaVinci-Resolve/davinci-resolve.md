---
title: DaVinci Resolve
category: entity
summary: Professional video editing and color grading software by Blackmagic Design, with integrated Fusion VFX and Fairlight audio.
tags: [davinci-resolve, film-editing, color-grading, vfx, fusion, plugins]
sources: 2
updated: 2026-05-30
---

# DaVinci Resolve

Full post-production suite: edit, color, VFX (Fusion), and audio (Fairlight) in one application. Free tier is highly capable.

## Modules

- **Cut / Edit** — timeline editing
- **Color** — node-based color grading
- **Fusion** — node-based VFX and motion graphics
- **Fairlight** — audio post-production
- **Deliver** — export and encoding

## Workflow tips

From ingested tutorials and notes ([[notion-export-filmmaking-vfx-editing]], [[davinci-resolve-reddit-workflow-tips-source]]):

- **Custom ruler guides** — set ruler guides in the viewer for Photoshop-style precision alignment of titles, graphics, and on-screen elements
- **One-click color grading presets** — apply PowerGrades or LUTs as a starting point when working with flat/log footage; refine per scene on top (see [[cinematic-shooting]])
- **Productivity shortcuts** — keyboard shortcut fluency is cited as a primary multiplier for editing speed: J K L scrubbing, I/O in/out, Alt+,/. for frame nudge

### Page strategy
- **Rough cut on Cut page** (not Edit) — dual-timeline + Source Tape mode is faster for assembly; switch to Edit only for precision trimming

### Organisation
- **Smart Bins** — right-click Media Pool → Add Smart Bin → rule-based auto-population on import (e.g. clip name contains "B-roll"); pairs with consistent on-set naming
- **Proxy media** — right-click → Generate Proxy Media at half/quarter-res H.264; full-res auto-renders at export; essential for 4K+ on non-beast machines

### Color
- **Remote Grades / Remote Versions** — grade one interview clip, apply to all matching clips at once; change once, updates everywhere
- **Gallery stills as look reference** — grab stills before grading; use right-click → View as Wipe for split-screen comparison against current clip

### Performance & delivery
- **Background caching** — Playback → Render Cache → Smart; red timeline lines turn blue when cached; point cache to a fast SSD separate from media drive
- **Custom export presets** — save named presets per format (YouTube, Client Review, Master File); never configure export from scratch

## Plugins

Arek maintains a personal plugin catalog (Notion note: "Resolve Plugins", added 2025-10-10). Specific plugins TBD — update when the Resolve Plugins note is ingested in more detail.

## Shooting-to-grade pipeline

Resolve is the destination for footage shot using the [[cinematic-shooting|cinematic shooting]] approach:
```
Shoot flat/log → Import → Apply base LUT → Refine nodes → Deliver
```

## Related pages

- [[cinematic-shooting]]
- [[Synthesis/filmmaking-production-overview]]
- [[notion-export-filmmaking-vfx-editing]]
- [[davinci-resolve-reddit-workflow-tips-source]]
