---
title: Automated Instagram Carousel Creation Pipeline
category: project
summary: Implement automated carousel creation pipeline using Claude Code + DESIGN.md design system to generate on-brand IG posts with consistent visual identity for Reality Rove social media. Replaces manual Canva/Photoshop workflow.
tags: [instagram, carousels, content-pipeline, claude-code, higgsfield-mcp, social-media, design-system]
updated: 2026-06-30
status: Queued
priority: P2 (Strategist-owned)
owner: Strategist + Emily for implementation
---

# Instagram Carousel Automation Pipeline

> **Goal:** Build an automated pipeline that generates fully custom, on-brand carousel posts in minutes instead of hours. Replaces manual Canva/Photoshop work for Reality Rove social content.

## Source Material

**Video 1:** "How I Use Claude Code to Make INSANE Instagram Carousels" — jFAH0txMwiI
**Key concepts:** DESIGN.md spec, Higgsfield MCP integration, Aurora carousel skill template
**Video duration:** ~11 min tutorial

---

## Core Architecture (from video)

### Components

| Component | Role | Status | Our Setup |
|---|---|---|---|
| **DESIGN.md** | Google's design token spec: colors, typography, spacing, component styles as code | ❌ Not created | Need our brand tokens |
| **Claude Code CLI** | Agent that reads design system + prompt, generates carousel HTML/CSS | ✅ Available | Already installed on Spark |
| **Higgsfield MCP** | Visual generation server via Model Context Protocol | ❌ Not connected | Need to set up |
| **Aurora Skill** | Reusable Claude Code skill for consistent carousel generation | ❌ Not built | Template exists in video |
| **Blotato API** | Instagram scheduling & posting automation | ❌ Not integrated | New dependency |

### Pipeline Flow

```
Pinterest/Reference Images → DESIGN.md system spec → Claude Code generates HTML/CSS carousels → Higgsfield renders visual variants → Export as PNG/JPEG → Schedule via Blotato → Post to IG ✅
```

---

## Implementation Roadmap

### Phase 1: Design System Foundation (Week 1-2)
- [ ] Extract Reality Rove brand colors, typography preferences, visual style tokens
- [ ] Create DESIGN.md following Google's token spec format
- [ ] Test design system with Claude Code on Spark (`hermes -p default code ...`)
- [ ] Validate visual output matches desired aesthetic before piping into schedule

### Phase 2: Agent Skill & Automation (Week 3)
- [ ] Build reusable "carousel creator" skill in Hermes/Higgsfield MCP
- [ ] Template the Aurora carousel style with our tokens
- [ ] Test 5-10 sample carousels on Rove VFX content topics
- [ ] Iterate until quality matches Strategist's current manual output

### Phase 3: Content Scheduling (Week 4)
- [ ] Connect Blotato API for automated Instagram scheduling
- [ ] Configure posting cadence strategy (e.g., 3 posts/week minimum)
- [ ] Test full pipeline end-to-end with actual social account
- [ ] Monitor engagement metrics, adjust content strategy monthly

### Phase 4: Scale & Iterate (Week 5+)
- [ ] Expand to TikTok/YouTube Shorts carousel variants
- [ ] Add A/B testing for different design system iterations
- [ ] Build analytics dashboard to track which carousel styles drive most saves/shares
- [ ] Connect to Strategist's engagement tracking workflow

---

## Why This Matters

**Current state:** Manual carousel creation via Canva/Photoshop = ~2-3 hours per batch of 5 posts
**Target state:** Prompt → 10 min → 5 fully on-brand carousels ready for scheduling

**Strategic value:**
- Frees up Strategist for higher-leverage engagement planning
- Ensures consistent visual brand across ALL social content
- Enables rapid testing of new carousel formats/styles without design bottleneck
- Scales content output 3-4x while improving quality bar
- Directly increases Rove's discoverability via saves/shares algorithm boost

---

## Dependencies & Blockers

| Dependency | Status | Notes |
|---|---|---|
| **Brand identity docs** | 🟡 Need extraction | Current RR branding assets to feed into design system |
| **Higgsfield MCP access** | 🔴 Not installed | Requires API key/account creation, install on Spark |
| **Blotato account** | 🔴 Not connected | Scheduling API integration needed |

---

## Budget Estimate

| Line Item | Monthly Cost | Notes |
|---|---|---|
| Claude Code API (usage-based) | ~$20-40 | Depends on carousel volume, 50 posts/month |
| Higgsfield MCP render calls | TBD | Pricing unclear until access granted |
| Blotato subscription | $9-19/mo | Instagram scheduling platform |
| Agent compute overhead | Minimal | Spark DGX handles background runs efficiently |

**Total estimate:** ~$40-80/month for automated pipeline vs. 5-7 hours of manual work per week

---

## Related Projects

- Strategist's engagement tracking workflow at `HEALTH/Engagement-metrics.md` (placeholder)
- Reality Rove social account credentials in system secrets
- [Connect with Emily to set up Higgsfield MCP on Spark]

---

*Created: 2026-06-30 | Next review: Weekly with Strategist*
