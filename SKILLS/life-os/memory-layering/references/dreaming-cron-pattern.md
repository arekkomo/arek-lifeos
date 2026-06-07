# "Dreaming" Cron Pattern for Memory Hygiene

> **Purpose:** Automated nightly process that prevents "context rot" by promoting recurring themes from daily notes into long-term memory and archiving stale content.
> **Trigger:** Cron job, runs nightly (~02:00 UTC)

## Process

1. **Scan** `DAILY/` entries for the past 7–14 days (or since last run).
2. **Score** topics by:
   - Frequency (how many mentions across entries)
   - Significance (mentioned by Arek directly vs. incidental)
   - Recency (within last 3 days gets higher weight)
3. **Promote** recurring/pattern themes:
   - `ABOUT-YOU/*` → Personal facts/preferences discovered through repetition
   - `LEARNING/Synthesis/*` → Cross-domain patterns
   - `LEARNING/index.md` → New cross-references
4. **Archive** daily entries to `raw/archive/` (preserved as audit trail, not deleted).
5. **Report** changes in `shared_sync.md`.

## Implementation

Run via cronjob with agent or as a script. The agent reads DAILY/ entries, scores themes, and writes promoted content with proper frontmatter.

```
cronjob(action="create", 
    name="daily-memory-dreaming",
    schedule="0 2 * * *",
    prompt="Scan DAILY/ entries from last 7 days. Score topics by frequency/significance. Promote recurring themes to ABOUT-YOU/ or LEARNING/Synthesis/. Archive entries to raw/archive/. Report changes.",
    deliver="origin"
)
```

## Pitfalls

- Don't promote one-off mentions — only recurring patterns.
- Don't create knowledge pages from daily entries that are just casual notes.
- Keep archived originals forever — they're audit trail, not noise.
- Always update INDEX.md when promoting cross-domain content.