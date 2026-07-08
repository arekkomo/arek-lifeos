---
title: LTX 2.3 Prompting Guide
category: concept
summary: Complete LTX-2.3 prompt writing methodology — structure rules, cinematographic language, camera directions, lighting specs, environment detail, character descriptions, negative prompt strategies
tags: [ltx-2, ltx-2.3, prompting, prompt-engineering, guide, cinematography, camera-direction]
sources: 2
updated: 2026-07-04
---

# LTX 2.3 Prompting Guide

> **Primary Reference**: [[github:LTX-2 README]] + [[blog:ltx-prompting]]

## Core Principle

LTX-2 needs **detailed, chronological descriptions of actions and scenes** — written in a single flowing paragraph. Start directly with the action. Think like a **cinematographer describing a shot list**. Keep prompts within 200 words for best results.

## Prompt Building Structure

### Step 1: Main Action (Single Sentence)
Start with a direct, concrete main action description — what happens in the scene.

> "A woman walks through a desert canyon at golden hour"
> **NOT** "Imagine you're creating a video of a..." or "Can you show me..."

### Step 2: Movements & Gestures (Specific Details)
Describe precise movement patterns, body language, and gestures.

> "She raises her hand to shield her eyes as dust swirls around her boots"
> **NOT** vague descriptions like "she moves naturally"

### Step 3: Character/Objec

t Appearances (Precise)
Detail exact appearance — clothing items, colors, textures, skin tone, hair style.

> "She wears a faded khaki sleeveless shirt with rolled sleeves and worn leather boots, her dark curly hair tied back with a red scarf"

### Step 4: Background & Environment Details
Describe the full environment — terrain, weather, time of day, background objects.

> "Towering sandstone formations in deep orange and rust shades rise on both sides, with scattered creosote bushes dotting the canyon floor"

### Step 5: Camera Angles & Movements (Critical)
Specify camera position, angle, and motion with technical cinema terminology.

> "Low-angle tracking shot following her from behind as she advances deeper into the canyon"
> **NOT** just "nice camera work" or leaving it unstated

### Step 6: Lighting & Colors
Describe lighting quality, direction, color temperature, and palette.

> "Warm golden-hour backlight creates dramatic rim light along her silhouette while deep orange shadows pool between rock formations"

### Step 7: Changes or Events (Narrative Arc)
Include temporal progression — what changes during the shot.

> "As she steps into a narrow passage, sunlight catches a hidden waterfall cascading from an unseen ledge, mist catching prismatic refraction in the air"

## Cinematographic Camera Directions Reference

| Direction | Technical Term | Prompt Phrase Example |
|-----------|---------------|----------------------|
| Follow behind camera | Tracking shot / Dolly back | "Tracking shot following her from behind |
| Side movement | Trucking / Whip pan | "Camera tracks left along the shoreline with the subject" |
| Circle around | Arc shot / Crane rotation | "Slow 360° arc shot circling the fountain |
| Approach camera | Dolly in / Zoom in | "The figure walks slowly toward the camera as lights fade to black |
| Pull back | Dolly out / Zoom out | "Rapidly pull back revealing a hidden cliff, revealing a hidden valley with smoke rising from the canopy and distant mountains visible through cloud layers
| Low angle looking up | Low-angle shot | "Low-angle of the character standing against blue sky
| High angle looking down | High-angle / Overhead | "Drone shot descending through clouds into an ancient forest" |
| Eye level static | Locked-off | "Locked camera at eye level as subject enters frame from right to left |
| Dutch/tilted angle | Dutch tilt | "Slight dutch tilt adds tension as the character turns their head |
| Shallow depth of field | Rack focus / Deep focus | "Shallow depth of field with background melting into soft bokeh" |
| Fast motion | Time lapse / Speed ramp | "Time-lapse of city traffic with streaking light trails" |

## LTX-2 Specific Prompting Techniques

### ✅ DO:
- Use **active voice** and **direct commands**: "A man opens a door", not "There is a man who opens a door"
- Include **specific temporal progression**: "She turns → pauses → looks back" (not just static scenes)
- Write in **present continuous tense**: "walking through", "shining on", "filling the room"
- Specify exact **colors, materials, and lighting** with precise terminology
- Include **character movement trajectories**: "moving from left to right across the frame"
- Add **environmental atmosphere**: "mist rolling through", "dust motes floating", "raindrops cascading"

