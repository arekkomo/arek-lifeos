---
title: Blender MCP Hermes Operations
category: concept
summary: Setup, interface, safe workflow and troubleshooting guide for controlling a live Blender session from Hermes via the catalog Blender MCP.
tags: [blender, hermes, mcp, bpy, troubleshooting, automation]
sources: 1
updated: 2026-07-16
---

# Blender MCP Hermes Operations

## Scope
The catalog Blender MCP gives Hermes a curated interface to a live Blender desktop session. It is not a general remote desktop protocol and it does not replace Blender UI training. [[Blender Official + Hermes Blender MCP Source Summary]]

## Expected setup
1. Install the catalog server once: `hermes mcp install blender`. [[Blender Official + Hermes Blender MCP Source Summary]]
2. Install the Blender addon from the catalog post-install guidance; the upstream skill specifies Blender Preferences → Add-ons → Install `addon.py` and enable **Interface: Blender MCP**. [[Blender Official + Hermes Blender MCP Source Summary]]
3. Start Blender first. In a 3D Viewport press `N`, open the **BlenderMCP** tab and click **Connect to Claude**. [[Blender Official + Hermes Blender MCP Source Summary]]
4. Start a Hermes session after MCP installation, so tool discovery can register the server's tools. [[Blender Official + Hermes Blender MCP Source Summary]]
5. On a displayless Linux host, use a live virtual display (`xvfb-run blender`), not `blender -b`; the documented addon refuses background mode. [[Blender Official + Hermes Blender MCP Source Summary]]

## Curated tool interface
| Tool | Use | Guardrail |
|---|---|---|
| `get_scene_info` | List objects/scene state before edits | First tool on every new scene. [[Blender Official + Hermes Blender MCP Source Summary]] |
| `get_object_info` | Inspect transform/materials for a target object | Verify name/state before mutation. [[Blender Official + Hermes Blender MCP Source Summary]] |
| `get_viewport_screenshot` | Review composition and visual result | Use after each major construction stage. [[Blender Official + Hermes Blender MCP Source Summary]] |
| `execute_blender_code` | Run focused `bpy` operations | Treat as trusted arbitrary Python; one logical step per call. [[Blender Official + Hermes Blender MCP Source Summary]] |

Optional asset-service tools (Poly Haven, Sketchfab, Hyper3D, Hunyuan3D) are disabled by default and must be intentionally enabled through `hermes mcp configure blender`. [[Blender Official + Hermes Blender MCP Source Summary]]

## Recommended agent procedure
1. Inspect scene; preserve existing work unless the task explicitly authorizes clearing it.
2. State and implement one stage at a time: create/modify geometry, assign material, animate, light, configure render.
3. Inspect/screenshot between stages; bridge timeouts are more likely with monolithic scripts. [[Blender Official + Hermes Blender MCP Source Summary]]
4. Set an absolute render output path. It resolves on the Blender host—not necessarily the agent host. [[Blender Official + Hermes Blender MCP Source Summary]]
5. Confirm expected objects and the output artifact; report the absolute rendered path.

## Troubleshooting
| Failure | Likely cause | Fix |
|---|---|---|
| Tools absent | MCP installed after the current Hermes session started | Install/repair catalog entry and open a new Hermes session. [[Blender Official + Hermes Blender MCP Source Summary]] |
| Connection refused | Blender stopped or addon bridge not connected | Start Blender and reconnect in N-panel; do not retry blind. [[Blender Official + Hermes Blender MCP Source Summary]] |
| Bridge timeout | Excessive code in a single call | Split by construction stage and validate between calls. [[Blender Official + Hermes Blender MCP Source Summary]] |
| Render cannot be found | Relative path or wrong machine assumption | Use an absolute Blender-host path and verify it after render. [[Blender Official + Hermes Blender MCP Source Summary]] |
| Script changes wrong object/mode | `bpy.ops` context/selection dependency | Inspect state; explicitly select/activate/mode-set or favor data API. [[Blender Python Automation]] |

## Security
`execute_blender_code` is not sandboxed. Never relay untrusted scripts, arbitrary URLs or opaque code into the live Blender process. Use the curated MCP interface rather than raw TCP/JSON workarounds, which the Hermes skill explicitly deprecates. [[Blender Official + Hermes Blender MCP Source Summary]]

## Related pages
- [[Blender Operations Index]]
- [[Blender Python Automation]]
- [[Blender Rendering Assets and Maintenance]]
