---
title: PhysiFormer — Diffusion Transformer for 3D Physical Motion
category: concept
summary: Diffusion transformer that simulates physically-plausible 3D object motion by predicting vertex trajectories directly in world coordinates, with attention factorized over time, space, and objects.
tags: [diffusion-transformer, physics-simulation, 3d-motion, diT, generative-ai, vfx, rigid-body, mechanics]
sources: 1
source_path: arxiv/2606.27364
source_date: "2026-06"
authors: [Yiming Chen, Yushi Lan, Andrea Vedaldi]
ingested: "2026-06-27"
updated: "2026-06-27"
---

# PhysiFormer — Diffusion Transformer for 3D Physical Motion

**arXiv:** 2606.27364 | **Published:** June 25, 2026
**Authors:** Yiming Chen, Yushi Lan, Andrea Vedaldi (Oxford VGG)
**Project Page:** https://yimingc9.github.io/physiformer

## Problem statement

Most world models for simulation operate in pixel space. They predict next frames
from camera views, which means representations are tied to specific viewpoints.
This blocks geometry-aware reasoning and generalizes poorly across viewing angles.

Existing neural physics simulations either:
- Build ad-hoc latent spaces (hard to interpret)
- Explicitly enforce rigidity/causality as hard constraints
- Use autoregressive generation that accumulates error over time

## Core method

PhysiFormer casts vertex trajectory prediction as a **single denoising diffusion
process in 3D world coordinates**. No intermediate representation needed.

**Inputs:** Initial vertex positions + velocities + material type (rigid/elastic)
**Outputs:** Sampled future vertex trajectories via diffusion sampling

### Architecture design choices

1. **World-space formulation** — Models predict vertex positions directly in
   global 3D coordinates, not view-dependent pixels. This makes representations
   inherently viewpoint-invariant.

2. **No explicit physics inductive biases** — Unlike prior work that hard-codes
   rigidity constraints or energy conservation, PhysiFormer lets the diffusion
   process learn physics implicitly from data. The probabilistic formulation
   naturally captures uncertainty in dynamics.

3. **Factorized attention** — Attention is split over three dimensions:
   - **Time**: Models temporal evolution of trajectories
   - **Space**: Models spatial relationships between vertices
   - **Objects**: Enables permutation-invariant multi-object reasoning without
     explicit object identity encoding

4. **Probabilistic dynamics** — The diffusion formulation samples plausible
   futures from initial conditions. Multiple forward passes at the same input
   produce different valid trajectories, which is useful when real-world
   systems contain unobserved variables.

## Training data

- Over 100,000 simulated physics trajectories
- Covers rigid body mechanics and elastic deformation
- Mixed-material compositions (some objects rigid, others elastic in same scene)

## Results

- Substantially outperforms autoregressive baselines on trajectory accuracy
- Preserves rigidity constraints without explicit enforcement
- Maintains momentum-based physical consistency across simulated steps
- Generalizes to: unseen real-world geometries, larger object counts than
  seen during training, and mixed-material settings

## Practical implications for VFX workflows

Rather than running a separate physics engine, PhysiFormer offers a
learned dynamics layer that can:

- Post-process AI-generated video to add physical plausibility
- Validate simulated motion in [[comfyui]] video generation pipelines
- Generate diverse plausible motion futures for storyboarding or pre-vis
- Integrate with 3D compositing tools like [[davinci-resolve]] via geometry export

The world-coordinate formulation means outputs are compatible with any
downstream 3D engine without coordinate transformation overhead.

## Relation to existing work

Existing simulation approaches in the vault:

- [[mvtrack4gen]] uses multi-view point tracking for novel-view video diffusion
  — PhysiFormer complements this by handling post-generation dynamics rather
  than generation-time geometry supervision
- [[tryoncrafter]] uses 4D Gaussian Splatting for virtual try-on — PhysiFormer
  could add physical realism to those renderings (gravity, deformation)

The diffusion-as-simulator paradigm parallels how [[danceopd-flow-distillation]]
uses flow models for image editing. Both treat diffusion not just as a generative
tool but as a learned dynamical system.

## Comparison with neural rendering approaches

Unlike [[pages]] which focuses on panoramic geometry estimation, or
[[deja-view]] for novel-view synthesis, PhysiFormer targets physical motion
dynamics specifically. It is orthogonal to those reconstruction pipelines —
its role is to simulate what happens after geometry exists.

## Code availability

Models, visualizations, and code are available at the project page:
https://yimingc9.github.io/physiformer

## Related pages

- [[mvtrack4gen]]
- [[tryoncrafter]]
- [[danceopd-flow-distillation]]
- [[pages]]
- [[deja-view]]
- [[comfyui]]
- [[ai-video-generation]]
