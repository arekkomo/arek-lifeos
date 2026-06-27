---
title: "RayPE — Ray-Space Positional Encoding for 3D-Aware Video Generation"
category: concept
summary: Positional encoding that injects 6D Plucker ray coordinates into self-attention queries/keys to give video diffusion transformers native 3D geometric awareness without explicit geometry conditioning. <0.1% parameter overhead, zero-initialized for drop-in compatibility with pretrained models.
tags: [positional-encoding, plucker-coordinates, 3d-aware-video, diffusion-transformer, camera-controllability, video-consistency, self-attention, video-generation]
sources: 1
source_path: arxiv/2606.27345
source_date: "2026-06"
authors: [Minghao Yin, Jiahao Lu, Wenbo Hu, Wang Zhao, Shan Ying, Kai Han]
ingested: "2026-06-27"
updated: "2026-06-27"
---

# RayPE — Ray-Space Positional Encoding for 3D-Aware Video Generation

**arXiv:** 2606.27345 | **Published:** June 25, 2026
**Authors:** Minghao Yin, Jiahao Lu, Wenbo Hu, Wang Zhao, Shan Ying, Kai Han
**Categories:** cs.CV

## Problem statement

Standard video diffusion transformers position tokens using rotary positional encoding (RoPE) on the `(u, v, t)` axes — the camera's 2D image grid plus time. This parametrization says nothing about the actual 3D structure of the scene behind the camera. Two tokens that correspond to the same 3D point but appear at different screen coordinates receive no geometric signal from their shared spatial origin.

Consequences:
- Poor camera controllability (model doesn't understand how rays relate in 3D)
- Cross-frame 3D inconsistency (same object seen from different angles lacks coherence)
- Inability to generalize across heterogeneous camera motion patterns

## Core method

RayPE replaces/extends flat RoPE with **Plucker coordinate-based positional encoding** that directly encodes the 3D geometry of each token's corresponding camera ray.

### Key insight: Plucker algebra meets Transformer attention

The geometric relation between two camera rays is captured by the **Plucker reciprocal product**, which is bilinear in the two rays. The dot product in Transformer self-attention is also bilinear. This structural analogy means a 6D Plucker coordinate can be injected additively into queries and keys such that their dot product naturally decomposes into geometric terms.

### Architecture

1. **Per-token 6D Plucker coordinates** — Each video token gets a 6D vector encoding its camera ray (direction + moment)
2. **Additive injection into Q/K** — Unlike RoPE which rotates embeddings, RayPE adds the Plucker coordinate directly to queries and keys
3. **Query/key flip arrangement** — Symmetric identity configuration of the flip operator coincides exactly with the reciprocal product, ensuring attention scores have the right geometric semantics
4. **Attention score decomposition** — Splits into: content term + geometry term + two cross-terms (content×geometry). Experiments show all four components are individually necessary

### Stability mechanisms

Video datasets vary wildly in camera-translation scale (SfM reconstructions, deep SLAM, metric-scale data). To handle this:

1. **Decouple direction from moment magnitude** — Separate the unit ray direction from the moment's norm
2. **Learned log-magnitude gating** — Scale the encoding by a learned function of `log(|moment|)` so small and large translations get appropriately weighted
3. **RMSNorm alignment** — Apply RMSNorm to the geometric branch so its activation statistics match the QKNorm-normalized content branch, preventing training instability

### Integration properties

- Adds **<0.1% parameters** to a pretrained video DiT (i.e., primarily additive, almost no new weights)
- **Zero-initialized** — Model starts identical to the pretrained checkpoint; geometry learns from scratch without disrupting existing capabilities
- Compatible with any RoPE-based video diffusion transformer as a drop-in module

## Results

Evaluated on a four-dataset training mixture. Improvements reported across three axes:

1. **Camera controllability** — Generated video better follows specified camera trajectories
2. **Cross-frame 3D consistency** — Objects maintain coherent geometry across different viewpoints within the same clip
3. **Overall video quality** — FID/quality metrics improved, confirming geometry helpfully complements content generation rather than interfering

## Practical implications for VFX and filmmaking workflows

For [[ai-video-generation]] in [[comfyui]]:
- Native 3D awareness without requiring explicit depth maps or point clouds as conditioning inputs
- Additive injection means existing LoRA adapters, control nets, and training checkpoints remain fully compatible
- Particularly valuable for multi-camera scene generation where cross-view consistency matters

For VFX compositing in [[davinci-resolve]]:
- Better 3D consistency reduces the need for manual geometry correction in post-production
- Camera-controllable generation enables virtual camera movement over AI-generated scenes

## Relation to existing work in the vault

> ⚠️ **Contradiction:** The daily scan from June 26 (see [[arxiv-scan-2026-06-26-source]]) mentioned a "RayPE" paper with arXiv ID `2606.24217` that described "novel 3D positional encodings designed specifically for video latents" and benchmarked on "4D Gaussian Splatting + ControlNet hybrid pipelines." However, the actual RayPE paper (2606.27345) describes a fundamentally different method based on Plucker coordinates and attention injection, running on standard DiT architectures with a four-dataset mixture (no 4D GS benchmarking). That scan entry appears to have mixed up metadata from multiple papers. This page reflects the actual published content from arXiv 2606.27345.

Complementary vault entries:
- [[mvtrack4gen]] uses multi-view point tracking for geometric supervision — RayPE provides a lighter-weight alternative that works at the positional encoding level rather than requiring tracking data
- [[physiformer-diffusion-physics-transformer]] simulates physical motion in world coordinates — RayPE gives generation models native 3D awareness so their outputs are more geometry-consistent from the start
- [[tryoncrafter]] uses 4D Gaussian Splatting for virtual try-on — RayPE's camera controllability directly benefits camera-controllable try-on scenarios

## Technical depth notes

The Plucker coordinate representation is an elegant choice: any line in 3D space can be represented as a point on the Plucker manifold, and two lines' intersection/parallelism can be computed via bilinear products. By exploiting this algebraic structure that mirrors Transformer attention's dot product, the authors achieved geometric awareness "for free" in terms of architectural changes.

The zero-initialization + RMSNorm design shows strong engineering discipline — adding a module that starts as an identity operation and only learns to deviate from it when geometry actually helps is a proven recipe for stable transfer learning. This same pattern was used in [[disco-lora-multi-concept-video]] (Z-score regularization) and resonates with the distillation approach in [[danceopd-flow-distillation]].

## Limitations

- Requires camera parameters (intrinsics + extrinsics) to compute Plucker coordinates — not applicable to videos without camera metadata
- Tested on a four-dataset mixture; generalization to edge cases (extreme FOV, drone footage, microscope data) is unverified
- Performance impact of added attention computation at inference time not explicitly benchmarked

## Code availability

Paper does not yet include a code release link. Check arXiv 2606.27345 for updates. Authors are from Tencent AI Lab (Kai Han), which typically releases code within 1-3 months of publication.

## Related pages

- [[mvtrack4gen]]
- [[physiformer-diffusion-physics-transformer]]
- [[tryoncrafter]]
- [[disco-lora-multi-concept-video]]
- [[danceopd-flow-distillation]]
- [[ai-video-generation]]
- [[comfyui]]
