---
title: Printing Press
category: entity
summary: CLI factory and library for AI agents — turns any tool into a token-efficient command-line interface that Claude Code can use natively.
tags: [printing-press, cli, claude-code, ai-agents, automation, go]
sources: 1
updated: 2026-05-09
---

# Printing Press

**Website:** [printingpress.dev](https://printingpress.dev)
**GitHub (library):** https://github.com/mvanhorn/printing-press-library
**GitHub (CLI):** https://github.com/mvanhorn/cli-printing-press

Printing Press is a CLI factory + pre-built CLI library for AI agents. Created in response to the token inefficiency of APIs and MCP servers in agentic workflows. Inspired by Peter Steinberger (creator of OpenClaw) building his own CLIs because official ones were too verbose.

## Two components

**1. Library** — 50+ pre-built CLIs, ready to install and use:
- ESPN, Flight Goat, Movie Goat, Recipe Goat (starter pack)
- Amazon, Craigslist, eBay, TikTok Shop, Shopify, Airbnb
- Linear, Hacker News, Contact Goat, and more

**2. Factory** — Helps Claude Code build a custom CLI for any tool in ~10 minutes using natural language. Generates Go-based CLIs with SQLite local mirrors.

## How it works

1. Install Printing Press (requires [Go](https://go.dev))
2. Claude Code uses `pp` commands to interact with tools
3. CLI output is pre-formatted and token-minimal (~200 tokens vs raw JSON)
4. CLIs can be packaged into skills and chained together

## Key features

- **SQLite backend** — local mirror means no round trips and no rate limits
- **Agent-native output** — clean text, not raw JSON
- **Chrome session support** — works on sites with anti-scraping (e.g., All Recipes)
- **Team sharing** — push to private GitHub repo, team clones and swaps API keys
- **Skill wrapping** — natural language invocation via Claude Code skills

## Performance

- 35× fewer tokens than equivalent MCP on the same task
- 100% reliability vs 72% for MCP on complex tasks
- Example: 132,000 token API response → ~2,000 tokens in Claude's context

## Requirements

- [Go](https://go.dev) (free, open-source, by Google)
- Claude Code (primary integration target)

## Related pages

- [[cli-for-agents]] — concept: why CLIs beat APIs and MCPs for agents
- [[claude-code]] — primary tool this integrates with
- [[printing-press-cli-source]] — source transcript (Nate Herk, 2026-05-08)
