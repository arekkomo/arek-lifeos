---
title: "NVIDIA ARDY — Official Source Summary"
aliases: ["NVIDIA ARDY — Official Source Summary"]
category: source
summary: Primary-source record for NVIDIA ARDY, an interactive autoregressive text-to-motion system with live kinematic control.
tags: [nvidia, ardy, text-to-motion, human-motion, prompt-engineering, kinematic-constraints]
sources: 3
source_path: https://github.com/nv-tlabs/ardy
source_date: 2026-07
authors: [NVIDIA Toronto AI Lab, Kaifeng Zhao, Mathis Petrovich, Haotian Zhang, Tingwu Wang, Siyu Tang, Davis Rempe]
ingested: 2026-08-09
updated: 2026-08-09
---

# NVIDIA ARDY — Official Source Summary

ARDY is NVIDIA's autoregressive diffusion system for interactive skeletal motion generation. It accepts streaming text and optional root-path, waypoint, full-body-keyframe, and sparse joint-position/rotation constraints; it outputs motion data rather than rendered video. [Official repository](https://github.com/nv-tlabs/ardy) · [NVIDIA project page](https://research.nvidia.com/labs/sil/projects/ardy/) · [ACM TOG record](https://dl.acm.org/doi/10.1145/3811284)

## What the official material actually says about prompts

NVIDIA does not publish a long natural-language prompt formula or a negative-prompt system. The repository's shipped presets are short, declarative human-action sentences: "A person is walking," "A person jumps backwards," "A person is kicking with their right leg," and sequential actions such as "A person bows down and then stands upright." This supports a conservative working rule: write one body action, its direction/body part, and—only when needed—its ordered next beat. [Repository presets](https://github.com/nv-tlabs/ardy/blob/main/scripts/interactive_demo/common.py)

The demo applies a changed text prompt from the current frame forward, so ARDY is designed for timed re-direction rather than a single cinematic master prompt. Long-horizon spatial intent belongs in its explicit constraints: root trajectory/waypoints, keyframes, or end-effector joints. [Interactive-demo guide](https://github.com/nv-tlabs/ardy#interactive-demo)

## Scope and limits

Released checkpoints are currently for the generic Core skeleton and Unitree G1; the repository describes a SOMA body-model checkpoint as forthcoming. ARDY's output files include joints, rotations, root positions, contacts, FPS, and source text, making it an upstream blocking/animation component rather than an image or video generator. [Checkpoint and output documentation](https://github.com/nv-tlabs/ardy#checkpoints)

> ⚠️ Contradiction: [[LTX-2.3-Prompting-Guide]] uses cinematography, lighting, appearance, and camera language because it conditions rendered video. Those tokens are not documented ARDY controls. For ARDY, describe the performer’s motion; use constraints for spatial precision and a downstream renderer for shot design.

## Related pages

- [[ARDY]] — original Motion-Capture source page
- [[ARDY Text-to-Motion Prompting]] — operational prompt rules
- [[ARDY Prompt Pattern Library]] — reusable prompt forms
- [[ARDY Streaming Prompt and Constraint Workflow]] — temporal and spatial control
- [[ARDY Motion Quality Review]] — evaluation and iteration loop
