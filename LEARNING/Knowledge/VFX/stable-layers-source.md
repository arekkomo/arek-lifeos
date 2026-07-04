---
title: Stable Layers (Source)
category: source
summary: Open-source image decomposition framework by Stability AI converting single images into semantically segmented editable layers, enabling automated element extraction for compositing pipelines.
tags: [Image-Decomposition, Layer-Extraction, VFX, Compositing]
sources: 1
updated: 2026-07-03
source_path: raw/notion-export/stable-layers-entry.md
source_date: 2026-06
authors: [Stability AI]
ingested: 2026-07-03
---

# Stable Layers (Source)

## Summary
Open-source image-to-layers decomposition framework by Stability AI that automatically separates a single input image into individual semantically-layered outputs using computer vision segmentation models. Extracts foreground objects, backgrounds, text overlays, and visual elements as independent layers with transparent PNG masks — ready for import into VFX compositing workflows like DaVinci Resolve Fusion or Nuke.

## What it does
- Takes a single flat (monolithic) image as input
- Runs semantic segmentation via foundation CV model to identify distinct visual elements
- Outputs each identified element as an individual layer with alpha/mask channel
- Preserves original spatial layout and high-resolution quality during extraction

## Technical Architecture
```
Input: Single image → Semantic segmentation (foundation CV model) → Layer mask generation → Alpha compositing per element → Output: Directory of layered images (.PNG with alpha channels)
```

## Use Cases
- Rapid extraction of individual elements from concept art for targeted color grading in DaVinci Resolve Fusion
- Separating foreground subjects from backgrounds for compositing over new environments
- Breaking down AI-generated images into components that can be independently modified (color, blur, effects per element)  
- Preparing layered assets for downstream 3D integration

## Pros/Cons vs Manual Workflow
| Manual (Photoshop/AE) | Stable Layers (Automated) |
|----------------------|---------------------------|
| Hours to days per image | Sub-second generation |
| Manual masking/rotoscoping | Automatic semantic segmentation |
| High skill requirement | Accessible to all skill levels |
| Element-dependent manual process | Scalable batch processing possible |

## Appears In
- Notion dtb Knowledge base entry (2026-06-08), tagged `VFX`, Type=`Github`
- Source URL: https://github.com/stability-ai/stable-layers

