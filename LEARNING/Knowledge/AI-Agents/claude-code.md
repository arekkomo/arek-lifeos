---
title: Claude Code
category: entity
summary: Anthropic's agentic CLI for software engineering, featuring skills/plugins, hooks, slash commands, and MCP server integrations.
tags: [claude-code, ai-agents, anthropic, agentic-workflows, automation]
sources: 5
updated: 2026-05-14
---

# Claude Code

Anthropic's official CLI for Claude. Designed for agentic software engineering — reads/writes files, runs commands, integrates with MCP servers, and supports a skills/plugin system.

## Key capabilities

- Skills & plugins (slash commands, reusable workflows)
- Hooks (automated shell commands on events)
- MCP server integrations (Gmail, Notion, n8n, Google Drive, etc.)
- Memory system (project-scoped markdown memory files)

## CLI tooling (preferred over MCP)

CLIs are the most token-efficient interface for Claude Code agents — 35× fewer tokens than equivalent MCP usage. See [[cli-for-agents]] for the full comparison.

[[Printing Press]] is the primary CLI factory: builds custom CLIs for any tool in ~10 minutes, with a library of 50+ pre-built CLIs.

## Website Building Workflow

Claude Code + VS Code is a capable no-code website builder when set up correctly. Key system:
- **CLAUDE.md** — project system prompt: brand rules, screenshot instructions, deploy protocol
- **Frontend design skill** — install globally; auto-invoked for polished, professional output
- **Screenshot loop** — Puppeteer takes screenshots, Claude visually reviews and self-corrects
- **Inspiration cloning** — feed a full-page screenshot + CSS to clone any site's structure
- **21st.dev components** — copy-paste component prompts for individual UI elements
- **Deploy stack** — GitHub → Vercel autodeploy; localhost preview before any push

See [[claude-code-website-building-source]] for full workflow notes.

## Cloudbot / Autonomous Assistant Pattern

Claude Code can be run as an always-on executive assistant ("Cloudbot") on a dedicated Mac Mini or VPS. Core setup: identity files (soul.md + user.md), heartbeat cron, Kanban dashboard, dedicated AI accounts. Enables overnight autonomous task execution and proactive deliverables. See [[autonomous-ai-assistant]] and [[clawdbot-assistant-source]].

## Skill Self-Improvement (Karpathy Loop)

Skills can self-improve overnight using binary eval assertions. Create an `evals/eval.json` in the skill folder with 25 true/false checks; prompt Claude to run the loop until perfect score. See [[skill-self-improvement-loop]] and [[self-improving-skills-source]].

## Skill Patterns

Claude Code skills cluster into four functional categories. See [[claude-code-skill-patterns]] for full taxonomy, install status, and priority recommendations for Arek & Co.

Key categories:
- **Session Management** — calibrate, coordinate, onboard, claude-mem
- **Quality Control** — superpowers, GSD, /review, /ultra-review, devil, align
- **Context Engineering** — context-mode, GSD (prevents context rot)
- **Output Exploration** — burst, tweak, skill-creator (✅ installed)

> ⚠️ **Arek's Note (2026-05-14):** Wants these skills reviewed against current setup and useful ones implemented. See [[claude-code-skills-daily-7-source]] and [[claude-code-skills-best-6-source]] for full details. Flagged for live session.

## Related pages

- [[cli-for-agents]] — CLI vs API vs MCP for agents
- [[printing-press]] — CLI factory and library
- [[claude-code-website-building-source]] — website building workflow (5 hacks)
- [[claude-in-chrome]] — browser companion for Cowork sessions
- [[autonomous-ai-assistant]] — Cloudbot pattern
- [[skill-self-improvement-loop]] — Karpathy eval loop for skills
- [[clawdbot-assistant-source]] — Klaus build walkthrough
- [[self-improving-skills-source]] — self-improving skills tutorial
- [[claude-code-skill-patterns]] — skill taxonomy, install status, priority for Arek & Co.
- [[claude-code-skills-daily-7-source]] — 7 daily skills (calibrate, coordinate, align, devil, burst, tweak)
- [[claude-code-skills-best-6-source]] — 6 best skills (superpowers, GSD, context-mode, claude-mem)
- `synthesis/ai-agents-automation-overview.md`
