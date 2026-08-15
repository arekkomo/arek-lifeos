---
title: MiniMax Music 3 Prompting Guide
category: concept
summary: Structured Caption format, lyric/section-tag rules and hard limits for MiniMax-Music3 text-to-music, plus four behaviours measured on the Spark GB10 box that appear in no documentation.
tags: [minimax-music3, prompting, t2m, music, structured-caption, rrhub]
sources: 2
updated: 2026-08-15
---

# MiniMax Music 3 Prompting Guide

**Written 2026-08-15.**

## Sources

Official:

- <https://github.com/MiniMax-AI/MiniMax-Music3> — repository README, prompting section and API example.
- <https://huggingface.co/MiniMaxAI/MiniMax-Music3> — model card (README verified against the raw file at `/raw/main/README.md`).

Empirical:

- Bring-up runs on the Spark GB10 box, 2026-08-15. The four findings in *Measured behaviour* below were established on that hardware and are **not** in either official source.

### Evidence key

| Tag | Meaning |
|---|---|
| *(unlabelled)* | **Documentation.** Stated on the GitHub README or the HuggingFace model card. |
| **[MEASURED]** | **Observed on our own hardware**, Spark GB10, 2026-08-15. Undocumented anywhere upstream. This is the strongest evidence in this file — it is first-hand, not reported. |
| **[INFERENCE]** | Drawn by this author from the documented facts; not stated anywhere. |

Nothing here comes from community folklore. The model is new enough that no meaningful
third-party corpus exists, which is a feature: there is nothing unreliable to filter.

---

## What the model is

A text-and-lyrics-to-music model producing 32 kHz 16-bit stereo. Architecture, per the model card: an 8B global LLM (initialised from Qwen3-8B) modelling long-range structure over the first RVQ codebook, a 0.6B local LLM predicting the remaining acoustic codebooks, then a 2.4B flow-matching stage and a 123M Flow-VAE decoder. The music tokenizer is an 8-layer RVQ (16,384 semantic entries, 1,024 per acoustic codebook). Inference requires CUDA.

## The two inputs

The service exposes an OpenAI-speech-shaped API. The two content fields are distinct and must not be mixed:

| API field | Carries |
|---|---|
| `input` | **Lyrics** — the words to be sung, with optional section tags. |
| `instructions` | **Music description** — the style prompt. This is what a prompt-generating agent produces. |

Other parameters in the official request example: `model` (`minimax_ttm`), `response_format` (e.g. `wav`), `seed` for reproducibility, `max_new_tokens`, and `stream` (documented as `false` — streaming is not supported).

## Structured Caption — the recommended `instructions` format

The model card recommends a three-section Structured Caption:

- **Global Metadata** — genre, subgenre, BPM, key, scale, emotional progression, listening scenario, and production profile.
- **Vocal Details** — vocal gender, timbre, performance style, harmony, backing vocals, and vocal effects.
- **Arrangement** — primary and secondary instruments, section-level instrument evolution, groove, bass, percussion, textures, and spatial effects.

Note what this implies and where it differs from other engines: **BPM and key belong inside the caption here.** MiniMax has no separate metadata parameters — the only way to ask for 92 BPM in A minor is to write it into `instructions`. (This is the exact opposite of ACE-Step, where the docs tell you to keep metadata *out* of the caption because it travels in its own fields.)

"Emotional progression" and "section-level instrument evolution" are both explicitly part of the schema, so the caption is expected to describe **change over time**, not just a static texture. A caption that names a mood and stops is under-using the format.

### Shape

Write the three sections as labelled fields, one per line:

```text
Global Metadata: <genre, subgenre, BPM, key/scale, emotional arc, listening scenario, production profile>
Vocal Details: <gender, timbre, performance style, harmony/backing, vocal effects>
Arrangement: <lead and secondary instruments, how they enter/evolve per section, groove, bass, percussion, textures, spatial effects>
```

**[INFERENCE]** The labels are a faithful rendering of the documented three-section recommendation, but the model card does not print a labelled worked example, so the exact separator is **not** itself documented. Treat the labels as a formatting convention over a documented schema, not as a required syntax.

### When plain natural language is better

The card also documents a purely descriptive `instructions` string, given verbatim as:

> "A warm acoustic pop song with intimate female vocals, fingerpicked guitar, soft piano, and a gradual emotional build into a wide final chorus."

Structured Caption is described as the option for **precise control**. So:

- Use the **structured** form when the brief is specific: a named genre, a required tempo or key, a defined vocal, a required arrangement change.
- Use the **plain-language** form when the brief is a vibe rather than a spec, or when a structured caption would mostly be filled with invented specifics. A short honest sentence beats three sections of fabricated BPM and key.

Do not half-do it: a caption with two of the three labels and a trailing prose fragment reads worse than either pure form.

### Guidance, not guarantee

