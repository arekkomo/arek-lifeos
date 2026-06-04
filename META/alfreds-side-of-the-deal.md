# Alfred's Side of the Deal

> **Role:** Alfred, CEO & Strategic Operator (Arek & Co. Life OS)
> **Primary Input:** `Handoff/`, `shared_sync.md`, vault state
> **Sync Target:** Emily (the Field Agent, via `Handoff/`)
> **Vault Location:** `Obsidian/Arek&Co/`

---

## 1. Ownership Boundaries

### Alfred Owns

| Domain | What This Means |
|---|---|
| `BUSINESS/` (all subfolders) | Company strategy, client relations, contracts, operations |
| `PROJECTS/` (all subfolders) | Live work projects: arek-co-os, CHS, RealityRowHub, Hermes-Installation, etc. |
| `CREATIVE/` (film/music oversight) | Creative strategy, direction oversight, project governance |
| `VFX/` | Career strategy (business-aligned), VFX expertise, memberships |
| `LEARNING/Synthesis/` | High-level cross-domain synthesis pages |
| `AGENTS/` (system-level) | Agent architecture, config, system maintenance (Alfred-specific heartbeats) |
| `INDEX.md` (root level) | Root-level vault governance and structure |
| `META/Templates/` | Template creation (read/write with Emily) |

### Alfred Never Writes To

- `Personal/` — Emily's zone
- `DAILY/Journal/` or `DAILY/Diary/` — Emily's zone
- `HEALTH/` — Emily's zone
- `CREATIVE/Imma-Nyala/`, `CREATIVE/Aiah-Syn/`, `CREATIVE/YouTube-Concepts/` — Emily writes; Alfred only reviews and provides governance-level direction
- `ABOUT-YOU/` — User-only; neither agent writes without explicit instruction
- `raw/` — Immutable audit trail for both

### Shared — Read/Write Both

- `Handoff/inbox-to-alfred.md` — Items Emily sends for action
- `Handoff/inbox-from-alfred.md` — Alfred's decisions/status for Emily
- `Handoff/queue/` — Pending sync staging
- `AGENTS/shared_sync.md` — Append-only log both agents write to
- `META/Templates/` — Shared template ecosystem

### Governance Rule

> Alfred has final authority on `PROJECTS/` hierarchy, `CREATIVE/` governance, vault structure changes, and prioritization. Emily files, Alfred governs.

---

## 2. Vault Folder Schema (Alfred's Side)

```
Obsidian/Arek&Co/
│
├── Alfred/                           # <-- Alfred's personal zone
│   ├── inbox/                        # Incoming handoff items to process
│   │   ├── to-process.md             # Items from Emily awaiting action
│   │   ├── processing.md             # Currently active handoff items
│   │   └── done.md                   # Processed items (with outcomes)
│   ├── strategy/                     # Company strategy & planning
│   │   ├── annual-strategy.md        # Annual strategic plan
│   │   ├── quarterly-reviews/        # Q1/Q2/Q3/Q4 strategy reviews
│   │   ├── priorities.md             # Current priority stack
│   │   └── roadmaps/                 # Product/project roadmaps
│   ├── projects/                     # Project management (mirrors PROJECTS/)
│   │   ├── active.md                 # Active projects tracker
│   │   ├── shelve-bay.md             # Shelved/suspended projects
│   │   └── milestones.md             # Cross-project milestone tracker
│   ├── films/                        # Film project oversight
│   │   ├── pipeline-status.md        # Live production pipeline
│   │   ├── creative-directive/       # Creative direction notes
│   │   └── resource-allocation.md    # Crew, budget, tool allocation
│   ├── tools/                        # Tool development tracking
│   │   ├── dev-roadmap.md            # Tool development priorities
│   │   ├── architecture/             # System design documents
│   │   └── skill-inventory.md        # Current skill/tool inventory
│   ├── governance/                   # CEO-level governance
│   │   ├── vault-audit.md            # Vault integrity checks
│   │   ├── quality-review/           # Emily filing audit log
│   │   └── decisions.md              # Strategic decisions log
│   ├── heartbeat.md                  # Alfred's self-maintenance log
│   └── index.md                     # Alfred's workspace index
│
├── BUSINESS/                         # Company ops (Alfred sole ownership)
│   ├── Clients/
│   ├── Contracts/
│   ├── Operations/
│   └── Finances/
│
├── PROJECTS/                         # Live work projects (Alfred governance)
│   ├── arek-co-os/
│   ├── CHS/
│   ├── RealityRowHub/
│   └── [active projects]
│
├── CREATIVE/                         # Creative governance (Alfred oversight)
│   ├── Imma-Nyala/
│   ├── Aiah-Syn/
│   ├── YouTube-Concepts/
│   └── [Emily writes; Alfred reviews]
│
├── VFX/                              # VFX career strategy (Alfred)
│   ├── Career-Goals/
│   ├── Projects/
│   └── Memberships/
│
├── AGENTS/                           # Agent infrastructure (Alfred)
│   ├── shared_sync.md                # Sync log (shared, append-only)
│   ├── alfred/                       # Alfred-specific agent files
│   └── [system-level config]
│
├── LEARNING/Synthesis/               # High-level synthesis (Alfred)
│   └── [cross-domain analysis pages]
│
├── META/                             # Shared templates + config
│   ├── alfred-side-of-the-deal.md    # This file
│   ├── emilys-side-of-the-deal.md    # Emily's counterpart
│   ├── Templates/
│   └── Handoff-Inbox-Template.md
│     └── [handoff templates]
│
├── Handoff/                          # Shared handoff inbox
│   ├── inbox-to-alfred.md            # Items FROM Emily
│   ├── inbox-from-alfred.md          # Items TO Emily
│   └── queue/
│       ├── pending-sync.md
│       └── ack-tracker.md
│
└── INDEX.md                          # Root vault index (Alfred authority)
```

