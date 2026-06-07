---
title: Mamma (Motion Capture)
category: entity
summary: Markerless multi-person motion capture system — max Planck Institute research for video-only mocap.
tags: [motion-capture, markerless, multi-person, max-planck-institute, research]
sources: 1
updated: 2026-06-07
---

# Mamma (Markerless Multi-person Motion Capture)

**By:** Max Planck Institute (IS)
**Released:** 2026
**GitHub:** https://github.com/cuevhv/mamma
**Paper:** https://mamma.is.tue.mpg.de/
**Project Page:** https://mamma.is.tue.mpg.de/

---

## What It Is

Markerless multi-person motion capture system. Estimates full-body pose and shape of multiple people from monocular or multi-view video without any markers or sensors on the body.

---

## Key Architecture

- **Markerless**: No physical markers needed — pure video-based estimation
- **Multi-person**: Detects and tracks multiple individuals simultaneously
- **Full-body pose/shape**: Estimates both skeletal pose and body geometry
- **Video input**: Standard cameras sufficient (no specialized mocap stage needed)

---

## Capabilities

- Markerless full-body pose estimation
- Multi-person simultaneous tracking
- Body shape estimation alongside pose
- Standard video camera input

---

## VFX / Filmmaking Applications

- **On-set performance capture**: Capture performances without mocap suits/costumes
- **Crowd animation**: Generate realistic crowd movement from video reference
- **Acting reference**: Capture actor performances for animation rigging
- **Remote performance capture**: Capture performers via camera feeds from anywhere
- **Pre-vis from reference video**: Convert reference footage into animated performance data

---

## Requirements

- Video camera(s) for input (single or multiple views)
- GPU compute for real-time inference
- Standard motion capture post-processing pipeline

---
