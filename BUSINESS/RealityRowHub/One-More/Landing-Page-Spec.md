---
title: "One More" Landing Page — Test Build Spec
date: 2026-07-07
status: draft
owner: Strategist (creative handoff → Director)
---

# "ONE MORE" — Tiny Test Page

## Purpose
Validate visual direction and "food as destination" concept before investing in full site. Single-screen landing page linked from Instagram bio once posting begins.

## Scope
- **One viewport, no scroll** (or one scroll section max)
- No booking, no menu, no about-us — proof of concept only
- Fast turnaround: 2–3 hours build

---

## Anatomy

| Section | Content | Priority |
|---------|---------|----------|
| Wordmark | "ONE MORE" logotype (simple serif or custom) | **Must have** |
| Tagline | One line capturing the concept — e.g., _"Stay for the meal."_ | **Must have** |
| Hero visual | Food photo or short loop video of a dish we already filmed (3 dishes on hand) | **Must have** |
| Instagram CTA | "@onemore — coming soon" with handle link | Must have |
| Location tease | "Sunshine Coast, BC" (low-key, bottom) | Nice to have |

## Design Tokens

- **Palette:** Earthy neutrals (warm stone / sage green accent), let food photography carry saturation
- **Typography:** Serif for wordmark (editorial feel), sans-serif body (clean, functional)
- **Mood:** Rustic minimal — not rustic-craft. Think A24 meets a Japanese inn.
- **Aspect:** Mobile-first (Instagram traffic is 90% mobile)

## Tech Stack
| Layer | Choice | Rationale |
|-------|--------|-----------|
| Framework | Plain HTML/CSS or Astro SSG | Zero overhead, no CMS to maintain |
| Hosting | GitHub Pages / Netlify free tier | Already on our toolchain, zero cost |
| Domain | Subdomain (e.g., `onemore.rrh.link`) or parking now → proper later | Low commitment |
| Analytics | None yet (add Plausible when launched) | Track after validation |

## Content Checklist Before Build
- [ ] Wordmark direction confirmed (hand-picked font vs. custom logotype vs. text-only)
- [ ] Tagline locked in
- [ ] 1 hero image selected from filmed dishes (Robert provides still)
- [ ] Instagram handle verified + account exists
- [ ] Domain decision: subdomain now, buy later?

## Success Criteria
We know this works when:
1. Arek + Robert look at it and say "this is us"
2. We can link it from Instagram bio within 7 days of first post
3. Load time < 1s on mobile (Lighthouse)

---

## Next Steps
1. **Arek/Robert:** Confirm wordmark direction, tagline, select hero image
2. **Director:** Review spec, hand off to builder or build directly
3. **Test deploy → share link → iterate if needed**
