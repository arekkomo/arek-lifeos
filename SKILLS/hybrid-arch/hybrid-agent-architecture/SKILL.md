---
name: hybrid-agent-architecture
description: "Configure and operate a hybrid agent system with both a switchboard (Operator routing) and direct specialist threads. Governs profile creation, routing rules, and profile-template usage."
---

# Hybrid Agent Architecture

A system where the Operator (Emily) serves as both **router** and **generalist**, with specialists accessible via direct threads. Users talk to specialists directly when they know who to call; the Operator handles everything else.

## Architecture

| Layer | Role | Access |
|-------|------|--------|
| **Operator** (main thread) | Generalist, daily admin, journaling, routing | Full context |
| **Specialist threads** (Coach, Finance, Director, Connector) | Domain-specific work, isolated context | Only their domain |
| **Kanban** (future) | Multi-phase projects, only when needed | Spawns from Operator |

## Dual routing layer

### Layer 1: Telegram topic routing (primary, direct)
When the group has topics wired up, routing is automatic by thread. Each topic = a session with the right profile loaded. No @-mention needed.

**To wire a topic to a profile:** User creates the topic in Telegram app, then shares the topic ID with the Operator. The Operator confirms and activates the corresponding specialist profile for that thread.

**Recommended topic setup for 4-agent architecture:**
| Topic name | Agent | Domain |
|-------------|-------|--------|
| 🏋️ Coach | `coach` profile | Health, fitness, nutrition, recovery |
| 💰 Finance | `finance` profile | Portfolio, budgeting, tax, net worth |
| 🎬 Director | `director` profile | Film, music, creative pipeline |
| 📡 Connector | `connector` profile | Events, contacts, networking, social drafts |

Each topic should be created in Telegram (Arek & Emily & Co group → Edit Topics → New Topic). Long-press the topic name and share the topic ID with the Operator for wiring.

### Layer 2: Content-based routing (fallback, only in DMs)
When Arek sends a message:
1. Check for specialist triggers (`@coach`, `@finance`, or clear domain intent)
2. If triggered → load the specialist profile, forward the message, reply in main thread: "Filed to /{name}. They'll handle it."
3. If unclear → answer yourself as Operator
4. If a large project → flag for Kanban activation

**Specialist triggers:**
| Intent | Route To | Trigger words |
|--------|---------|----|
| Fitness, gym, protein, recovery, nutrition | `coach` profile | "gym", "workout", "protein", "weight", "recovery" |
| Portfolio, net worth, budget, tax, money | `finance` profile | "net worth", "portfolio", "TD", "stock", "budget" |
| Imma Nyala, music, script, video, creative | `director` profile (future) | "script", "idea", "video", "Imma", "Aiah Syn" |
| Events, contacts, networking, meetings | `connector` profile (future) | "event", "meeting", "contact" |

## Critical rules
- **Never partially answer for a specialist.** If it's Coach business, you forward it. Zero overlap.
- **Specialists have isolated context.** They don't see creative, financial, or scheduling data — and vice versa.
- **Kanban only for real projects.** Daily flow goes through specialist threads, not boards.

## Creating new specialist profiles (procedure)

When adding a new specialist, follow this sequence:

1. **Write `~/.hermes/profiles/<name>/config.yaml`** — profile config with skills list and toolsets
2. **Write `~/.hermes/profiles/<name>/SKILL.md`** — specialist context (read/write paths to Obsidian, domain scope)
3. **Create a skill file** (`~/.hermes/skills/hybrid-arch/<name>-specialist/SKILL.md`) — behavior/spec for the specialist
4. **Add routing rules** — include the new specialist in the Operator's routing table above
5. **(Optional) Update the profile-template** (see `templates/profile-template/SKILL.md`)

Use `templates/profile-template/SKILL.md` as the scaffold for each new profile.

## Pitfalls
- **Don't build a specialist without updating Operator routing.** If there's no route rule, no message will ever reach it.
- **Don't give specialists access to each other's data.** Keep the isolation hard. Coach reads nothing financial. Finance reads nothing creative.
- **Don't make the Operator also a fallback for specialist work.** If the user wants Coach advice, route to Coach. Don't try to answer it yourself.

## Absorbed Profile Setup and Routing Playbooks

This skill is now the umbrella for hybrid profile architecture, specialist profile setup, and prefix/topic routing. Preserved full legacy playbooks:

- `references/coach-profile-setup.md`
- `references/coach-profile-setup-coach-dedicated-telegram-group.md`
- `references/channel-routing.md`

### Coach profile setup pattern

Coach is the reference specialist profile pattern: an isolated Hermes profile with its own config, identity skill, domain skills, Obsidian scope, Notion data source, and Telegram topic/bot wiring.

Use Coach as the template for new specialists:

1. Create `~/.hermes/profiles/<specialist>/config.yaml` with only the specialist's domain skills/toolsets.
2. Create `~/.hermes/profiles/<specialist>/SKILL.md` for identity, scope, and response prefix.
3. Give long-lived specialists their own bot/topic credentials when they should run concurrently with the default profile.
4. Wire routing in the Operator and in Telegram topics; profile isolation is only useful if routing is explicit.
5. Verify the specialist can read/write only its intended domain folders/data sources.

### Prefix routing fallback

When Telegram topics or direct specialist threads are unavailable, use prefix routing as the fallback DM convention. Typical buckets: `finance:`, `write:`, `project:`, `research:`, `diary:`, `context:`, and `meta:`.

Hard rule: if confidence that a message belongs to exactly one bucket is below the routing threshold, ask the user which route to use instead of silently choosing.
