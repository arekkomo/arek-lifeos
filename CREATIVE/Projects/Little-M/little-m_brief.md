---
type: "note"
title: "Little M — Brief"
project: "Little-M"
stage: "Development"
version: "current"
updated: "2026-08-18"
---# Little M

## Project intent
The song and music video are one project: polished, commercially credible club-pop whose humor comes only from the contrast with its absurd punchline.

## Components
- [[little-m_song]] — canonical lyrics, hooks, and Suno direction.
- This master brief — visual development and production planning.

## Status
Development. The canonical song now contains lyrics and Suno direction; confirm it is final, then generate first Suno takes before video production.



---

## Consolidated Project Material



### Little M — Music Video Brief

# Little M

> **Owner:** Director (Creative)
> **Status:** P2 · Planning
> **Format:** Song + Music Video → RRHub integration

## Overview

A creative project following the full song production pipeline: lyrics, Suno music production, music video concept and storyboard, then integration with Reality Rove Hub.

## Current State

- [ ] Lyrics drafted
- [ ] Musical prompt / Suno generation
- [ ] Music video concept & script
- [ ] Scene list + shot breakdown
- [ ] Storyboard image prompts per shot
- [ ] RRHub show/scene/shot integration
- [ ] Dev → Prod deployment (your approval required)

## Pipeline Stages

See `AGENTS/Director/Skills/song-production-pipeline.md` for the 6-step workflow.

## Next Steps



### Little M — Production Notes

# Little M — Suno Technical Reference

## Tag Structure for Custom Mode Prompt
```
[Instr: Intro]
[Intro] Instrumental only, no vocals

### Verse Tags
[Verse]
Melodic verses
Short phrasing
Minimal verbs

### Pre-Chorus Tags
[Pre-Chorus]

### Chorus Tags
[Chorus]
Chant rhythm
Repetitive hook structure

### Special Sections
[Fake-out pause]
[Bass drop / Heavy beat drop]
[Outro]

```

**Key rule:** Use bracketed tags for section structure and inline descriptors for style. Suno recognizes:

- `[Verse]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Intro]`, `[Outro]`
- `(spoken)` or `[Spoken word]` for punchline delivery
- Descriptors *inside* tags like `[Verse: melodic, minimal verbs]`
- **Cold instrumental intro** via `[Instrumental Intro]` or `[Intro] Cold instrumental start`

## Character Limits (Custom Mode)
- **Prompt/Style description ~ limit: ~200 characters recommended** for style descriptions
- **Lyrics box:** ~6,000 characters max, but Suno tends to cut off around 3,500-4,000 characters effectively
- Keep prompts concise and impactful.



### Little M — Song Brief

# Little M — Song Project

## Status: Active Development

## Concept
A legitimate club anthem built around one absurd punchline. The production is serious, polished, and commercially viable. The humor comes entirely from the lyrics' unexpected delivery — not from parody or novelty framing.

## Core Philosophy
- **Treat it like writing a genuine hit.** If production/melody/vocals are completely serious, polished and infectious, the absurd line becomes exponentially funnier.
- **Less explanation = funnier.** Let the listener fill in the blanks.
- **Snapshots over stories.** Every line should be a vivid impression, not a plot point.

---

## Target Feeling
- Mischievous, campy, flirtatious
- Stylish, slightly surreal
- "Looking for trouble" energy
- The confidence that comes with Saturday night — every bad decision suddenly feels like a great idea
- **Become your Saturday-night alter ego.** Not about sex directly. Implies slutty behavior without explicitly talking about it.

---

## Lyric Style Guide

### Preferred
| Rule | Example |
|------|---------|
| Very few verbs | "Pretty little menace" |
| Short phrases / slogans | "No receipts" |
| Ambiguity over clarity | "Your tricks are freakes..." |
| Attitude over exposition | "Crooked little smile" |
| Simple vocabulary | "Makes a lot of sense" |
| Melodic phrasing | Room for melody, chant rhythm |

### Avoid
- Telling a story / linear narrative
- Explaining emotions directly
- Over-writing / long sentences
- **Generic dance-pop clichés** (see below)

### Cliché Blacklist
```
neon lights / neon glow
city's heartbeat
something's in the air
feel it in my bones
dance all night / party all night
calling out my name
living for tonight
looking for trouble  ← irony flagged
```

---

## Punchline Architecture

### Golden Rule
The joke must appear **only after** the first massive build/beat drop.
- Never mention it before
- Never tease it in the intro or Verse 1
- First time the listener hears the punchline should coincide with a fake-out pause + biggest musical moment
- Fake-out pause → huge beat drop → "…spread your butt cheeks."

### Why This Works
The contrast between serious/commercial production and sudden absurdity is the entire concept. The song should be enjoyed musically **first**, then laughed at second.

---

## Arrangement Map (Reference)
```
Instrumental intro (cold — no vocals)
Verse 1: Pretty little menace / Dressed in innocence...
Pre-chorus
Chorus: "Oh, what happened?" / "It must be Saturday!"
Fake-out pause
MASSIVE BEAT DROP
"…spread your butt cheeks."
Return to groove
```

---

## Remaining Work
- [ ] Verse 2 — currently generic, needs same memorable identity as Verse 1
- [ ] Pre-chorus hook — needs stronger melodic phrasing / chant rhythm
- [ ] Chorus rhythm — needs punchier chant quality
- [ ] All lyrics: verify against cliché blacklist before finalization

---

## Generated Assets
- `LYRICS-DRAFT.md` — Working lyric drafts
- `DIRECTIVE.md` — This file's condensed direction for reference
- `LYRIC-COMPONENTS/` — Individual sections and hooks bank
