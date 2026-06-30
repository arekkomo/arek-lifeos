---
title: "Delta Forcing — Trust Region Steering for Interactive Autoregressive Video"
category: source
summary: Prevents teacher-induced drift in streaming autoregressive video generation by constraining unreliable supervision within an adaptive trust region, balancing event reactivity with temporal coherence.
tags: [autoregressive-video, streaming-generation, trust-region, interactive-video, conditional-bias, temporal-coherence]
sources: 1
source_date: "2026-05"
updated: "2026-07-01"
---

# Delta Forcing — Trust Region Steering for AR Video Generation

**arXiv:** [2605.14382](https://arxiv.org/abs/2605.14382) (v4)
**Domain:** Real-time streaming autoregressive video generation

## Problem: Conditional Bias in Teacher Supervision

When distilling a bidirectional teacher model into an autoregressive generator, the teacher may provide guidance that is condition-aligned but *trajectory-agnostic*. This biases the student toward locally valid but globally inconsistent frames — persistent drift after conditions change.

### The Drift Phenomenon

Existing approaches (distillation → streaming long tuning) work well for stable sequences but exhibit a structural weakness: when new events arrive during generation, the teacher's guidance may pull the trajectory away from temporal coherence in favor of matching the current condition *in isolation*. The model becomes reactive at the expense of consistency.

## Approach: Trust Region Constraint

Inspired by TRPO (Trust Region Policy Optimization) from reinforcement learning:

1. **Delta estimation**: Compute the latent delta between teacher trajectory and student trajectory
2. **Transition consistency scoring**: Higher delta → teacher is less reliable for this transition
3. **Adaptive balancing**: Blend teacher supervision with a *monotonic continuity objective*:
   - When delta is small (teacher aligns with continuity): follow teacher more
   - When delta is large (teacher diverges from trajectory): trust region shrinks, continuity dominates

This suppresses unreliable teacher-induced shifts while preserving responsiveness to genuinely new conditions.

## Results

- Significant improvement in temporal consistency metrics
- Event reactivity is maintained (no latency penalty)
- Works as a drop-in training regularization — no architecture changes needed

## Relevance to Pipeline

Directly relevant to any streaming/interactive video generation pipeline. Wan-Streamer (already indexed) uses autoregressive generation; Delta Forcing's trust region mechanism could prevent the kind of drift that makes long interactive sessions visually jarring. Also applicable to live VFX compositing where scene conditions change dynamically.

## Caveats

- Training-time technique, not inference-time — requires retraining or fine-tuning the student model
- Paper evaluates on navigation/robotic tasks; creative video applicability is architectural but needs empirical testing
- Trust region parameter tuning may be task-dependent
