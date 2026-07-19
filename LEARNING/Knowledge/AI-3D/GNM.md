---
title: "GNM — Generative aNthropometric Model Ecosystem"
category: source
summary: Google’s open parametric-human ecosystem, initially releasing GNM Head: a high-fidelity statistical 3D head model with disentangled identity, expression, pose, and internal-anatomy controls.
tags: [gnm, parametric-human, 3d-morphable-model, digital-human, face-rig, facial-animation, google]
sources: 1
source_path: https://github.com/google/GNM
source_date: 2026-07
authors: [Google]
ingested: 2026-07-19
updated: 2026-07-19
---

# GNM — Generative aNthropometric Model Ecosystem

**Repository:** [google/GNM](https://github.com/google/GNM) · **License:** Apache 2.0

## What it is

GNM is Google’s emerging ecosystem of statistical, parametric human models plus related perception/analysis technology. The first released package is **GNM Head**, a high-fidelity 3D morphable model of the human head and face.

## GNM Head controls

- Identity / head shape
- Facial expression
- Head pose
- Eyeballs, teeth, and tongue as controllable internal anatomy
- Semantic parameter sampling
- Backends for NumPy, JAX, PyTorch, and TensorFlow

## Where it fits

This is **geometry and rigging infrastructure**, not a video generator. It can provide a stable, editable face representation for digital-human, animation, avatar, or VFX workflows before a rendering/lip-sync/video stage.

## Status

- GNM Head released
- Broader model/perception suite is on the roadmap
- Package-specific citation is marked “coming soon” in the repository

## Related

- [[Parametric-Digital-Humans]] — reusable 3D human representation pattern
- [[ID-LoRA]] — generates identity-consistent audio-video, whereas GNM supplies an explicit editable head representation
- [[DreamActor-M1]] — expressive rendered face animation; GNM is a potential geometry/rig substrate upstream
