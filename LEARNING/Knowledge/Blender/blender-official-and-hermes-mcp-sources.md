---
title: Blender Official + Hermes Blender MCP Source Summary
category: source
summary: Primary-source digest for Blender 5.2 LTS operations and Hermes' catalog-managed Blender MCP workflow.
tags: [blender, hermes, mcp, source, bpy, operations]
sources: 7
source_path: external://blender-official-and-hermes-blender-mcp
source_date: 2026-07
authors: [Blender Foundation, Hermes Agent, alireza78a, kshitijk4poor]
ingested: 2026-07-16
updated: 2026-07-16
---

# Blender Official + Hermes Blender MCP Source Summary

## TL;DR
Blender is the Blender Foundation's GPL-licensed 3D creation suite, with a documented Python API, render engines, extensions, asset libraries and command-line surface. Hermes' catalog Blender MCP integrates a live desktop Blender session through four curated tools; its addon bridge is a separate, per-session prerequisite.

## Verified source claims
- Blender's official site describes the product as free and open-source 3D creation software and exposes download, LTS, previous-version, extension, manual and Python API channels. [Blender.org](https://www.blender.org/)
- The Blender 5.2 LTS documentation enumerates EEVEE, Cycles and Workbench rendering documentation, Geometry Nodes, asset libraries, extensions and command-line operation. [Manual](https://docs.blender.org/manual/en/latest/getting_started/about/index.html)
- The API documentation identifies `bpy.context`, `bpy.data`, `bpy.ops`, `bpy.types`, `bpy.app`, path utilities and handlers as its principal application modules. [Python API](https://docs.blender.org/api/current/)
- Hermes documents `hermes mcp install blender` as the catalog installation command and a curated tool set: `get_scene_info`, `get_object_info`, `get_viewport_screenshot`, and `execute_blender_code`. [Hermes Blender MCP skill](https://github.com/NousResearch/hermes-agent/blob/main/optional-skills/creative/blender-mcp/SKILL.md)
- Hermes requires an enabled Blender MCP addon, a live Blender desktop session, and a manual **Connect to Claude** action in Blender's N-panel for each Blender session. [Hermes Blender MCP skill](https://github.com/NousResearch/hermes-agent/blob/main/optional-skills/creative/blender-mcp/SKILL.md)
- The MCP skill says Blender background mode is unsupported by the addon; on displayless Linux it recommends `xvfb-run blender`. [Hermes Blender MCP skill](https://github.com/NousResearch/hermes-agent/blob/main/optional-skills/creative/blender-mcp/SKILL.md)
- `execute_blender_code` is arbitrary in-process Python without a sandbox and must be treated with the trust level of terminal access. [Hermes Blender MCP skill](https://github.com/NousResearch/hermes-agent/blob/main/optional-skills/creative/blender-mcp/SKILL.md)

## Source links
1. Blender official site — https://www.blender.org/
2. Blender 5.2 LTS manual — https://docs.blender.org/manual/en/latest/
3. Blender Python API — https://docs.blender.org/api/current/
4. Blender scripting manual — https://docs.blender.org/manual/en/latest/advanced/scripting/index.html
5. Blender asset libraries — https://docs.blender.org/manual/en/latest/files/asset_libraries/index.html
6. Blender rendering engines — https://docs.blender.org/manual/en/latest/render/render_engines.html
7. Hermes Blender MCP skill — https://github.com/NousResearch/hermes-agent/blob/main/optional-skills/creative/blender-mcp/SKILL.md

## Contradictions / version boundaries
> ⚠️ Version boundary: official sources currently document Blender 5.2 LTS, whereas the Hermes skill requires Blender 3.0+. Treat engine identifiers, addon APIs and `bpy` details as version-sensitive; check the installed Blender version before reusing a recipe.

## Where cited
- [[Blender Operations Index]]
- [[Blender Production Foundations]]
- [[Blender Python Automation]]
- [[Blender Rendering Assets and Maintenance]]
- [[Blender MCP Hermes Operations]]
