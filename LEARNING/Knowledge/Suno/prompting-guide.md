---
title: Suno Style Prompting Guide
category: concept
summary: How to write Suno Style-field prompts, with every claim graded by evidence quality — because the public Suno prompting corpus is largely unreliable and much of it is fabricated or laundered from two 2024 documents.
tags: [suno, prompting, t2m, music, style-field, evidence-graded]
sources: 30
updated: 2026-08-15
---

# Suno Style Prompting Guide

**Written 2026-08-15.**

## Read this first: the corpus is unreliable

This guide is graded rather than comprehensive, and that is deliberate. Suno publishes very little prompting documentation. The gap has been filled by a large community corpus that does not survive inspection:

- A widely-upvoted "GOD MODE MANUAL" contains **fabricated numeric scoring systems** presented as mechanism.
- A widely-upvoted "V5.5 Prompt Structure" post was **admitted by its own author** to be an LLM summary of release notes that do not exist.
- Most circulating "1000+ meta tags" lists descend from **two 2024 documents**, republished with 2026 datelines and no new testing.
- **Two sources agreeing is usually one source copied.** At least one prominent 2026 field guide lifted its slider tables and Exclude mappings wholesale from an earlier post. Apparent corroboration in this corpus is frequently citation laundering.

So the value of this file is its **epistemics, not its coverage**. Every substantive claim below carries a status tag. Do not promote a claim to a higher tier when quoting this file elsewhere.

| Tag | Meaning |
|---|---|
| **[OFFICIAL]** | Stated on a Suno-owned domain (help.suno.com, suno.com/hub, /blog, /release-notes). |
| **[WELL-EVIDENCED]** | No official statement, but consistently reported by practitioners across genuinely independent sources. Safe to act on. |
| **[SINGLE-SOURCE]** | One source only, or several that trace to one. Act on cautiously. |
| **[CONTESTED]** | Sources actively disagree, including official vs community. Do not present as settled. |
| **[CARGO CULT]** | Circulates widely with no evidence in either direction, or is demonstrably fabricated. Do not use. |

A methodological warning that applies to anyone extending this file: during research, an automated page summarizer **materially inverted a source** — reporting that technical descriptors outperform vague emotional language when the raw page said the exact opposite. **For any claim that will shape a skill, read the raw text, not a summary.**

## Sources

Official (Suno-owned):

- <https://suno.com/hub/how-to-make-a-song> — the single most useful official page; the only official documentation of bracket syntax found.
- <https://suno.com/hub/create-music-with-ai>
- <https://help.suno.com/en/articles/5782849> — Detailed Style Instructions (V4.5 prose guidance)
- <https://help.suno.com/en/articles/5782977> — Better Prompts in Lyrics
- <https://help.suno.com/en/articles/5782593> — What's new in V4.5
- <https://help.suno.com/en/articles/9010177> — Music Glossary (Suno's own prompt vocabulary)
- <https://help.suno.com/en/articles/3161921> — Exclude
- <https://help.suno.com/en/articles/6141377> — Creative Sliders
- <https://help.suno.com/en/articles/3198209> — Does Suno moderate songs?
- <https://suno.com/community-guidelines>
- <https://help.suno.com/en/articles/3484161> — Personas; <https://help.suno.com/en/articles/11362433> — Voices FAQ
- <https://help.suno.com/en/articles/2872257> — Covers; <https://help.suno.com/en/articles/6882817> — Add Vocals
- <https://help.suno.com/en/articles/10625537> — Suno Sounds
- <https://help.suno.com/en/articles/5804417> — Creative Prompt Boosting
- <https://help.suno.com/en/articles/6141505> — Song Editor
- <https://suno.com/release-notes>, <https://suno.com/blog/v5-5>, <https://help.suno.com/en/articles/5782721> (Model Timeline — stale, omits v5.5)

Community (all read directly; quality varies wildly — see grading):

- <https://docs.sunoapi.org/suno-api/generate-music> — third-party API spec; best available limits evidence
- <https://blakecrosley.com/guides/suno> (13 May 2026), <https://blakecrosley.com/blog/suno-style-field-style-influence> (4 Aug 2026)
- <https://jackrighteous.com/en-us/pages/suno-ai-meta-tags-guide> (rev. 15 Aug 2026) — most epistemically careful source found
- <https://learnstemlab.com/suno-ai-song-control-metatags-guide> (Apr 2026)
- <https://raagengine.com/blog/suno-prompt-guide/> (15 Apr 2026)
- <https://aimusicapi.ai/en/blog/suno-ai-prompt-character-limits> (3 Jul 2026), <https://hookgenius.app/learn/suno-character-limits/> (Jul 2026)
- <https://sunoaiwiki.com/resources/2024-05-13-list-of-metatags/> — **2024, stale; ancestor of most circulating tag lists**

