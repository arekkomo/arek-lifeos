---
title: GPT Image 2 Reframe — Source Summary
category: source
summary: Evidence ledger for GPT Image 2 reframe/outpaint workflows, centered on OpenAI image-generation and image-editing guidance.
tags: [gpt-image-2, openai, image-editing, reframe, outpainting]
sources: 3
updated: 2026-08-09
source_date: 2026-08
authors: [OpenAI]
ingested: 2026-08-09
---

# GPT Image 2 Reframe — Source Summary

## Scope and evidence status

This folder is an operational prompt reference for **image editing used as reframing/outpainting**: retain the supplied image and describe only the visual information that should exist in newly extended or editable canvas regions. The official material documents the Image API's generation and editing interfaces, image inputs, masking, output controls, and iteration patterns; it does not prescribe a single official "outpaint prompt" syntax. The prompt patterns in [[GPT Image 2 Reframe Prompt Architecture]] and [[GPT Image 2 Outpaint Continuity Controls]] are therefore production heuristics derived from those documented controls, not quoted OpenAI instructions.

> ⚠️ Version boundary: OpenAI's public guide uses the generic Image API / GPT Image terminology and may change model aliases or parameters. Confirm the deployed model name and accepted image-edit parameters against the current API reference before automating a workflow.

## Primary sources

1. [OpenAI Image generation guide](https://platform.openai.com/docs/guides/image-generation) — Image generation/editing workflow, inputs, masks, response formats, and parameter documentation.
2. [OpenAI Images API reference](https://platform.openai.com/docs/api-reference/images) — Endpoint-level contract for generation and edits.
3. [OpenAI GPT Image API FAQ](https://help.openai.com/en/articles/11128753-gpt-image-api) — Operational FAQ and availability notes for GPT Image API use.

## Evidence-backed operating constraints

- An image-edit request combines a prompt with one or more image inputs; use the edit interface rather than treating a reframe as a text-only recreation. [OpenAI Image generation guide](https://platform.openai.com/docs/guides/image-generation)
- A mask is an alpha-bearing image-control input. Transparent/opaque regions are used to delimit editable versus preserved areas, but the guide cautions that mask behavior is not necessarily pixel-exact at the boundary. [OpenAI Image generation guide](https://platform.openai.com/docs/guides/image-generation)
- Output size, quality, and format are API choices, not semantic prompt details. Select the final framing/aspect strategy outside the creative instruction. [OpenAI Images API reference](https://platform.openai.com/docs/api-reference/images)

## Folder map

- [[GPT Image 2 Reframe Prompt Architecture]] — compact prompt grammar and worked patterns.
- [[GPT Image 2 Outpaint Continuity Controls]] — continuity constraints for lens, light, geometry, and negative space.
- [[GPT Image 2 Canvas and Mask Preparation]] — geometry, alpha, and plate-preparation checklist.
- [[GPT Image 2 Reframe Iteration and QA]] — staged edit loop and acceptance criteria.

## Related vault context

This is an image-editing layer between a source plate and downstream work in [[Flux.Image.Edit]], [[Stable Layers]], and [[image-blaster]]. For VFX use, treat an outpainted result as a candidate plate: validate seams, perspective, and color before composition or 3D reconstruction.
