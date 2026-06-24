---
title: ComfyUI v0.26 and Kling V3-Turbo Integration
category: update
summary: ComfyUI reaches v0.26.x with partner node architecture, notably adding native Kling V3-Turbo model support for AI video generation workflows.
tags: [comfyui, kling, ai-video, workflow, integration, nvidia]
sources: 1
updated: 2026-06-24
---

# ComfyUI v0.26 and Kling V3-Turbo Integration

ComfyUI passed v0.25.x (June 18) and reached v0.26.0 by June 23, 2026, introducing the **Partner Nodes** architecture that enables third-party AI companies to publish native workflow integrations.

## Partner Node system

- **What it is** -- A new distribution channel where partner organizations (e.g., [[kling-ai]], Runway, [[minimax]]) publish official ComfyUI nodes with guaranteed API support
- **Why it matters** -- Previously, community nodes were reverse-engineered and broke on every API change. Partner nodes come with version-pinned SDKs and changelog tracking
- **First partner node** -- Kling V3-Turbo model support (PR #14528)

## Release timeline

| Version | Date | Highlights |
|---------|------|------------|
| v0.26.0 | 2026-06-23 | Updated OpenAPI contract, continued partner node infrastructure |
| v0.25.1 | 2026-06-18 | **Kling V3-Turbo** partner node (PR #14528) |
| v0.25.0 | 2026-06-16 | Partner nodes framework foundation, cloud API contract sync |
| v0.24.0 | 2026-06-03 | Routine updates |
| v0.23.0 | 2026-06-01 | Feature release cycle accelerating |

## Practical workflow impact

- **Kling V3-Turbo in ComfyUI** -- Direct text-to-video and video-to-video generation from within ComfyUI workflows, no separate API calls needed
- **Pipeline chaining** -- Kling output can feed into [[davinci-resolve|DaVinci Resolve]] export nodes for automated post-processing pipelines (when n8n bridges are active)
- **Multi-model comparison** -- Having Kling, MiniMax, and Open-Sora as parallel ComfyUI nodes enables side-by-side quality testing in the same workflow

## Architecture note

The shift from community reverse-engineered nodes to official partner SDKs signals ComfyUI is maturing from hackable prototype to production workflow engine. This aligns with DGX Spark hosting capabilities -- stable API contracts enable pre-built workflow templates rather than custom scripts.

## Related pages

- [[comfyui]]
- [[kling-ai]]
- [[minimax]]
- [[runway-ml]]
- [[ai-video-generation]]
- [[notion-export-ai-video-animation]]
- [[agentic-creative-pipelines]]
