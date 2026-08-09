---
title: MiniMax H3 Official Source Summary
category: source
summary: Primary-source record for MiniMax H3's audiovisual generation modes, limits, and structured prompt guides.
tags: [minimax-h3, ai-video, native-audio, prompting, source]
sources: 4
updated: 2026-08-09
source_path: https://huggingface.co/MiniMaxAI/MiniMax-H3
source_date: 2026-08
authors: [MiniMax]
ingested: 2026-08-09
---

# MiniMax H3 Official Source Summary

MiniMax H3 is an omni-modal generation system that accepts text plus optional images, video and audio, and generates video with native 32 kHz stereo audio. The model card documents output up to 2K and 15 seconds. [[MiniMax H3 Prompting Guide]] and [[MiniMax H3 Reference and Audio Workflow]] extract its two official prompt schemas.

## Confirmed modes

- **T2VA:** text-to-audio-video.
- **I2VA / FL2VA:** first-frame, last-frame, or first-and-last-frame image-to-audio-video.
- **Ref2VA / R2V:** reference-to-audio-video using images, videos and/or audio.

The Ref2VA model card permits up to nine images, three reference videos, and three audio clips, with a 12-file mixed-input maximum. The team request's five-image limit is therefore an operational authoring limit, not H3's documented maximum.

## Primary sources

1. [MiniMax H3 model card](https://huggingface.co/MiniMaxAI/MiniMax-H3)
2. [Base prompt-writing guide](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_base_en.md)
3. [Full-reference prompt-writing guide](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_ref_en.md)
4. [ComfyUI H3 integration announcement and examples](https://blog.comfy.org/p/minimax-h3-day-0-support-in-comfyui)

## Related pages

- [[MiniMax H3 Prompting Guide]]
- [[MiniMax H3 Reference and Audio Workflow]]
- [[MiniMax]]
