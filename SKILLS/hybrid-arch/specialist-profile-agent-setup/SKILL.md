---
name: specialist-profile-agent-setup
description: Use when Arek wants to create a new specialist Hermes profile/agent with isolated instructions, vault-synced context, dedicated Telegram bot, and optional dedicated group/topics. Prevents false starts between topic-routing, skill-loading, and true separate-profile/bot architecture.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [hermes, profiles, telegram, specialist-agents, life-os, setup]
    related_skills: [hermes-agent, hybrid-agent-architecture, native-mcp]
---

# Specialist Profile / Agent Setup

## Overview

Use this skill to set up a new specialist agent in the Arek & Co. Life OS: a separate Hermes profile, dedicated role instructions, vault-synced context, profile-specific tools/MCP, a dedicated Telegram bot, and optionally a dedicated Telegram group with forum topics.

The key lesson from the Coach setup: **do not confuse a topic skill binding with a true separate agent**.

There are three distinct architectures:

1. **Default profile + topic skill binding** — one gateway/profile; a Telegram topic loads extra skills. Fast, but not isolated.
2. **Separate Hermes profile without dedicated bot** — isolated config/memory exists, but needs routing/spawning from another gateway. Easy to misunderstand.
3. **Separate Hermes profile + dedicated Telegram bot/group** — clean specialist-agent architecture. This is preferred when Arek wants direct specialist communication.

For obvious specialist domains — Coach, Finance, Director, Connector, etc. — prefer architecture #3 unless Arek explicitly asks for lightweight topic routing.

## When to Use

Use when Arek says things like:

- “Create a new agent/profile for X.”
- “Set up a dedicated bot for X.”
- “Move X out of this group into its own group.”
- “I want conversations across different topics with X.”
- “Sync instructions from the vault for a new specialist.”
- “Make this specialist direct, not routed through Emily.”

Do **not** use for:

- A one-off temporary role/persona inside the current chat.
- A simple Telegram topic that should only load an extra skill in the default profile.
- A coding subagent/delegation task; use agent delegation skills instead.

## Decision Tree

Before changing config, classify the target setup:

1. **Does Arek want a persistent specialist with its own memory/config?**
   - Yes → create/use a named Hermes profile.
   - No → use topic skill binding or a session-loaded skill.

2. **Does Arek want to talk to it directly from Telegram without Emily/default routing?**
   - Yes → create a dedicated Telegram bot token and a profile-specific gateway service.
   - No → configure gateway topic routing from default to the specialist profile only if supported.

3. **Does Arek want multiple conversations within that specialist?**
   - Yes → create a dedicated Telegram group, enable forum topics, add the specialist bot.
   - No → a direct DM with the bot is enough.

4. **Does the specialist need vault/Notion/MCP access?**
   - Yes → configure only the domain-specific tool access and write explicit isolation rules.
   - No → keep tools minimal.

## Prerequisite Checks

Always verify current state before editing:

```bash
hermes profile list
systemctl --user list-units 'hermes-gateway*' --no-pager
```

Inspect default and specialist configs:

```bash
hermes config path
hermes --profile <profile> config path
```

Check whether the existing “specialist” is only a topic skill binding:

```bash
python3 - <<'PY'
import yaml, json
from pathlib import Path
p = Path.home()/'.hermes/config.yaml'
c = yaml.safe_load(p.read_text()) or {}
print(json.dumps((c.get('platforms') or {}).get('telegram') or {}, indent=2))
print(json.dumps(c.get('telegram') or {}, indent=2))
PY
```

Important Telegram routing note:

- Current Hermes group-topic bindings live at `platforms.telegram.extra.group_topics`.
- Old `telegram.group_topics` mappings are stale/ignored in current gateway code.
- A topic skill binding is not the same as a separate profile.

## Step 1 — Create or Verify the Profile

Create a profile when it does not exist:

```bash
hermes profile create <name>
hermes profile show <name>
```

Expected profile path:

```text
~/.hermes/profiles/<name>/
```

