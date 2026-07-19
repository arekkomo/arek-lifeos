---
title: "Long-Form Music-Conditioned Video"
category: concept
summary: Generating extended video that follows full-track musical structure while retaining motion continuity and character identity.
tags: [music-to-video, dance-video, long-horizon-video, temporal-consistency, audio-conditioning]
sources: 1
updated: 2026-07-19
---

# Long-Form Music-Conditioned Video

Music-to-video systems need two kinds of alignment:

1. **Global structure** — phrases, section changes, energy arcs, and planned choreography across the full track.
2. **Local continuity** — believable motion and identity within each short generated segment.

A hierarchical workflow separates these jobs: plan sparse global anchors/keyframes from the full audio context, then refine the intervening motion locally. This avoids treating a one-minute piece as one unbounded diffusion rollout.

## Library links

- [[Wan-Dancer]] — concrete Wan-based implementation: global keyframe video + local high-resolution refinement
- [[Suno Music Style Tags Guide]] — useful vocabulary for defining the track/style input upstream
- [[ARDY]] / [[HY-Motion-1.0]] — skeletal-motion alternatives when the goal is editable animation rather than a final raster video
- [[LongForcing]] — related long-horizon problem, but for causal video/world generation rather than music-driven choreography
