---
title: Blender Operations Index
category: synthesis
summary: System-facing operating index for installing, maintaining, troubleshooting and safely using Blender with Hermes on Spark.
tags: [blender, hermes, mcp, spark, operations, runbook]
sources: 2
updated: 2026-07-16
---

# Blender Operations Index

## Purpose
This is the entry point for System and creative agents. It separates three concerns that must not be conflated: Blender application health, the Blender MCP server registered with Hermes, and the in-application addon bridge. [[Blender Official + Hermes Blender MCP Source Summary]]

## Operating model
1. **Blender host:** a supported desktop Blender instance is running; Hermes' documented minimum is Blender 3.0+. [[Blender Official + Hermes Blender MCP Source Summary]]
2. **Hermes side:** install or inspect the catalog entry with `hermes mcp install blender`; start a new Hermes session after installation so its tools can be discovered. [[Blender MCP Hermes Operations]]
3. **Blender side:** install and enable the addon, then in every Blender session open Viewport N-panel → BlenderMCP → **Connect to Claude**. [[Blender MCP Hermes Operations]]
4. **Agent side:** inspect before mutation, script in small logical steps, use a viewport screenshot after meaningful stages, and use absolute output paths. [[Blender MCP Hermes Operations]]

## Fast diagnostic decision tree
| Symptom | First check | Corrective path |
|---|---|---|
| No Blender MCP tools in agent session | Catalog install and session startup timing | Reinstall with `hermes mcp install blender`; start a fresh Hermes session. [[Blender MCP Hermes Operations]] |
| Tool reports connection refused | Is Blender running and the addon connected? | Reconnect in N-panel; do not repeatedly retry an unavailable bridge. [[Blender MCP Hermes Operations]] |
| Calls time out | Is one large script doing too much? | Divide build into geometry, material, animation and render calls. [[Blender MCP Hermes Operations]] |
| Render missing or in unexpected place | Is path absolute on the Blender host? | Set an absolute `scene.render.filepath`; validate host-visible path. [[Blender MCP Hermes Operations]] |
| Automation differs after Blender update | Version and compatibility review | Check installed `bpy` API and engine behavior against current official docs; pin/retest before production. [[Blender Python Automation]] |

## Maintenance baseline for Spark
- Prefer a planned Blender release channel (LTS for stability; newer feature release only after workflow validation) and record the exact version plus GPU driver/CUDA context in the System runbook. Blender publishes both LTS and experimental/current build channels. [[Blender Official + Hermes Blender MCP Source Summary]]
- Before upgrades, preserve a small suite of representative `.blend` scenes and render them before/after; render engine behavior, extensions and Python APIs are version-sensitive. [[Blender Rendering Assets and Maintenance]]
- Treat add-ons/extensions as supply-chain code: document source, version, permissions, compatibility and the rollback location. Blender exposes extensions/add-ons as a managed surface. [[Blender Official + Hermes Blender MCP Source Summary]]
- Keep production assets outside individual `.blend` files where reusable: configure asset libraries, explicit relative/absolute path policy, and a shared naming convention. [[Blender Rendering Assets and Maintenance]]

## Spark validation snapshot — 2026-08-13
- Spark is `aarch64`/Ubuntu noble arm64; `nvidia-smi` sees NVIDIA GB10 with driver 580.142 and CUDA 13.0. Active GPU processes included ComfyUI and Ollama during validation and were not interrupted.
- Host packages are installed and verified: `/usr/bin/blender` reports Blender 4.0.2; `/usr/bin/Xvfb` is present; dpkg reports `blender 4.0.2+dfsg-1ubuntu8 arm64` and `xvfb 2:21.1.12-1ubuntu1.6 arm64`.
- Separate CLI/background render path works: `blender -b --python ...` created `/tmp/blender-system-validation/spark_blender_cli_render.png` (512×512 PNG, 165,614 bytes) and `/tmp/blender-system-validation/spark_blender_validation_scene.blend`.
- Hermes Blender MCP dependency fix applied for Systems: upstream `blender-mcp==1.6.4` currently resolves incompatible `mcp 2.0.0`, which lacks `mcp.server.fastmcp`. Systems now launches MCP through `/home/realityrove/bin/blender-mcp-hermes`, a wrapper for `uvx --with 'mcp<2' blender-mcp==1.6.4`. `hermes mcp test blender` connects and discovers 22 upstream tools; Systems config still selects the four core tools.
- Blender addon was downloaded to `/home/realityrove/.local/share/blender-mcp/addon.py`, installed into Blender user config, enabled as module `addon`, and saved in `/home/realityrove/.config/blender/4.0/config/userpref.blend`. Live Blender under `xvfb-run -a blender --python ...` started the addon bridge on `localhost:9876`.
- Fresh Hermes CLI MCP validation against live Xvfb Blender succeeded for `execute_blender_code`, `get_object_info`, and `get_viewport_screenshot`: it created `Hermes_MCP_Live_Test`, rendered `/tmp/blender-system-validation/spark_blender_mcp_render.png` (512×512 PNG, 130,724 bytes), and captured viewport screenshot `/home/realityrove/.hermes/profiles/systems/cache/images/img_dc06657f209a.png` (1000×851 PNG, 11,336 bytes). `get_scene_info` timed out in the broad fresh-session test, so use targeted object inspection or smaller scene queries until investigated.

## Agent-safe default workflow
`get_scene_info` → `get_object_info` as needed → small `execute_blender_code` calls → `get_viewport_screenshot` → render to absolute path → verify artifact. [[Blender MCP Hermes Operations]]

## Related pages
- [[Blender Production Foundations]] — what the application subsystems do
- [[Blender Python Automation]] — `bpy` and batch patterns
- [[Blender Rendering Assets and Maintenance]] — assets, engines, performance and update policy
- [[Blender MCP Hermes Operations]] — connection/setup/troubleshooting detail
- [[SimWorlds — Multi-Agent Blender Pipeline for Dynamic 4D Scene Generation|SimWorlds]] — research example of a planner-coder-reviewer Blender pipeline