### ❌ DON'T:
- Start with "A video of..." or "Show me..." (wastes token space)
- Use abstract art terms ("evocative", "atmospheric", "beautiful") without visual specifics
- Over-explain metaphorical meaning — LTX-2 needs **literal visual descriptions**
- Include multiple unrelated scenes in one prompt — keep to **one continuous shot**
- Omit movement entirely — static prompts produce shorter, less dynamic results
- Use contradictory terms ("bright but dark", "fast and slow" without specification)

### Prompt Length Guidelines:

| Length | Best For | Quality Risk |
|--------|----------|-------------|
| 100-120 words | Quick prototypes, testing concepts | May lack detail for complex scenes |
| **130-160 words** | **Sweet spot — most prompts** | **Optimal balance of detail + clarity** |
| 170-200 words | Complex scenes requiring precise control | Good but diminishing returns above 200 |
| 200+ words | Over-specified — model may ignore late details | Risk of conflicting signals |

## Camera + LoRA Combinations (Critical Technique)

LTX-2 has dedicated camera motion LoRAs. Use these **explicitly in prompts** to activate them:

```
Prompt structure with camera LoRA:
[Scene description] + "[camera direction LoRA]" + [lighting details]
```

Example prompt using Camera LoRA:
> "A lone figure climbs the stairs toward a cathedral entrance, dramatic chiaroscuro lighting carving shadows across stone steps. Slow dolly in following upward movement with depth of field keeping foreground sharp while background blurs gradually"

Where "slow dolly in" activates the Dolly-In camera motion LoRA automatically.

## Enhancement Techniques

### Automatic Prompt Enhancer
LTX-2 pipelines support `enhance_prompt=True` to automatically expand shorter prompts into full cinematographic descriptions. Use for:
- When you have a concept but lack technical phrasing
- Rapid prototyping of ideas before refining manually
- Converting rough scene concepts into production-ready prompts

### Negative Prompt Strategy (Implicit)
LTX-2 doesn't use explicit negative prompts, but you can achieve similar results by:
- **Specify what IS present** to implicitly exclude what isn't
- Use precise camera framing statements: "Camera frame stays tight on subject" prevents unwanted wide shots
- Specify fixed aspects: "Lighting remains consistent throughout the shot" prevents unexpected lighting shifts

## Example Prompts (Template Format)

### Scene 1 — Character Action:
"A woman in a crimson coat walks briskly through a narrow London alley at twilight. Rain-slicked cobblestones reflect the warm glow of wrought-iron street lamps as puddles splash around her heels. Low-angle tracking shot moving parallel to her, keeping her in the right third of frame while background buildings tilt inward with slight dutch angle. Cool blue ambient from evening sky fills the upper frame with amber pools of light below."

### Scene 2 — Nature Landscape:
"Mist rolls through an ancient redwood forest at dawn. Tall trunks rise vertically into a canopy where single shafts of golden light pierce through fog and illuminate floating pollen particles. Ground level locked camera as gentle breeze causes fern fronds to sway rhythmically in foreground while the background remains still."

### Scene 3 — Product/Detail Shot:
> "Extreme close-up of hand placing fresh basil leaves onto pizza dough spreading in slow motion, olive oil glistening on golden crust surface with steam beginning to rise. Shallow depth of field with bokeh lights from kitchen in background transitioning to soft focus"

## Advanced Prompting Techniques

### Temporal Control Strategy
LTX-2 responds well to explicit temporal markers:
| Time Marker | Effect |
|-------------|--------|
| "At first... then..." | Clear before/after transition for scene events |
| "Gradually over the course of 5 seconds,..." | Smooth continuous changes |
| "Suddenly,", | Abrupt event triggering |
| "As the light fades," | Temporal lighting progression |

### Character Detail Protocol
LTX-2 excels with detailed character descriptions. Use this structure:
```
[Name/role], [age approx], [build], [distinctive features], [clothing materials/colors]
```

Example:
> "An elderly fisherman in his 70s, wiry build with weathered skin and silver beard, wearing a faded teal wool sweater and oilskin coat"

### Environment Construction Pattern
Build environments using the **Foreground → Midground → Background** formula:
```
[Foreground details] + [Midground subjects/actions] + [Background environment/atmosphere]
```


## Cross-Reference Map

LTX-2 Prompting ↔ Related Knowledge Pages:
- [[Model Architecture]] — Understanding RoPE explains WHY certain camera terms work better
- [[Video Production Techniques]] — Practical workflow from concept to final video
- [[TI2VidTwoStagesPipeline]] — Which pipeline to use for different prompt complexity levels
- [[DIstilledLoRA]] — Quick-turnaround for testing prompts iteratively
- [[IC-LORA: Camera Motion Control]] — How camera LoRAs integrate with natural language