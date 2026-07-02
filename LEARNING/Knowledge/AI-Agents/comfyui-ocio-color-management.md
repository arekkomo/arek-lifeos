---
title: "ComfyUI-OCIO — OpenColorIO Color Management Nodes for ComfyUI"
category: entity
summary: Nuke-style color-space management nodes for ComfyUI. Supports EXR, ProRes, LogConvert, CDL, ACES transforms via OpenColorIO, bringing professional VFX-grade color pipeline control to node-based AI generation workflows.
tags: ["comfyui", "color-management", "ocio", "vfx-pipeline", "n8n-alternative"]
source_path: "github.com/SlavaSexton/ComfyUI-OCIO"
source_date: "2026-07-02"
authors: ["Slava Sexton"]
ingested: "2026-07-02"
updated: "2026-07-02"
---

# ComfyUI-OCIO

> GitHub: [SlavaSexton/ComfyUI-OCIO](https://github.com/SlavaSexton/ComfyUI-OCIO) — 14 stars, updated July 2, 2026

## Overview

Brings Nuke-grade color pipeline management into ComfyUI via OpenColorIO integration. Provides a complete set of professional color-space nodes that were previously unavailable in node-based AI generation environments.

## Node Set Includes

- **EXR read/write** — HDR sequence I/O with layer support
- **ProRes read/write** — Apple codec for intermediate video formats
- **ColorSpace transforms** — Arbitrary color space conversion via OCIO configuration files
- **LogConvert** — Camera log profile to display/referential conversions (S-log, C-log, E-log, V-log)
- **Display mapping** — View transform lookup for monitoring on different output devices
- **CDL (Color Decision List)** — Slope/offset/power adjustments following Academy specification
- **FileTransform** — Per-file look configuration for footage-specific color correction
- **LookTransform** — Creative grading looks that can be chained and composed

## Technical Details

Backed by OpenColorIO + ACES, the same color management system used in DNeg, Flame, Truelight, and most high-end film/VFX pipelines. Color transforms are deterministic and match industry-standard reference implementations.

Integration is straightforward — install as a ComfyUI custom node and OCIO nodes appear alongside existing image processing tools. No separate OCIO configuration required for standard workflows; ships with built-in ACEScg support.

## Practical Implications

This fills a structural gap in the ComfyUI color pipeline: most AI generation tools work in sRGB without any proper color space awareness, making it difficult to integrate generated content into professional post-production workflows that use OpenEXR or Log formats. These nodes enable ComfyUI to sit properly within a Resolve or DaVinci-native pipeline with correct color transform chains.

The tool complements the existing [[ComfyUI MCP Agent Panel]] for workflow orchestration by adding the color management layer that AI-generated content needs before entering editorial review. Combined with the v0.26 partner node architecture, OCIO transforms can sit between generation and output nodes without extra compositing software.

## Related Work

- DaVinci Resolve's built-in color management is comparable but not accessible from ComfyUI workflows
- [[Nuke]] provides similar node-based color control in a full VFX environment; this brings the concept to AI generation specifically