Not reachable: reddit.com (blocked from the research environment). Reddit-sourced claims reaching this file came via the coordinating session's own corpus review, not from pages read here.

---

## Product state, August 2026

**[OFFICIAL]** v5.5 shipped 26 Mar 2026 (Voices, Custom Models, My Taste). Neither its blog post nor its help article says anything about prompting, the Style field, or limits. Release notes through 2026: a lyrics-editor overhaul with song-structure labels (9 Jul), a **Duration slider** (20 Jul), Voices on mobile (7 Aug), Studio 2.0 (13 Aug). A BMG partnership announced 12 Aug names a future industry model that has **not** shipped.

**Unverified:** whether v5.5 is the default model in the create form. Not confirmable from any primary page.

---

## Style field vs Lyrics field

**[OFFICIAL]** Custom mode fields are **Lyrics**, an **Instrumental** toggle, **Styles** (labelled "Style of Music" in the Personas article), **Title**, and Advanced Options containing **Exclude**.

**[OFFICIAL]** The Style field is the musical description: genre, mood, instrumentation, tempo, vocal gender.

**[WELL-EVIDENCED]** **Text placed in the wrong field gets performed.** Style-like prose dropped into the Lyrics box is liable to be *sung*; bracketed cues can be sung aloud rather than interpreted. This is the best-attested behaviour in the whole corpus and it is the reason field separation is the first rule of Suno prompting. Note the honest caveat: **no official page documents it.** The nearest official-adjacent evidence is a community guide advising that when a bracketed cue is sung, you shorten it, isolate it on its own line, and strip sentence-like wording.

**[WELL-EVIDENCED]** The practical three-layer split: **Style** = the broad sound; **Lyrics** = section labels and local events; **Exclude** = removals.

**[SINGLE-SOURCE]** Section tags placed in the Style field are ignored or misinterpreted. One explicit source, but consistent with every other source's field-separation rule.

### The one place vocal tags invert

**[WELL-EVIDENCED]** **Vocal-type tags work better in the Style field than in the lyrics box.** This is the exception to "structure goes in lyrics" — vocal character (gender, timbre, delivery) belongs in Style, not as a bracketed tag among the lyrics. This is commonly inverted by people applying the field-separation rule too mechanically.

---

## Length

**[OFFICIAL]** No limits table exists. The entire help category tree, hub, blog and release notes were searched. Nothing.

**[SINGLE-SOURCE, but the best available]** A third-party API reseller documents per-model maxima, corroborated by two independent write-ups (which disagree with each other on the title field, suggesting they are not simply copies):

| | V4 | V4.5 / V4.5+ | V5 | V5.5 |
|---|---|---|---|---|
| style | 200 | 1,000 | 1,000 | 1,000 |
| lyrics | 3,000 | 5,000 | 5,000 | 5,000 |

**Working figure: ~1,000 characters of Style field on v4.5 and later.** State it as community-reported, never as official.

**[WELL-EVIDENCED]** Regardless of the ceiling, **brevity outperforms**. Fewer, sharper descriptors beat a long list. Aim far below the limit.

**[CARGO CULT]** Precise claims of the form "the first 20–30 words carry most of the weight". Unverifiable numerics with no mechanism behind them. Do not repeat.

---

## What actually steers Suno

**[OFFICIAL]** Suno's own worked style prompt, from the hub:

> Bright pop track, 110 BPM, female vocals, chorus with big synth hook, verse with intimate piano.

That single line officially sanctions genre, numeric BPM, vocal gender, instrumentation and per-section instrumentation inside the Style field.

**[OFFICIAL]** The hub lists specifiable dimensions: vocal characteristics (tone, gender, layering), instrumentation, tempo and key, and effects such as reverb or saturation.

**[OFFICIAL]** The **Music Glossary** is Suno's own suggested vocabulary, in nine buckets: tempo & rhythm (adagio, allegro, syncopation, groove); dynamics & expression (crescendo, staccato, legato, vibrato); song structure; melody & harmony (chord progression, major/minor, arpeggio, dissonance); genres; instrumentation & texture (orchestration, layering, timbre, sparse/dense); vocal techniques (falsetto, belt, melisma, scat, a cappella); production & effects (reverb, delay, compression, distortion, EQ); advanced (modulation, cadence, ostinato, coda). It suggests combining terms — "upbeat allegro pop".

**[WELL-EVIDENCED]** **Emotion outperforms engineering.** "Desperate" steers better than "minor key with sidechain compression". Suno responds to affective and characterful language; technical mixing jargon is largely inert. (This is also the specific claim an automated summarizer inverted — the raw source says emotion wins.)

