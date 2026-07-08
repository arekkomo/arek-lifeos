---
title: Stable Layers — Multi-Layer Image Editing with ControlNet
category: entity
summary: Stable Layers is a ComfyUI-based tool for controlling light sources in images while preserving existing details, leveraging multi-layer representation and control networks for fine-grained image synthesis.
tags: [comfyui, layer-manipulation, stable-diffusion, image-editing, controlnet]
updated: 2026-07-04
sources: 4
---

# Stable Layers

## Overview
Stable Layers is a framework for deep multi-layer representation and manipulation in image synthesis using ControlNet-based architectures. It enables fine-grained editing without requiring structural rewrites of the underlying generation pipeline.

## Key Features (from dump collection)
- Multi-layer decomposition of existing images into independent control channels
- Light source manipulation while preserving original composition
- ControlNet integration for condition-specific layer targeting
- Non-destructive editing paradigm — layers remain independently modifiable
- Compatible with Stable Diffusion backends and ComfyUI workflows

## Potential Applications
- VFX environment relighting (match live-action elements to new lighting setups)
- Product mockup generation (maintain product details while varying presentation environment)
- Concept art iteration (preserve key design elements across multiple lighting/atmospheric passes)

> **Synthesis Note:** Stable Layers' layer decomposition maps directly to DaVinci Resolve's OFX compositing node model — background/foreground/midground layers correspond to matte channels in Fusion. The light source manipulation capability has direct parallel in color grading workflows where key/fill/rim relationship adjustments are fundamental controls.
