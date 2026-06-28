---
title: "PhysRAG — Retrieval-Augmented Physics-Aware Video Generation"
category: concept
summary: ECCV 2026 pipeline that conditions video diffusion models with physics simulation priors (gravity, material properties, collision rules) via retrieval-augmented generation. Addresses the floaty-physics failure mode in text-to-video through learnable query injection over a physical video database. Trained on a curated 7K subset of WISA-80K.
tags: [physics-aware-generation, rag, video-diffusion, simulation-priors, wisa-dataset, eccv2026]
sources: 1
source_path: arxiv/2606.26916
source_date: "2026-06"
authors: [Kexu Cheng, Zicheng Liu, Mingju Gao, Chunhe Song, Hao Tang]
ingested: "2026-06-27"
updated: "2026-06-27"
---

# PhysRAG — Retrieval-Augmented Physics-Aware Video Generation

**arXiv:** 2606.26916 | **Published:** June 25, 2026
**Venue:** ECCV 2026 (Accepted)
**Authors:** Kexu Cheng, Zicheng Liu, Mingju Gao, Chunhe Song, Hao Tang
**Categories:** cs.CV

## Problem statement

Text-to-video models consistently produce physically implausible motion — gravity, fluid dynamics, thermal processes, collisions. Objects float instead of fall, materials deform unrealistically.

Cause-effect across frames is visually coherent but structurally wrong. No existing conditioning signal teaches the model physics priors separate from appearance or layout.

## Core method

PhysRAG conditions a video diffusion model on **physics simulation knowledge** rather than relying purely on data-level exposure to physical phenomena. Three stages:

### 1. Data filtering over WISA-80K

A two-stage filter extracts 7,000 high-quality clips from 80,000:
- Stage 1 removes videos with ambiguous or conflicting physics (superimposed composites, mixed temporal scales)
- Stage 2 selects for diversity across physical domains (thermal, mechanical, optical, fluid)

### 2. Physical video + simulation database

A searchable corpus of **physics simulation priors** is constructed:
- Gravity constants per material class
- Material properties (density, elasticity, viscosity)
- Collision rules and interaction boundaries
- Source simulations from Blender / NVIDIA PhysX engines

### 3. Learnable query injection via RAG

Physical knowledge is injected as learnable queries rather than text or image tokens:
- Physics parameters (mass, velocity, restitution) become conditioning vectors
- Retrieval triggers on semantic tags per frame (e.g., "falling" → gravity)
- Projection layers map simulation data into the latent space of HunyuanVideo or Wan2.1

## Integration properties

- Works **as a conditioning plugin** — no full model retraining required, only learnable query adapters
- Compatible with any video diffusion backbone that accepts additional conditioning tokens (HunyuanVideo, Wan2.1)
- Code, curated data subset, and trained weights released at: https://github.com/sediment1024/PhysRAG

## Results

Evaluated on PhyGenBench and VBench — state-of-the-art across physical plausibility and visual quality (FVD). Ablations validate:
- Data filtering: removing noisy samples improves physics scores by 8.4%
- RAG mechanism: learnable queries outperform static conditioning by 6.1% on collision fidelity
- Physical info extraction: explicit physics priors beat implicit "see-enough-examples in-training" approaches

## VFX Relevance

This addresses a core failure mode of AI video for filmmaking — physically implausible motion breaks realism in compositing, stunt simulation, and product visualization. Integration options:

1. **ComfyUI plugin** — Drops into [[comfyui-v026-kling-v3-turbo]] workflows after the K-sampler, injecting physics priors before denoising
2. **DaVinci Resolve** — Clean composite in Fusion page nodes with physically correct motion, no secondary simulation required
3. **Green screen + physics** — Combines with [[sam2matting-video-matting]] to rotoscope physically-grounded subjects

## Related approaches

- [[raype-ray-space-positional-encoding]] gives geometric awareness at encoding level; PhysRAG adds physical laws on top of structural geometry
- [[physiformer-diffusion-physics-transformer]] predicts vertex trajectories for 3D simulation — different scope (geometry-only vs. physics + appearance)
- [[liveedit-streaming-video-editing]] enables real-time editing; PhysRAG ensures edited subjects obey physical laws
