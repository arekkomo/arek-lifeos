---
title: Reference Song Analysis Template for Converting Any Song Description into Suno Style Prompt
category: concept
summary: Structured analysis template that breaks down any described song or reference track into a Suno-style prompt using only sonic descriptors — no artist names. Includes fill-in worksheet, worked examples, and conversion algorithms.
tags: [suno, reference-analysis, prompt-conversion, music-theory, prompt-engineering, ai-music]
sources: 2
updated: 2026-06-29
---

# Reference Song Analysis Template for Converting Any Song Description into Suno Style Prompt

> **RULE ZERO: Never use artist or band names in any Suno field.** This template exists to translate your musical ideas (even references to existing tracks) into pure sonic descriptions that Suno can generate from scratch. If you hear a reference track on your end, describe it — never name it.

## Why You Need a Template

Going from "I want something that feels like..." or "a song about X with the energy of..." to a working Suno prompt requires translation into observable sonic parameters. This template forces you to analyze what makes a sound work before telling Suno what to build.

---

## The Analysis Worksheet — Fill In These Fields

Take your reference song (or conceptual idea) and fill out:

### 1. TEMPO & RHYTHM
- **Approximate BPM:** What's the pulse? Fast, moderate, or dragging?
- **Groove feel:** Straight? Swing? Syncopated? Half-time? Double-time?
- **Rhythmic density:** Sparse and spacious or busy and driving?

### 2. INSTRUMENTATION MAP — Primary Layer
- **Lead instrument(s):** What carries the melody/primary identity?
- **What makes this sound recognizable?** (e.g., that specific synth patch, the guitar tone)

### 3. INSTRUMENTATION MAP — Secondary Layer
- **Harmony/support instruments:** What fills out the chords and texture?
- **Rhythm section:** How does bass and drums interact? Lock tight or loose?

### 4. VOCAL DESCRIPTION
- **Gender/voice quality:** Smoky, clear, raspy, breathy, powerful, light?
- **Delivery style:** Whispered verses into belted chorus? Rap vs melody? Spoken word?
- **Vocal arrangement:** Solo voice? Harmonies stacked? Choir layered under?

### 5. PRODUCTION / MIXING CHARACTERISTICS
- **Recording texture: Clean digital? Warm analog? Gritty tape hiss? Raw unmastered?
- **Space/environment sense:** Intimate close-mic? Vast reverb space? Mono punchy dry room?

### 6. DYNAMIC ARC
| Song Section | Energy Level (1-10) | What's different from previous section? |
|--------------|-------------------|--------------------------------------|
| Intro | | |
| Verse 1 | | What changes? |
| Pre-Chorus | | What builds/channels something? |
| Chorus | | What explodes/strikes in? |
| Verse 2 | | How does it change from Verse 1? |
| Bridge | | Where is the detour? |
| Final section | | How does the energy land? |

### 7. MOOD & NARRATIVE CONTENT
- **Emotional core:** What emotion lands first? (longing, joy, anger, nostalgia, etc.)
- **Narrative perspective:** Someone looking back? Someone in the moment? An outside observer?
- **Key imagery or phrases:** (only describe; never reference the actual lyrics of a real song)

### 8. GENRE CATEGORIES
- Primary genre: `____`
- Secondary genres: `____`
- What you're **NOT** trying to avoid: `____` → put this in Exclude Styles

---

## Template Output — Converting to Prompts

Once the worksheet is filled, produce TWO outputs from it.

### Output A: Full Style Prompt (up to 1,000 chars for v5)
Use this formula: `[Genre + BPM] | [Mood/atmosphere] | [Instruments by layer] | [Vocal persona description] | [Production quality] | [Dynamic arc summary]`

### Output B: Metatag Set
Map the analysis into structural metatags for section-by-section control in the Lyrics field.

---

## Worked Example — Converting a Hypothetical Reference

**Scenario:** You hear a track and want to recreate its feel without referencing it by name.

### Analysis Worksheet Completion (hypothetical example)

