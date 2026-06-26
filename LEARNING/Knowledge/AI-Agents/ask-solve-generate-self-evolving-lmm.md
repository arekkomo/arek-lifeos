---
title: Ask-Solve-Generate — Self-Evolving Unified Multimodal Understanding and Generation
category: concept
summary: Self-evolving training framework that improves both visual understanding and image generation in unified large multimodal models using only unlabeled images and internal consistency signals. No human annotations, preference labels, or external reward models required.
tags: [multimodal, self-evolving, vision-language, image-generation, self-consistency, unsupervised-training, BAGEL, BLIP3o]
sources: 1
source_path: arxiv/2606.27376
source_date: "2026-06"
authors: [Ritesh Thawkar, Shravan Venkatraman, Abdelrahman Shaker, Fahad Khan, Salman Khan, Rao Muhammad Anwer]
ingested: "2026-06-25"
updated: "2026-06-25"
---

# Ask-Solve-Generate — Self-Evolving Unified LMM Training

**arXiv:** 2606.27376 | **Published:** June 25, 2026
**Authors:** Ritesh Thawkar et al. (MBZUAI)

## Problem statement

Unified large multimodal models (LMMs) that handle both visual understanding and image generation still rely heavily on curated post-training supervision: human annotations, preference labels, or external reward/judge models. These are expensive to produce and limit autonomous self-improvement.

**Research question:** Can a unified LMM improve *both* understanding and generation abilities autonomously using only unlabeled images?

## Core architecture — Three internal roles

The framework decomposes training into three self-derived roles that generate their own supervision signals:

1. **Proposer** — Generates visual questions about input images (creates the curriculum)
2. **Solver** — Answers those questions and evaluates its own response quality (self-critique loop)
3. **Generator** — Synthesizes images conditional on understanding tasks (closed-loop generation)

Training uses only self-derived consistency signals throughout. No human annotations, no preference datasets, no task-trained judge models.

### Solver Token Entropy (STE)

To stabilize learning when sample-level consistency becomes unreliable, the framework introduces **Solver Token Entropy** — a continuous difficulty signal based on token-level prediction uncertainty from the Solver module. High entropy indicates uncertain predictions; low entropy means confident answers. This signals which samples should contribute more to the gradient update.

### Multi-scale internal evaluation (generation)

For image generation quality assessment, a two-pronged scheme:
- **Question-answer fidelity scoring** — Generated images are fed back through the Proposer-Solver loop; if the Solver can answer questions about the generated image consistently with the original intent, quality is confirmed
- **Cycle-consistent captioning** — Encoded → decoded caption loops verify semantic preservation across generation cycles

## Results

Method tested across three architecture families (architecture-agnostic):
| Model family | Architecture | Key result |
|---|---|---|
| BLIP3o | Diffusion LMM | +improvement on 8/8 understanding metrics |
| BAGEL | Rectified-flow LMM | +3.5% absolute on MMMU benchmark; GenEval: 82% → 85% |
| VARGPT-v1.1 | Autoregressive LMM | Consistent improvement across vision benchmarks |

Same role decomposition, reward logic, and training schedule applied uniformly across all three backbones. Each only needed its native prompting/generation interface.

## Practical implications for agentic pipelines

This approach is relevant to [[n8n]] and AI agent workflows where autonomous self-improvement without external supervision matters:

- Removes the need for curated datasets in LMM fine-tuning pipelines
- Self-evolving loop could be integrated into [[ai-agents]] that generate iterative visual content
- Architecture-agnostic design means it plugs into existing infrastructure with minimal changes
- The Proposer→Solver→Generator pipeline mirrors agentic workflow decomposition

## Code and model availability

Paper states code and models are publicly released. See arXiv 2606.27376 for links.

## Related pages

- [[ai-agents]]
- [[n8n]]
- [[notion-export-ai-agents-automation-n8n]]
- [[wan-streamer-v01-realtime]]
- [[free-story-character-consistency]]
