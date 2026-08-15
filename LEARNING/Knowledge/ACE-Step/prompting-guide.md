---
title: ACE-Step 1.5 Prompting Guide
category: concept
summary: Caption (style) and lyrics rules for ACE-Step 1.5 text2music as it is wired into RealityRoveHub — acestep-v15-turbo DiT plus acestep-5Hz-lm-4B, with BPM/key/time-signature/language supplied as structured fields.
tags: [ace-step, prompting, t2m, music, caption, rrhub]
sources: 4
updated: 2026-08-15
---

# ACE-Step 1.5 Prompting Guide

**Written 2026-08-15.**

## Sources

Primary (the exact checkout running on Spark, `~/Projects/Spark-Installations/ace-step-15`):

- `docs/en/Tutorial.md` — the official prompting chapter: *About Caption*, *About Lyrics*, *About Music Metadata*. This is the authoritative source for everything below unless marked otherwise.
- `docs/en/ace_step_musicians_guide.md` — official plain-language guide: caption/lyrics roles, task modes, model tiers.
- `docs/en/GRADIO_GUIDE.md` — official UI reference: field names, sampler defaults, thinking/CoT switches.
- Upstream project: <https://github.com/ace-step/ACE-Step-1.5> and <https://github.com/ace-step/ACE-Step>; docs site <https://ace-step.github.io/> (`docs/index.md`).

App integration (read to know what the style prompt must *not* duplicate):

- `~/Projects/RealityRoveHub-dev/web/src/lib/ace-native.ts` — parameter catalogs and the `/release_task` payload builder. Field names verified there against `acestep/api/http/release_task_models.py` (`GenerateMusicRequest`).

### Evidence key

Unlike the Suno KB — where the public corpus is unreliable and everything needs grading —
ACE-Step's prompting guidance comes from official docs shipped inside the running
checkout, so the evidence quality here is uniformly high. Two labels still matter:

| Tag | Meaning |
|---|---|
| *(unlabelled)* | **Documentation.** Stated in the official ACE-Step docs listed above. |
| **[RRHub]** | **This repo's verified working recipe** — a RealityRoveHub production decision or measured result, not an upstream statement. |
| **[INFERENCE]** | Drawn by this author from the documented facts; not stated anywhere. |

No claim in this file is unsourced folklore. Where the docs are silent, the file says so
rather than guessing.

---

## The two-brain model

ACE-Step 1.5 runs a language model ("the songwriter") in front of a diffusion transformer ("the studio engineer"). The LM reads the caption and lyrics, infers the metadata you left blank (BPM, key, structure, energy map), and can rewrite/expand the caption via chain-of-thought. The DiT then renders audio.

Consequences for prompt writing:

- The caption is read by an LM before it reaches the audio model, so it does not have to be a rigid tag list — natural language survives the trip.
- The docs state the LM generalizes a caption **less** well than the DiT does. With `thinking` on, an unreasonable or self-contradicting caption is less likely to produce a happy accident and more likely to degrade.
- The songwriter brain is active only for `text2music`, `lego` and `complete`. It is silently bypassed for `cover`, `repaint` and `extract`.

## The RRHub recipe this guide is written for **[RRHub]**

| Piece | Value | Why |
|---|---|---|
| DiT | `acestep-v15-turbo` | Default in `ace-native.ts`; chosen by A/B listening tests 2026-07-16 — turbo beat the XL family on vocals in both pipelines. |
| LM | `acestep-5Hz-lm-4B` | Default in `ace-native.ts`; largest songwriter brain, so caption interpretation is at its best. |
| Sampler | 8 steps, guidance 1.0 | `samplerDefaults()`: turbo is step-distilled and runs without CFG. (SFT = 50 steps / 7.0, base = 32 / 7.0.) |
| Task | `text2music` | The only task the style-prompt path uses. |
| Thinking | on by default | So the LM *will* infer whatever metadata is left unset. |

Available but unused by the style-prompt path: DiT `acestep-v15-base | -sft | -xl-base | -xl-sft | -xl-turbo`; LM `acestep-5Hz-lm-0.6B | -1.7B`; tasks `repaint | cover | extract | lego | complete`. `lego`, `extract` and `complete` require a base/SFT model — they do not run on turbo.

---

## Caption vs Lyrics — the division of labour

Official framing: the **caption is the song's overall portrait** (style, atmosphere, timbre); the **lyrics are the song's temporal script** (what happens, in what order, at what energy).

The caption field is `prompt` in the API payload. The docs call it "the most important factor affecting generated music."

**Format is deliberately flexible.** The docs state the model was trained to accept simple style words, comma-separated tags, *and* complex natural-language descriptions, and that "text format doesn't significantly affect model performance." So a comma-separated caption and a prose caption are both legitimate; pick one and be internally consistent.

