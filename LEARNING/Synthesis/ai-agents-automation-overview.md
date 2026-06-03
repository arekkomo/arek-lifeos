---
title: AI Agents & Automation — Overview
category: synthesis
summary: Map of AI agent frameworks, agentic workflows, n8n automation, and Claude Code usage patterns.
tags: [ai-agents, n8n, claude-code, automation, agentic-workflows]
sources: 0
updated: 2026-04-19
---

# AI Agents & Automation — Overview

This synthesis covers agent frameworks, workflow automation, and agentic AI systems.

## Topic clusters

- **AI Agents** — ReAct loops, tool use, multi-agent systems, agent design patterns
- **[[n8n|n8n]]** — node-based automation, workflow patterns, MCP integration
- **[[claude-code|Claude Code]]** — agentic coding, skills/plugins, hooks, slash commands
- **Agentic Workflows** — combining LLMs + tools + automation for end-to-end pipelines

## Documented patterns (from knowledge base)

### n8n + Claude for knowledge ingestion
The YouTube → Notion pipeline in the dtb Knowledge database is a real production example:
- n8n handles triggering, data flow, and Notion writes
- Claude handles classification and tagging (LLM-as-classifier pattern)
- Result: automated knowledge base that populated itself
See [[n8n]] for the full pattern.

### Agentic creative pipelines
For creative generation (image/video), agents outperform n8n. Agents with prompting memory are more robust than node graphs for iterative creative work.
See [[agentic-creative-pipelines]].

### AI Automation Agency (AAA) model
Business model: sell AI automation services to businesses. Real and documented, though income claims in sources are promotional.
See [[ai-automation-agency]].

## Frontier model context

- **[[google-deepmind|Gemini 2.0]]** — first major frontier model explicitly designed "for the agentic era"; multimodal
- **[[state-space-models|Mamba/SSMs]]** — architectural research worth tracking; efficient long-context processing

## Key questions this wiki tracks

- What are the reliable patterns for building robust agents (tool selection, error handling, loops)?
- How do n8n workflows integrate with LLM APIs?
- What Claude Code skills/patterns are worth internalizing?
- Where do agentic workflows break down and why?
- When does n8n win, and when do agentic platforms win?

## Related pages

- [[Synthesis/ai-creative-tools-overview]] — agents can automate creative generation pipelines
- [[n8n]]
- [[claude-code]]
- [[google-deepmind]]
- [[agentic-creative-pipelines]]
- [[ai-automation-agency]]
- [[state-space-models]]
