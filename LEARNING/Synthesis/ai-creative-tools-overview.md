---
title: AI Creative Tools — Overview
category: synthesis
summary: High-level map of AI tools for image and video generation, covering Midjourney, video generators, and the broader generative media landscape.
tags: [ai-video, ai-images, midjourney, generative-ai, creative-tools]
sources: 1
updated: 2026-04-19
---

# AI Creative Tools — Overview

This synthesis covers the landscape of AI-powered tools for generating and editing images and video.

## Topic clusters

- **AI Image Generation** — text-to-image models, style control, inpainting, upscaling → [[ai-image-generation]]
- **AI Video Generation** — text-to-video, image-to-video, video-to-video, consistency → [[ai-video-generation]]
- **AI 3D Generation** — text/image-to-3D models and environments → [[ai-3d-generation]]
- **Diffusion model fine-tuning** — LoRA, DreamBooth, kohya_ss → [[diffusion-model-fine-tuning]]
- **[[midjourney|Midjourney]]** — dedicated tracker for prompts, versions, techniques

## AI Video Generation landscape (as of 2026-04)

| Tool | Paradigm | Strength |
|---|---|---|
| [[minimax\|MiniMax]] | Text-to-video | Full scene generation; production pipelines |
| [[runway-ml\|Runway ML]] | Text/image/video-to-video | Versatile; industry standard |
| [[kling-ai\|Kling AI]] | Text-to-video | Motion quality; often paired with Runway |
| [[open-sora\|Open-Sora]] | Text-to-video | Open-source; self-hostable |
| [[domoai\|DomoAI]] | Video-to-animation | Stylization of live footage |
| [[opusclip\|OpusClip]] | Video clipping | Automated short-form from long-form |

See full concept: [[ai-video-generation]]

## AI Avatar, Lipsync & Motion

- [[cap4d\|CAP4D]] — digital doubles from stills/short video
- [[move-ai\|Move AI]] — markerless motion capture, finger-level accuracy
- just-dub-it — ASR → translate → lipsync dubbing pipeline
- chatterbox — real-time voice cloning + streaming TTS

See full concept: [[ai-avatar-lipsync]]

## AI Image Generation landscape (as of 2026)

| Tool | Type | Strength |
|---|---|---|
| [[midjourney\|Midjourney]] | Hosted | Aesthetic quality; Pan/VR character consistency; Describe tool |
| [[flux\|Flux]] | API/integration | Editing + generation; customization |
| [[stability-ai\|Stable Diffusion]] | Open-source | Ecosystem (ComfyUI, LoRA, ControlNet); self-hostable |
| [[nvidia-edify\|NVIDIA Edify]] | Enterprise | 3D + image; clean quad topology; 4K PBR |

See full concept: [[ai-image-generation]]

## AI 3D Generation landscape (as of 2026)

| Tool | Input | Target |
|---|---|---|
| [[tripo-ai\|Tripo AI]] | Text / image / doodle | Consumer; rapid prototyping; 3D environments |
| [[nvidia-edify\|NVIDIA Edify]] | Text / image | Enterprise; production-ready topology |
| [[dejavu\|dejavu]] | Video / image | VFX; photogrammetry |
| stepfun Step1X-3D | Image | Open-source |

Key research: "Generating Worlds" (spatial intelligence); Katja Schwarz panoramic world generation.
See full concept: [[ai-3d-generation]]

## Diffusion model tooling

- [[comfyui\|ComfyUI]] — node-based UI; the standard for advanced local SD workflows
- [[diffusion-model-fine-tuning\|LoRA / DreamBooth (kohya_ss)]] — custom character/style training on top of SD

## Emerging pattern: Agentic creative pipelines

Agents trained on prompting best practices outperform manual n8n/Weave for complex creative generation. See [[agentic-creative-pipelines]].

## Key questions this wiki tracks

- Which tools excel at which use cases (realism, stylization, motion, coherence)?
- How do prompting strategies differ across tools?
- What are the best workflows for integrating AI-generated assets into real productions?
- How are capabilities evolving (model releases, benchmarks)?

## Related pages

- [[Synthesis/filmmaking-production-overview]] — where generated assets land in production
- [[Synthesis/ai-agents-automation-overview]] — automation of generation pipelines
- [[ai-video-generation]]
- [[ai-animation]]
- [[ai-avatar-lipsync]]
