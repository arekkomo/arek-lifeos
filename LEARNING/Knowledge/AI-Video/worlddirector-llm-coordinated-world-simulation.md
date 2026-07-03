---
title: WorldDirector — LLM-Coordinated World Simulation for Controllable Video Generation
category: concept
summary: Decouples video generation into LLM-driven 3D trajectory orchestration + separate visual rendering pipeline, enabling persistent entity identity across prolonged out-of-view periods and unrestricted camera exploration.
tags: [video-generation, world-model, llm-vision, 3d-trajectory, controllable-video, multi-object]
sources: 1
source_path: arXiv 2607.02517v1
source_date: 2026-07
authors: [Hanlin Wang, Hao Ouyang, Qiuyu Wang, Yujun Shen, Qifeng Chen et al.]
ingested: 2026-07-03
updated: 2026-07-03
---

# WorldDirector

Controllable video world model that separates semantic motion orchestration from pixel-level rendering.

## Problem

Existing [[Video Generation]] and [[World Model]] approaches couple physical dynamics with visual rendering in a single network.

This coupling means:

Model needs continuous frame-by-frame observation to sustain entity motion.
Once an object leaves the viewport, identity degrades on re-entry.
Camera control requires prompting hacks or external adapters like [[TrajLoc]].

## Architecture

WorldDirector uses a two-phase pipeline:

### Phase 1 — LLM Trajectory Coordinator

An [[LLM]] takes textual scene descriptions and generates structured 3D trajectories for each dynamic entity plus synchronized camera paths.

Output is a trajectory graph, not pixels.

Each entity carries position, orientation, velocity through time steps. Camera coordinates follow independently.

### Phase 2 — Video Generation from Trajectory Graph

A video diffusion model (e.g., [[Wan-Video]] or [[CogVideoX]]) receives the trajectory as conditioning signal instead of text prompts alone.

Denoising process uses the graph as a spatial-control prior, similar to how [[ComfyUIControlNet]] operates but for multi-object temporal coordination.

## Key Insight

Decoupling orchestration (LLM) from rendering (diffusion) allows each component to specialize.

The LLM handles physical logic: object A passes behind object B before re-emerging on the left side.

The diffusion model handles appearance fidelity without needing to learn physical reasoning.

This separation also enables editing: modify trajectories without re-rendering, or swap rendering models without changing scene logic.

## Results

Experiments demonstrate persistent entity identity across 30+ second clips with multiple occlusion events.

Object appearances remain consistent even after extended out-of-view periods where baseline methods show identity drift.

Multi-scene synthesis shows improved physical plausibility on object interaction benchmarks.

Method supports unrestricted viewpoint exploration — camera can orbit anywhere without generation collapse.

## Relation to Existing Work

> ⚠️ **Contrast:** [[World Narrative Model]] also uses explicit 4D instance graphs for video orchestration, but relies on a dedicated world engine rather than an LLM coordinator. WorldDirector trades explicit physical simulation for the reasoning flexibility of pre-trained language models.

> ⚠️ **Contrast:** [[TrajLoc]] operates at the cross-attention level inside a single diffusion pass. WorldDirector works at a higher architectural layer — whole pipeline orchestration before denoising begins.

## Practical Path to [[ComfyUI]]

Custom node could accept JSON trajectory files and map them to ControlNet-style conditioning inputs.

Current ecosystem lacks multi-object temporal control beyond [[ComfyUIControlNet]] single-frame inputs.

Workflow: text scene description → LLM (local or API) → trajectory JSON → video generation node with trajectory conditioning.

## References

- Paper: https://arxiv.org/abs/2607.02517
- Project page: https://worlddirector.github.io/
