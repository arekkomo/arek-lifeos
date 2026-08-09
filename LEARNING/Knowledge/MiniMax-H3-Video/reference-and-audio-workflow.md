---
title: MiniMax H3 Reference and Audio Workflow
category: concept
summary: R2V prompt method for explicitly retaining or transforming multiple visual references alongside voice, SFX and music.
tags: [minimax-h3, r2v, reference-images, dialogue, audio-video]
sources: 2
updated: 2026-08-09
---

# MiniMax H3 Reference and Audio Workflow

H3 Ref2VA uses six ordered sections: `subject_definitions`, `summary`, `retention_analysis`, `detailed_description`, `overall_soundscape`, and `non_diegetic_music`. This explicit relationship ledger is the control surface for references; write it before the shot description.

## Operational five-image method

Use only the references that have different jobs, ordinarily one to five images:

1. **Character identity** — face, wardrobe and silhouette.
2. **Key prop or costume detail** — only when it must survive the shot.
3. **Environment / grade** — location, palette, production design.
4. **Composition or pose** — a concrete first/key/last frame.
5. **Style or secondary subject** — only if it cannot be expressed from the preceding assets.

In `subject_definitions`, map each retained person/object/environment to `<Subject N>` and name the source `<Picture N>`. Use standalone `<Picture N>` only when it is an actual keyframe or composition anchor. The official model card permits up to nine images; five is a deliberate production constraint to keep each reference role clear.

## Video and audio references

Use `<Video N>` only for editing, continuation, or a whole-video source relationship. When a video supplies merely motion, cuts or rhythm, describe it as `reference generation`, not an edit. Use `<Audio N>` for copied audio, a voice timbre, music style, beat, dialogue/lyric content, SFX texture or continuity.

State the result honestly in `retention_analysis`: visual assets use `fully_preserved`, `partially_preserved`, `attribute_transfer`, or `weak_reference`; audio uses `fully_copy`, `partially_copy`, `reference`, or `weak_reference`.

## Synced dialogue recipe

1. Define the character as `<Subject 1>` and bind voice reference as `<Audio 1> ... for <Subject 1> (S1)`.
2. In the timeline, write `<Subject 1> (S1)` physically speaking and put the exact line in `<d>[Language] ...</d>`.
3. State mouth closure or the next facial action immediately after the line; for narration, say `says in an off-screen voiceover` and that lips remain closed.
4. Put score reuse/reference in `non_diegetic_music`; place ambience and Foley reuse/reference in `overall_soundscape`.

This keeps identity, lip activity, dialogue, ambience and score as distinct but synchronized instructions.

## Source

See the [official full-reference prompt-writing guide](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_ref_en.md) and [[MiniMax H3 Official Source Summary]].
