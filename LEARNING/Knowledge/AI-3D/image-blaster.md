---
title: image-blaster
category: entity
summary: Converts a single image into a full 3D environment with meshes, Gaussian splat, and SFX in under 5 minutes using Claude, World Labs, and FAL.
tags: [ai-3d, gaussian-splatting, ai-automation, claude-code, sfx, github]
sources: 1
updated: 2026-05-15
---

# image-blaster

**By:** neilsonnn
**GitHub:** https://github.com/neilsonnn/image-blaster

---

## What It Is

image-blaster is a Claude Code agent pipeline that takes a single image and produces a fully meshed 3D environment in under 5 minutes. It separates the scene into dynamic objects (exported as `.glb`/`.obj` via Hunyuan 3D) and a static environment (Gaussian splat `.spz` via World Labs Marble), then generates ambient and physics-based SFX per object via ElevenLabs. The whole pipeline is orchestrated by Claude acting as the agent brain.

---

## Capabilities

- Generates `.glb` / `.obj` 3D models of dynamic objects in an image
- Creates explorable Gaussian splat (`.spz`) of the static environment
- Generates ambient looping audio + per-object physics SFX (`.mp3`)
- Image cleanup and object isolation via `nano-banana` (or `gpt-image-2`); see [[GPT Image 2 Reframe — Source Summary]] for controlled reframe/outpaint plate preparation.
- Tunable 3D output: face count, PBR materials, polygon type, geometry mode
- Embeddable into Unity, Unreal, Godot, Blender, Maya, Three.js, Electron
- Full pipeline runs interactively via Claude — confirm each step

---

## VFX / Filmmaking Use Cases

- **Location scouting → 3D scout**: blast a reference photo to get a walkable Gaussian splat environment for previsualization
- **Clean plates**: `nano-banana` removes dynamic objects first, great for background plate extraction
- **Concept art to 3D**: take a single piece of concept art and instantly generate a blockout environment for layout
- **Prop extraction**: isolate and mesh individual props from production stills for use in Blender/Maya
- **Ambient sound design**: auto-generate environment-specific sound beds from a single image (huge for short film work)
- **Game/VR pre-production**: rapid world-building from moodboard images for RealityRowHub or similar projects

---

## Requirements

- Claude Code (`claude` CLI) — install via `curl -fsSL https://claude.ai/install.sh | bash`
- World Labs API key (platform.worldlabs.ai) — for Marble 3D environment model
- FAL API key (fal.ai) — for Hunyuan 3D model generation
- ElevenLabs API — for SFX generation (implied by `elevenlabs-sfx` model reference)

---

## Quick Start

```bash
git clone https://github.com/neilsonnn/image-blaster
cd image-blaster
claude
# → provide World Labs + FAL API keys when prompted
# → place image in input/ and say: "blast it and confirm each step with me"
```

---

## Models Used

| Model | Provider | Purpose |
|---|---|---|
| `marble-1.1` | World Labs | Explorable 3D Gaussian splat environment |
| `hunyuan-3d` | FAL | 3D object model generation (.glb/.obj) |
| `nano-banana` | — | Image edit / clean plates / object reference |
| `gpt-image-2` | OpenAI | Alternate image edit provider |
| `elevenlabs-sfx` | ElevenLabs | Ambient + physics SFX |

---

## Notes

- Uses Claude Code as the orchestration agent — not a standalone script, it's a Claude skills project
- The React viewer (`/app`) is locked by default via `.claudeignore` — remove to allow Claude to modify it
- Face count defaults to 50k (vs Hunyuan's API default of 500k) — good for real-time use cases
- PBR material generation on by default
- The World Labs Marble model is still relatively new — worth watching for quality improvements
