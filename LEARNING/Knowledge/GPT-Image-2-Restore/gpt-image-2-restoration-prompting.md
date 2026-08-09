---
title: GPT Image 2 Restoration Prompting
category: concept
summary: Reusable constrained prompts for conservative photo cleanup, repair, tonal correction, and iterative review.
tags: [gpt-image-2, prompting, photo-restoration, image-editing, archival]
sources: 1
updated: 2026-08-09
---

# GPT Image 2 Restoration Prompting

These templates turn OpenAI’s documented edit pattern—specific change plus an explicit preserve list—into restoration prompts. They deliberately avoid claims about details absent from the source. [[GPT Image 2 Restore Sources]]

## Base restoration template

```text
Task: conservatively restore this archival photograph.
Target: remove [specific damage] in [specific location].
Preserve exactly: the original people and their identity, facial features, body proportions, pose, crop, camera angle, object geometry, background layout, text, clothing, jewellery, lighting direction, tonal character, and period-appropriate film grain.
Do not: add, remove, beautify, reinterpret, sharpen into new detail, change the composition, alter text, or introduce modern colour grading.
Output: a natural photographic repair that looks like the same original image after careful physical restoration.
```

## Defect-class prompts

### Dust and light scratches

```text
Change only: remove the small dust, scanning specks, and fine surface scratches. Keep all photographic detail, grain, edges, facial features, lettering, and contrast exactly as in the source. Do not smooth skin or fabrics; do not invent texture in damaged areas.
```

### Tear or crease repair

```text
Repair only the torn/creased area at [location]. Reconstruct the minimum continuous texture needed to join the surrounding photograph. Preserve the subject, object boundaries, perspective, lighting and all visible evidence outside the damaged strip. If a detail is unknowable from adjacent pixels, keep it restrained rather than inventing a distinct object, facial feature, or letter.
```

### Tonal restoration

```text
Correct only faded exposure and colour cast. Preserve the image’s original contrast character, shadow detail, highlight roll-off, film grain, composition, and all scene content. Do not apply HDR, beauty retouching, a modern cinematic grade, or artificial sharpening.
```

## Iteration protocol

1. Start with one defect class and one objective acceptance test.
2. Review the result against the original at full scale.
3. Follow up with one delta only: “restore the original background,” “reduce smoothing in the face,” or “remove the remaining crease at lower left.”
4. Repeat the full preserve list whenever a result starts drifting.

OpenAI explicitly recommends small, single-change follow-ups and re-stating critical invariants across edit iterations. [[GPT Image 2 Restore Sources]]

## Avoid

- “Make it better,” “enhance everything,” or “make it modern”: these lack a stable preservation boundary.
- One prompt that combines cleanup, large reconstruction, retouching, reframing, and colorization.
- Calling generated repair “recovered information.” It is a plausible visual completion unless corroborated elsewhere. [[GPT Image 2 Restore Sources]]

## Related pages

- [[GPT Image 2 Restoration Workflow]]
- [[GPT Image 2 Colorization Control]]
- [[GPT Image 2 Restore Sources]]
