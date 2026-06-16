---
title: Skill Systems Pattern
category: concept
summary: Architectural pattern where skills are modular components that reference shared context files rather than baking in context — enabling one-update propagation across all skill systems.
tags: [claude-code, skills, architecture, context-management, arek-and-co]
sources: 2
updated: 2026-05-28
---

# Skill Systems Pattern

## Core Idea

A skill should not be a self-contained task that bundles context (voice, ICP, formatting) internally. Instead:

- **Shared context lives in reference files** — one file per concern (voice, audience, formatting rules)
- **Skills chain reference files** — they pull from shared files at runtime
- **Updates propagate automatically** — change the voice file → every skill that references it gets the update

## Anti-pattern (baked-in context)

```
write-linkedin-post.md
  ├── voice: "professional, direct, no fluff..."   ← duplicated
  ├── ICP: "solo operators, 30–50..."               ← duplicated
  └── format: "hook, 3 bullets, CTA"               ← duplicated

write-email-campaign.md
  ├── voice: "professional, direct, no fluff..."   ← same thing, again
  └── ...
```

Problem: brand voice shifts → 15 places to update. Easy to miss one. Outputs diverge.

## Correct pattern (reference files)

```
ABOUT-YOU/
  ├── About-Me-Creative.md       ← single voice source
  └── About-Me-General.md        ← single persona source

skills/
  ├── write-linkedin-post.md     → references About-Me-Creative.md
  └── write-email-campaign.md    → references About-Me-Creative.md
```

Brand voice shifts → one edit → both skills updated automatically.

## Arek & Co Implementation

The shared context files already exist:

| Context type | File |
|---|---|
| Voice / creative identity | `ABOUT-YOU/About-Me-Creative.md` |
| General persona / goals | `ABOUT-YOU/About-Me-General.md` |
| Finance context | `ABOUT-YOU/About-Me-Finance.md` |
| Health context | `ABOUT-YOU/About-Me-Health.md` |

**Check needed:** verify `creative-film-pipeline` and `creative-song-pipeline` skill files reference `About-Me-Creative.md` rather than duplicating voice/style instructions inline.

## Hermes Failure Mode

Hermes's auto-skill-creation generates new skills per task. Over time → V1, V2, "for this client", "for that client" — 15 near-identical skills with similar descriptions. Claude doesn't know which to use. Maintenance becomes impossible. The skill systems pattern prevents this.

## Related

- [[hermes-openclaw-agentic-os-source]] — source
- [[claude-code-skill-patterns]] — existing skill pattern notes
- [[self-improving-skills-source]] — Karpathy loop for skill quality
