---
title: Implement CLI Layer in Arek & Co System
owner: Strategist
status: Backlog
priority: Medium
created: 2026-05-09
updated: 2026-05-09
tags: [cli, claude-code, automation, system, printing-press, ai-agents]
---

# Project: Implement CLI Layer in Arek & Co System

> **Status:** Backlog — not started. Arek flagged interest but not ready to begin.
> **Routed by:** Operator (2026-05-09)
> **Knowledge source:** [[printing-press-cli-source]]

---

## The Idea

Replace or supplement MCP servers in the Arek & Co system with CLIs using [Printing Press](https://printingpress.dev). CLIs are significantly more token-efficient than MCPs (35× fewer tokens, 100% vs 72% reliability on complex tasks) and work on tools that have no public API.

---

## Why This Matters for Arek & Co

The current system uses MCPs (Gmail, Google Calendar, Notion, Google Drive, n8n, Apple Notes, etc.). Each MCP loads its full tool descriptions into context every session — even when not used. As the agent stack grows, this creates compounding token overhead.

Switching key integrations to CLIs would:
- Reduce per-session token cost
- Improve agent reliability on complex tasks
- Enable access to tools with no official MCP or API (e.g., Skool community, YouTube data)

---

## Scope (when ready to start)

### Phase 1 — Foundation
- [ ] Install Go on machine
- [ ] Install Printing Press (starter pack + factory)
- [ ] Test with pre-built CLIs (ESPN, Movie Goat, etc.)
- [ ] Understand how CLIs wrap into skills

### Phase 2 — Replace high-value MCPs with CLIs
- [ ] Audit current MCPs: which are used most? Which have token-heavy responses?
- [ ] Priority candidates: Gmail, Google Calendar, Notion, YouTube Data API
- [ ] Build or find CLIs for each priority tool
- [ ] Test side-by-side: CLI vs MCP reliability + token cost

### Phase 3 — Build custom CLIs for gap tools
- [ ] Identify tools with no MCP or API (e.g., Skool)
- [ ] Use Printing Press factory to build custom CLIs
- [ ] Wrap each in a Claude Code skill for natural language invocation

### Phase 4 — System integration
- [ ] Update AGENTS system instructions to prefer CLI over MCP where available
- [ ] Document the CLI catalog in `AGENTS/System/`
- [ ] Share relevant CLIs with any team collaborators (private GitHub repos)

---

## Dependencies

- Go installed on Arek's machine
- Printing Press factory + library installed
- Time investment: ~2–4 hours for Phase 1–2; ongoing for Phase 3+

---

## Strategic fit

This is a **System** project (read: infrastructure). The payoff is compounding — every agent session gets cheaper and more reliable. Low urgency but high long-term ROI. Schedule when there's a quiet window, not competing with creative or VFX priorities.

**Suggested trigger:** pick this up during a low-energy work block or when MCP token costs become noticeable.

---

## Resources

- [[printing-press]] — entity page
- [[cli-for-agents]] — CLI vs API vs MCP concept
- [printingpress.dev](https://printingpress.dev)
- [GitHub — CLI library](https://github.com/mvanhorn/printing-press-library)
- [GitHub — CLI factory](https://github.com/mvanhorn/cli-printing-press)
- [Source video](https://www.youtube.com/watch?v=YHk45NEpspE) — Nate Herk, 2026-05-08
