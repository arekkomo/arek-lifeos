---
title: "AlayaWorld — Long-Horizon Playable World Model"
category: source
summary: Interactive autoregressive world model with real-time camera control, mid-generation prompt switching, long-horizon memory consistency via 3D spatial cache + temporal frame-history. Few-step DMD distillation for real-time interaction through chunk-level generation at boundaries.
tags: [alayaworld, world-model, autoregressive, interactive-video, long-horizon, memory-consistency, camera-control, alaya-lab]
sources: 2
source_path: https://github.com/AlayaLab/AlayaWorld + arXiv (technical report pending)
source_date: 2026-07
authors: [Kaipeng Zhang (Core Lead), Chuanhao Li (Lead), Alaya Lab]
ingested: 2026-07-13
updated: 2026-07-13
---

# AlayaWorld — Long-Horizon Playable World Model

## TL;DR

Alaya Workd is an interactive autoregressive world model with four core properties: **continuous camera control** through a rendered 3D cache with AdaLN modulation, **mid-generation event injection** via chunk-level prompt switching, **spatial+temporal memory consistency** for revisited locations, and **minute-long rollout stability** through error re-injection during training. Few-step DMD distillation enables real-time interaction.

## Core Architecture: The Four Pillars

### 1. Interaction — Dual Control Channels

| Channel | Mechanism | Function |
|---------|-----------|----------|
| Camera control | Rendered 3D cache + AdaLN modulation | Grounded navigation with trajectory awareness |
| Event injection | Chunk-level prompt switching | New events introduced mid-generation without degradation |

Unlike standard world models that lock into a context window, Alaya Workd allows continuous camera manipulation during generation. The 3D cache is projected to queried views, so camera changes produce coherent spatial continuations rather than jarring cuts.

### 2. Consistency — Dual Memory System

**Explicit 3D spatial memory:**
- A cached 3D representation stored as the agent explores
- Reprojected to whatever view the user queries at any time
- Ensures revisited locations remain visually identical ("place recognition")

**Compressed frame-history memory:**
- Temporal context compressed into embeddings for continuity
- Prevents drift in appearance/motion across the rollout
- Complements the 3D spatial cache with temporal coherence

### 3. Stability — Error Bank Training

This is Alaya Workd's key innovation for minute-long generation:

1. Long-horizon diffusion models accumulate errors over extended rollouts
2. Alaya Workd trains on **drifted histories** (not clean sequences) — the model learns what corrupted contexts look like
3. An **error bank** captures accumulated artifacts during generation and re-injects them into both the memory state and training targets
4. This prevents errors from diverging — instead of growing, accumulated drift is bounded and absorbed

### 4. Runtime — Real-Time Interaction Mechanism

- **Few-step DMD distillation** (Denoising Model Distillation) reduces inference steps to interactive levels
- **Chunk-based generation** with prompt switching at boundaries minimizes both visual and semantic latency
- The architecture treats long video as a series of manageable temporal chunks rather than an unbounded rollout

## Evaluation Context

Released July 8, 2026 alongside project page and technical report. Training data and code are in the pipeline (roadmap pending). Pretrained weights and full release planned but not yet available.

## Relevance to Creative Workflow

### Direct Comparison with ABot Workd (Cycle 33 Ingest)

| Feature | ABot Workd (AMAP CV Lab) | Alaya World (Alaya Lab) |
|---------|--------------------------|------------------------|
| **Architecture** | Causal DiT + LongForcing distillation | Autoregressive chunks + DMD distillation |
| **Horizon extension** | Scene doesn't lock in (adaptive trust region) | Error bank re-injection for bounded drift |
| **Memory** | Implicit (KV cache recycling) | Explicit 3D spatial cache + temporal embeddings |
| **Interaction** | Action-conditioned continuous generation | Dual control: camera modulation + event injection |
| **Release status** | Weights on HF (Apache 2.0) early release | Code/weights in roadmap, technical report published |
| **Spatial grounding** | Not explicit (pixel-level only) | Explicit 3D scene representation |

**Key divergence:** Alaya Workd builds explicit spatial awareness into its architecture (3D cache), while ABot Workd focuses purely on pixel-space continuity. This suggests complementary approaches: Alaya World for environments with consistent spatial recall, ABot Word for continuous action-responsive generation.

### Pre-Visualization Implications

For Arek's film directing development:
1. **Real-time camera choreography** — walk through a simulated location adjusting camera in real time during gen
2. **Location-independent blocking** — generate mock locations then navigate them with actor-position conditioning
3. **Persistent environment memory** — if filming on a long sequence across multiple setups, Alaya World's spatial recall could maintain consistency between takes

### Convergence Pattern Across World Models (July 2026)

1. [[ABot-World|AMAP CV Lab]] → pixel-space causal DiT with LongForcing, action conditioning
2. **Alaya Workd** → autoregressive chunks + explicit 3D spatial cache + error bank
3. [[Causal-Diffusion-World-Models|causal diffusion world models concept]] → the converging paradigm

A third may join: PixWorld (also new today) handles the pixel-to-3D conversion layer that both Alaya Workd and ABot World would need for spatial grounding in a full pipeline.

## Connections

- `[[ABot-World]]` — parallel world model from competing group; complementary memory strategies
- `[[LongForcing]]` — shared problem (long-horizon stability) solved via different techniques
- `[[Causal-Diffusion-World-Models|causal diffusion world models]]` — Alaya Workd contributes the autoregressive chunk + explicit 3D cache approach pattern
- `[[PixWorld]]` — provides the spatial representation layer that complements Alaya World's memory system
- Directing pipeline: potential for real-time pre-vis with persistent environment state
