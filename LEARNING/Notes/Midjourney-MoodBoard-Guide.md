---
title: Midjourney Mood Board Prompting Guide
category: note
summary: Step-by-step guide for creating structured Midjourney mood boards — from concept to reference generation, including parameter selection and iteration techniques
tags: [midjourney, prompt-engineering, mood-board, visual-research, prompt-parameters]
sources: 1
updated: 2026-07-04
---

# Midjourney Mood Board Prompting Guide

**Comprehensive guide for creating mood boards in Midjourney.** Structured approach to generating visual references directly from creative concepts — essential for pre-production and storyboarding.

## Step-by-Step Process

### 1. Define the Emotional Context
Start with broad emotional/thematic descriptors before any specific imagery:
- Film, show, or concept name (if applicable)
- Overall mood/feeling desired
- Color palette references
- Artistic influences/comparisons

### 2. Select Core Visual Elements
Choose what to reference directly vs. describe through prompts:
- **Direct upload**: Best for existing artwork, photos, architecture
- **Prompted**: Use when starting from conceptual descriptions
- **Hybrid**: Mix of uploaded references + text guidance works best

### 3. Structure the Prompt Layers

**Layer 1: Subject/Scene** — what's in the frame
`A coastal lighthouse at sunset`

**Layer 2: Style Reference** — visual treatment
`cinematic photography, anamorphic lens flare`

**Layer 3: Composition Rules** — framing and angle
`wide-angle shot, rule of thirds, leading lines`

**Layer 4: Technical Parameters**:

| Parameter | What it does | Typical values |
|---|---|---|
| `--ar` | Aspect ratio | `--ar 2.39:1`, `--ar 16:9`, `--ar 2.76:1` |
| `--v` or `--version` | Model version | `--v 6.0`, `--v niji 6` |
| `--s` or `--stylize` | MJ artistic interpretation intensity | `--s 50-250` for subtle, `--s 750-1000` for strong artistic effect |
| `--c` or `--chaos` | Diversity of output per prompt | `--c 80` = high variety (useful in mood boards) |
| `--tile` | Seamless repeating texture mode | For background elements/patterns |

### 4. Refine Through Iteration

**When images don't match your intent:**
- Adjust specific element descriptors rather than rewriting entire prompt
- Use "variations" (V1-V4/U1-U4) to explore compositional options
- Add `--no` parameter to explicitly exclude unwanted elements
- Increase/decrease stylize value based on how artistic vs literal you need it

## Advanced Techniques for Mood Board Production

### Reference Mixing Strategy
For cohesive mood boards, upload multiple reference images in the same prompt:
1. Start with one strong base image (style anchor)
2. Add secondary references as composition guide
3. Use weight syntax `::` to control influence balance

### Batch Generation for Variety
Generate 4 variations of each key compositional idea:
- **V1**: Direct variation of the prompt
- **V2**: Slight rephrasing of descriptors
- **V3**: Swap color/texture emphasis
- **V4**: Change aspect ratio to test different framing

### Parameter Optimization

| Mood Board Goal | Recommended Config | Rationale |
|---|---|---|
| Consistent palette | Low chaos (`--c 10`), high stylize (`--s 250`) | Tight color consistency across images |
| Exploration phase | High chaos (`--c 80`), medium stylize (`--s 100`) | Maximum compositional variety |
| Reference accuracy | Low chaos, low reference weight, `--no artistic` elements | Faithful reproduction of references |

> ⚠️ Cross-domain: Mood board output feeds directly into pre-production workflow. Consider exporting as ComfyUI reference inputs for subsequent AI video generation — the visual language established in mood boards should be preserved through to production.

## Key Prompt Structures
1. `subject + style + framing + parameters` (standard)
2. `multiple references + shared aesthetic description` (reference mixing)
3. `emotional context + visual translation → prompt` (conceptual approach)

> **Pro tip:** Save your successful parameter combinations as templates for each production phase (concept, pre-vis, final). Consistency across phases is critical for mood board effectiveness.

```
## [2026-07-04] ingest | Mood Board Guide
Captured substantive content (3.1KB) from Notion dump as operational guide note. Source: raw/dtb_export_archive_2026-07-04/InspiraUI.md
```
