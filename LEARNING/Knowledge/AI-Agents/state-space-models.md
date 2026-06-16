---
title: State Space Models (SSMs) / Mamba
category: concept
summary: Architectural alternative to transformers for sequence modeling; bounded state size enables better efficiency at long-context tasks.
tags: [llm, mamba, state-space-models, transformers, architecture, research]
sources: 1
updated: 2026-04-19
---

# State Space Models (SSMs) / Mamba

A family of sequence modeling architectures that rival transformers, with key efficiency advantages for long-context tasks.

## Core idea

Transformers scale quadratically with sequence length (attention over all tokens). SSMs maintain a **bounded state** — a compressed representation of prior context — that updates recurrently. Result: linear scaling with sequence length.

## Mamba

The most prominent SSM architecture (Gu & Dao, 2023). Key properties:
- Selective state spaces — the model learns what to remember and what to forget
- Efficient at long-context tasks: audio, video, long documents
- Competitive with transformers on language tasks at similar parameter counts

## Why it matters for this wiki

- Potentially significant for **AI video generation** — video is long-sequence; SSMs could enable longer, more coherent video
- Relevant to **AI agents** with long context windows — more efficient long-context reasoning
- Worth tracking: if SSMs displace transformers at scale, tool selection and infrastructure choices shift

## Status (as of 2026-04)

Still primarily a research direction. Transformers dominate production deployments. Mamba-based models exist but haven't overtaken transformer-based frontier models.

> ⚠️ Track for developments: if Mamba-class models reach frontier performance, implications for agentic workflows and creative pipelines are significant.

## Related pages

- [[google-deepmind]]
- [[Synthesis/ai-agents-automation-overview]]
- [[notion-export-ai-agents-automation-n8n]]
