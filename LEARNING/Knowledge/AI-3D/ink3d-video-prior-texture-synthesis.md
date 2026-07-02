---
title: "Ink3D — Complex Texture Synthesis for 3D Assets via Video Generative Models"
category: concept
summary: Framework that bridges 3D geometry generation with large-scale video priors to synthesize complex surface textures. Decouples mesh reconstruction from texture baking, using orbit-scan videos and a neural optimization module for coherent multi-view integration.
tags: ["3d-generation", "texture-synthesis", "video-priors", "gaussian-splatting", "neural-rendering"]
sources: 1
updated: "2026-07-02"
---

# Ink3D

> arXiv **2607.01222** — Published July 1, 2026

## Overview

3D generative models struggle with surface appearance because training data for textured 3D assets is scarce compared to the massive image and video corpora available for 2D generative models. Ink3D closes this gap by using video generative models as its texture synthesis engine.

## Method

Two decoupled stages, each leveraging specialized priors:

**Stage 1 — Geometry Reconstruction:**
Uses an off-the-shelf 3D generation model to reconstruct clean white-mesh geometry. This separates shape learning from appearance learning.

**Stage 2 — Texture Synthesis:**
- OrbitPainter, a conditional video generative model, produces dense orbit-scan videos that capture object appearance across continuous viewpoints
- TextureOptimizer, a neural baking module, integrates dense multi-view observations into coherent UV textures while mitigating geometry inconsistencies introduced by the video generation step

## Key Design Choices

- Textures come from video priors trained on datasets orders of magnitude larger than any 3D dataset available today. This gives Ink3C access to complex patterns (fabric weaves, weathered materials, organic surfaces) that dedicated 3D generators cannot reproduce
- Decoupling geometry and texture avoids the joint optimization problem where shape errors propagate into appearance

## Practical Implications

For VFX and 3D production pipelines, Ink3D offers a path from reference images to textured assets without manual UV painting. In ComfyUI workflows that already handle OrbitCoder-style orbit videos, adding TextureOptimizer as a post-processing node creates an end-to-end image-to-textured-mesh pipeline. The approach is complementary to [[StereoGS — Sparse-View 3D Gaussian Splatting]] for geometry quality and could potentially replace parts of the [[OrbitForge]] reconstruction pipeline with higher-fidelity surface detail.

## Comparison to Related Work

- [[OrbitForge]] also converts video to 3D scenes, but uses Gaussian Splatting rather than explicit mesh + texture
- [[PhysiFormer]] simulates 3D motion via diffusion; Ink3D focuses purely on static appearance synthesis
- Traditional baking tools (Substance Painter, Mari) give full artist control; Ink3D gives fast AI-assisted approximation suitable for concept/prototyping workflows

## Links

- arXiv: <https://arxiv.org/abs/2607.01222>
