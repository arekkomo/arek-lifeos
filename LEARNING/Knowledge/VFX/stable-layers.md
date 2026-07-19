---
title: Stable Layers — Stability AI
category: entity
summary: Framework for converting images into editable, transparent layer structures suitable for VFX compositing pipelines, enabling rapid element extraction and targeted downstream treatment.
tags: [Image-Decomposition, Layer-Extraction, VFX, Compositing, Image-to-Layers]
sources: 2
updated: 2026-07-03
---

# Stable Layers

> ⚠️ Contradiction with traditional VFX workflows: currently in VFX pipelines, layer extraction from a single photograph is manual (selective masks in Photoshop/AE taking hours → days) or requires pre-production separation. Stability AI's Stable Layers automates this entirely — turning monolithic images into layered compositing assets in seconds rather than days.

## What it is
[[Stable Layers]] is an image decomposition framework by Stability AI that converts single images into editable, transparent layer structures using semantic segmentation. Each identified visual element (foreground objects, backgrounds, text overlays, etc.) is extracted as its own independent layer with preserved spatial layout and detail — suitable for direct import into VFX compositing tools like DaVinci Resolve Fusion or Nuke.

## Why it matters
This collapses a critical bottleneck in the [[VFX]] pipeline where AI-generated images (from Midjourney, Flux, etc.) are monolithic and uneditable at the element level. Stable Layers lets you extract individual components for targeted treatment — color correction on specific elements, compositing over new backgrounds, layer-based effects — without manual rotoscoping or masking work.

## Key Facts
| Capability | Details |
|-----------|---------|
| Framework | Open-source image decomposition framework |
| Core technology | Semantic segmentation-based layer separation |
| Spatial coherence | Preserves original spatial structure and detail during extraction |
| Output format | Structured layers suitable for compositing (multi-channel/transparent PNGs) |
| Input formats | Standard image inputs (JPG, PNG, etc.) |

## Use Cases (from source blocks)
- Fast layer extraction for VFX compositing pipelines — core [[Compositing]] workflow tool
- Break down AI-generated images into element layers for manipulation — direct application to [[AI-Image-Midjourney]] output processing
- Separate foreground/background/elements for targeted VFX treatment — enables precise color grading per-element in [[DaVinci-Resolve]]
- Generate layered reference assets for downstream compositing — useful for pre-vis and pitch deck production

## Cross-Domain Connections to Existing Vault Knowledge
1. **[[AI-Image-Midjourney]]**: Midjourney outputs are typically flat/monolithic; Stable Layers provides the bridge to layer-based editing. This means you can generate concept art in MJ, then extract layers for VFX treatment — a previously impossible workflow.
2. **[[DaVinci-Resolve]]**: Extracted layers → import as multi-channel sequences in Resolve Fusion. Each layer becomes an independent node input for targeted grade/VFX work on specific elements within the frame.
3. [[Compositing-Separate]]: The ability to separate foreground/background/elements automatically transforms from manual rotomation (1-2 hours per shot) to sub-second semi-extraction.
4. [[Lucida]]: When the needed result is one foreground alpha matte rather than a semantic multi-layer decomposition—particularly for glass, text/logo shadows, glow, camouflage, or illustration assets—Lucida is the more targeted still-image tool.

## Setup / How to Use (from source blocks)
```bash
git clone https://github.com/stability-ai/stable-layers.git
cd stable-layers
pip install -r requirements.txt
python separate.py --input image.png --output layers/
```

> ⚠️ Note: ComfyUI node availability not confirmed in source — should verify on project repo for pipeline integration.

## Questions For Further Exploration
1. Quality of layer separation (edge precision, handling of complex overlapping elements)?
2. Minimum input resolution / any compression artifacts introduced?
3. Supported output formats (PNG with alpha, OpenEXR, etc.)?
4. ComfyUI integration status — plugin/node available or raw Python interface only?
5. Does it handle video frame-by-frame or is it image-only at present?

## Appears In
- [[stable-layers-source]] — Notion knowledge base entry (2026-06-08), tagged VFX, Type=`Github`
