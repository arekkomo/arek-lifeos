# Little M — Suno Technical Reference

## Tag Structure for Custom Mode Prompt
```
[Instr: Intro]
[Intro] Instrumental only, no vocals

### Verse Tags
[Verse]
Melodic verses
Short phrasing
Minimal verbs

### Pre-Chorus Tags
[Pre-Chorus]

### Chorus Tags
[Chorus]
Chant rhythm
Repetitive hook structure

### Special Sections
[Fake-out pause]
[Bass drop / Heavy beat drop]
[Outro]

```

**Key rule:** Use bracketed tags for section structure and inline descriptors for style. Suno recognizes:

- `[Verse]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Intro]`, `[Outro]`
- `(spoken)` or `[Spoken word]` for punchline delivery
- Descriptors *inside* tags like `[Verse: melodic, minimal verbs]`
- **Cold instrumental intro** via `[Instrumental Intro]` or `[Intro] Cold instrumental start`

## Character Limits (Custom Mode)
- **Prompt/Style description ~ limit: ~200 characters recommended** for style descriptions
- **Lyrics box:** ~6,000 characters max, but Suno tends to cut off around 3,500-4,000 characters effectively
- Keep prompts concise and impactful.