```
TEMPO & RHYTHM:
- BPM: ~95 BPM, moderate pace
- Groove: Straight with slight shuffle on the hi-hat
- Density: Driving but not overcrowded

INSTRUMENTATION — Primary Layer:
- Lead: Clean electric guitar with bright twang and chorus effect
- What makes it recognizable: the interlocking fingerpicked guitar pattern throughout

INSTRUMENTATION — Secondary Layer:
- Harmony: Warm synthesizer pads underneath, subtle strings on chorus entries
- Rhythm: Tight upright bass walking line with brushed snare kit

VOCAL DESCRIPTION:
- Voice: Androgynous with a warm tenor quality and slight natural crack in the upper register
- Delivery: Conversational intimate phrasing that opens into melodic chorus hook
- Arrangement: Solo lead vocal with whispered double-tracked harmony underneath

PRODUCTION QUALITY:
- Texture: Warm analog warmth with room mic bleed, not ultra-polished
- Space: Tight studio space feel — instruments sitting close together but distinct
- Vocals: Dry intimate close-mic'd sit right in the center

DYNAMIC ARC:
Intro (2→) → Verse 1 (3→) Pre-Chorus (5→) Chorus (6→) Verse 2 (7→)
  Bridge (3→) Final Chorus (9→) Outro (2→)

MOOD & CONTENT:
- Emotional core: Nostalgic warmth with underlying melancholy
- Genre: Indie folk / alternative country / singer-songwriter fusion

---END ANALYSIS---
```

### Output A — Full Style Prompt (~950 chars):
```
Indie folk / alternative country at 95 BPM. Clean twangy electric guitar leading interlocking fingerpicked pattern throughout, warm synth pads underneath, tight upright bass walking line, brushed snare kit. Swelling strings section joins on chorus entries. Androgynous warm tenor vocal with slight upper-register crack — conversational intimate phrasing opens into melodic chorus hook with whispered double-tracked harmony under verses. Warm analog production with room mic bleed, dry intimate close-mic vocals sitting center. Starts sparse two-note guitar intro (energy 2). Verses stay at energy 3-5 with bass and brushed kit joining (5→6 on first chorus). Bridge drops to quiet arpeggio only (3), then massive final chorus with full band and strings exploding to full power (9). Outro collapses to single fingerpicked guitar fading out (2→).
```

### Output B — Metatag Set for Lyrics:
```
[Intro] [Low Energy] [Sparse arrangement]
[Verse 1] [Intimate] [Smooth delivery] [Building Energy]
[Pre-Chorus] [Gradual swell]
[Chorus] [Harmonized Chorus] [Higher energy] [Emotional Climax]
[Breakdown]
[Verse 2] [Building Energy] [Belted]
[Bridge] [Quiet arrangement] [Falling tension] [Melancholic]
[Final Chorus] [Explosive] [Powerful] [Orchestral swell] [Emotional Climax]
[Outro] [Slow Down] [Low Energy] [Silence]
```

---

## Worked Example 2 — From Text Description

**Input (no reference track):** "A haunting song about someone walking through their childhood hometown at night, the old places half-remembered, with a deep sense of longing and the faint hope that something beautiful still lives there."

### Analysis Worksheet Completion:

```
TEMPO & RHYTHM:
- BPM: ~68 BPM, slow ballad tempo, dragging slightly behind the beat like tired footsteps
- Groove: Straight but loose — not metronomic. Feel like someone walking at night
- Density: Sparse verses building to fuller choruses

INSTRUMENTATION — Primary Layer:
- Lead: Solo acoustic guitar with a minor key melody
- What's recognizable: The open string drone underneath chords creating atmosphere, solo voice without accompaniment in intro/verse 1

INSTRUMENTATION — Secondary Layer:
- Harmony: Subtle cello enters on verse 2. Piano joins on chorus entry
- Rhythm: Very light brushed percussion — almost ghostly presence

VOCAL DESCRIPTION:
- Voice: Smoky husky baritone with a slight tremor on held notes showing vulnerability
- Delivery: Half-spoken introspective verses that open into fragile but earnest chorus melody
- Arrangement: Solo vocal in verse, stacked harmonies (low male bass line + mid tenor) enters in chorus

PRODUCTION QUALITY:
- Texture: Lofi bedroom recording aesthetic — slightly intimate and raw feel
- Space: Mix of close-mic'd dry vocals with occasional long hall reverb tail on last words of lines

DYNAMIC ARC:
Intro (1→Verse 1 (2→) Pre-Chorus (5→) Chorus (6→) Verse 2 (7→Bridge (3→Final Chorus (9→Outro (2→)

MOOD & CONTENT:
- Emotional core: Melancholic nostalgia with underlying warm hope (not despair — a quiet light at end)
- Genre: Indie folk / dark ambient crossover / cinematic singer-songwriter
```

