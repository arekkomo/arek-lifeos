---
title: n8n
category: entity
summary: Open-source, node-based workflow automation platform with self-hosting support and LLM integration.
tags: [n8n, automation, workflow, no-code, ai-agents]
sources: 0
updated: 2026-04-19
---

# n8n

Node-based workflow automation tool. Self-hostable. Strong integration ecosystem and growing AI/LLM node support.

## Core concepts

_Nodes, triggers, webhooks, credentials, expressions, sub-workflows._

## AI & LLM integration

_AI Agent nodes, MCP server connections, LangChain integration, Claude/OpenAI nodes._

## Key workflow patterns

### YouTube → Notion ingestion pipeline (production use)
The workflow that built the dtb Knowledge database:
1. YouTube video URL triggers n8n
2. Claude extracts title, description, key takeaways
3. Claude classifies into 12-category tag taxonomy
4. Structured data written to Notion dtb Knowledge database

This is a proven, production-grade pattern for automated knowledge ingestion with LLM classification.

### When n8n wins vs. when agents win

| n8n | Agentic platforms |
|---|---|
| Deterministic data flows | Creative generation with judgment |
| Structured API integrations | Tasks requiring iteration/evaluation |
| Simple trigger → action chains | Complex multi-step reasoning |

See [[agentic-creative-pipelines]] for the full breakdown.

## Related pages

- [[Synthesis/ai-agents-automation-overview]]
- [[agentic-creative-pipelines]]
- [[ai-automation-agency]]
- [[notion-export-ai-agents-automation-n8n]]
