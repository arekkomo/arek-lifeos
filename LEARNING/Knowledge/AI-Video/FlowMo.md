---
title: FlowMo
category: entity
summary: Flow-based motion control system for video generation — enables real-time trajectory and gesture control over generated content
tags: [ai-video, motion-control, flow-mapping]
sources: 1
updated: 2026-07-04
---

# FlowMo

Motion control framework designed to provide **granular trajectory and gesture control** in video generation. Moves beyond basic pose markers by using a flow-based system that maps continuous motion paths — useful for choreography-specific applications.

## Key Features
- Flow-mapped motion trajectories (continuous rather than discrete)
- Real-time parameter adjustment during generation
- Gesture refinement controls for specific body regions
- Compatible with existing diffusion pipelines

## Use Cases
Choreographed content creation, dance animation, and narrative sequences requiring precise motion control (e.g., "person walks forward then turns right and raises arm"). Better suited for choreographic precision than text-to-motion prompts.

> ⚠️ Synergy: Output from FlowMo can feed as ControlNet input to `[[VACE-Alibaba]]` or `[[Wan2-Open]]` for high-fidelity video output. For motion capture alternatives, compare with `[[Yoom-MotionCapture]]`.

## Access
Created by arielshaulov. [GitHub](https://github.com/arielshaulov/FlowMo) — check repository for setup instructions and model downloads.

```
## [2026-07-04] ingest | FlowMo
Created entity page from Notion dump — flow-based motion control system. Source: raw/dtb_export_archive_2026-07-04/FlowMo.md
```