### Output A — Full Style Prompt (~850 chars):
```
Cinematic indie folk ballad at 68 BPM. Solo acoustic guitar with minor key melody and open string drone texture underneath chords. Haunting solo baritone vocals that gradually gain accompaniment: subtle cello enters verse two, sparse piano on chorus entries. Very light ghostly brushed percussion, barely audible beneath instrumentation. Smoky husky baritone vocal — half-spoken conversational verses into fragile earnest chorus melody. Verses feature whispered double-tracked harmony under lead voice. Lofi bedroom recording aesthetic at first, then widening to spacious hall reverb tails in second half. Dry intimate close-mic vocals centered. Intro is pure solo guitar energy (1). Verses sparse single guitar and vocal only (2→5). Pre-chorus adds soft cello (6→8) massive emotional climax with full strings and layered harmony belting (9). Bridge drops to bare minimum again (3), final chorus explodes then strips mid-way, ending on barely-there single sustained note held over silence.
```

### Output B — Metatag Set for Lyrics:
```
[Intro] [Low Energy] [Sparse arrangement only] [Melancholic]
[Verse 1] [Intimate] [Spoken Word] [Building Energy] [Whispered double-harmony underneath lead]
[Pre-Chorus] [Gradual swell] [Atmosphere builds]
[Chorus] [Powerful] [Harmonized Chorus] [Emotional Climax] [Ethereal strings underlay]
[Verse 2] [Building Energy] [Gritty, more conviction] [Low Energy bass harmony line]
[Bridge] [Quiet arrangement only guitar] [Falling tension] [Silence for last two syllables]
[Final Chorus] [Orchestral swell] [Explosive] [Belted] [Melismatic on final words]
[Outro] [Slow Down] [Low Energy] [Vinyl Crackle background tone] [End]
```

---

## Worked Example 3 — From Musical Reference Only (No Lyrics)

**Scenario:** "I want that feeling when an old R&B track suddenly kicks into a major chord and everything goes golden, with heavy bass and soft falsetto vocals."

### Analysis Worksheet:

```
TEMPO: ~100 BPM. Mid-tempo groove with laid back swing feel. Tight syncopated bass/drums.
PRIMARY LAYER: Heavy sub-bass playing root-fifth-octave pattern through minor verses. Bright Rhodes electric piano accents on chorus entries.
SECONDARY LAYER: Tight snare backbeat slightly behind beat for "pocket" feel. Shimmering synth pad beds underneath.
VOCALS: Soft head-voice falsetto light airy upper-register male voice. Breath-intimate delivery, no strain. Layered three-part harmony stacked thirds under lead line.
PRODUCTION: Crisp modern digital production but warm EQ curves — never sterile. Vocals sit dead center dry; other instruments spread wide.
DYNAMIC ARC: Intro (4) → Verses (7→Pre-Chorus (7→Major Chord Hit" drops to bright major chord (9→Verses return minor) (5→Final chorus explodes into FULL MAJOR with everything layering and doubling the melody) (10-> Outro fades on sustained major chord and bass note (3→
GENRE: Neo-soul / contemporary R&B / modern funk fusion
```

### Output A Style Prompt (~920 chars):s
```
Contemporary R&B neo-soul at 100 BPM. Tight syncopated sub-bass root-fifths-octave pattern driving verses in minor key. Bright electric piano (Rhodes) accents on chorus entries. Shimmering synth pad beds fill the gaps between vocal phrases. Heavy tight snare backbeat sits slightly behind beat creating deep pocket feel. Soft head-voice falsetto male vocals — breathy intimate delivery no strain, layered three-part harmony stacked thirds under lead line in chorus. Crisp modern digital production with warm EQ curves never sterile. Dry close-mic vocals dead center; everything else spreads wide stereo field. Verses stay grounded in minor (energy 7). Pre-chorus builds tension upward (8→Chorus hits sudden major chord shift everything goes bright gold energy (9) Verses return grounding minor (5→Final chorus explodes into FULL MAJOR with layered melodies doubling lead line, full bass presence wide and driving energy (10→Outro sustains last major chord over fading sub-bass rumble then silence (3→
```