Configure the profile model/provider. For Arek’s local Ollama setup, Coach used:

```yaml
model:
  default: qwen3.6:latest
  provider: custom
  base_url: http://10.0.0.61:11434/v1
```

Verify model availability when relevant:

```bash
curl -sS --max-time 5 http://10.0.0.61:11434/v1/models
```

Do not assume the profile is active just because it exists. A profile is only usable through a running CLI/gateway/cron/worker process using `--profile <name>`.

## Step 2 — Sync Instructions from Vault / Source of Truth

Create a profile-level `SOUL.md` for durable identity and behavioral rules:

```text
~/.hermes/profiles/<name>/SOUL.md
```

Use vault context as the source of truth where available. See `references/vault-synced-specialist-soul.md` for the source-resolution pattern and verification checklist.

Do **not** assume the specialist `Brief.md` is complete. In Arek's vault it may be only a stub pointing to the real operational instructions. Check `CoWork-Instructions-LIVE.md`, `CoWork-Instructions.md`, `Task-Management.md`, `Technical-Setup/*.md`, `memory/MEMORY.md`, relevant `memory/*.md`, and matching skill files such as `SK-SY-*` for System. Quote vault paths because `/home/realityrove/Obsidian/Arek&Co/` contains `&`.

The `SOUL.md` should contain:

- Identity: who this specialist is.
- Mandate: what domain it owns.
- Scope boundaries: what it must not access or decide.
- User-specific context from vault notes.
- Data access: exact allowed folders/databases/tools.
- Response format/prefix if needed.
- Tool discipline: when to use tools and when to answer directly.
- Source-of-truth files read from the vault and optional files left for deeper sync.

For Arek’s Life OS, prefer a mandatory prefix for specialist clarity:

```markdown
Every response must start with:

**<SpecialistName>:**
```

This prevents confusion between Emily/default and specialist profiles.

## Step 3 — Install / Create Specialist Skills

Add only the skills needed by the profile. In profile config:

```yaml
skills:
- hybrid-arch:<specialist-skill>
- domain-specific-skill-1
- domain-specific-skill-2
```

Rules:

- Keep skills domain-specific.
- Do not load Emily/Alfred/global strategy skills unless this profile needs them.
- For health/finance/private domains, explicitly prohibit unrelated vault folders.
- If a specialist needs a new reusable workflow, create a skill instead of stuffing all procedure into `SOUL.md`.

## Step 4 — Configure Tools and MCP Minimally

Avoid enabling broad toolsets by default. Give each specialist only what it needs.

For a conversational specialist, consider disabling heavy toolsets:

```yaml
agent:
  disabled_toolsets:
  - terminal
  - code_execution
  - cronjob
  - delegation
```

Tighten tool-loop guardrails:

```yaml
tool_loop_guardrails:
  warnings_enabled: true
  hard_stop_enabled: true
  warn_after:
    exact_failure: 1
    same_tool_failure: 2
    idempotent_no_progress: 1
  hard_stop_after:
    exact_failure: 2
    same_tool_failure: 3
    idempotent_no_progress: 2
```

Remove unnecessary auto-approval for dangerous/heavy commands:

```yaml
command_allowlist: []
```

### Notion MCP — single master token architecture (updated 2026-06-09)

All profiles inherit NOTION_MCP_TOKEN from the parent/gateway-level `.env` at `/home/realityrove/.hermes/.env`. **Do NOT add `NOTION_MCP_TOKEN` to a profile's `.env` file.** If a profile's `.env` has a duplicate Notion token, delete that line — the inheritance from the parent is automatic and ensures a single source of truth.

Add the Notion MCP block to `config.yaml` (same for every profile):

```yaml
mcp_servers:
  notion:
    command: npx
    args:
    - -y
    - '@notionhq/notion-mcp-server'
    - --transport
    - stdio
    env:
      NOTION_TOKEN: ${NOTION_MCP_TOKEN}
      OPENAPI_MCP_HEADERS: '{"Authorization":"Bearer ${NOTION_MCP_TOKEN}","Notion-Version":"2022-06-28"}'
    enabled: true
    name: Notion MCP (local stdio)
    timeout: 120
    connect_timeout: 60
```

