---
title: "MV-Forcing — Long Multi-View Video Generation via 4D Self-Forcing"
category: concept
summary: Combines temporal autoregression with view-wise autoregression through a 3D reconstruction bridge to generate long, consistent multi-view videos of dynamic scenes
tags: [video-generation, multi-view, autoregressive, gaussian-splatting, novel-view, diffusion]
sources: 1
updated: 2026-07-07
source_path: arxiv.org/abs/2607.05376
source_date: "2026-07"
authors: [Gal Fiebelman, Hadar Averbuch-Elor, Sagie Benaim]
ingested: 2026-07-07
---

## What It Does

Video diffusion models either generate long clips (single view) or short multi-view captures. MV-Forcing generates **long sequences across multiple synchronized camera viewpoints** of a dynamic scene in one unified process. The key insight: an autoregressive 3D reconstruction model naturally interfaces between sequentially generated views.

## How It Works

1. **4D Geometric Bridge** — Between each temporally autoregressed frame block, a Gaussian Splatting proxy is reconstructed from the current view's latents
2. **View-to-View Conditioning** — The 3DGS proxy renders new viewpoints that seed the next autoregressive step as spatial priors for bidirectional attention
3. **Self-Forcing** — Instead of ground-truth supervision, each view is conditioned on its predecessor's rendered prediction, forming a 4D chain through both time and space

## Key Technical Details

- Uses the same diffusion model for single-view generation AND multi-view extension (no separate models)
- The 3DGS bridge is lightweight: fitted per temporal block (~60 frames), discarded after rendering new viewpoints
- Spatio-temporal self-forcing means errors are bounded by reconstruction quality rather than compounding unconditionally

## Relevance Pipeline: Where It Fits

- **ComfyUI**: Requires custom node for the 3DGS bridge + view conditioning; not a standard ComfyUI workflow yet
- **3D Asset Generation**: Multi-view consistent output directly feeds into [[OrbitForge]]-style reconstruction pipelines
- **Filmmaking**: Storyboard shots from multiple angles without re-generating each angle independently

## Comparison to Existing Work

| Method | Temporal Length | Multi-View | 3D Bridge | Approach |
|--------|----------------|------------|-----------|----------|
| **MV-Forcing** | Long (minutes) | ✓ Multiple views | Yes (3DGS) | Self-forcing chain |
| [[SimWorlds]] | Variable | ✓ Blender scenes | LLM agents | Planner-coder-reviewer loop |

> **Adjacent to**: [[SimWorlds]], [[Ink3D]], Gaussian Splatting, 3D Reconstruction workflows

## Limitations

- 3DGS fitting per block adds ~2s overhead per 60-frame window
- Dynamic deformation beyond the diffusion model's capacity is not improved by the multi-view bridge
- Requires consistent scene identity; best suited for character/asset-focused sequences, not rapidly changing environments
