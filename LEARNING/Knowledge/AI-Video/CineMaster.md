---
title: CineMaster
category: entity
summary: AI-powered 3D camera control for video generation — generates camera trajectories and spatial positioning parameters
tags: [ai-video, camera-control, cinematography]
sources: 1
updated: 2026-07-04
---

# CineMaster

**Two-stage 3D-aware text-to-video framework.** Stage 1: interactive workflow for positioning **object bounding boxes + camera trajectories** in 3D space. Stage 2: control signals rendered to depth maps, feed via Semantic Layout ControlNet (semantic injector + DiT-based) with camera adapter for joint object+camera motion control.

> ⚠️ **Cross-domain:** CineMaster's automatic annotation pipeline uses `[[SAM-3]]` segmentation → `[[Depth-Anything-V2]]` metric depth → 3D point cloud → bounding box calculation. Full pipeline documented on project page.

## Architecture
1. **Semantic Layout ControlNet** = semantic injector (fuses 3D spatial layout + class labels) + DiT-ControlNet (adds fused features to base model hidden states)
2. **Camera Adapter** injects camera trajectories for joint control
3. **Data Annotation Pipeline:** Instance Segmentation → DepthAnything V2 → Inverse projection for 3D point clouds → Entity tracking + 3D box adjustment

## What It Controls Independently
- **Object motion & static camera** — "The tortoise crawls while the hare hops"
- **Static object & moving camera** — "A ginger cat lounges on a rock with sea background" (camera orbits)
- **Joint control** — "A car passes another car from behind" (object tracks + camera dolly)

## Use Cases
The director's tool in AI video generation — specify exact spatial layout, object positions, and camera movement semantically. No trial-and-error prompting needed for compositional precision.

> ⚠️ Synergy: CineMaster output → `[[FilmPort]]` pipeline orchestration → `[[Wan2-Open]]` or `[[SkyReels-V2]]` high-fidelity generation. For reference consistency, add `[[VACE-Alibaba]]` as ControlNet input in stage 1.

## Access
[Project Page](https://cinemaster-dev.github.io/) | [Abstract + demos page](https://cinemaster-dev.github.io/) contains qualitative comparisons vs SOTA and model design diagrams.

> [[source: dtb Knowledge dump, 2025-03-21+05]] | [Project Page](https://cinemaster-dev.github.io/)

```
## [2026-07-04] update | CineMaster
Updated with full research content from dual Notion entries (abstract + demos). Architecture details added including ControlNet design, data annotation pipeline, and all demo categories. Source: raw/dtb_export_archive_2026-07-04/CineMaster-dual.md
```


```
## [2026-07-04] ingest | CineMaster
Created entity page from Notion dump — 3D camera control system. Source: raw/dtb_export_archive_2026-07-04/CineMaster.md
```
