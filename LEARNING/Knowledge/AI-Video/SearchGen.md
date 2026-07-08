---
title: SearchGen — Agentic Visual Generation with Knowledge Boundary Discovery
category: concept
summary: Teaches visual generators to use search tools for world-knowledge-grounded generation by discovering a generator-specific knowledge boundary.
tags: [agentic-generation, search-augmentation, video-generation, image-generation, knowledge-boundary, benchmark]
sources: 1
source_path: arxiv/2607.05382
source_date: 2026-07
authors: []
ingested: 2026-07-07
updated: 2026-07-07
---

# SearchGen — Evolving the Knowledge Boundary in Agentic Visual Generation

## What It Is

Visual generators score only 21–28/100 on world-knowledge-grounded requests. Prompts about new characters or trending entities fall outside training data. Existing benchmarks test generative quality but not factual grounding.

[[SearchGen]] introduces SearchGen-Bench (20,839 prompts across 12 failure categories). It also ships with SearchGen-Corpus-1M for reproducible evaluation.

## The Knowledge Boundary Problem

Visual generators render well within training distribution. The bottleneck is structural: fixed corpora versus open-ended world knowledge. Naive search fails by injecting noise into prompts the generator already handles, degrading quality on in-distribution requests.

The solution is discovering the **generator-specific knowledge boundary**. This divides what a model has internalized from what requires external context. The boundary is hard to specify but discoverable through training.

## Method

### Teach-Then-Search Co-Training

1. **Teach phase**: Show the generator ground truth for borderline requests.
2. **Search phase**: Enable multimodal retrieval tools for genuinely unknown concepts.
3. **Co-training loop**: The agent learns which prompts to search versus generate directly. Improvement is monotonic as the knowledge frontier expands.

Even a minimal recipe produces steady gains. The paper frames this as recursive self-improvement infrastructure.

## Datasets & Benchmarks

| Resource | Size | Purpose |
|---|---|---|
| SearchGen-20K | 20,839 prompts | Training data across 12 failure categories |
| SearchGen-Bench | Paired with corpus | Evaluation benchmark (frontier generators: 21–28/100) |
| SearchGen-Corpus-1M | 1M multimodal items | Pre-executed search corpus for offline research |

All data and corpus released as a replayable harness.

## Practical Relevance

Directly applicable to [[ComfyUI]] agent workflows. The system decides whether to generate from internal priors or fetch external reference material.

- Character-reference pipelines in [[ComfyUI-Agent-Kit]]
- Fact-grounded image generation for storyboarding tools
- Avoiding prompt injection noise with vision-language search

## Related Work

- [[World Director]] — LLM-coordinated world simulation, similar agent-augmented approach
- [[FilmPort]] — Multi-generator orchestration where knowledge boundaries matter
- [[Gazer]] — Training-free mid-generation correction via VLM feedback.
  (Different error source: composition vs. world knowledge)
