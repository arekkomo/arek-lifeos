---
title: AI Video Generation
category: concept
summary: The landscape of AI tools and techniques for generating video from text, images, or other video — covering text-to-video, image-to-video, and video-to-video approaches.
tags: [ai-video, text-to-video, image-to-video, video-to-video, diffusion, generative-ai]
sources: 1
updated: 2026-04-19
---

# AI Video Generation

AI video generation covers three main paradigms, each with distinct tools and use cases.

## Three paradigms

### 1. Text-to-video
Input: text prompt → Output: video clip

Key tools: [[minimax|MiniMax]], [[runway-ml|Runway ML]], [[kling-ai|Kling AI]], [[open-sora|Open-Sora]]

Use: generating scenes from scripts; base layer for AI film production pipelines.

### 2. Image-to-video
Input: still image → Output: animated video

Key tools: Runway ML, Open-Sora, Kling AI

Use: animating concept art, storyboards, or AI-generated images into motion.

### 3. Video-to-video
Input: existing video → Output: stylized/transformed video

Key tools: [[domoai|DomoAI]], CMR M1 (hardware), Stable Diffusion-based pipelines, Lucy-Edit-ComfyUI

Use: style transfer, animation stylization, AI-guided editing.

## Production pipeline pattern

A typical AI film pipeline (from the knowledge base):
```
Script/prompt
  → ChatGPT (refine + structure)
  → MiniMax / Runway (video scene generation)
  → DomoAI (stylization, if needed)
  → DaVinci Resolve 19 (compile, color, edit)
```

## Research advances (early 2026)

- **Light-A-Video** — training-free temporally consistent lighting across video frames
- **Enhance-A-Video** (Feb 2025) — quality enhancement on top of existing generated video
- **ReVideo** — localized video editing: change motion AND content simultaneously with diffusion
- **Open-Sora** — open-source, self-hostable text-to-video

## Hardware AI

**CMR M1 AI Cinema Camera** — first camera with Stable Diffusion built in for in-camera video-to-video processing. Signals AI moving from software post-production into hardware capture.

## Agentic video generation

Next evolution: agents trained on prompting best practices that autonomously prompt video models — see [[agentic-creative-pipelines]]. Outperforms manual n8n workflows for complex creative pipelines.

## Related pages

- [[ai-animation]]
- [[ai-avatar-lipsync]]
- [[agentic-creative-pipelines]]
- [[minimax]]
- [[runway-ml]]
- [[kling-ai]]
- [[domoai]]
- [[open-sora]]
- [[Synthesis/ai-creative-tools-overview]]
- [[Synthesis/filmmaking-production-overview]]