**Verification checklist:**
- [ ] Profile `.env` file (e.g., `~/.hermes/profiles/<name>/.env`) contains `NOTION_MCP_TOKEN=***`
- [ ] `config.yaml` has the notion MCP block with `enabled: true` under `mcp_servers`
- [ ] Profile has Notion MCP listed in toolsets or `plugins` section if needed

## Step 5 — Dedicated Telegram Bot

For a true independent specialist over Telegram, use a dedicated BotFather bot token.

Tell Arek to create the bot:

1. Message `@BotFather`.
2. Send `/newbot`.
3. Pick a display name, e.g. `Arek Coach`.
4. Pick a username ending in `bot`, e.g. `Coach_arco_bot`.
5. Paste the **API token**, not just the bot username or ID.

Do not claim setup is complete from the username alone. The gateway needs the token.

Configure the specialist profile’s Telegram platform. Exact config shape may vary by Hermes version, so verify with docs/config and existing profile config, but target state is:

```yaml
platforms:
  telegram:
    enabled: true
```

The token is usually stored via environment/config mechanisms, not exposed in replies. Never print the raw token back to chat.

Verify the bot identity without leaking the token, e.g. with Telegram `getMe` or logs showing Telegram connected.

## Step 6 — Start a Profile-Specific Gateway Service

Install/start a gateway under the specialist profile:

```bash
hermes --profile <name> gateway install
hermes --profile <name> gateway start
```

Or, if a systemd service already exists:

```bash
systemctl --user start hermes-gateway-<name>.service
systemctl --user enable hermes-gateway-<name>.service
systemctl --user status hermes-gateway-<name>.service --no-pager -l
```

Expected process shape:

```text
python -m hermes_cli.main --profile <name> gateway run --replace
```

Verify:

```bash
systemctl --user is-active hermes-gateway-<name>.service
systemctl --user is-enabled hermes-gateway-<name>.service
```

If restart hangs because an old turn is draining, force only that specialist service:

```bash
systemctl --user kill --signal=SIGKILL hermes-gateway-<name>.service || true
systemctl --user reset-failed hermes-gateway-<name>.service || true
systemctl --user start hermes-gateway-<name>.service
```

Use this only after confirming the service is stuck in `deactivating` and not simply starting slowly.

## Step 7 — Pair / Approve Arek

Check pairing under the specialist profile, not default:

```bash
HERMES_HOME=/home/realityrove/.hermes/profiles/<name> hermes pairing list
```

Approve if a pending pairing exists:

```bash
HERMES_HOME=/home/realityrove/.hermes/profiles/<name> hermes pairing approve telegram <CODE>
```

If Arek is already approved, the list should show his Telegram user ID.

For Coach, the approved Telegram ID was `8178908137`.

## Step 8 — Dedicated Telegram Group and Topics

If Arek wants multiple conversations inside the specialist domain:

1. Create a new Telegram group dedicated to the specialist.
2. Add the specialist bot.
3. Enable Telegram topics/forum mode if desired.
4. Create domain topics, e.g. for Coach:
   - Training
   - Nutrition
   - Sleep/recovery
   - Body composition
   - Health/labs
   - General check-ins
5. Remove the specialist bot from old/default groups if it should no longer listen there.

A dedicated group with topics is cleaner than routing through Emily/default when the domain is obvious.

## Step 9 — Verify Real Routing

Do not stop at “service active.” Verify an actual message reaches the intended profile.

Check specialist gateway logs:

```bash
python3 - <<'PY'
from pathlib import Path
p = Path('/home/realityrove/.hermes/profiles/<name>/logs/gateway.log')
for line in p.read_text(errors='replace').splitlines()[-120:]:
    if 'inbound message' in line or 'response ready' in line or 'Connected to Telegram' in line:
        print(line[:900])
PY
```

Expected evidence:

```text
inbound message: platform=telegram user=Arek ... chat=<new_group_id> msg='hi'
conversation turn: ... model=<profile_model> provider=<profile_provider> platform=telegram
response ready: platform=telegram chat=<new_group_id> ...
```

Also check that default gateway did **not** receive the new specialist-group message:

```bash
python3 - <<'PY'
from pathlib import Path
p = Path('/home/realityrove/.hermes/logs/gateway.log')
for line in p.read_text(errors='replace').splitlines()[-120:]:
    if 'inbound message' in line or 'response ready' in line:
        print(line[:900])
PY
```

## Step 10 — Test Behavior, Not Just Connectivity

Run a simple profile-local test:

```bash
HERMES_HOME=/home/realityrove/.hermes/profiles/<name> hermes chat -q 'hi' --profile <name> --quiet
```

Then confirm no tool loop:

```bash
python3 - <<'PY'
from pathlib import Path
p = Path('/home/realityrove/.hermes/profiles/<name>/logs/agent.log')
for line in p.read_text(errors='replace').splitlines()[-80:]:
    if '<session_id_from_test>' in line:
        print(line[:1000])
PY
```

Expected:

```text
api_calls=1 ... tool_turns=0 ... reason=text_response
```

If a simple greeting triggers tools, patch `SOUL.md` with response/tool discipline immediately.

## Recommended Response Discipline Snippet

Add this to specialist `SOUL.md` for conversational specialists:

```markdown
## Response Discipline

Default to a direct <SpecialistName> reply. Do **not** inspect files, search history, query Notion, run code, or use tools for simple conversational messages.

Fast-path messages that should receive an immediate short reply with no tools:

- greetings: "hi", "hey", "hello", "<specialist>?"
- setup checks: "are you there?", "test", "is this working?"
- lightweight check-ins without data: "I'm back", "starting now", "rough day"

For these, answer in 1–3 sentences, starting with `**<SpecialistName>:**`, and ask for the next useful domain datum only if appropriate.

Use tools only when the user explicitly asks you to log, retrieve, compare, analyze an image/file, update a database/note, or verify a factual/current claim. If a tool is useful but not necessary, skip it and respond from specialist context.

Never use code execution or terminal-style tools for ordinary conversation. If a tool loop starts, stop after one failed/no-progress attempt and give the best direct answer.
```

## Common Pitfalls

### Cloned-profile hygiene for dedicated Telegram bots

When creating a specialist by cloning `default`, do a cleanup pass before declaring the bot ready. Cloned profiles can inherit platform env/config that makes the gateway appear “running” while Telegram replies fail or route to the wrong place.

Required cleanup for a Telegram-only specialist:

```bash
# Keep only the specialist's own TELEGRAM_BOT_TOKEN in the profile .env.
# Remove cloned defaults from ~/.hermes/profiles/<name>/.env:
# - DISCORD_BOT_TOKEN, DISCORD_HOME_CHANNEL, DISCORD_HOME_CHANNEL_THREAD_ID, DISCORD_ALLOWED_USERS
# - WHATSAPP_MODE, WHATSAPP_ALLOWED_USERS, WHATSAPP_ENABLED
# - TELEGRAM_HOME_CHANNEL, TELEGRAM_HOME_CHANNEL_THREAD_ID

hermes --profile <name> config set platforms.discord.enabled false
hermes --profile <name> config set platforms.whatsapp.enabled false
hermes --profile <name> config set telegram.allowed_chats ''
hermes --profile <name> config set platforms.telegram.allowed_chats ''
```

Also disable cloned MCP servers/toolsets that the specialist does not need. OAuth MCPs and broken stdio MCP configs can delay/noise startup and obscure the real Telegram issue:

```bash
hermes --profile <name> config set mcp_servers.linear.enabled false
hermes --profile <name> config set mcp_servers.graphthulhu.enabled false
hermes --profile <name> config set mcp_servers.notion.enabled false
```

Pairing alone may not be enough if the gateway is running with allowlists enabled. For Arek, seed both the pairing store and a Telegram allowlist when no pairing code is produced:

```bash
# pairing file
~/.hermes/profiles/<name>/pairing/telegram-approved.json

# profile .env
TELEGRAM_ALLOWED_USERS=8178908137
```

After restart, verify with a fresh message from Arek and recent logs. Do not trust stale `gateway status` health warnings from before the restart; inspect logs since the latest service start.

1. **Calling a topic skill binding a “profile.”**
   - A Telegram topic that loads Coach skills is still Emily/default unless the message is routed to a separate profile/gateway.

2. **Creating a profile but not connecting it to Telegram.**
   - A profile directory alone does nothing. It needs a running process: CLI, gateway, cron, or worker.

3. **Using the same Telegram bot for multiple profiles.**
   - Prefer one bot token per direct specialist. It avoids routing ambiguity and session confusion.

4. **Leaving the specialist bot in the old group.**
   - Telegram will still deliver messages from that group to the specialist gateway if the bot remains there.

5. **Not approving Arek in the specialist profile.**
   - Pairing data is profile-scoped. Default approval does not necessarily mean specialist approval.

6. **Over-enabling tools.**
   - Broad toolsets make simple messages slow and can create loops. Start minimal, then add tools only when needed.

7. **Not testing behavior after connectivity.**
   - “Connected to Telegram” only proves transport. Always send `hi` and confirm the profile answers directly.

8. **Leaking bot tokens.**
   - Never quote raw tokens in final summaries. Redact token-like values in logs and replies.

9. **Trusting stale documentation in old references.**
   - If references say the profile does not own its own Telegram client, re-check live config/service state. Architecture may have changed.

10. **Restart hanging on active agent drain.**
   - Check `systemctl status`. If stuck `deactivating` for minutes due to an old loop, kill only that specialist service and restart fresh.

## Verification Checklist

- [ ] Profile exists at `~/.hermes/profiles/<name>/`.
- [ ] Profile config has correct model/provider.
- [ ] `SOUL.md` exists with identity, scope, prefix, access rules, and tool discipline.
- [ ] Domain skills are loaded and unrelated skills are not.
- [ ] Required MCP/tools are configured minimally.
- [ ] Dedicated Telegram bot token is configured for the profile.
- [ ] `hermes-gateway-<name>.service` is active and enabled.
- [ ] Telegram logs show `Connected to Telegram` under the specialist profile.
- [ ] Arek is approved in the specialist profile pairing list.
- [ ] New dedicated group receives specialist messages.
- [ ] Old/default group no longer has the specialist bot if separation is desired.
- [ ] Specialist gateway logs show inbound message from the new group.
- [ ] Default gateway logs do not show the new specialist group message.
- [ ] `hi` test returns a direct prefixed response.
- [ ] Agent logs show `tool_turns=0` for simple greeting tests.
- [ ] If the profile was cloned from default, run the cleanup in `references/cloned-profile-telegram-hygiene.md` before declaring the bot ready.

## Minimal Setup Runbook

Use this as the fast path:

```bash
# 1. Create/verify profile
hermes profile create <name> || true
hermes profile show <name>

# 2. Edit profile config + SOUL.md
$EDITOR ~/.hermes/profiles/<name>/config.yaml
$EDITOR ~/.hermes/profiles/<name>/SOUL.md

# 3. Start profile gateway
hermes --profile <name> gateway install
hermes --profile <name> gateway start
systemctl --user status hermes-gateway-<name>.service --no-pager -l

# 4. Pair user
HERMES_HOME=/home/realityrove/.hermes/profiles/<name> hermes pairing list

# 5. Verify logs after Telegram test message
python3 - <<'PY'
from pathlib import Path
p=Path('/home/realityrove/.hermes/profiles/<name>/logs/gateway.log')
for line in p.read_text(errors='replace').splitlines()[-100:]:
    if 'inbound message' in line or 'response ready' in line or 'Connected to Telegram' in line:
        print(line[:900])
PY

# 6. Local behavior test
HERMES_HOME=/home/realityrove/.hermes/profiles/<name> hermes chat -q 'hi' --profile <name> --quiet
```