### Caption dimensions (official table)

| Dimension | Examples from the docs |
|---|---|
| Style / genre | pop, rock, jazz, electronic, hip-hop, R&B, folk, classical, lo-fi, synthwave |
| Emotion / atmosphere | melancholic, uplifting, energetic, dreamy, dark, nostalgic, euphoric, intimate |
| Instruments | acoustic guitar, piano, synth pads, 808 drums, strings, brass, electric bass |
| Timbre texture | warm, bright, crisp, muddy, airy, punchy, lush, raw, polished |
| Era reference | 80s synth-pop, 90s grunge, 2010s EDM, vintage soul, modern trap |
| Production style | lo-fi, high-fidelity, live recording, studio-polished, bedroom pop |
| Vocal characteristics | female vocal, male vocal, breathy, powerful, falsetto, raspy, choir |
| Speed / rhythm | slow tempo, mid-tempo, fast-paced, groovy, driving, laid-back |
| Structure hints | building intro, catchy chorus, dramatic bridge, fade-out ending |

Official example caption, given in the Tutorial's complete worked example:

> `female vocal, piano ballad, emotional, intimate atmosphere, strings, building to powerful chorus`

That is the house shape: comma-separated, ~8–14 items, spanning several dimensions, no metadata numbers.

### Official caption principles

