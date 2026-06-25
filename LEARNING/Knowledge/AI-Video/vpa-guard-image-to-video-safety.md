---
title: VPA-Guard and VVA-Bench for Image-to-Video Safety
category: source
summary: Benchmark (VVA-Bench) and defense framework (VPA-Guard) for visual prompt attacks on image-to-video generation models. Tests show attack success rates of 100% on Wan 2.7 and 74.8% on Veo 3.1. VPA-Guard uses retrieval-augmented reasoning to identify malicious intent in visual inputs, reducing attack success by 44.2% and harmfulness scores by 73.4%.
tags: [ai-video, image-to-video, safety, benchmark, adversarial, wan-2, veo-3]
sources: 1
source_path: arxiv/2606.25592v1
source_date: 2026-06
authors: [Yining Sun, Haoyu Kang, Jiajun Wu, Heng Zhang, Danyang Zhang]
ingested: 2026-06-24
updated: 2026-06-24
---

# VPA-Guard: Visual Prompt Attack Defense

Image-to-video models accept visual cues as control signals. [[wan-2]] and [[veo-3]] interpret arrows, sketches, or emojis in input images. Model orchestrates video dynamics from these elements.

Static visual prompts can be crafted as harmful instructions. They trigger unsafe content without text prompts. Existing benchmarks only cover text-based jailbreaks.

## VVA-Bench: First Safety Benchmark

VVA-Bench is the first benchmark for vision-centric attacks on video models. Tests include directional arrows, motion sketches, and emoji triggers. Results show high vulnerability:

| Model | ASR |
|-------|-----|
| Wan 2.7 | 100.0% |
| Veo 3.1 | 74.8% |

## VPA-Guard Defense

The defense uses retrieval-augmented detection:

- **Few-shot reasoning**: Identifies malicious intent before generation
- **Self-evolution**: Updates patterns from new attack variants
- **Results**: 44.2% ASR reduction, 73.4% harmfulness reduction
- **Utility preserved**: Legitimate user edits still work

## Practical Relevance

Partner nodes in [[comfyui-v026-kling-v3-turbo]] feed into local pipelines. I2V safety matters for automated generation chains. If user-submitted images drive video generation via [[n8n]], visual prompt attacks become supply-chain risk.

## Related Pages

- [[comfyui-v026-kling-v3-turbo]]
- [[wan-2]]
- [[veo-3]]
- [[ai-video-generation]]
- [[image-to-video]]
- [[adversarial-midjourney]]
- [[n8n]]
