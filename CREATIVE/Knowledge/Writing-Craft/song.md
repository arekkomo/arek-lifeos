---
title: Song
category: creative-writing-craft
file_suffix: _song
rrhub_type: song
updated: 2026-08-18
---

# Song

## Definition
One canonical file containing final lyrics and its music-generation direction, separated by the exact `=== SUNO STYLE ===` delimiter.

## Pipeline job
The songwriting authority for generation, review, and downstream picture/edit decisions.

## Metadata
Use the shared project frontmatter: `type`, `title`, `project`, `stage`, `version`, and `updated`. Add `source:` when the document is directly paired to a script; keep the canonical file inside its project folder.

## Required sections
- Lyrics with structural performance tags
- Exact `=== SUNO STYLE ===` delimiter
- Style direction: genre, emotional arc, instruments, vocal persona, production, exclusions
- Creative intent and project identity constraints
- Decision-level change log

## House writing rules
- Keep all singable words above the delimiter and all style direction below it.
- Write lyrics for prosody, image, and emotional turn.
- Describe sonic movement as an arc, not tag laundry.
- Use descriptive qualities rather than artist imitation.
- Apply Aiah Syn constraints only to Aiah Syn work.

## Quality gate
- [ ] One current lyric and one current style block.
- [ ] Delimiter is exact.
- [ ] Each section has a dramatic or emotional function.
- [ ] Style names vocal persona, arrangement, texture, and dynamics.

## Starter template
```markdown
## Lyrics
[Verse 1]
...

=== SUNO STYLE ===
[Genre: ...]
[Vocals: ...]
[Instrumentation: ...]
[Mood: ...]
[Production: ...]

## Creative intent
...
```

## Sources
- Suno Help Centre — https://help.suno.com/
- Sheila Davis, The Craft of Lyric Writing — https://openlibrary.org/search?q=The+Craft+of+Lyric+Writing+Sheila+Davis
