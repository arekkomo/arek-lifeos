---
title: "ARDY Streaming Prompt and Constraint Workflow"
aliases: ["ARDY Streaming Prompt and Constraint Workflow"]
category: concept
summary: Separate semantic motion prompts from spatial and temporal constraints when directing ARDY’s continuing motion stream.
tags: [ardy, streaming, constraints, waypoints, keyframes, text-to-motion]
sources: 1
updated: 2026-08-09
---

# ARDY Streaming Prompt and Constraint Workflow

ARDY combines text prompts with live kinematic controls. Use the text to name what the body is doing; use the constraint channel to specify where, when, or how precisely it must happen. [[NVIDIA ARDY — Official Source Summary]]

## Control allocation

| Need | Preferred ARDY control |
|---|---|
| Motion class or next performance beat | Short text prompt |
| Travel route or arrival point | Root trajectory or waypoint |
| Required whole-body pose at a time | Full-body keyframe |
| Hand/foot position or orientation | Sparse end-effector joint constraint |
| Locomotion heading and speed | Target velocity / target heading |
| Shot, lens, lighting, appearance | Downstream tool — not ARDY |

## Streaming direction loop

1. Start with one clear locomotion or action prompt.
2. Add a path/waypoint or target velocity if travel matters.
3. At the current frame, update the prompt to introduce the next performance beat.
4. Add keyframes or end-effector targets only for non-negotiable poses/contact.
5. Inspect the transition; keep a successful seed/session for comparison.

NVIDIA’s demo represents prompts as timeline segments and lets text updates take effect from the current frame. Its history-crop setting trades faster adaptation to prompt/constraint changes against more context for complex semantics and smoother transitions. [[NVIDIA ARDY — Official Source Summary]]

## Constraint-first warning

Do not attempt to encode a spatial brief such as “walk to the mark, plant the right foot at the chair, face north, and place the hand on the table” entirely in prose. Split it: text for `A person walks forward and stops`; root/waypoint for the mark; keyframe and end-effector constraints for the foot, heading, and hand placement.

## Related

- [[ARDY Text-to-Motion Prompting]]
- [[Interactive-Kinematic-Motion-Generation]]
- [[ARDY Motion Quality Review]]