1. **Specific beats vague.** "sad piano ballad with female breathy vocal" outperforms "a sad song".
2. **Combine multiple dimensions.** One dimension alone leaves the model too much room; style + emotion + instruments + timbre anchors the direction.
3. **References work.** "in the style of 80s synthwave", "reminiscent of Bon Iver" — the docs explicitly endorse artist and era references as shorthand for a complex aesthetic. (Note this is the opposite of Suno's hosted policy; ACE-Step is local and has no such filter.)
4. **Texture adjectives are load-bearing.** warm / crisp / airy / punchy influence mixing and timbre.
5. **A caption is a starting point, not an endpoint.** Write a direction, then iterate.
6. **Granularity is a dial.** Fewer words = more model freedom and more seed-to-seed variance; more words = tighter constraint. Choose deliberately.
7. **Avoid conflicting words.** "classical strings" plus "hardcore metal" in one caption degrades output — the model attempts a fusion and usually fails. Two documented remedies:
   - *Repetition reinforcement* — repeat words for the element that should dominate.
   - *Conflict to evolution* — convert the clash into a timeline: "starts with soft strings, becomes dynamic metal rock in the middle, ends in hip-hop". The model handles a stated progression far better than a blend.

---

## The rule that matters most for RRHub: do not restate metadata in the caption

The RRHub ACE modal collects **BPM, key/scale, time signature and vocal language as separate structured fields** and puts them in the `/release_task` payload as `bpm`, `key_scale`, `time_signature` and `vocal_language`, alongside `prompt` (the caption) and `lyrics`. Verified in `buildReleaseTaskPayload()` in `ace-native.ts`.

The official Tutorial's recommended practice is explicit:

> Don't write tempo, BPM, key, and other metadata information in Caption. These should be set through dedicated metadata parameters … Caption should focus on style, emotion, instruments, timbre, and other musical characteristics.

And, separately: if manually-set metadata does not seem to take effect, the first thing to check is a **conflict with the caption** — the doc's own example is caption "slow ballad" against `bpm=160`, which confuses the model.

So the style prompt for this app **must not** contain:

- a BPM number,
- a key or scale name ("in A minor", "C major"),
- a time signature ("4/4", "waltz time" is borderline — it names the signature),
- a language name for the vocal ("sung in Polish"),
- a duration.

Relative tempo *feel* words (`slow tempo`, `mid-tempo`, `driving`, `laid-back`) remain fine and are in the official dimension table — they must simply agree with whatever BPM the modal is sending. A caption that says "downtempo" while the modal sends `bpm=160` is the documented failure case.

### What the structured fields accept

From `ace-native.ts` (which clamps before sending) and the Tutorial's control table:

| Field | Accepted | Notes |
|---|---|---|
| `bpm` | 10–300 clamped by RRHub; docs give 30–300 | Docs: 60–180 is well-trained; extremes are unstable. `null` = let the LM decide. |
| `key_scale` | `<root> major` / `<root> minor` over 17 roots | Docs: C, G, D, Am, Em are stable; rare keys may be ignored or shifted. `""` = unset. |
| `time_signature` | `""`, `2`, `3`, `4`, `6` | Docs: 4/4 most reliable, 3/4 and 6/8 usually fine, 5/4 and 7/8 are advanced. |
| `vocal_language` | ~50 ISO codes | The LM usually auto-detects from the lyrics anyway. |
| `audio_duration` | 10–600 s, `-1` = auto | Docs: 30–60 s and 2–4 min are stable; very long runs risk repetition. |

The Tutorial is clear these are **guidance, not commands**: `bpm=120` is an anchor, and the result may land at 118 or 122.

**Quality note [RRHub]:** the comment in `ace-native.ts` records the GRADIO_GUIDE's advice to leave duration / BPM / key / time-signature unset and let the LM plan them. When the user has left them blank, the caption is the *only* signal the LM has — so a caption with a clear tempo/energy character is doing real work in that case.

---

## Lyrics and structure tags — context, not your output

RRHub sends lyrics separately; the style prompt never contains them. But the caption must not contradict them, so know the lyric conventions.

**Structure tags** (official table):

| Category | Tags |
|---|---|
| Basic structure | `[Intro]` `[Verse]` / `[Verse 1]` `[Pre-Chorus]` `[Chorus]` `[Bridge]` `[Outro]` |
| Dynamic sections | `[Build]` `[Drop]` `[Breakdown]` |
| Instrumental sections | `[Instrumental]` `[Guitar Solo]` `[Piano Interlude]` |
| Special | `[Fade Out]` `[Silence]` |

Tags may be qualified with a hyphen — `[Chorus - anthemic]`, `[Bridge - whispered]` — which the docs prefer to a bare tag. Vocal-control tags (`[raspy vocal]`, `[whispered]`, `[falsetto]`, `[powerful belting]`, `[spoken word]`, `[harmonies]`, `[call and response]`, `[ad-lib]`) and energy tags (`[high energy]`, `[building energy]`, `[explosive]`, `[melancholic]`, `[euphoric]`, `[dreamy]`, `[aggressive]`) live in the **lyrics**, not the caption.

Two documented failure modes:

- **Stacking tags.** `[Chorus - anthemic - stacked harmonies - high energy - powerful - epic]` risks the model singing the tag text as lyrics, and confuses it. Keep tags to one qualifier; complex style description belongs in the caption.
- **Caption/lyrics conflict.** The docs' example: caption says "violin solo, classical, intimate chamber music" while the lyrics carry `[Guitar Solo - electric - distorted]`. "Models are not good at resolving conflicts."

The official consistency checklist:

- instruments in caption ↔ instrumental section tags in lyrics
- emotion in caption ↔ energy tags in lyrics
- vocal description in caption ↔ vocal-control tags in lyrics

**[INFERENCE]** Practical read for a style-prompt author: **skim the supplied lyrics before writing the caption.** If the lyrics contain `[Guitar Solo]`, name a guitar in the caption. If they contain `[Drop]`, the caption should be an electronic style that has drops. If they contain no section tags at all, the caption's structure-hint dimension ("building intro", "catchy chorus", "fade-out ending") is the only structural signal the LM gets.

Lyric craft rules (context only — RRHub's lyrics come from elsewhere): 6–10 syllables per line, UPPERCASE for shouted words, (parentheses) for backing vocals.

---

## Anti-patterns for the caption

| Don't | Why |
|---|---|
| BPM numbers, key names, time signatures, duration, vocal language | Duplicates the structured fields; a mismatch actively confuses the model (official). |
| Section tags — `[Chorus]`, `[Verse]` — in the caption | They are a lyrics-field mechanism. The caption has a structure-hint vocabulary instead ("catchy chorus", "building intro"). |
| Lyric lines, or a paraphrase of the lyrics | Not a caption dimension; wastes the field and risks the LM treating it as content. |
| Clashing genres in one flat list | Documented degradation. Use repetition to weight, or state a progression. |
| Meta-instructions to the model ("make it good", "high quality song") | Carries no musical dimension. |
| Negative phrasing ("no drums", "without vocals") | There is **no negative prompt on this path.** `lm_negative_prompt` exists in the Gradio UI (default `"NO USER INPUT"`) for LM CFG, and turbo runs at guidance 1.0 with no DiT CFG at all. State what you *do* want; for an instrumental, use the lyrics field's `[Instrumental]`. |

## Caption template

```text
<genre / subgenre>, <era or production reference>, <2-3 instruments>,
<vocal gender + delivery>, <2-3 timbre/texture words>, <mood>,
<one structural or arc hint>
```

Roughly 8–16 comma-separated items. Longer is legal — the format is flexible — but the official example sits at this size, and more words means less room for the model to surprise you.

### Worked example

Brief: "moody late-night drive, female vocal". Modal is sending bpm 92, A minor, 4/4, language `en`.

```text
dark synthwave, late-80s analog production, brooding female vocal, breathy and
close-mic'd, warm analog pads, arpeggiated bass synth, gated reverb drums,
melancholic and nocturnal, sparse verses building to a wide anthemic chorus,
tape-saturated and spacious mix
```

No tempo number, no key, no language — those are already in the payload. The tempo *feel* ("brooding", "sparse verses building") agrees with 92 BPM rather than fighting it.
