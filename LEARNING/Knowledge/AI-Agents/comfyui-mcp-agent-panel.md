---
title: "ComfyUI Agent Panel by artokun — Autonomous AI Agent in ComfyUI Sidebar"
category: source
summary: Autonomous AI agent embedded directly in the ComfyUI sidebar that drives canvas edits via natural language. Supports both Claude and ChatGPT subscriptions with no API keys required. Part of the comfyui-mcp orchestration project enabling live graph editing, workflow loading, and custom node installation.
tags: [comfyui, ai-agent, mcp, canvas-editing, claude-integration, chatgpt, workflow-automation]
sources: 2
source_path: https://github.com/artokun/comfyui-mcp-panel
source_date: 2026-06
authors: [artokun / ComfyUI-MCP team]
ingested: 2026-06-29
updated: 2026-06-29
---

# ComfyUI Agent Panel: Autonomous AI Agent in Canvas Sidebar

## Overview

Autonomous AI agent embedded in the ComfyUI sidebar that sees the current graph and edits it live from natural language instructions. Uses either Claude or ChatGPT subscription with no API keys needed. Every edit is undoable via Ctrl+Z. Part of the comfyui-mcp project on GitHub, an MCP server plus agent orchestrator for ComfyUI.

## Architecture: MCP Server Plus Panel

### The Orchestrator Layer

The comfyui-mcp server runs as a background process started by the panel. It provides the agent with live canvas state including current node graph and selected nodes. Node definitions cover available custom nodes and parameters. Model registry tracks installed checkpoints and LoRAs. Workspace file system access enables workflow loading.

### The Panel Agent Layer

The sidebar provides the conversational interface with full feature parity across both providers:

| Capability | Claude | ChatGPT |
|------------|--------|---------|
| Live canvas edits | Yes | Yes |
| Workflow loading | Yes | Yes |
| Node installation | Yes | Yes |
| Cost guardrails | Yes | Yes |

### Example Interactions

Add a KSampler and wire it to my checkpoint results in nodes on the canvas that are auto-connected. Load a workflow from Civitai parses JSON and places all nodes. Install ControlNet fetches from ComfyUI-Manager registry.

## Installation

Available on ComfyUI-Manager as comfyui-agent-panel. Also published to the Comfy Registry. Uses native ComfyUI design system for visual consistency. Documentation at comfyui-mcp.artokun.io docs.

## Relevance to Video Workflows

Multi-node compositions like VAE encode through sampler to VAE decode can be generated conversationally. New custom nodes for video models require fewer wiring steps. Agent sees graph state and can identify disconnected nodes or mismatched datatypes during error debugging.

The MCP server exposes canvas operations as tools that n8n already supports natively, enabling orchestration of ComfyUI generations from automation workflows. This enables multi-agent pipelines where an orchestrator agent designs a workflow and the ComfyUI agent executes it.

## Integration with Existing Tools

Similar paradigm to [[claude-code]] applied to node-graph workflows instead of code repositories. ComfyUI-Manager handles installation but not graph construction, which the Agent Panel fills. The cost model runs on existing subscriptions with no per-request API pricing beyond current plan limits. MCP orchestrator runs locally.

> **Note:** Four GitHub stars as of June 2026 indicates early adoption stage. The MCP architecture and registry listing indicate readiness for production use in ComfyUI video pipelines.
