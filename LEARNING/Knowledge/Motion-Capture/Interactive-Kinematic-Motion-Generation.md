---
title: "Interactive Kinematic Motion Generation"
category: concept
summary: Generating skeletal motion continuously while accepting live text and spatial constraints such as paths, keyframes, and joint targets.
tags: [human-motion, text-to-motion, kinematic-constraints, animation-blocking, real-time]
sources: 1
updated: 2026-07-19
---

# Interactive Kinematic Motion Generation

A control paradigm for motion systems that generate a continuing motion stream while accepting live direction, rather than outputting a fixed motion clip from a single prompt.

## Useful control types

| Control | Directing / animation analogue |
|---|---|
| Text prompt | Performance/action intention |
| Root path or waypoint | Blocking and travel path |
| Full-body keyframe | Pose-to-pose animation beat |
| Sparse joint targets | Hand/foot placement or contact constraint |
| Target velocity | Locomotion tempo and direction |

## Current library links

- [[ARDY]] — autoregressive diffusion model designed around streaming text and long-horizon constraints
- [[MotionLCM]] — low-latency latent-consistency alternative for text and pose control
- [[ProxyPose]] — a complementary *capture* tool: derives object/camera trajectory from footage rather than generating new character motion

## Pipeline note

These models output motion data. A usable cinematic pipeline still needs character rig retargeting, scene layout, and a renderer/video generator downstream. This makes the pattern valuable for previsualization and animation blocking, not a replacement for final-character performance capture.
