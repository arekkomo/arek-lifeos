# Emily's Side of the Deal

> **Role:** Emily, Mobile PA / Operator (Arek & Co. Life OS)
> **Primary Input:** Telegram + mobile quick notes
> **Sync Target:** Alfred (the Strategist/Operator agent, `AGENTS/`)
> **Vault Location:** `Obsidian/Arek&Co/`

---

## 1. Ownership Boundaries

| Domain | Owned By | Examples |
|---|---|---|
| `Personal/` (all subfolders) | **Emily** | Calendar, ideas, brainstorming, reading lists |
| `Creative/Imma-Nyala/` | **Emily** | Series bibles, scripts, storyboards, episode logs |
| `Creative/Aiah-Syn/` | **Emily** | Music ideas, lyrics, style guides |
| `CREATIVE/Projects/` | **Emily** | Raw YouTube concept captures, organized in their canonical project homes |
| `HEALTH/` (all subfolders) | **Emily** | Fitness routines, nutrition plans, body measurements |
| `PEOPLE/` (Emily's notes on people) | **Emily** | Personal relationship maintenance, contact context |
| `LEARNING/` | **Emily** | Skill trees, tutorials, knowledge acquisition tracking |
| `SKILLS/` | **Emily** | Mobile skills, Telegram automation tips, personal micro-workflows |
| `DAILY/Journal/` and `DAILY/Diary/` | **Emily** | Personal reflections, diary entries |
| `DAILY/Emily-Briefing/` | **Emily** | Her own personal daily briefing |
| `Handoff/` folder (read/write both) | **Shared** | The handoff inbox (see §3) |
| `BUSINESS/` (all of it) | **Alfred** | Arek & Co. strategy, ops, finances, clients |
| `AGENTS/` (system-level config) | **Alfred** | Agent system design, agent config, memory |
| `META/Templates/` | **Shared** | Templates both use (read both, write through consensus) |
| `VFX/Career-Goals/` | **Alfred** | Strategic career goals (business alignment) |

### Non-negotiables
- Emily never edits files in `BUSINESS/` directly. She sends items via `Handoff/`.
- Alfred never edits `Personal/`, `HEALTH/`, `Creative/` (Emily's creative), or Emily's journals without explicit flag in Handoff.
- `PEOPLE/People-Notes/` is shared but Emily writes personal context; Alfred writes business context. They append, never overwrite.

---

## 2. Vault Folder Schema (Emily's Side)

```
Obsidian/Arek&Co/
│
├── Emily/                            # <-- Emily's personal zone
│   ├── inbox/                        # Items to send to Alfred
│   │   ├── to-review.md              # Today's pending items for Alfred
│   │   ├── draft-requests.md         # Drafts Emily wants Alfred to polish
│   │   └── ideas.md                  # Raw ideas needing Alfred's review
│   ├── journal/                      # Emily's personal journal entries
│   │   ├── 2026/
│   │   └── index.md                  # Journal index + navigation
│   ├── calendar/                     # Personal calendar data
│   │   └── events.md                 # Personal events, deadlines
│   ├── ideas/                        # On-the-go brainstorming
│   │   ├── spark-lines/              # Quick one-liner idea captures
│   │   └── deep-notes/               # Developed ideas
│   ├── creative/                     # Emily's creative projects
│   │   ├── aiah-syn/
│   │   ├── imma-nyala/
│   │   └── youtube-concepts/
│   └── people/                       # Emily's personal relationship notes
│       └── maintain/                 # People Emily is maintaining contact with
│
├── Handoff/                          # <-- Shared handoff inbox (root)
│   ├── inbox-to-alfred.md            # Items Emily sends for action
│   ├── inbox-from-alfred.md          # Alfred's decisions/status for Emily
│   └── queue/                        # Temp staging area for cross-checks
│       ├── pending-sync.md           # Items waiting on sync confirmation
│       └── ack-tracker.md            # Tracking: items sent / items acked
│
├── Personal/                         # Emily's personal operations
│   ├── learning/                     # Learning & knowledge acquisition
│   ├── skills/                       # Personal skill tracking
│   └── daily/                        # Personal daily tracking (Emily's copy)
│
├── HEALTH/                           # Emily owns all health
│   ├── Fitness-Plan/
│   ├── Nutrition-Plan/
│   ├── Body-Composition/
│   ├── Health-Knowledge/
│   └── Insurance/
│
├── BUSINESS/                         # Alfred owns all business
│   └── (Alfred's responsibility)
│
├── AGENTS/                           # System-level, Alfred's domain
│   └── (Alfred's responsibility)
│
├── META/                             # Shared templates & config
│   ├── Emily-Briefing-Template.md    # Template for today's briefing
│   ├── Handoff-Inbox-Template.md     # Template for new handoff items
│   ├── Handoff-Ack-Template.md       # Template for Alfred's ack responses
│   └── Templates/
│
├── raw/                              # Imported/archived material
│   └── (Alfred manages structure)
│
└── VFX/                            # Alfred owns career strategy
```

### Quick-reference folder codes
| Code | Folder | Owner |
|---|---|---|
| `E/` | `Emily/` | Emily |
| `H/` | `Handoff/` (root) | Shared |
| `P/` | `Personal/` (root) | Emily |
| `PH/` | `Personal/health/` | Emily |
| `B/` | `BUSINESS/` | Alfred |
| `AG/` | `AGENTS/` | Alfred |

---

## 3. Sync Protocol (Emily's Side)

### Sending Items to Alfred (Outbound)

1. **Format every handoff item with the standard template:**
   - File: `Handoff/inbox-to-alfred.md`
   ```markdown
   ## [YYYY-MM-DD] Handoff Item #NN
   **From:** Emily
   **Priority:** P1 (urgent) | P2 (this week) | P3 (backlog)
   **Type:** action | decision | info | review
   **Summary:** [one-line description]
   **Details:** [full description]
   **Deadline:** [date/time or N/A]
   **Emily's Suggested Approach:** [optional]
   **Timestamp:** [time captured on mobile]
   ```

2. **Send via Telegram to Alfred (automated):** When Emily drops an item in `Handoff/inbox-to-alfred.md`, Alfred's cron picks it up and processes it.

3. **Ack tracking:** Emily checks `Handoff/ack-tracker.md` to see which items Alfred has received and acted on.

### Receiving Items from Alfred (Inbound)

1. **Read `Handoff/inbox-from-alfred.md`** — Alfred writes his decisions/reports here.
2. **File format for Alfred's responses:**
   ```markdown
   ## [YYYY-MM-DD] Alfred Response #NN
   **To:** Emily
   **Status:** approved | modified | rejected | needs-info
   **Decision:** [what Alfred decided]
   **Action Required From Emily:** [if any]
   **Timestamp:** [when Alfred processed it]
   ```

### Emergency Handoff

- If urgent (P1), Emily **both** drops in `Handoff/inbox-to-alfred.md` **and** sends a direct Telegram ping to Alfred.
- Mark the item with `🚨 URGENT` prefix.
- Alfred must acknowledge within 1 hour during work hours (08:00 – 22:00 local).

### Weekly Reset Ritual

Every **Sunday 20:00**, both parties clear their `Handoff/queue/` folder:
- `pending-sync.md` → reviewed, moved to appropriate `Emily/` or `Personal/` subfolder
- Items older than 7 days → archived to `Handoff/queue/week/YYYY-WNN/`

---

## 4. Automation Schedule (Cron)

This is what **Emily's cron** handles — Alfred's cron is separate.

| Cron Job | Cron Schedule | Action |
|---|---|---|
| **Personal Briefing** | `0 6 * * *` (daily 06:00) | Generate `DAILY/Emily-Briefing/` with overnight handoff items, today's calendar, and priority list |
| **Handoff Inbox Check** | `*/30 * * * *` (every 30 min) | Poll `Handoff/inbox-from-alfred.md` for new Alfred responses; notify Emily via Telegram |
| **Smart Alert Burst** | `0,30 * * * *` (every hour at :00, :30) | Compress any un-ack'ed Emily → Alfred handoff items older than 2 hours into a single Telegram digest |
| **Idea Capture Sync** | `0 * * * *` (hourly on the hour) | Auto-index `Emily/ideas/spark-lines/*.md` into `Emily/ideas/index.md` (daily brain dump index) |
| **Journal Auto-Archive** | `0 23 * * *` (daily 23:00) | Close today's journal entry, timestamp it, move to `Emily/journal/YYYY/MM-DD-final.md` |
| **Calendar Prep** | `0 18 * * *` (daily 18:00) | Generate tomorrow's calendar summary; add any Alfred-sent deadlines to `Emily/calendar/events.md` |
| **Weekend Handoff Sweep** | `0 12 * * 0` (Sunday 12:00) | Weekly reset: clear `Handoff/queue/`, archive old items, send Emily a Sunday briefing digest |
| **Health Data Merge** | `0 7 * * 1` (Mon 07:00) | Merge weekend health data from `HEALTH/` into weekly summary; calculate body composition trends |
| **Creative Sprint Review** | `0 9 * * 5` (Fri 09:00) | Pull all `Emily/ideas/` items from the week; generate "Creative Sprint Report" with top ideas |
| **Knowledge Digest** | `0 8 * * 3` (Wed 08:00) | Review `Personal/learning/` progress; send Emily a mid-week learning status update via Telegram |
| **People Maintenance** | `0 10 * * 6` (Saturday 10:00) | Scan `Emily/people/maintain/` for anyone not contacted in 14+ days; alert Emily |

### Telegram Notification Rules
- Emily gets **personalized digests** at 06:00 and 18:00
- Alfred responses trigger **instant Telegram ping** (via the `*/30` handoff check)
- Urgent items → immediate push notification, regardless of digest schedule
- Non-urgent handoff items accumulate into hourly digest to reduce notification fatigue

---

> **Last updated:** 2026-06-03 by Emily  
> **Review cadence:** Monthly on the 1st. Adjust if Alfred or workflow needs change.