---

## Quick-Conversion Cheat Sheet (No Reference Track — Just Concept)

When you have a concept but no specific reference track:

| What You Describe | Translate to → Suno Prompt Elements |
|------------------|------------------------------------|
| "Dark moody night" | `minor key, deep sub-bass, heavy reverb tails, slow half-time groove, smoky baritone voice` |
| "Bright hopeful morning" | `major key, bright clean guitar or electric piano, upbeat mid-tempo 120 BPM, clear soprano/alto vocal, crisp production` |
| "Angry driving energy" | `distorted power chords, aggressive snare patterns, fast tempo 150+ BPM, gritty/raspy vocal delivery, high energy throughout` |
| "Ethereal floating feeling" | `ambient synth pads, granular synthesis textures, slow tempo 70-80 BPM, head-voice falsetto vocals, vast reverb spaces, low energy dynamic arc` |
| "Vintage retro warmth of 1970s" | `tape saturation coloration, warm analog production, Hammond organ, acoustic bass, loose pocket drum feel, soulful mid-range vocal` |
| "Future glitchy electronic" | `FM synthesis bells/chimes, glitch-hop stutter loops, fast tempo 140-160 BPM, sharp snare drops, sub-bass oscillators, dry crisp modern production` |

---

## Converting Real Lyrics into Metatag Structure

When you have lyrics and need metatags:

**Step 1:** Read through the entire lyrics. Identify natural sectional breaks.

**Step 2:** For each section, answer:
- What is the emotional state at this point? (choose from mood tags)
- How loud/intense is it compared to previous section? (dynamic tag)
- What vocal quality fits best? (vocal performance tag)
- Does anything happen instrumentally I should cue? (SFX or instrumental break tag)

**Step 3:** Cross-check with [[suno-v5-prompt-engineering-best-practices.md]] for metatag formatting rules.

---

## Template File — Copy-Paste Version

```
### TEMPLATE: Reference Song Analysis Worksheet ###

1. TEMPO & RHYTHM
   - BPM: ___
   - Groove feel: ___
   - Density: ___

2. PRIMARY INSTRUMENTATION (what defines the sound)
   - Lead instrument: ___
   - Recognizable element: ___

3. SECONDARY INSTRUMENTATION (support, rhythm)
   - Harmony instruments: ___
   - Rhythm section: ___

4. VOCAL ANALYSIS
   - Quality: ___
   - Delivery style: ___
   - Arrangement: ___

5. PRODUCTION CHARACTERISTICS
   - Texture: ___
   - Spatial setting: ___

6. DYNAMIC ARC (energy 1-10)
   Intro (___) → Verse 1 (___) → Pre-Chorus (___)
   Chorus (___) → Verse 2 (___) → Bridge (___) → Final section (___)

7. MOOD / GENRE
   - Emotional core: ___
   - Primary genre: ___
   - Secondary genres: ___
   - Avoid: [Exclude Styles] ___

---CONVERT TO PROMPT---

Style Prompt (~950 chars target):
[Genre+BPM | Mood | Instruments | Vocal | Production | Arc]

Metatag Set:
[Intro tag line]
[Verse 1 tag line]
[Pre-Chorus tag line]
[Chorus tag line]
[Verse 2 tag line]
[Bridge tag line]
[Final Chorus tag line]
[Outro tag line]
```

---

## Synthesis: Connecting to Visual Work

This analysis template is essentially **scoring a scene backward** — you're reverse-engineering what makes a musical moment land, then translating that into production parameters. That maps directly to how you'd score a sequence in DaVinci Resolve or build audio in [[DaVinci Resolve]]Fairlight. The energy arc numbers (1-10) are identical curves to the intensity curves you'd draw on a color timeline — just moving from visual emotion to sonic emotion and back again.

Referenced related pages:
- [[MuScriptor]] / [[Audio-to-MIDI-Transcription]] — use an audio-to-MIDI pass to add instrument and note-timing evidence to the listening-based reference analysis
- [[suno-v5-prompt-engineering-best-practices.md]] for metatag formatting rules and v5 interface details
- [[DaVinci Resolve]] for scoring integration with video
- ``visual-storytelling`` concept from filmmaking — the arc analysis is the same structure used in visual storytelling but applied to sound
