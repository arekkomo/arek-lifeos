---
title: CLI for AI Agents
category: concept
summary: Command-line interfaces are the most token-efficient way for AI agents to interact with external tools — more efficient than APIs or MCPs.
tags: [cli, api, mcp, token-efficiency, ai-agents, claude-code, agentic-workflows]
sources: 1
updated: 2026-05-09
---

# CLI for AI Agents

A CLI (command-line interface) is a way to interact with a tool by running typed commands rather than clicking UI buttons or making HTTP calls. For AI agents, CLIs are increasingly considered the optimal interface layer.

## Why CLIs win for agents

| | CLI | API | MCP |
|---|---|---|---|
| Output format | Pre-formatted, ~200 tokens | Raw JSON, can be 100k+ tokens | Varies |
| Token overhead | Low | Medium | High (loads all tool descriptions) |
| Discovery | Lazy (on demand) | None built-in | Built-in (but costly) |
| Auth | Stored once locally | Per-request | Per-server |
| Round trips | SQLite local mirror, no round trips | HTTP, potential pagination | HTTP |
| Works without API | Yes (Chrome session) | No | Depends |

**Benchmark (from [[printing-press-cli-source]]):** MCP used **35× more tokens** than CLI on the same task. Reliability: 100% CLI vs 72% MCP on complex tasks.

## The agent tool hierarchy

When connecting Claude Code (or any agent) to a new tool, prefer:

1. **Find or build a CLI** — fastest, cheapest, most reliable
2. **Use the API directly** — fallback if no CLI; any API can be turned into a CLI
3. **MCP server** — last resort; useful when tool discovery matters more than efficiency

## Use cases for CLIs over APIs

- Sites with no public API (Skool, ESPN, Craigslist, Domino's)
- Tools with anti-scraping protection (CLI uses a real Chrome session)
- Rate-limited APIs — CLI doesn't bypass rate limits, but adds a local SQLite mirror for caching
- Any task where context window efficiency matters (paying per token)

## Building CLIs

With [[Printing Press]], Claude Code can build a custom CLI for almost any tool in 10–60 minutes using natural language. Requires Go to be installed. Built CLIs can be shared with teams via private GitHub repos.

## Context

The shift toward CLIs is being driven by MCP context bloat — loading 50 MCP tool descriptions every session, even when unused, wastes tokens. CLIs solve this with lazy discovery.

## Related pages

- [[printing-press]] — the primary CLI factory tool
- [[claude-code]] — primary agent this integrates with
- [[printing-press-cli-source]] — source transcript