**[WELL-EVIDENCED]** **Fewer, sharper descriptors.** Genre first, at most two genres. Three to five instruments, named as singular nouns. Past roughly seven descriptors the output reportedly goes muddy — over-constrained prompts produce a compromise that partially satisfies each term instead of committing to any.

**[OFFICIAL]** Era and decade: **no official guidance exists.** Not in the glossary, not on any hub page. Era words are in universal community use and are the standard substitute for a banned artist name (below), so they are usable — but nothing documents how well they land.

### BPM and key — genuinely contested

**[CONTESTED]** Officially, `110 BPM` appears in Suno's own example and the hub says you can specify tempo and key. Community-side, one detailed source lists exact BPM control among things that silently fail. **No source in either camp demonstrates tempo-accurate adherence.**

Honest position: BPM and key are *valid syntax* and cost little. Write them plainly (`92 BPM`, `D minor`) and treat them as a nudge, never a lock. Do not promise a user a tempo.

### Prose vs tags — also contested

**[CONTESTED]** Since V4.5 Suno's **own documentation endorses conversational prose** in the Style field, with a before/after that replaces `deep house, emotional, melodic` with a multi-clause sentence. Prevailing community practice insists on 4–7 comma-separated descriptors instead.

This is a real disagreement between the vendor and its user base and **must not be resolved by fiat in either direction**. Both forms are defensible. A compact comma-separated line is the safer default for a machine-generated prompt because it is harder to accidentally write something that reads as lyrics — which matters given the misplaced-text behaviour above.

---

## Structure and meta tags (Lyrics field)

**[OFFICIAL]** `[Verse]`, `[Chorus]`, `[Bridge]`, `[Intro]` are named as bracketed structure markers on one hub page. **That is the only official documentation of bracket syntax that exists.** The Music Glossary lists structure terms as prompt vocabulary but not as tags. The Jul 2026 lyrics-editor release note names "song structure labels" as a feature, which supports the concept but describes a UI affordance, not typed syntax.

**[SINGLE-SOURCE / COMMUNITY]** `[Outro]`, `[Instrumental]`, `[End]` — community convention only, despite universal use.

**[CARGO CULT]** The wider bracketed-tag universe — `[Guitar Solo]`, `[Female Vocal]`, `[Whispered]`, `[Build]`, `[Drop]`, and the SFX tag families (applause, rain, thunder, crowd, silence). **Zero official documentation.** The circulating lists trace largely to a 2024 wiki page. A meaningful negative signal: Suno ships **Suno Sounds** as a *separate* feature for generating SFX and ambience as standalone samples, and its article says nothing about SFX tags inside lyrics.

Some experienced practitioners report a subset working (`[Guitar Solo]`, `[Whisper]`, `[Choir]`, `[Fade Out]`, numbered `[Verse 1]`, case-insensitivity, and colon-parameterised `[Verse: whispered vocals, acoustic guitar only]`). That is **[SINGLE-SOURCE]** and untested. The most careful source in the corpus frames all of these as "prompt signals, not deterministic switches" and warns against tag stuffing.

**[SINGLE-SOURCE]** `[no vocals]` does **not** work — use the Instrumental toggle.

### Lyric-side conventions that are well-attested

**[WELL-EVIDENCED]** **Parentheses mark backing vocals** — `(oh oh)`, `(never again)`. Critically: **their content is performed.** Never put a production instruction inside parentheses; it will be sung.

**[WELL-EVIDENCED]** **ALL CAPS conveys intensity**, dosed to **1–3 words**. Capitalising a whole line does not scale the effect and degrades the read.

---

## What backfires

**[OFFICIAL — the hardest constraint in this file]** **Artist and public-figure names are actively blocked.** Suno's moderation article names artist/public-figure names, copyrighted or trademarked terms, derogatory or defamatory language, and excessive profanity. Consequences are real: the song may **not generate at all**; staff may force it to Link Only; or it may be **removed without notice**. The Community Guidelines separately prohibit impersonation, reproducing existing songs, and using a real person's voice or likeness without permission.

**The fix is always the same: translate the artist into traits.** Era + production texture + instrumentation + vocal character. "Reminiscent of Bon Iver" becomes "falsetto male vocal, heavily layered harmony, processed and intimate, sparse folk arrangement".

**[SINGLE-SOURCE / mechanism unverified]** The observed failure is a pre-generation error about inappropriate material, triggerable from the prompt, title, lyrics *or* Style field. Community write-ups describe a punctuation-stripping substring matcher plus a contextual scorer. **That mechanism is asserted, never demonstrated** — do not state it as fact. The actionable rule stands regardless.

**[WELL-EVIDENCED]** Too many genres, or contradictory genre stacking, yields a muddy compromise.

**[WELL-EVIDENCED]** Technical mixing jargon is largely inert. See "emotion beats engineering" above.

