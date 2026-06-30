---
title: "Goku — Million-Scale Instruction-Based Video Editing Dataset and Benchmark"
category: source
summary: 2M-pair dataset extending video editing from appearance-only to multi-task structural manipulation, with dual-branch Goku-Edit model using MLLM text encoder and dedicated mask branch.
tags: [video-editing, benchmark, dataset, instruction-following, dual-branch, MLLM, ComfyUI-relevant]
sources: 1
source_path: "arXiv 2606.30599"
source_date: "2026-06"
authors: ["Sen Liang", "Cong Wang", "Zhentao Yu", "Fengbin Guan"]
ingested: "2026-06-30"
updated: "2026-06-30"
---

# Goku: Million-Scale Universal Dataset for Instruction-Based Video Editing

## Overview

Goku addresses a gap in instruction-based video editing: existing datasets (VE1K, InstructPix2Pix-Video) focus narrowly on single-task appearance edits. Goku provides 2M instruction-aligned video editing pairs covering multi-task and structural manipulations — including precise subject movement control.

## Dataset Construction Pipeline

The authors decompose complex edits into controllable sub-problems:

1. **Task decomposition** — Structural edits (motion, layout) separated from appearance edits (style, color).
2. **Progressive filtering** — Three-stage reliability filter: synthetic fidelity check, instruction alignment score, human verification sample.
3. **Scale** — 2M pairs total. Covers 7 edit categories including object insertion, removal, style transfer, attribute change, motion control, structural layout, and combined multi-task edits.

## Goku-Edit Architecture

The paper proposes an associated model architecture:

- **MLLM text encoder** — Uses a multimodal LLM to parse complex editing instructions into structured representations, replacing standard CLIP encoders.
- **Decoupled dual-branch design** — Dedicated mask branch handles structural control signals. Main branch focuses on appearance rendering. Separation reduces cross-task interference.
- **Training setup** — Trained on Goku dataset with 504×504 resolution at video length of 16 frames.

## Goku-Bench Evaluation

A held-out benchmark of 1,000 human-verified test cases introduces 7 editing-specific metrics:

| Metric | Measures |
|--------|----------|
| Instruction Following (IF) | Adherence to edit command |
| Structural Fidelity (SF) | Preservation of unedited scene structure |
| Appearance Consistency (AC) | Coherence of edited appearance |
| Temporal Smoothness (TS) | Frame-to-frame continuity |
| Artifact Score (AS) | Presence of visual artifacts |
| Motion Alignment (MA) | Accuracy of motion instructions |
| Multi-Task Coherence (MC) | Coordination across simultaneous edits |

Goku-Edit achieves up to +8% improvement over open-source baselines on instruction following. Tested against [[ComfyUI]]-compatible video diffusion models and standalone editing frameworks.

## Relevance to Current Workflows

Goku's structural editing taxonomy maps directly to workflows in [[Video Diffusion Transformers]] and [[AI Video Generation Tools]]. The dual-branch architecture has parallels with [[FreeStory]]'s entity-grounded feature reuse approach, where control signals are separated from content generation. ComfyUI integration is feasible through custom node adaptation of the mask branch output.

## Key Numbers

- 2M training pairs
- 7 edit categories  
- 1,000 test cases in Goku-Bench
- +8% instruction following vs. open-source baselines
- 504×504 resolution, 16-frame sequences

---

*Source: https://arxiv.org/abs/2606.30599*
