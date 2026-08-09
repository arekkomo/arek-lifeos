---
title: Z-Image Generation Settings
category: concept
summary: Documented base versus Turbo settings and a controlled testing protocol for storyboard-still generation.
tags: [z-image, text-to-image, diffusers, cfg, seed, storyboard]
sources: 4
updated: 2026-08-09
---

# Z-Image Generation Settings

## Choose the checkpoint by job

| Need | Choose | Why |
|---|---|---|
| Fast breadth-first thumbnailing or rapid board iteration | **Z-Image-Turbo** | Distilled eight-forward generation; official example uses zero guidance. [[Z-Image Official Source Summary#Confirmed operating facts|[1]]] |
| Negative-prompt control, more deliberate steering, or look exploration | **Z-Image** | Official documentation exposes 28–50 steps, CFG 3–5 and strongly recommends negative prompts. [[Z-Image Official Source Summary#Confirmed operating facts|[1]]] |

## Documented starting settings

| Setting | Z-Image | Z-Image-Turbo |
|---|---:|---:|
| Resolution | 512×512 to 2048×2048 total dimensions, any aspect ratio | Start at the delivery frame size; the official example is 1024×1024 |
| Steps | 28–50 | 9 scheduler steps / 8 DiT forwards in official example |
| Guidance / CFG | 3.0–5.0 | 0.0 |
| Negative prompt | Strongly recommended | Do not assume it operates as it does on base |
| CFG normalization | False for general stylism; true for realism | Not applicable to the documented Turbo path |

All values above are reported from Tongyi-MAI’s repository/model-card examples; they are starting points, not a quality guarantee for every workflow. [[Z-Image Official Source Summary#Confirmed operating facts|[1]]]

## Controlled storyboard test ladder

1. **Lock format.** Set the intended editorial aspect ratio before evaluating composition. Create a landscape, portrait or square board intentionally rather than cropping a generic frame later.
2. **Lock seed and prompt.** Compare one setting at a time; Diffusers supports a seed generator for repeatable runs. [[Z-Image Official Source Summary#Confirmed operating facts|[1]]]
3. **Select composition before texture.** First decide whether frame, blocking, eyeline and prop state work. Only then tune palette, grade or material detail.
4. **Branch deliberately.** Make separate variants for framing, action and lighting. Do not blend all changes into one retry, because the cause of improvement cannot be identified.
5. **Record the accepted still.** Keep checkpoint, dimensions, steps, guidance, seed, full prompt, negative prompt if used, and the accepted image ID in the shot card.

## Diagnostic retakes

| Failure | First retake action |
|---|---|
| Subject placement or eyeline is wrong | Move the relation earlier in the prompt and simplify competing composition detail. |
| Prop/wardrobe continuity drifts | Promote the anchor into subject/environment sentences; remove nonessential novelty. |
| Image has the right content but wrong board mood | Keep seed and composition fixed; alter only lighting, palette and finish terms. |
| Base checkpoint produces persistent unwanted element | Add the specific unwanted element to a concise negative prompt; do not paste a generic long blacklist. |
| Turbo output lacks desired constraint | Clarify the positive description or generate a controlled seed batch; do not apply base CFG assumptions. |

## Related pages

- [[Z-Image Official Source Summary]]
- [[Z-Image T2I Prompting]]
- [[Z-Image Storyboard Stills]]
