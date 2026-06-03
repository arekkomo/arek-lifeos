---
title: Reddit — DaVinci Resolve Pro Workflow Tips
category: source
summary: 8 high-impact workflow tips from a 3+ year professional Resolve editor, covering editing speed, organisation, color, and export.
tags: [davinci-resolve, workflow, keyboard-shortcuts, color-grading, proxy-media, smart-bins, export]
sources: 1
updated: 2026-05-30
source_path: raw/From the davinciresolve community on Reddit.md
source_date: 2026-05
authors: [unknown — r/davinciresolve]
ingested: 2026-05-30
---

# Reddit — DaVinci Resolve Pro Workflow Tips

**Source:** r/davinciresolve (shared via Reddit link, content pasted manually by Arek)
**Arek's note:** "I wanna remember and learn those tips"

## TL;DR

A consolidated list of 8 workflow improvements from a working professional editor. Covers keyboard fluency, page strategy, media organisation, performance, color consistency, and export efficiency.

---

## Key Tips

### 1. Keyboard shortcuts
- Print the shortcut sheet and keep it visible for a week
- Critical shortcuts: **J K L** (scrubbing), **I / O** (in/out points), **Alt + , / Alt + .** (nudge frame by frame)

### 2. Cut page for rough assembly
- Cut page is underused — dual-timeline (source + program) is faster for assembly
- **Source Tape mode** shows all clips as one long tape — no more hunting individual clips
- Switch to Edit page only for precision trimming

### 3. Smart Bins for organisation
- Right-click Media Pool → Add Smart Bin → set rules (e.g. clip name contains "B-roll")
- Auto-populates on import; pairs with consistent on-set naming conventions

### 4. Proxy media for 4K+ footage
- Right-click in Media Pool → Generate Proxy Media
- Set to half-res or quarter-res H.264 for smooth scrubbing
- Full-res renders automatically at export — no reconform needed

### 5. Remote Grades for consistent color
- For interview setups (same angle, multiple clips): right-click graded clip → Grab Still → Apply to group
- Or use Remote Versions — change grade once, updates everywhere

### 6. Gallery stills for look reference
- Grab reference stills in Color page Gallery before grading
- Split-screen wipe between reference and current clip: right-click still → View as Wipe

### 7. Background caching
- Playback → Render Cache → Smart
- Red timeline lines turn blue when cached (full frame rate playback)
- Point cache directory to a fast SSD separate from media drive

### 8. Custom export presets
- Save render presets per delivery format: YouTube, Client Review, Master File, etc.
- Never configure export settings from scratch again

---

## Relevance to Arek

Directly applicable to Arek's VFX + filmmaking workflow. All 8 tips are immediately actionable in current Resolve projects. Proxy workflow and Smart Bins are highest-priority if not already in use.

## Related pages

- [[davinci-resolve]]
- [[cinematic-shooting]]
- [[Synthesis/filmmaking-production-overview]]
