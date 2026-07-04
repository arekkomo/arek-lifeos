---
title: "Creative Project Operating Rules"
category: note
summary: Master rules for creating, naming, storing, and syncing all creative projects. Prevents orphan folders like LITTLE-M from ever happening again.
tags: [operating-rules, creative-library, project-management]
updated: 2026-07-03
---

# Creative Project Operating Rules

> **Purpose:** One canonical system for all creative work. No more orphaned folders on the root level. Everything has a home, and that home is inside the Arek&Co Obsidian vault under `CREATIVE/`.

---

## 1. Naming Convention

All projects use **Title-Case with hyphens** (kebab-case):

```
✓ Little-M     ✓ New-York-Film
✓ Imma-Nyala   ✓ Sycophantic-AI
✗ little-m     ✗ LittleM       ✗ imma_nyala
```

Apply to ALL project folder names, file names, and Notion page titles.

---

## 2. Project Bootstrap (Automatic)

When Arek states a new creative project exists or wants to start one:

1. **Determine domain:** Song / Music Video / Film / Aiah Syn / YouTube Concept
2. **Create the folder structure** (see §3 below)
3. **Create `Project-Brief.md`** inside it with:
   - YAML frontmatter (`title`, `summary`, `stage`, `domain`, `created`)
   - One-line concept
   - Core philosophy / emotional intent
   - Status line
4. **Update Project-Catalog.md** — add a row to the appropriate section (Active / Idle)
5. **Do NOT sync to Notion yet** — wait for Production stage (§7)

---

## 3. Domain-Specific Folder Structures

### Song Projects (`CREATIVE/Song-Projects/<Project-Title>/`)

```
Song-Projects/Little-M/
├── Project-Brief.md           ← concept, style guide, punchline rules (REQUIRED)
├── LYRICS-DRAFT/              ← all lyric iterations
│   └── lyrics-final.md        ← latest version (always update in place)
├── SUNO-PROMPTS/             ← Suno custom-mode prompts + research/docs
├── CONCEPTS/                  ← hook ideas, structure experiments
└── REFERENCES/                ← tonal references visual/audio
```

**Rules:**
- Only ONE `lyrics-final.md` per project — overwrite as draft evolves
- Every song concept also gets logged to `CREATIVE/Library/<category>/` (§8)
- Suno research (tag structures, limits, analysis docs) stays in SUNO-PROMPTS/

### Music Video Projects (`CREATIVE/Music-Video-Projects/<Project-Title>/`)

```
Music-Video-Projects/Little-M/
├── Project-Brief.md           ← visual concept, style references
├── STORYBOARD/                ← shot-by-shot descriptions
├── SHOT-LIST/                 ← breakdown for production
└── ASSETS/                    ← generated images/prompts per shot
```

**Note:** Film and Music Video projects may be separate folders (e.g. Little-M has both) OR combined into one if MV is exclusively for that song. Decision stays with Arek at creation time.

### Aiah Syn Projects (`CREATIVE/Aiah-Syn-Projects/<Project-Title>/`)

```
Aiah-Syn-Projects/Summer-State/
├── Project-Brief.md
├── LYRICS-DRAFT/
├── SUNO-PROMPTS/
└── REFERENCES/
```

Same structure as Song Projects but under Aiah-Syn domain. Always check `Aiah-Syn-Style.md` for persona/aesthetic alignment before creating concept content.

### Film Projects (`CREATIVE/Film-Projects/<Project-Title>/`)

```
Film-Projects/New-York-Film/
├── Project-Brief.md           ← logline, treatment, characters
├── SCRIPTS/                   ← all script versions
├── SHOT-LIST/                 ← per-scene shot breakdowns
├── STORYBOARD/                ← visual storyboards
└── REFERENCES/                ← tonal/composition refs
```

### YouTube Concepts (`CREATIVE/YouTube-Concepts/<Concept-Title>/`)

```
YouTube-Concepts/Sycophantic-AI/
├── Project-Brief.md           ← hook, outline, target format
└── SCRIPTS/                   ← full script if written
```

---

## 4. CREATIVE Library (Cross-Project Searchable Archive)

The `CREATIVE/Library/` folder is a **living searchable archive** — NOT project storage. Everything that has reusability value gets logged here alongside its project home.

### Categories (5):

| Category | What goes here |
|----------|---------------|
| Beats-and-Blocking | Physical actions, choreography, staging moments |
| Dialogue-Drips | Standalone lines, dialogue cadences, spoken patterns |
| Voice-Directing | Vocal tone notes, narration concepts, performance directions |
| Visual-Inspiration | Camera/framing/composition/color references |
| Tone-and-Reference | Mood comparisons, genre blends, tonal targets |