## Coach Setup Lessons Captured

From the Coach setup:

- The user wanted **direct specialist communication**, not central routing through Emily.
- The final clean architecture was: `coach` profile + dedicated `@Coach_arco_bot` + dedicated Coach Telegram group/topics.
- The old topic `145` binding in `Arek & Emily & Co` was removed from default config.
- The new group was verified by logs using chat ID `-1003951808887`.
- The Coach profile needed explicit no-tools-for-greetings discipline because `qwen3.6:latest` initially overused tools on a simple `hi`.
- The fix was not just connectivity; it included behavioral prompt/config tightening and a real `hi` test with `tool_turns=0`.


## Director + Scholar Setup Lessons (2026-06-09/10)

From building Director and Scholar profiles end-to-end, including debugging two full sessions of failures:

### 🔴 CRITICAL: Never Write Bot Tokens — Always Ask User via nano

When writing Telegram bot tokens to `.env` files, they ALWAYS get truncated or corrupted through tool calls (execute_code, write_file, terminal echo). The system replaces or strips parts of the token.

**Correct flow:**
1. Build all profile infrastructure FIRST (directories, config files, SOUL.md, MEMORY.md, etc.)
2. Tell the user: "Please paste the bot token: `nano /home/realityrove/.hermes/profiles/<name>/.env`"
3. Ask user to confirm the correct Telegram chat ID
4. Restart the gateway and verify from logs
5. Verify token length > 45 characters (Telegram tokens are 48 chars)

**ALWAYS verify after user says "done":**
```bash
# Check token length — must be 48 for valid token
sed -n '1p' /home/realityrove/.hermes/profiles/<name>/.env | awk -F= '{print length($2)}'
```

**Never do this:**
- Hard-code a placeholder token
- Write token programmatically in your response
- Assume "user pasted token" == "file has full value" — VERIFY the length
- Keep re-prompting the user for the same info without confirming the file state first

### 🔴 CRITICAL: The `providers:` Block Must Exist — NOT Just `provider: custom`

Having `provider: custom` on the model line is necessary but NOT sufficient. You MUST also have a **top-level `providers:` block** OR a `custom_providers:` entry in the main config.

**Pattern 1 — Profile-level custom_providers (preferred for new profiles):**
```yaml
model:
  default: qwen3.6:latest
  provider: custom
  base_url: http://10.0.0.61:11434/v1
custom_providers:
- name: <Name>
  base_url: http://10.0.0.61:11434/v1
  model: qwen3.6:latest
```

**Pattern 2 — Empty providers block (relies on global config):**
```yaml
model:
  default: qwen3.6:latest
  provider: custom
  base_url: http://10.0.0.61:11434/v1
providers: {}
```

When `custom_providers` is properly set, Coach works because it has the entry in main config. When `providers: {}` and no `custom_providers`, the profile has NO inference provider and silently fails.

**Scholar-specific lesson:** The `type: ollama` key inside providers blocks is REJECTED as invalid — `unknown config keys ignored: type`. This causes the entire providers block to be ignored. Do NOT include `type:` in provider configs.

**When it fails, the gateway logs show:**
`WARNING hermes_cli.config: providers.custom: unknown config keys ignored: type`

**If providers is empty `{}`, the gateway shows:**
`WARNING gateway.run: No inference provider configured`

**Neither shows an error about "bad model" — look for `no inference provider` or `unknown config keys ignored`.**

### 🔴 CRITICAL: systemctl "active" Does NOT Mean Telegram Is Connected

systemctl can show `active (running)` while the gateway Python process is:
- Failing to auth with Telegram
- Having network errors
- Crashing silently
- Using the wrong chat ID

**Always check the gateway logs directly after every restart:**
```bash
# Look for the Telegram connection confirmation
journalctl --user -u hermes-gateway-<name>.service --since "HH:MM" -n 50 | grep -iE 'connect|start|ready|telegram|ollama|provider|channel|id'

# Expected SUCCESS lines:
# ✓ telegram connected
# set_my_commands OK
```

