---
title: "Astryx — Meta’s Agent-Ready React Design System"
category: source
summary: MIT-licensed Meta React design system with 150+ accessible components, CSS-variable theming, templates, and CLI tooling designed for both developers and coding agents.
tags: [astryx, design-system, react, frontend, ui-components, stylex, coding-agents, meta]
sources: 1
source_path: https://github.com/facebook/astryx
source_date: 2026-07
authors: [Meta]
ingested: 2026-07-19
updated: 2026-07-19
---

# Astryx — Meta’s Agent-Ready React Design System

**Links:** [GitHub](https://github.com/facebook/astryx) · [Docs](https://astryx.atmeta.com) · [Storybook](https://facebook.github.io/astryx/storybook/) · [Sandbox](https://facebook.github.io/astryx/sandbox/) · **License:** MIT · **Status:** Beta

## What it is

Astryx is Meta’s open React design system, developed internally over eight years and reportedly used across 13,000+ apps. It ships accessible components, themes, patterns/templates, and a CLI so developers and coding agents use the same discoverable conventions.

## Practical properties

- 150+ typed React components
- Seven ready themes plus CSS custom-property overrides for branding
- StyleX internally, but consumers can override with Tailwind, CSS modules, or plain CSS
- CLI for component docs, templates, scaffolding, themes, and codemods
- “Swizzle” workflow exports a component’s source for full ownership/customization
- No required build plugin for ordinary consumption

## Install baseline

`@astryxdesign/core` + a theme package; `@astryxdesign/cli` as a dev dependency. The project documents Next.js, Tailwind, Vite, and CDN setups.

## Where it fits

A candidate UI foundation for a future RealityRowHub web surface or internal agent dashboards. It is **not** a visual-design generator; it provides production UI primitives and predictable conventions that make agent-written frontend code easier to review and maintain.

## Related

- [[Agent-Ready-Design-Systems]] — selection/framework pattern
- [[Claude Code]] — Astryx’s CLI and documented conventions give coding agents a stable interface for component discovery/scaffolding
- [[Printing Press]] — analogous principle: developer tools made legible and efficient for agents, but applied to frontend UI components
