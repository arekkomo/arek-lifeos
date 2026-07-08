# neilsonnn/image-blaster

Tags: AI Automation
Description: Converts a single image into a full 3D environment with meshes, Gaussian splat, and SFX in under 5 minutes using Claude, World Labs, and FAL.
URL: https://github.com/neilsonnn/image-blaster
Date Added: May 15, 2026 8:33 PM
Type: Github
Archive: No
Spark: No

## About

image-blaster is a Claude Code agent pipeline that takes a single image and produces a fully meshed 3D environment in under 5 minutes. It separates dynamic objects (exported as .glb/.obj via Hunyuan 3D) from the static environment (Gaussian splat .spz via World Labs Marble), then generates ambient + physics-based SFX per object via ElevenLabs. Claude acts as the orchestration agent throughout.

**GitHub:** [https://github.com/neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster)

## Capabilities

- Generates .glb / .obj 3D models of dynamic objects from a single image
- Creates explorable Gaussian splat (.spz) of the static environment
- Generates ambient looping audio + per-object physics SFX (.mp3)
- Image cleanup and object isolation via nano-banana (or gpt-image-2)
- Tunable output: face count, PBR materials, polygon type, geometry mode
- Embeddable into Unity, Unreal, Godot, Blender, Maya, Three.js, Electron
- Full pipeline runs interactively via Claude — confirm each step

## VFX / Filmmaking Use Cases

- Location scouting → 3D scout: blast a reference photo to get a walkable Gaussian splat for previsualization
- Clean plates: nano-banana removes dynamic objects first, great for background plate extraction
- Concept art to 3D: instantly generate a blockout environment from a single piece of concept art
- Prop extraction: isolate and mesh individual props from production stills for use in Blender/Maya
- Ambient sound design: auto-generate environment-specific sound beds from a single image
- World-building: rapid environment creation from moodboard images

## Models

| Model | Provider | Purpose |
| --- | --- | --- |
| marble-1.1 | World Labs | Explorable 3D Gaussian splat environment |
| hunyuan-3d | FAL | 3D object model generation (.glb/.obj) |
| nano-banana | — | Image edit / clean plates / object reference |
| gpt-image-2 | OpenAI | Alternate image edit provider |
| elevenlabs-sfx | ElevenLabs | Ambient + physics SFX |

## Requirements

- Claude Code CLI — `curl -fsSL https://claude.ai/install.sh | bash`
- World Labs API key ([platform.worldlabs.ai](http://platform.worldlabs.ai))
- FAL API key ([fal.ai](http://fal.ai))
- ElevenLabs API key (implied)

## How to run it

```bash
git clone https://github.com/neilsonnn/image-blaster
cd image-blaster
claude
# provide World Labs + FAL API keys when prompted
# place image in input/ and say: "blast it and confirm each step with me"
```

## Notes

- Orchestrated by Claude Code as agent — not a standalone script
- React viewer (/app) locked by .claudeignore by default — remove to let Claude modify it
- Face count defaults to 50k (vs Hunyuan API default of 500k) — better for real-time use
- PBR material generation on by default
- World Labs Marble model is relatively new — quality improving rapidly