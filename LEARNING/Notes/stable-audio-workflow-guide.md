---
title: Stable Audio Workflow Guide — Prompt Engineering for Text-to-Audio
category: note
summary: Comprehensive guide to Stable Audio workflow covering prompt engineering patterns, genre/era/tagging systems, structural organization (intro/verse/chorus), vocal style control, and multi-pass refinement strategies for AI music and sound design.
tags: [stable-audio, prompt-engineering, ai-music, workflow-guide, audio-workflow]
updated: 2026-07-04
---

# Stable Audio Workflow — Prompt Engineering and Generation Strategies

**Source:** Notion dump export (dtb Knowledge) | Category: Audio/Music production reference

## Prompt Architecture Framework
Stable Audio's prompt system uses structured tagging for genre, era, instrumentation, mood, and vocal attributes. Effective prompting requires understanding the model's learned category boundaries.

### Layered Prompting Strategy
1. **Genre layer** (primary signal) — "synthwave," "classical," "ambient"
2. **Mood/energy layer** (secondary modulation) — "melancholic," "uplifting," "tense"
3. **Instrumentation layer** (timbral control) — "piano-driven," "heavy bass," "strings and brass"
4. **Era/style layer** (aesthetic reference) — "80s production," "modern lo-fi," "baroque arrangement"

## Structural Patterns
- Long-form structure: `intro → build → climax → resolution` maps to standard musical forms
- Loop-friendly generations for SFX beds and ambient layers
- Short-form burst for hits, impacts, musical stings

## Multi-Pass Refinement Technique
1. Generate 3-5 variations with broad prompts
2. Identify promising seed/generation characteristics
3. Refine with narrower prompt specs based on which elements worked
4. Extend successful generations across longer durations

> **Synthesis Note:** Stable Audio's category tagging system reveals how the model's training corpus organized musical knowledge — genre, era, and instrumentation act as orthogonal axes in the model's latent space. Understanding these boundaries prevents wasted generation cycles where you're fighting against learned priors rather than working with them.
