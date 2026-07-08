---
title: WildSplat — Feedforward Gaussian Splatting from Unposed In-the-Wild Images
category: concept
summary: First feedforward 3D Gaussian Splatting for appearance-conditioned novel-view synthesis from unposed images under varying illumination via dual-branch decoupling.
tags: [gaussian-splatting, novel-view-synthesis, appearance-conditioning, feedforward-3d, unposed-images]
sources: 1
source_path: arxiv/2607.05347
source_date: 2026-07
authors: []
ingested: 2026-07-07
updated: 2026-07-07
---

# WildSplat — Appearance-Conditioned Feedforward Gaussian Splatting

## What It Is

Feedforward 3D reconstruction excels at speed but collapses under varying illumination. **WildSplat** is the first feedforward [[Gaussian Splatting]] framework that handles inconsistent photometric conditions across unposed input images. Outputs appearance-conditioned novel views in a single forward pass. Outperforms both optimization-based and existing feedforward methods on in-the-wild benchmarks.

## The Problem

Most feedforward Gaussian Splatting assumes consistent lighting across all inputs. Real-world captures rarely satisfy this — sunlight shifts, indoor lights flicker, weather changes. Previous approaches produce blurry results because geometry and appearance features are entangled in a single encoder.

## Architecture

### Dual-Branch Geometry-Appearance Decoupling

| Branch | Role | Output |
|---|---|---|
| **Geometry** | Appearance-invariant 3D structure | Gaussian primitives with consistent geometry |
| **Appearance** | Target appearance via cross-attention | Rendering features modulated by desired look |

### Key Components

The geometry branch extracts structure invariant to lighting changes. Camera poses are predicted jointly — no separate pose step required.

A **globally pre-modulated cross-attention** module injects target appearance cues into content features. The user specifies which reference image controls rendering.

**Joint multi-reference training** supervises multiple lighting conditions simultaneously. This prevents shortcut learning that works for only one condition.

## Practical Relevance

Fits AI generation pipelines where 3D proxies are needed. For example, [[MV-Forcing]] uses a GS-based temporal autoregression framework.

Appearance editing changes scene look without re-capture. Useful for storyboarding in [[ComfyUI]]. Works from sparse unposed inputs unlike optimization methods.

## Benchmarks

Surpasses optimization-based methods on in-the-wild novel-view synthesis while maintaining feedforward speed. SOTA performance reported across single-pass reconstruction tasks from sparse, unposed inputs.

## Related Work

- [[Pano2World]] — Single panorama to Gaussian Splatting (different input, same GS target)
- [[StereoGS]] — Sparse-view GS via stereo priors (geometry at 3–8 views)
- [[Ink3D]] — Video-prior texture synthesis for 3D assets (also bridges video to 3D)
