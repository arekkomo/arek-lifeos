---
title: DanceOPD — On-Policy Generative Field Distillation for Flow Models
category: concept
summary: Training framework that unifies text-to-image, local editing, and global editing in flow-matching models via on-policy generative field distillation, resolving capability interference during multi-skill training.
tags: [flow-matching, distillation, text-to-image, image-editing, model-training, generative-ai]
sources: 1
source_path: arxiv/2606.27377
source_date: "2026-06"
authors: [Wei Zhou, Xiongwei Zhu, Zelin Xu, Bo Dong, Yongyuan Liang, Lingdong Kong, Wei Liu, Tat-Seng Chua]
ingested: "2026-06-25"
updated: "2026-06-25"
---

# DanceOPD — On-Policy Generative Field Distillation

**arXiv:** 2606.27377 | **Published:** June 25, 2026
**Authors:** Wei Zhou et al. (NUS, SMU)

## Problem statement

Modern image generation models need to unify text-to-image (T2I), local editing, and global editing in a single architecture. These capabilities are not naturally aligned — they interfere during training:

- Editing tasks degrade T2I quality
- Global and local editing conflict with each other
- Existing multi-capability fine-tuning causes catastrophic forgetting of anchor skills

## Core method

DanceOPD frames generative model training as **field distillation over a shared flow state space**.

**Key mechanism:** Each capability (T2I, local edit, global edit) is defined as a *velocity field* over the shared ODE/flow-matching state space. Instead of standard off-policy distillation, DanceOPD routes each sample to its target capability field and queries a low-noise student-induced state before computing MSE loss against that field's velocity.

### Training pipeline

1. **Capability routing** — Each training sample is assigned to one expert field (T2I / local-edit / global-edit)
2. **On-policy query** — Student model generates its own rollout states under low noise, then queries the target field at those states
3. **Velocity MSE loss** — Standard flow-matching objective: minimize distance between predicted and target velocity

### CFG absorption

The framework also absorbs manually defined fields like classifier-free guidance (CFG) as capability sources. This means CFG can be learned implicitly rather than applied at inference time, reducing the 2× forward-pass overhead of standard CFG.

## Results

- Improves multi-capability composition across all tested configurations
- Stronger target capability performance while preserving anchor generation quality
- Validated on flow-matching DiT backbones with T2I + editing unified training
- CFG absorption shows quality comparable to unconditional CFG at half the inference cost

## Practical implications for ComfyUI workflows

DanceOPD provides a principled way to train unified image models that handle both generation and editing without degradation. For [[comfyui]] pipelines, this means:

- Single-model workflows for T2I + edit without model switching
- Potential reduction in VRAM since one model replaces two specialized checkpoints
- Inference-time CFG becomes optional if the model has absorbed it implicitly

## Relation to existing work

> ⚠️ Contradiction: [[fire-red-image-edit]] describes distillation as a path toward faster inference (distill + quantize → 4.5s/sample). DanceOPD uses distillation differently — not for speed, but for capability composition. Both are valid application paths of flow-model distillation.

The approach is related to knowledge distillation in [[flux-2-klein-architecture]] where BFL used KV-cache and model compression for efficiency, but here the goal is multi-skill composition rather than parameter reduction.

## Code availability

Paper states code will be released upon publication. Check arXiv page 2606.27377 for updates.

## Related pages

- [[flux-2-klein-architecture]]
- [[comfyui]]
- [[fire-red-image-edit]]
- [[ai-image-generation]]
- [[stability-ai]]
