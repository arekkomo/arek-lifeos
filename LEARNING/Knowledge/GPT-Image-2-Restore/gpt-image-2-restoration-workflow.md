---
title: GPT Image 2 Restoration Workflow
category: concept
summary: Evidence-preserving staged workflow for repairing scanned or damaged photographs with GPT Image 2.
tags: [gpt-image-2, photo-restoration, image-editing, archival, workflow]
sources: 1
updated: 2026-08-09
---

# GPT Image 2 Restoration Workflow

Use GPT Image 2 as an **interpretive repair tool**, not a forensic authority. The goal is to remove visible damage while holding composition, identity, and historically meaningful evidence stable. The workflow applies OpenAI’s documented “change only X” and explicit-invariants pattern. [[GPT Image 2 Restore Sources]]

## 1. Establish the source of truth

1. Preserve an untouched scan and record its provenance, date range, and known people/objects.
2. Inspect at full resolution; list defects separately: dust, scratches, crease, stains, fading, missing edge, or severe loss.
3. Decide the allowed intervention. A family archive may permit aesthetic reconstruction; historical documentation usually requires a conservative repair plus an unedited master.

> ⚠️ Contradiction: a visually convincing restoration may invent pixels or soften evidence. Do not label an output “authentic” merely because it looks photographic. [[GPT Image 2 Restore Sources]]

## 2. Repair in defect-class passes

Work from the smallest, least interpretive intervention to the most interpretive:

1. **Surface cleanup:** dust, specks, small scratches and scanning noise.
2. **Structural repair:** tears, folds, emulsion loss, missing background regions.
3. **Tonal correction:** exposure, contrast and neutral balance without changing photographic era cues.
4. **Detail recovery:** only after the prior pass is accepted; constrain against invented text, jewellery, facial features, or background objects.
5. **Colorization:** a separate pass; use [[GPT Image 2 Colorization Control]].

A mask may narrow the intended region, but it is only guidance and may not follow its exact silhouette. Keep an exclusion list in the prompt and compare output against the original after every pass. [[GPT Image 2 Restore Sources]]

## 3. Prompt structure

Use labeled, reproducible instructions:

- **Task:** name one repair class only.
- **Target:** identify exact physical damage and location.
- **Preserve:** people, identity, pose, crop, geometry, lighting direction, background objects, film grain, text and era character.
- **Do not:** list plausible failure modes for the specific source.
- **Output:** request a clean but natural photographic restoration, not a beauty retouch or reinterpretation.

See [[GPT Image 2 Restoration Prompting]] for copyable templates. OpenAI’s guidance favors clear constraints, a stable order, and small single-change follow-ups over an all-at-once revision. [[GPT Image 2 Restore Sources]]

## 4. Quality-control gate

Before accepting a pass, check at 100%:

- Facial proportions, hands, lettering, uniforms and jewellery unchanged unless the repair was explicitly authorized.
- Edges around repair regions have no repeated texture, halo, blur, or implausible sharpness.
- No newly invented background detail, accessories, signage, or people.
- Grain/noise scale remains coherent across repaired and untouched areas.
- File retains a traceable name such as `source-v01-cleanup`, `v02-tear-repair`, and `v03-colour`.

For layer-aware follow-up work, use [[Stable Layers]] after acceptance rather than trying to solve unrelated compositing changes inside the restoration pass. For a local/open alternative with an explicitly listed restoration capability, compare [[FireRed-Image-Edit]].
