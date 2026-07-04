---
title: "LocalDPO — Direct Localized Detail Preference Optimization for Video Diffusion"
category: concept
summary: LocalDPO is a post-training alignment framework for text-to-video diffusion that constructs preference pairs at the spatio-temporal region level rather than globally. It treats real videos as positive samples and generates negatives by locally corrupting masked regions, restoring only those regions with the frozen base model. A region-aware DPO loss restricts learning to corrupted areas, improving convergence speed over global DPO baselines on Wan 2.1 and CogVideoX.
tags: [dpo, preference_optimization, video_alignment, post_training, diffusion_reward]
sources: 1
updated: 2026-07-03
---

## Overview

Aligning text-to-video models with human preferences matters for quality. Global DPO methods fail at scale for two reasons.

Multi-sample ranking multiplies inference cost per prompt. Global labels are ambiguous when preferred and dispreferred videos differ across many dimensions. The optimizer receives diluted or contradictory signals.

LocalDPO solves both by localizing preference learning to corrupted regions.

## Method

### Automated Preference Pair Pipeline

Given a prompt and a real high-quality reference as the positive sample:

1. Apply random spatio-temporal masks to the real video.
2. Restore masked regions with the frozen base T2V model.
3. The result is a preference pair that differs locally at known coordinates.

One usable pair per prompt emerges from this process. Multi-sample ranking disappears entirely. No critic models or human annotation needed.

### Region-Aware DPO Loss

Standard DPO applies its loss over the full sequence. LocalDPO masks the loss to count only tokens in corrupted regions. The optimizer receives focused gradient signal instead of diluted feedback. Convergence accelerates because of this localization.

The base model stays frozen throughout training. Updates apply only to a lightweight adapter layer.

## Results

Tests used Wan 2.1 and CogVideoX backbones:

- Consistent improvement in fidelity metrics over global DPO
- Faster convergence since gradient signal is region-localized
- Lower data-collection cost with one pass per prompt

## Practical Implications

For ComfyUI users who run local fine-tuning, LocalDPO offers a post-training alignment step. It improves output quality without manual preference datasets. The frozen-base approach keeps the original checkpoint usable alongside the adapter.

Related to [[Shell-LCC]] which provides reward signals at inference time. LocalDPO works at training time while Shell-LCC works during sampling. They target different phases and could combine.

## Contradictions and Caveats

> Note: LocalDPO needs real reference footage as positive samples per prompt category. Signal quality drops in domains where real footage is scarce since the corruption approach requires a grounded baseline.

No contradiction with vault entries. Complements inference-time methods like [[DiffRGD]].

## Related Work

- [[Wan 2.1]]: Primary test backbone
- [[CogVideoX]]: Secondary test backbone
- [[Shell-LCC]]: Inference-time reward signals (complementary approach)
- [[DiffRGD]]: Riemannian guidance for distribution matching at inference time
- [[Prompt2Effect]]: Training-free adaptation, contrasts with post-training approach
- [[TrajLoc]]: Attention-level control in I2V at lower granularity
