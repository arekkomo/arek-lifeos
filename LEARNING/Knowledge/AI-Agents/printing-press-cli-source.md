---
title: "Printing Press — CLI Factory for AI Agents (Nate Herk)"
category: source
summary: YouTube walkthrough of Printing Press, a CLI factory/library that helps AI agents like Claude Code talk to tools more efficiently than APIs or MCPs.
tags: [cli, printing-press, claude-code, ai-agents, mcp, automation, token-efficiency]
sources: 1
source_path: raw/This is The Most Powerful Tool to Give to Claude Code.md
source_date: 2026-05
authors: [Nate Herk]
ingested: 2026-05-09
updated: 2026-05-09
---

# Source: Printing Press — CLI Factory for AI Agents

**Source:** [YouTube — Nate Herk | AI Automation](https://www.youtube.com/watch?v=YHk45NEpspE)
**Published:** 2026-05-08

## TL;DR

[[Printing Press]] is a CLI factory + library that lets Claude Code (and other agents) talk to external tools via CLI instead of APIs or MCPs. CLIs are faster, token-efficient, and often work on sites with no public API. A pre-built library of 50+ CLIs is available. Custom CLIs can be built in ~10 minutes using the factory tool.

## Key claims

- **MCP used 35× more tokens than CLI on the same task.** Reliability also dropped from 100% (CLI) to 72% (MCP) as task complexity increased.
- A Skool.com scraping task consumed ~132,000 tokens server-side but only ~2,000 tokens entered Claude's context window via CLI.
- Printing Press can build a custom CLI for any site in 10–60 minutes using natural language instructions to Claude Code.
- CLIs have a SQLite local mirror — no round trips, no rate limits (per se).
- Sites without public APIs (ESPN, Craigslist, Skool, Domino's) can be accessed via CLI thanks to real Chrome sessions.

## Agent tool hierarchy (from video)

1. **CLI** — tier 1 for agents. Pre-formatted output, lazy discovery, no context bloat.
2. **API** — tier 2. Raw JSON, built for code not agents, but any API can be converted to CLI.
3. **MCP** — tier 3. Useful for tool discovery but loads all tool descriptions every session.

## Related pages

- [[cli-for-agents]] — concept page: CLI vs API vs MCP
- [[printing-press]] — entity page
- [[claude-code]] — primary tool this integrates with
