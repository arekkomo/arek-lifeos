---
title: "ARDY Prompt Pattern Library"
aliases: ["ARDY Prompt Pattern Library"]
category: concept
summary: Reusable terse prompt patterns for locomotion, gestures, pose changes, and short ordered human-motion sequences in ARDY.
tags: [ardy, text-to-motion, prompt-library, locomotion, gestures, choreography]
sources: 1
updated: 2026-08-09
---

# ARDY Prompt Pattern Library

These patterns follow the short declarative style of ARDY's official preset list. They are authoring templates, not claims that a particular checkpoint guarantees every result; primary evidence is in [[NVIDIA ARDY — Official Source Summary]].

## Locomotion

- `A person is walking.`
- `A person walks forward.`
- `A person is walking backwards.`
- `A person side steps to the right.`
- `A person walks forward elegantly.`

Use a root path, waypoint, or target velocity when the route, heading, arrival point, or speed must be exact. [[ARDY Streaming Prompt and Constraint Workflow]]

## Single visible action

- `A person jumps backwards.`
- `A person is kicking with their right leg.`
- `A person waves with their right hand.`
- `A person is standing.`

Name the laterality only when it matters. Avoid stacking multiple competing gestures into one beat.

## Pose transition and short sequence

- `A person bows down and then stands upright.`
- `A dancer walks forward, then turns to the left.`
- `A performer raises both arms, then lowers them to their sides.`

Keep the order observable and short. For choreography over multiple beats, use prompt changes on the timeline and explicit keyframes at the poses that cannot drift. [[ARDY Text-to-Motion Prompting]]

## Repair ladder

1. Reduce to one action if the result is mixed.
2. Add direction or body part if the action is wrong-sided or ambiguous.
3. Add one `then` transition if the order is missing.
4. Move path/pose/contact demands out of text and into constraints.
5. Review contact and constraint following before adding prose. [[ARDY Motion Quality Review]]
