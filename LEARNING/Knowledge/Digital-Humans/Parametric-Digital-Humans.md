---
title: "Parametric Digital Humans"
category: concept
summary: Editable statistical 3D representations of people that expose semantic controls for identity, expression, pose, and anatomy rather than only producing pixels.
tags: [digital-human, 3d-morphable-model, face-rig, facial-animation, vfx]
sources: 1
updated: 2026-07-19
---

# Parametric Digital Humans

A parametric digital-human model represents a person as explicit geometry plus interpretable parameters, rather than as a fixed mesh or an image/video output.

## Why it matters

- **Repeatability:** maintain a single character identity across shots
- **Editability:** adjust expression, gaze, head pose, or anatomy directly
- **Pipeline compatibility:** parameters can drive rigs, renderers, simulations, and downstream video tools

## Library links

- [[GNM]] — Google’s ecosystem; GNM Head exposes identity, expression, pose, eyes, teeth, and tongue
- [[ID-LoRA]] — pixel/latent-domain identity-preserving video counterpart
- [[DreamActor-M1]] — rendered expressive face-animation tool

Use parametric models where an editable character asset is needed; use generative talking-head/video systems where speed matters more than rig-level control.