### How to log to Library (always):

1. **Where:** `CREATIVE/Library/<Category>/<slugified-name>.md`
2. **Frontmatter:** `title`, `category`, `summary`, `tags: [...]`, `source_project`, `created`
3. **Body:** 4-8 line entry covering — what it is, why it works, how to use
4. **Index.md** — append under correct category heading

### What gets logged from Songs (mandatory):

- ☑ Every song concept/hook at creation time → **Tone-and-Reference**
- ☑ Lyric snippets with emotional/thematic resonance → **Dialogue-Drips** or **Beats-and-Blocking**
- ☑ Suno-style breakthroughs / sonic concepts → **Voice-Directing**
- ☑ Visual references for associated MV → **Visual-Inspiration**

### What gets logged from Film/YouTube:

- ☑ Scene beats with reusable blocking → **Beat-and-Blocking**
- ☑ Standalone dialogue that could recur in future work → **Dialogue-Drips**
- ☑ Tonal references found during research → **Tone-and-Reference** or **Visual-Inspiration**

---

## 5. Project-Catalog.md — Single Source of Truth

Located at: `CREATIVE/Project-Catalog.md`

### Active projects section rules:
- Ordered by **last worked date** (most recent first)
- One row per project with: name, domain, status, location path, last active date
- When project is killed/paused: move to appropriate section, update status line
- When an idle folder has content added: promote from Idle → Active

### What belongs in the catalog vs. not:
- **In:** All creative/artistic projects regardless of size (even one-song experiments)
- **Out:** Engineering/system projects (REserved for the footer section only)
- **Out:** Raw Notion database entries — those live in Notion, the Catalog is the local mirror

---

## 6. Status Taxonomy (Standardized)

| Status | Meaning | Action |
|--------|---------|--------|
| **Active** | Being worked on now | Track last active date; ping if idle >2 months |
| **Development** | Scripted/structured, not yet production-ready | Normal active work |
| **Production** | Ready for AI tool generation (Suno, Kling, Runway etc.) | → TRIGGER NOTION SYNC |
| **Post Prod** | Generated, being edited/assembled | Normal active work |
| **Review** | Delivered, awaiting feedback/approval | Waiting on external input |
| **Done** | Complete and released/delivered | Archive in 30 days if no updates |
| **Paused** | Intentionally on hold, reason noted | Ping Arek every 3 months |
| **Archived** | Killed or dead. Reason noted in notes | Move to bottom, review annually |

### Status transitions:
- Idea/Development → Active (creator decides)
- Active → Production (**requires explicit "move to production" from Arek**)
- Production → Done (after generation/completion confirmed)
- Active/Paused → Archived (with documented reason)

---

## 7. Notion Sync Trigger (dtb Writing database)

### When to sync:
- **Only when a project moves to Production stage**
- At bootstrap (Idea/Development): NOTION SYNC → NO → local vault only
- This prevents spamming the database with incomplete/unverified entries

### What gets synced:
- Project-Brief.md content (title, summary, stage, tags)
- Updated when production is started
- Updated again when status changes to Done

### Process:
1. Create/confirm Notion page via dtb Writing MCP or API call
2. Sync folder path → database entry link
3. Set Database properties (Stage, Type, Platform if set)
4. Log sync event in Project-Catalog.md footer

---

## 8. Forbidden Actions (Never Do These)

- ❌ Create project folders on the root level (`/home/realityrove/SOMETHING`)
- ❌ Store creative content in `Downloads/` or Desktop
- ❌ Use Notion as primary storage (Obsidian vault is truth; Notion is mirror)
- ❌ Log only to project folder AND forget to log to Library (always do both for reusable items)
- ❌ Create duplicate song titles — check catalog before naming
- ❌ Leave empty folders indefinitely — if nothing created after 30 days, ask Arek if it's dead

---

## 9. Project Lifecycle Summary

```
Arek announces idea
    ↓
Director checks Project-Catalog for title conflict + Library for existing related entries
    ↓
Create domain-specific folder structure (§3)
Create Project-Brief.md (§2)
Log concept to Library (if reusability exists) (§8)
Update Project-Catalog.md — Active section
    ↓  [work happens here—no Notion]
Arek says "move to production"
    ↓
NOTION SYNC (dtb Writing database)
Status → Production in Catalog + Notion
    ↓
Suno generation / AI video production
    ↓
Done / Archived
```

---

*These rules are mandatory for all future creative work. Violating them creates orphans like LITTLE-M which then require manual cleanup. When in doubt, check this file first.*