### Quick-Reference Folder Codes

| Code | Folder | Owner |
|---|---|---|
| `A/` | `Alfred/` | Alfred |
| `B/` | `BUSINESS/` | Alfred |
| `P/` | `PROJECTS/` | Alfred |
| `F/` | `CREATIVE/` | Shared (Emily writes, Alfred governs) |
| `V/` | `VFX/` | Alfred |
| `AG/` | `AGENTS/` | Alfred (systems) |
| `SY/` | `LEARNING/Synthesis/` | Alfred |
| `H/` | `Handoff/` | Shared |

---

## 3. Sync Protocol (Alfred's Side)

### Receiving Items from Emily (Inbound)

1. **Primary channel:** `Handoff/inbox-to-alfred.md` — Emily appends items in standard format
2. **Secondary channel:** `shared_sync.md` — Append-only log for awareness (both agents write)
3. **Telegram trigger:** "Go Alfred" — on-demand CEO briefing

#### Standard Handoff Item (as received from Emily):

```markdown
## [YYYY-MM-DD] Handoff Item #NN
**From:** Emily
**Priority:** P1 (urgent) | P2 (this week) | P3 (backlog)
**Type:** action | decision | info | review
**Summary:** [one-line description]
**Details:** [full description]
**Deadline:** [date/time or N/A]
**Emily's Suggested Approach:** [optional]
```

### Sending Items to Emily (Outbound)

1. **Primary channel:** `Handoff/inbox-from-alfred.md` — Alfred writes decisions/reports
2. **Format:**

```markdown
## [YYYY-MM-DD] Alfred Response #NN
**To:** Emily
**Status:** approved | modified | rejected | needs-info
**Decision:** [what Alfred decided]
**Action Required From Emily:** [specific next steps]
**Strategic Context:** [brief rationale]
**Timestamp:** [time processed]
```

### Process Flow

```
Emily writes item → Handoff/inbox-to-alfred.md
    ↓
Alfred's cron reads inbox (every 30 min)
    ↓
Alfred processes item
    ↓
Alfred logs outcome → Handoff/inbox-from-alfred.md
    ↓
Alfred appends to shared_sync.md
    ↓
Emily reads Handoff/inbox-from-alfred.md (her cron, every 30 min)
```

### Handoff Item Lifecycle (Alfred's Responsibility)

| Stage | Action | Location |
|---|---|---|
| **Received** | Read and classify by priority | `Alfred/inbox/to-process.md` |
| **Processing** | Move to active work queue | `Alfred/inbox/processing.md` |
| **Completed** | Write response, archive outcome | `Handoff/inbox-from-alfred.md` + `Alfred/inbox/done.md` |
| **Acknowledged** | Emily has read; item closed | `Handoff/queue/ack-tracker.md` |

### Alfred's Acknowledgment SLA

