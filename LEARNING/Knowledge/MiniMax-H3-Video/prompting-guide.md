---
title: MiniMax H3 Prompting Guide
category: concept
summary: Official field schemas and shot-writing rules for MiniMax H3 text and image anchored audiovisual generation.
tags: [minimax-h3, prompting, t2v, i2v, audio-video]
sources: 2
updated: 2026-08-09
---

# MiniMax H3 Prompting Guide

This is the working companion to [[MiniMax H3 Official Source Summary]]. H3 prompts are audiovisual timelines, not visual-only descriptions: every meaningful visual, dialogue, diegetic sound and music layer has a named place.

## Base schema: T2VA and I2VA

Use exactly three labelled fields: `integrated_multimodal_description`, `overall_soundscape`, and `non_diegetic_music`. In the timeline, establish Shot 1's style/composition, visible subjects and positions, then actions, camera movement, dialogue and shot-specific diegetic sound. Later cuts use increasing timestamps such as `[Shot 2] At 00:03.500, the camera cuts to ...`.

For image-to-video, begin with the official first-frame instruction: `For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.` Preserve the image's identity, costume, composition, props and spatial relations, then describe action developing forward from it.

For first-and-last-frame work, state both frame alignments first and describe the visible transformation path; do not merely describe two disconnected stills. One continuous shot is the default.

## Audio rules

- Dialogue and singing occur in the timeline using a stable speaker ID and `<d>[Language] exact line</d>`.
- `overall_soundscape` contains ambience, physical SFX and non-verbal human sound; do not duplicate dialogue there.
- `non_diegetic_music` is audience-only score: specify instrumentation, tempo/rhythm and dynamics. Music heard by characters is diegetic and belongs in the timeline.
- Use `N/A` only for an absent layer (or complete silence in the soundscape when explicitly requested).

## Practical test

Before a run, identify: (1) opening frame/state, (2) one dominant action with a result, (3) camera motion or intentional cut, (4) speaker and exact dialogue if any, (5) ambient/Foley layer, and (6) audience-only music. If two of these are vague, simplify the shot before generating.

> ⚠️ Contradiction: H3's official base guide documents structured positive fields but no negative-prompt field. Do not copy negative-prompt defaults from [[LTX-2.3 Prompting Guide]] into H3 workflows without tool-specific evidence.

## Source

See the [official base prompt-writing guide](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_base_en.md) via [[MiniMax H3 Official Source Summary]].
