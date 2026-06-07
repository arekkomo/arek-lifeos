---
name: coach-profile-setup
description: "How to set up the Coach profile in Hermes: profile config, skills, skill registration, topic wiring, and Notion data source setup."
---

# Coach Profile Setup

## Architecture
Coach is a **Hermes profile** (`~/.hermes/profiles/coach/`) with:
- **Agent identity** — `hybrid-arch:coach-specialist` skill (persona, context, rules)
- **Domain skills** — five Coach skills (fitness, nutrition, body comp, sleep/recovery, health intel)
- **Obsidian access** — vault at `~/Obsidian/Arek&Co/` with HEALTH/ as primary read/write
- **Data source** — Notion workout database (needs MCP server installed)

## Profile Directory Structure
```
~/.hermes/profiles/coach/
├── config.yaml          # Skills list + toolsets + working_directory
├── SKILL.md             # Agent identity + context + response format (always prefix with **Coach:**)
├── skills/              # (optional: bundled supporting skills)
└── cron/                # (optional: cron jobs specific to Coach)
```

## Profile Config (required)
```yaml
name: coach
description: "Isolated fitness, health, nutrition, recovery specialist"
skills:
  - hybrid-arch:coach-specialist
  - coach-fitness-tracking
  - coach-nutrition-tracking
  - coach-body-composition
  - coach-sleep-recovery
  - coach-health-intelligence
model: {}
deliver: origin
toolsets:
  - file
  - search
  - vision
working_directory: /home/realityrove/Obsidian/Arek&Co
```

## Telegram Access Pattern
Preferred architecture: Coach should normally run as a **dedicated Hermes profile with its own Telegram bot and its own Coach-only group**, not as a topic inside the Emily/default group. This keeps Coach memory, skills, model, pairing, and logs isolated from Operator/Emily.

### Dedicated Coach Bot + Group
1. Create a Telegram bot via `@BotFather` and put the bot token in the Coach profile's Telegram config/env, not the default profile.
2. Run Coach gateway as its own service, e.g. `hermes-gateway-coach.service` using `hermes --profile coach gateway run --replace`.
3. Approve Arek in the Coach profile pairing DB: `HERMES_HOME=~/.hermes/profiles/coach hermes pairing list` and approve/revoke there, not in default.
4. Create a separate Coach-only Telegram group and add the Coach bot.
5. Enable Telegram topics inside that group for subdomains (Training, Nutrition, Sleep/recovery, Body composition, Health/labs, General check-ins). Let each topic become its own Telegram thread/session under the Coach profile.
6. Remove the Coach bot from the Emily/default group after migration so both gateways are not receiving the same Coach-ish conversation.

### Legacy Topic Wiring
Topic wiring inside the Emily/default group is legacy and should only be used as a temporary bridge. If used, prefer the current config path `platforms.telegram.extra.group_topics` with entries like `{chat_id, topics:[{name, thread_id, skill}]}`. Do **not** rely on stale `telegram.group_topics: {'145': 'coach'}` style config.

### Verification Checklist
- `systemctl --user is-active hermes-gateway-coach.service` → `active`.
- Coach status shows Telegram configured under the Coach profile: `HERMES_HOME=~/.hermes/profiles/coach hermes status --all`.
- Coach pairing list shows Arek approved: `HERMES_HOME=~/.hermes/profiles/coach hermes pairing list`.
- Coach logs show the new group chat ID in `~/.hermes/profiles/coach/logs/gateway.log` with `inbound message` and eventually `response ready`.
- Default logs should not be the primary receiver for the new Coach group.

### Behavior Pitfall
After the routing is correct, verify a trivial message like `hi`. If Coach receives it but spins through many tools/model calls before responding, the setup is correct but the Coach behavior prompt/tool discipline needs tightening: casual greetings, check-ins, food logs, and simple measurements should get direct Coach replies unless a tool is genuinely needed.

When tightening Coach behavior, update profile-level prompt/config rather than routing:
- Add no-tools-for-greetings rules to `~/.hermes/profiles/coach/SOUL.md` and local `SKILL.md`.
- Consider disabling heavy/non-Coach toolsets in Coach config (`terminal`, `code_execution`, `cronjob`, `delegation`) and removing `execute_code` from `command_allowlist`.
- Enable stricter `tool_loop_guardrails` so repeated/no-progress tool use stops quickly.
- Restart `hermes-gateway-coach.service`; if it hangs in `deactivating` because an old turn is draining, force-stop only that Coach service and start it fresh.
- Verify with `HERMES_HOME=~/.hermes/profiles/coach hermes chat -q 'hi' --profile coach --quiet`; healthy result is one short `**Coach:**` reply with `tool_turns=0` in logs.

More detail: `references/coach-dedicated-telegram-group.md`.

## Notion Data Source
Workout tracking lives in Notion, not Obsidian. The Coach needs a Notion MCP server to query workout DBs:
- Install: `npm install -g @notionhq/notion-mcp-server`
- Wire: `hermes mcp add notion --url https://mcp.notion.com/mcp`
- Auth: `ntn_xxx` token from Notion Settings → Connections
- **Pitfall:** Notion Integration (secret_xxx) is DIFFERENT from Connection (ntn_xxx). Use Connections for MCP.

## Coach vs Operator Distinction
- **Operator** handles routing, daily admin, journaling, cross-agent coordination
- **Coach** handles ONLY fitness/nutrition/sleep/recovery — never give partial answers, always route
- **Prefix:** Coach responses MUST start with `**Coach:**` for visual clarity
- Operator's SKILL.md should have routing rules to dispatch fitness/health content to Coach profile