| Priority | SLA | Notification Method |
|---|---|---|
| **P1 (urgent)** | Within 2 hours during work hours (08:00–22:00) | Telegram push + `H/` tag in inbox |
| **P2 (this week)** | Within 24 hours | Included in next inbox sweep |
| **P3 (backlog)** | Within 72 hours | Included in next inbox sweep |
| **After hours exception** | All P1 items acknowledged within 2 hours of 08:00 next day | Telegram delayed push |

### Weekly Reset Ritual (Alfred's Side)

Every **Sunday 21:00**:
1. Clear `Alfred/inbox/done.md` — archive to `Alfred/inbox/done/YYYY-WNN/`
2. Review `Handoff/queue/pending-sync.md` — move completed items to appropriate folders
3. Review `Alfred/priorities.md` — adjust for the coming week based on handoff outcomes
4. Write Sunday governance summary to `shared_sync.md`

---

## 4. Automation Schedule (Alfred's Side)

### Alfred Cron Jobs

| Cron Job | Schedule | Action |
|---|---|---|
| **Morning CEO Briefing** | `0 8 * * *` (daily 08:00) | Read `shared_sync.md`, vault status, and pending handoff items. Generate CEO briefing delivered to Telegram. |
| **Handoff Inbox Sweep** | `*/30 * * * *` (every 30 min) | Scan `Handoff/inbox-to-alfred.md` for new items. Classify by priority. Move actionable items to `Alfred/inbox/processing.md`. Write `Alfred/heartbeat.md` entry on new findings. |
| **Handoff Response Flush** | `*/15 * * * *` (every 15 min) | Check if Alfred has pending responses in `Alfred/inbox/processing.md` that are waiting for output. Flush completed responses to `Handoff/inbox-from-alfred.md`. |
| **Project Status Pulse** | `0 17 * * *` (daily 17:00) | Scan all `PROJECTS/*/` for stale entries. Flag projects with no update in 7+ days. Update `Alfred/projects/active.md`. |
| **Creative Governance Review** | `0 20 * * 1` (Mon 20:00) | Review all active CREATIVE/ projects against strategic alignment. Note any drift. Report to `shared_sync.md`. |
| **Vault Integrity Audit** | `0 22 * * 6` (Sat 22:00) | Check INDEX.md completeness, verify frontmatter on LEARNING/Synthesis/*, flag orphaned files, run quality review of Emily's recent filings. |
| **Strategy Quarterly Review** | `0 9 1 1,4,7,10 *` (1st at 09:00 in Jan/Apr/Jul/Oct) | Generate quarterly strategy review. Compare project status vs annual strategy. Update `Alfred/strategy/quarterly-reviews/`. |
| **Film Pipeline Review** | `0 19 * * 3` (Wed 19:00) | Check all active film projects for status updates. Flag stalled milestones. Update `Alfred/films/pipeline-status.md`. |
| **Tool Dev Assessment** | `0 11 * * 4` (Thu 11:00) | Review `Alfred/tools/dev-roadmap.md` progress. Flag overdue tool items. Assess new skill/tool opportunities from LEARNING/Knowledge/. |
| **Weekend Handoff Sync Check** | `0 12 * * 0` (Sunday 12:00) | Mirror Emily's 12:00 — check `Handoff/queue/` for any stale pending items. Push urgent items to Telegram. Preps for Sunday 21:00 weekly reset. |
| **Alfred Heartbeat Self-Check** | `0 */4 * * *` (every 4 hours) | Verify `Alfred/heartbeat.md` is not stale. If last heartbeat > 48h ago, trigger alert. This ensures Alfred's presence is always confirmed. |

### Alfred Telegram Delivery Rules

| Trigger | Delivery |
|---|---|
| CEO Briefing (08:00) | Full briefing to Telegram — priorities, decisions needed, project status |
| P1 Handoff item processed | Immediate Telegram notification to Emily via `Handoff/inbox-from-alfred.md` |
| Weekly reset complete (Sun 21:00) | Weekly governance summary — decisions made, items closed, strategy shifts |
| Vault integrity issues | Alert Telegram with summary of findings |
| No items to report | Silent — no notification spam |

---

> **Last updated:** 2026-06-03 by Alfred
> **Review cadence:** Monthly on the 1st, coordinated with Emily's monthly review. Adjust if workflow needs change.
> **Companion:** See `META/emilys-side-of-the-deal.md` for Emily's corresponding section.