**When it FAILS, look for:**
- `telegram.error.InvalidToken` — token is wrong
- `Httpx.ReadError` — either invalid token, DNS, or network issue
- `ChatMigrated` — chat ID was wrong, Telegram auto-redirected
- `Group migrated to supergroup` — same as ChatMigrated but different Telegram SDK path
- `No inference provider configured` — config issue, not Telegram issue

### 🟡 systemd Service File Lands in Wrong Directory

`hermes gateway install` creates the service file at:
```
~/.hermes/profiles/systems/home/.config/systemd/user/
```

But systemctl looks at:
```
~/.config/systemd/user/
```

**Always copy AFTER install:**
```bash
cp ~/.hermes/profiles/systems/home/.config/systemd/user/hermes-gateway-<name>.service    ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user start hermes-gateway-<name>.service
```

### 🟡 Vault Brief.md is Often Incomplete — Check for CoWork-Instructions

Vault agent folders often have a stub Brief.md that points to the REAL operational instructions. ALWAYS check for:

```bash
ls -la /home/realityrove/Obsidian/Arek&Co/AGENTS/<Agent>/
ls -la /home/realityrove/Obsidian/Arek&Co/AGENTS/<Agent>/memory/
```

Typical patterns:
- **Brief.md** = stub (59-288 bytes) with a pointer
- **CoWork-Instructions.md** = real operational content (200+ lines)
- **Heartbeat.md** = session-start checklist → needs to be installed as cron job
- **memory/** folder = may contain additional context files

Never assume Brief.md is the identity. The real instructions live in CoWork-Instructions.

### 🟡 Chat ID Needs `-100` Prefix for Supergroups

Telegram groups that migrated to supergroups get a new chat ID format:
- Old format: `-5129275629` or `-3955859735`
- New format: `-1003955859735` (prepend `-100`)

If you get `ChatMigrated` or `Group migrated to supergroup` in logs, use the new `-100...` ID.

When Arek provides a group invite link like `https://t.me/c/3955859735/1`, extract the numeric part and prepend `-100` → `-1003955859735`.

### 🟡 YAML Quoting Gotcha — Descriptions with Apostrophes

Long descriptions with apostrophes or single quotes will break YAML. When writing config files programmatically, wrap descriptions in double quotes:

```yaml
description: "Director - creative partner for Arek & Co.'s creative layer..."
```

The YAML linter will silently reject the write if not quoted.

### 🟡 Telegram Requires Re-adding Bot to Group After New Chat ID

If the group migrated to supergroup or was recreated, the bot token/identity may not carry over. You may need to:
1. Remove the bot from the old group
2. Re-add it to the new group via BotFather's `/setjoingroups` or manual invite
3. Confirm the new group chat ID in the bot's permissions

### New Minimal Setup Flow (Post-Director+Scholar)

1. Check vault: `ls /home/realityrove/Obsidian/Arek&Co/AGENTS/<Agent>/`
2. Read Brief.md — if stub (< 300 bytes), find CoWork-Instructions.md
3. Check Hindsight banks: `python3 -c "..."` or check ~/.hindsight/
4. Create profile: `hermes profile create <name>`
5. Write MEMORY.md and USER.md from vault (Brief.md + About-Me-*.md)
6. Write SOUL.md from CoWork-Instructions.md (NOT Brief.md)
7. Write config.yaml with `custom_providers:` block (not just `provider: custom`)
8. Add domain skills
9. **ASK USER to paste bot token via nano** — do NOT write it yourself
10. **ASK USER to confirm chat ID** — extract from invite link if needed
11. Install/start gateway + copy service file + daemon-reload
12. **CHECK LOGS** — `journalctl -u hermes-gateway-<name>.service | grep telegram`
13. **VERIFY token length > 45** — if shorter, ask user to redo
14. Test: send `hi` to Telegram group
15. Check `tool_turns=0` for simple greeting