The card notes section tags and descriptions provide guidance rather than strict guarantees. Do not promise a user that a caption produced an exact BPM.

## Lyrics and section tags

The documented tag set, placed in `input`:

`[Intro]` `[Verse]` `[Pre-Chorus]` `[Chorus]` `[Post-Chorus]` `[Bridge]` `[Instrumental]` `[Solo]` `[Outro]`

The card describes them as explicit structural markers on their own lines — see the first measured finding below, which makes that non-negotiable in practice.

## Hard limits

| Limit | Value | Source |
|---|---|---|
| Tokenized text prompt | 5,000 tokens | Model card, verbatim: "The tokenized text prompt is limited to 5,000 tokens." |
| Audio generation | 9,000 acoustic frames | Model card, verbatim: "Audio generation is limited to 9,000 acoustic frames." |
| Frame rate | 25 frames/s → 9,000 frames ≈ 360 s | Card states `max_new_tokens` sets maximum audio frames at 25 fps; the card also describes support up to about five minutes. Treat ~5 minutes as the practical ceiling. |

5,000 tokens is a generous cap for a style prompt — it is not a licence to fill it. It is shared with the rest of the tokenized text, and there is no evidence that a longer caption steers better.

---

## [MEASURED] behaviour — Spark GB10, 2026-08-15

**Not in any documentation.** Established empirically on this box. All four items in this
section carry the [MEASURED] tag.

### 1. A section tag must sit on its own line

`[Verse] some text` on a single line **silently drops the text**. The correct form is:

```text
[Verse]
some text
```

There is no error and no warning — the lyric simply does not appear in the song. Any lyric block that comes in with inline tags must be reflowed before it is sent.

### 2. Song length is driven by lyric volume, not by a duration parameter

`max_new_tokens` is a **ceiling only**. The realised length is set by how much lyric text there is. Measured: a request for 120 s with four lines of lyrics produced **29 s** of audio.

Consequence for a style-prompt author: **a style prompt cannot make a short lyric into a long song.** Asking the caption for "an extended outro" or "a long instrumental break" will not buy duration that the lyrics do not support. If a target duration matters, the lever is the lyric length (or explicit `[Instrumental]` / `[Solo]` sections), not the caption and not `max_new_tokens`.

### 3. Several familiar sampling parameters are rejected, not ignored

The server **rejects** `temperature`, `top_p`, `top_k`, `voice`, `speed`, and `stream: true`. These are hard errors, not silently-dropped fields. Sending an OpenAI-style speech payload out of habit will fail the request. The usable knobs are `seed` and `max_new_tokens`.

### 4. Generation is roughly 5.5× slower than realtime on this hardware

A 60-second song takes on the order of five and a half minutes. Budget accordingly; this is a batch operation, not an interactive one.

---

## Anti-patterns

| Don't | Why |
|---|---|
| Put lyrics, or a paraphrase of them, in `instructions` | Lyrics have their own field (`input`). |
| Put style description in `input` | It will be treated as words to sing. |
| Write a tag and its lyric on one line | Measured: the lyric is silently dropped. |
| Ask the caption for a longer song | Measured: length follows lyric volume; the caption cannot override it. |
| Send `temperature` / `top_p` / `top_k` / `voice` / `speed` / `stream:true` | Measured: rejected by the server. |
| Fabricate a BPM and key to fill out the structured form | The card offers plain natural language precisely for briefs that lack a spec. |
| Describe only a static texture | The schema asks for emotional progression and section-level instrument evolution. |
| Add a negative prompt | No negative-prompt field is documented for this model. |

## Worked example (structured)

Brief: "moody late-night drive, female vocal". Target ~3 minutes, English, lyrics with `[Verse]` / `[Chorus]` / `[Bridge]`.

```text
Global Metadata: dark synthwave with alt-pop leanings, 92 BPM, A minor, nocturnal and
introspective opening that tightens through the second verse and opens wide at the final
chorus, late-night driving music, late-80s analog production with tape saturation and a
wide stereo field.
Vocal Details: female lead, breathy and close-mic'd low-mid timbre, restrained and
conversational in the verses, full-voiced and sustained in the choruses, doubled octave
harmony on the chorus hook, light plate reverb and a slow quarter-note delay throw.
Arrangement: arpeggiated analog bass synth and warm pad hold the verses with a simple
gated-reverb drum machine; a chiming electric guitar enters at the pre-chorus; the chorus
adds sustained brass-like synth stabs and a busier hi-hat pattern; the bridge strips to pad
and voice before the full arrangement returns for the last chorus; outro decays on the
arpeggio.
```

## Worked example (plain language)

Same brief, but no tempo or key specified and the user wants room to be surprised:

```text
A moody late-night synthwave song with a breathy female lead, an arpeggiated analog bass
line and warm pads under sparse verses, opening into a wide, reverb-soaked chorus before
stripping back to voice and pad for the bridge.
```
