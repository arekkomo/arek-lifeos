---
title: "Song Production Pipeline"
summary: Standard 6-step workflow for song creation through RRHub integration — all steps defined with explicit knowledge sources and output specs
owner: Director
updated: 2026-07-13
tags: [songwriting, suno, music-video, rrhub, pipeline]
---

# Song Production Pipeline

> Owner: Director (Creative)
> Status: Active — use for all song/music video projects

**⚠️ CRITICAL READ BEFORE ANY SONG WORK:** Before Steps 1-3, always read these knowledge files from Scholar's research:
- `/LEARNING/Knowledge/Music-Production/suno-v5-prompt-engineering-best-practices.md` — Suno v5 prompt structure, metatags, exclusions
- `/LEARNING/Knowledge/Music-Production/suno-music-style-tags-guide.md` — BPM ranges, instrument palettes, vocal personas, production terms
- `/LEARNING/Knowledge/Music-Production/suno-reference-song-analysis-template.md` — How to analyze reference songs and convert to Suno-compatible descriptors

## The 6 Steps (in order)

### Step 1: Lyrics

**Input from Arek:** A saying, sentence, phrase, or description of feelings/emotions.

**Director does:**
- Convert the raw input into structured lyrics with proper song structure
- Use `[bracket tags]` for Suno metatags (structure, vocal performance, dynamics) — see suno-v5-prompt-engineering doc
- Follow existing `songwriting-and-ai-music` skill for craft guidelines
- Map emotional arc: verse intimacy → chorus power → bridge revelation → outro resolution

**Output:** Structured lyrics with Suno metatags, saved at `CREATIVE/Projects/<Project>/SONG/Lyrics.md`.

### Step 2: Musical Prompt Generation (Style Field)

**Input:** Finished lyrics from Step 1 + Arek's musical direction ("sounds like X") or reference song

**Director does:**
- If Arek provides a reference song → read `suno-reference-song-analysis-template.md`, analyze that song's technical characteristics, extract BPM/key/vocal/instrumentation descriptors
- **NEVER use artist/band names in Suno prompts** — this is against Suno terms of service
- Build the Style field using the formula from suno-music-style-tags-guide: `Genre + BPM range + Mood + Instruments + Vocal Persona + Production Quality + Energy Arc`
- Use specific descriptor language (e.g., "warm analog saturation, intimate close-mic male vocal" not "sounds moody")
- Exclude any style elements Arek specifically doesn't want

**Output:** Ready-to-paste Suno Style Field string saved next to Lyrics file. Confirm with Arek before sending to Suno.

### Step 3: Music Video Concept & Script

**Input:** Finished song (or strong mental reference of its sound/mood) + lyrics

**Director does:**
- Develop visual concept: core metaphor, setting, mood board description
- Write scene-by-scene script with timing aligned to song structure
- Reference `/CREATIVE/Creative-Style-Bible.md` for sonic/visual identity alignment

**Output:** Saved at `Video-Concept.md`. Present to Arek before moving forward.

### Step 4: Scene & Shot Breakdown List

**Input:** Approved video concept from Step 3

**Director does:**
- Break concept into individual shots/scenes with timing codes
- Define style/camera language per shot (wide, close-up, handheld, drone...)
- Flag any shots that might need green screen or VFX pass

**Output:** Saved at `Shot-Breakdown.md`. Confirm count and complexity with Arek before Step 5.

### Step 5: Storyboard / Generation Prompts

**Input:** Approved shot breakdown

**Director does:**
- Write generation prompts for each shot (AI video model instructions)
- Reference existing AI video prompting knowledge: `/LEARNING/Knowledge/AI-Video/`
- Keep prompts model-specific if targeting Kling/LTX/Hunyuan — check latest model guide before writing

**Output:** Saved at `Storyboard-Prompts.md`. Ready for rendering.

### Step 6: RRHub Integration

**Input:** Rendered video assets from Step 5

**Director does:**
- Commit work to RRHub repository via `claude code`
- **Only DeV branch by default** — prod promotion requires explicit Arek approval
- Tag commit with project name and step completed

**Output:** Git commit in RRHub. Report back to Arek with link/SHA.

---

## Quick Reference: Suno Prompt Rules (from Knowledge Base)

| Rule | Source |
|---|---|
| Never use artist/band names in prompts | suno-v5-prompt-engineering.md |
| Use metatags in `[brackets]` for structure/vocal cues | suno-v5-prompt-engineering.md |
| Style field max ~200 chars — be specific, not poetic | suno-v5-prompt-engineering.md |
| BPM: state as range (e.g., "95-105 BPM") not single number | suno-music-style-tags-guide.md |
| Instrument palette: lead first, then rhythm/texture layers | suno-music-style-tags-guide.md |
| Vocal persona: gender + tone + delivery style all 3 together | suno-music-style-tags-guide.md |

---

## Related Files
- `/AGENTS/Director/Learnings-Song-Pipeline.md` — Feedback from Arek on previous sessions (apply rules immediately)
- `/CREATIVE/Creative-Style-Bible.md` — Rove sonic/visual identity reference
- `/LEARNING/Knowledge/Music-Production/` — Scholar's full Suno knowledge library