### Exclusions — the syntax is commonly inverted

**[WELL-EVIDENCED]** Two different syntaxes, one per field, and they are **not** interchangeable:

| Where | Syntax |
|---|---|
| Inline in the **Style** field | `no X` — e.g. `no drums` |
| In the **Exclude** field | bare `X` — e.g. `drums` |

Writing `no drums` into the Exclude field is the common error; it reads as a request rather than an exclusion.

**[OFFICIAL]** Exclude lives in Advanced Options in Custom mode and takes "any information (instruments, etc) that you do not want in your track".

**[SINGLE-SOURCE]** Exclude is generative guidance rather than deletion: results vary run to run, and it fails outright when the Style field positively asks for the excluded thing. Pair every exclusion with a positive replacement.

---

## Cargo cult — circulating, unsupported, do not use

Listed explicitly because prompt authors will encounter and try them:

- **Numeric weighting** — `rock:1.5`, `(dark:1.2)`, Stable-Diffusion-style emphasis. **No evidence in either direction**; the syntax appears nowhere in the corpus, neither endorsed nor debunked. Imported from image models by assumption.
- **Tilde-for-vibrato** — `hold~~~`.
- **"MAX-MODE" token blocks** and similar named power-user modes.
- **JSON-structured Style fields.**
- **Word morphing** for pronunciation control.
- **The `-style` filter bypass** — a claimed trick for smuggling artist names past moderation. Beyond being unevidenced, attempting it courts the documented removal consequences.
- **Repetition-for-weight** and ALL-CAPS-for-emphasis *in the Style field* (as distinct from the well-attested ALL CAPS for vocal intensity in lyrics).
- **Numeric slider recommendations.** The sources offering ranges for Weirdness and Style Influence explicitly disclaim them as non-official. The **[OFFICIAL]** documentation is only: Weirdness runs Safe→Chaos with **50% as the normal/expected result**; Style Influence runs Loose→Strong and controls how closely output follows the style input; Audio Influence appears only with an audio upload. That is the whole of it.

---

## What the Style field does not need to carry

**[OFFICIAL]** Suno has dedicated features for several things a prompt author might otherwise cram into the style text:

- **Duration slider** (v5.5, web) — song length is not a style concern.
- **Instrumental toggle** — not `[no vocals]`.
- **Exclude** — removals.
- **Personas / Voices / Custom Models / My Taste** — vocal and stylistic identity. Selecting a Persona **auto-populates Style of Music**.
- **Covers** — keeps the melody, changes the style.
- **Song Editor, Replace Section, Extend, Add Vocals, Remaster, stem separation, Studio 2.0** — post-generation surgery. The style prompt need not encode arrangement fixes.
- **Creative Prompt Boosting / Enhance** — expands a terse style prompt in-app, which is a further argument for writing short.

**[OFFICIAL]** One exception where more is required: for **Add Vocals**, describe *both* the existing instrumental and the desired vocal in the style box.

---

## Recommended Style-field shape

Not a formula — a default that respects the well-evidenced material and avoids everything contested:

```text
<genre>, <optional second genre>, <era or production character>,
<vocal gender + delivery>, <3-5 instruments, singular nouns>,
<2-3 emotional/atmospheric words>, <tempo feel>
```

Comma-separated, well under the ~1,000-character community-reported ceiling — a couple of hundred characters is plenty. No artist names. No section tags. No lyrics. No mixing jargon.

### Worked example

Brief: "moody late-night drive, female vocal".

```text
dark synthwave, late-80s production, breathy female vocal, close and restrained,
analog synth bass, warm pads, gated reverb drums, electric guitar, melancholic,
nocturnal, yearning, mid-tempo
```

---

## Explicit gaps — do not fill these by inference

1. **All character limits.** No official source exists.
2. **Misplaced text.** No *primary* source documents what happens when lyrics go in Style or style prose goes in Lyrics — only strong, consistent community attestation that it gets performed.
3. **Non-structural bracketed tags** — zero official documentation; lists descend from a 2024 wiki.
4. **`[Outro]`, `[Instrumental]`, `[End]`** — community only. Only `[Verse]/[Chorus]/[Bridge]/[Intro]` have official mention.
5. **BPM adherence** — valid syntax, adherence never demonstrated; one source claims silent failure.
6. **Key adherence** — same.
7. **Numeric/weighted syntax** — no evidence found in either direction.
8. **The 4–7 descriptor sweet spot and the ">7 goes muddy" claim** — plausible and multi-source, but no published measurement.
9. **Moderation matcher internals** — asserted, never demonstrated.
10. **Slider numeric recommendations** — disclaimed as non-official by their own authors.
11. **Whether v5.5 is the create-form default** — not confirmable from a primary page.
