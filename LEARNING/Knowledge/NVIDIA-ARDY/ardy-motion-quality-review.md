---
title: "ARDY Motion Quality Review"
aliases: ["ARDY Motion Quality Review"]
category: concept
summary: A review checklist for semantic action, transitions, path/pose adherence, contact quality, and reproducible ARDY iteration.
tags: [ardy, quality-control, foot-skate, constraints, motion-generation]
sources: 1
updated: 2026-08-09
---

# ARDY Motion Quality Review

Evaluate ARDY as motion data before sending it to retargeting, animation, or rendering. The official output includes joints, rotations, root positions, contacts, FPS, and prompt text; the demo can show foot contacts and end-effector orientation. [[NVIDIA ARDY — Official Source Summary]]

## Review order

1. **Action:** Does the body perform the requested primary verb?
2. **Laterality/direction:** Is the named limb, travel direction, or turn correct?
3. **Beat order:** Does `then` produce the desired before/after transition?
4. **Spatial adherence:** Does the root path, waypoint, keyframe, or end-effector target hold?
5. **Contact:** Are feet stable at intended planted moments? Is foot skating acceptable?
6. **Continuity:** Does a prompt change retain a usable transition from prior motion?

## Controlled iteration

Change one variable per rerun: prompt wording, timeline change point, one constraint family, history context, or seed. Batch mode supports fixed seeds and multiple samples; preserve the prompt, seed, model, duration, and session/constraint file when comparing results. [[NVIDIA ARDY — Official Source Summary]]

## Officially documented corrective controls

The demo’s optional post-processing is intended to reduce foot skating and improve constraint following, though it is slower and disabled by default. The command-line generator also exposes `--no-postprocess`; its code disables the post-process path for G1 because it does not work well for that model. Treat this as model-specific behavior, not a universal clean-up guarantee. [[NVIDIA ARDY — Official Source Summary]]

## Escalation

- Wrong action → simplify the text to one action.
- Wrong placement → add/repair the appropriate spatial constraint.
- Bad transition → change the timeline point or increase usable history context.
- Foot/contact failure → inspect contact visualization and test post-processing on compatible models.
- Need a cinematic result → retarget/render downstream; ARDY itself is not a video renderer.

## Related

- [[ARDY Prompt Pattern Library]]
- [[ARDY Streaming Prompt and Constraint Workflow]]
- [[ARDY]]
