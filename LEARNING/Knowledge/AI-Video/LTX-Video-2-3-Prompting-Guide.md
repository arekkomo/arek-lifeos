---
title: LTX Video 2.3 — Prompting Guide
category: concept
summary: Official prompting guide for LTX-2.3 video generation — structure, rules, camera language, character description, examples, and limitations.
tags: [ai-video, ltx, prompting, video-generation, cinematic]
sources: 1
updated: 2026-05-07
source_path: https://ltx.io/model/model-blog/prompting-guide-for-ltx-2
source_date: 2025
authors: [LTX / Lightricks]
ingested: 2026-05-07
---

# LTX Video 2.3 — Prompting Guide

Source: https://ltx.io/model/model-blog/prompting-guide-for-ltx-2

---

## Prompt Structure

Write prompts as a **single flowing paragraph**, 4–8 descriptive sentences. Use this order:

1. **Establish the shot** — cinematography terms matching film genre and scale
2. **Set the scene** — lighting, color palette, textures, atmosphere/mood
3. **Describe the action** — natural sequence flowing beginning to end, present tense
4. **Define character(s)** — age, hairstyle, clothing, distinguishing details, emotion via physical cues
5. **Identify camera movement(s)** — when/how the view shifts, what subjects appear after motion
6. **Describe the audio** — ambient sounds, music, speech, dialogue in quotation marks with language/accent if needed

---

## Key Rules

### DO

- Keep prompt as a single flowing paragraph for a cohesive scene
- Use **present tense** verbs for movement and action
- Match detail to shot scale — closeups need more precise detail than wide shots
- Focus camera descriptions on the camera's **relationship to the subject**
- Include what subjects appear **after** camera motion to help the model complete the move
- Paint a complete picture flowing naturally from beginning to end
- Iterate — LTX-2 is designed for fast experimentation

### DON'T

- Avoid emotional labels ("sad", "confused") — use **physical cues** (posture, gesture, facial expression)
- Don't include readable text, logos, or signage — LTX-2 cannot generate consistent text
- Avoid complex physics or chaotic motion (jumping, juggling) — causes artifacts/glitches
- Don't overload scenes with too many characters, layered actions, or excessive objects
- Avoid mixing conflicting light sources unless clearly motivated
- Don't overcomplicate — too many actions/characters increases chance some won't render

---

## Camera Language

Use these technical style markers:

> "follows, tracks, pans across, circles around, tilts upward, pushes in, pulls back, overhead view, handheld movement, over-the-shoulder, wide establishing shot, static frame"

**Examples from the guide:**
- "the camera pans left to follow the truck's reckless drive"
- "The camera slowly pans right, revealing the grandfather"
- "the camera slowly arcs left around her, keeping her face and mic in sharp focus"
- "the camera dollys back and keeps the robot's slow walk in a medium shot"
- "slow dolly in," "handheld tracking," "over-the-shoulder"

**Key rule:** When describing camera movement, focus on the camera's relationship to the subject. Including how subjects or objects appear *after* the camera motion gives the model a better idea of how to finish the motion.

---

## Character Description

Required elements:
- Age range (e.g., "woman and a man in their 30s")
- Hairstyle (e.g., "short brown hair and bangs")
- Clothing specifics (e.g., "bodysuit with a tube attached to her neck")
- Distinguishing details
- Emotions via **physical cues only** — never abstract labels

Example from guide:
> "a young african american woman wearing a futuristic transparent visor and a bodysuit with a tube attached to her neck...she gets up slowly from her chair"

---

## Scene Description

Include:
- **Lighting:** flickering candles, neon glow, natural sunlight, dramatic shadows
- **Textures:** rough stone, smooth metal, worn fabric, glossy surfaces
- **Color palette:** vibrant, muted, monochromatic, high contrast
- **Atmospheric elements:** fog, rain, dust, particles, smoke

---

## Good Prompt Examples (verbatim)

**Monster truck / action:**
> "An action packed, cinematic shot of a monster truck driving fast towards the camera, the truck passes the cameras it pans left to follow the trucks reckless drive. dust and motion blur is around the truck, hand held feel to the camera as it tries to track its ride into the distance. the truck then drifts and turns around, then drives back towards the camera until seen in extreme close up."

**Dialogue / character scene:**
> "A warm sunny backyard. The camera starts in a tight cinematic close-up of a woman and a man in their 30s, facing each other with serious expressions. The woman, emotional and dramatic, says softly, 'That's it... Dad's lost it. And we've lost Dad.' The man exhales, slightly annoyed: 'Stop being so dramatic, Jess.' A beat. He glances aside, then mutters defensively, 'He's just having fun.' The camera slowly pans right, revealing the grandfather in the garden wearing enormous butterfly wings, waving his arms in the air like he's trying to take off. He shouts, 'Wheeeew!' as he flaps his wings with full commitment. The woman covers her face, on the verge of tears. The tone is deadpan, absurd, and quietly tragic."

**Interior / POV:**
> "INT. OVEN – DAY. Static camera from inside the oven, looking outward through the slightly fogged glass door. Warm golden light glows around freshly baked cookies. The baker's face fills the frame, eyes wide with focus, his breath fogging the glass as he leans in...Baker (whispering dramatically): 'Today… I achieve perfection.'"

**Cinematic performance (most relevant for music video work):**
> "A warm, intimate cinematic performance inside a cozy, wood-paneled bar, lit with soft amber practical lights and shallow depth of field that creates glowing bokeh in the background. The shot opens in a medium close-up on a young female singer in her 20s with short brown hair and bangs, singing into a microphone while strumming an acoustic guitar, her eyes closed and posture relaxed."

---

## LTX-2 Strengths

- Cinematic compositions — wide, medium, close-up with thoughtful lighting, shallow depth of field, natural motion
- Emotive human moments — single-subject emotional expressions, subtle gestures, facial nuance
- Atmosphere & setting — fog, mist, golden hour light, soft shadows, rain, reflections, ambient textures
- Clean camera language — "slow dolly in," "handheld tracking," "over-the-shoulder"
- Stylized aesthetics — painterly, noir, analog film look, fashion editorial, surreal
- Voice — characters can talk and sing in various languages (lipsync supported)
- Strong style range: stop-motion, 2D/3D animation, claymation, comic book, cyberpunk, 8-bit, film noir, fantasy, thriller, arthouse, documentary

---

## LTX-2 Limitations

| Issue | Detail |
|---|---|
| No readable text | Avoid signage, brand names, logos, printed material |
| Complex physics | Jumping, juggling → artifacts. Dancing works fine. |
| Scene overload | Too many characters or actions reduces quality |
| Emotional abstraction | Must use physical cues, not emotional labels |
| Lighting conflicts | Avoid unmotivated mixed light sources |
| Prompt overload | More = higher chance some elements won't render |

---

## Related Pages

- [[AI-Video/index]] — AI video tools overview
- [[Runway-Gen4]] — alternative video generator
- [[Kling-AI]] — alternative video generator
