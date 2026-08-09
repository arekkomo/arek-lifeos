---
title: "SeFi-Image 5B Turbo — Storyboard Still Prompt Grammar"
category: concept
summary: "A controllable six-field prompt grammar for turning a directing beat into rapid T2I storyboard stills."
tags: [sefi-image, storyboard, shot-design, prompting, filmmaking, t2i]
sources: 1
updated: 2026-08-09
---

# SeFi-Image 5B Turbo — Storyboard Still Prompt Grammar

This is a production grammar for storyboard stills, not a claimed official SeFi syntax. It is designed around the documented Turbo four-step default and its short natural-language examples: make the image-level decision explicit, then iterate it rather than burying it in prose.[1]

## The six fields

| Field | Question it answers | Example language |
|---|---|---|
| Frame | What is the designed image? | `wide 2.39:1 storyboard still`, `tight profile close-up` |
| Subject | Who/what must remain identifiable? | `Mara, 30s, shaved head, red flight jacket` |
| Beat | What single instant carries the scene? | `hesitates before opening the airlock` |
| Geography | Where is everyone in relation to the world? | `at the end of a narrow service corridor, doorway behind her` |
| Camera | How does the audience encounter it? | `low-angle 28mm, subject screen right, deep vanishing lines` |
| Light/finish | What emotional and material read completes it? | `cold overhead fluorescents, red emergency spill, matte industrial surfaces` |

## Assembly order

1. Write the **beat** as a still image, not a synopsis.
2. Add the indispensable **subject anchor** and one or two continuity cues.
3. Put the subject in a readable **geography**.
4. Select a **camera** that expresses power, distance, or discovery.
5. Add **light/finish** only after the dramatic image is clear.

The resulting prompt is one sentence, not six labels. Example:

`Medium-wide storyboard still of Mara, shaved head and red flight jacket, hesitating with one hand on an airlock wheel, alone at the end of a narrow service corridor with the doorway behind her, low-angle 28mm, subject screen right against deep vanishing lines, cold fluorescent top light cut by a red emergency spill, matte industrial production-design realism.`

## Coverage set for one beat

For a fast previsualization board, generate a deliberate set instead of random variants:

- **Establish:** geography and dominant visual problem.
- **Master:** the actor/blocking relationship to that geography.
- **Power frame:** the frame that clarifies the turn or imbalance.
- **Detail/insert:** only if an object or gesture changes the beat.

Keep the subject identity, location, time, and palette fixed across the set; change shot size, axis, and beat emphasis intentionally. Connect this to [[Purposeful Shot Lists]] and [[AI Video Scene Packet]] when the chosen stills become production tests.

## Sources

[1] https://github.com/jmliu206/SeFi-Image — SeFi-Image official inference repository
