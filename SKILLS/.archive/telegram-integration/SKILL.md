---
name: telegram-integration
domain: technical
version: 1.0
description: Set up and manage Telegram bot integration with Hermes Agent. Covers BotFather bot creation, token configuration, user pairing, gateway restart, and troubleshooting.
updated: 2026-06-02
---

# Telegram Integration (Hermes)

## Setup — 3 Steps

### Step 1: Create the bot via BotFather
1. Open [Telegram](https://t.me/BotFather) and search for **@BotFather**
2. Send `/newbot`
3. BotFather asks for a **display name**, then a **username** (must end in `bot`)
4. BotFather gives you an **API token** — format: `123456789:ABCdefGHI...`

### Step 2: Paste the token into Hermes
```bash
hermes config set TELEGRAM_BOT_TOKEN <your-token>
```
This writes the token to `~/.hermes/.env` (never edit `.env` manually).

### Step 3: Enable and restart
```bash
hermes config set gateway.telegram.enabled true
hermes gateway restart
```

### Dedicated bot for a non-default profile
When setting up a separate Hermes profile as a real specialist agent (for example `coach` or `systems`), do **not** reuse the default profile's Telegram token. Each running profile needs its own BotFather bot/token.

Bootstrap the specialist profile first, then keep Telegram disabled until its unique token is installed:

```bash
# Create the profile from default config/skills without cloning all state
hermes profile create <profile> --clone-from default --clone \
  --description 'One- or two-sentence specialist role description.'

# Add/replace specialist identity before starting the gateway
$EDITOR ~/.hermes/profiles/<profile>/SOUL.md

# Safety: if the profile was cloned, disable Telegram until the new BotFather token is set
hermes --profile <profile> config set platforms.telegram.enabled false
hermes --profile <profile> config set platforms.telegram.reactions false

# After BotFather provides the new token, write secret into the profile's .env, not default ~/.hermes/.env
hermes --profile <profile> config set TELEGRAM_BOT_TOKEN '<bot-token>'

# Enable Telegram, but strip inherited default-profile platform state before starting
hermes --profile <profile> config set platforms.telegram.enabled true
hermes --profile <profile> config set platforms.telegram.reactions false
hermes --profile <profile> config set platforms.discord.enabled false
hermes --profile <profile> config set platforms.whatsapp.enabled false
hermes --profile <profile> config set DISCORD_BOT_TOKEN ''
hermes --profile <profile> config set WHATSAPP_ENABLED false
hermes --profile <profile> config set TELEGRAM_HOME_CHANNEL ''
hermes --profile <profile> config set TELEGRAM_HOME_CHANNEL_THREAD_ID ''
hermes --profile <profile> config set telegram.allowed_chats ''
hermes --profile <profile> config set platforms.telegram.allowed_chats ''

# Install/start the profile gateway. `gateway install` is interactive; answer yes to install + enable.
yes y | hermes --profile <profile> gateway install
systemctl --user restart hermes-gateway-<profile>.service

# Verify profile-scoped status and pairing
hermes profile list
hermes profile show <profile>
hermes --profile <profile> status --all
hermes --profile <profile> gateway status
hermes --profile <profile> pairing list
```

Verification pattern:
- `getMe` should return `ok: true` and the expected bot username.
- `hermes profile show <profile>` should show `Gateway: running` after start; before token installation it should remain stopped/disabled.
- `hermes --profile <name> status --all` may show `Messaging Platforms → Telegram ✓ configured` if cloned token/home-channel data exists, even when the specialist gateway is stopped or Telegram has been deliberately disabled. Do not treat that line alone as proof the new bot is live; also verify `platforms.telegram.enabled`, the profile gateway status, and BotFather `getMe` for the new token.
- For specialist profiles, confirm their profile skills/SOUL.md identity are installed before starting the gateway.

Telegram cannot send a DM to a user until that user first presses **Start** or sends `/start` to the new bot. A `sendMessage` test returning `Bad Request: chat not found` means the user has not initiated the bot yet; it does not mean the token/gateway is broken.

Pairing is profile-scoped. If the user already has a known Telegram ID from the default profile, you can either ask them to message the new bot and approve the generated code, or seed the profile pairing store carefully at:

```text
~/.hermes/profiles/<profile>/pairing/telegram-approved.json
```

with shape:

```json
{
  "8178908137": {
    "user_name": "Arek Komorowski",
    "approved_at": 1780789180.0
  }
}
```

Keep file permissions restrictive (`0600`). Prefer the normal `hermes --profile <profile> pairing approve telegram <CODE>` flow when a code is available.

### Verify
```bash
curl -s "https://api.telegram.org/bot<token>/getMe" | python3 -m json.tool
```
Should return `"ok": true` with your bot's name/username.

## User Pairing — REQUIRED

Telegram bots **silently drop** messages from unpaired users. This is the #1 cause of "Telegram seems broken."

```bash
hermes pairing approve telegram <PAIRING_CODE>
```
- The pairing code is an 8-character alphanumeric string shown by BotFather after a user first messages your bot (or in the gateway logs)
- After approval, that user is recognized automatically on future messages
- Multiple users: run the command for each

### How to get the pairing code
- **From BotFather:** In the Telegram app, send any message to your bot, then BotFather shows a chat identifier. The pairing code may appear in gateway logs instead.
- **From gateway logs:** Check `~/.hermes/logs/gateway.log` for a pairing code or Telegram user alert.
- **Ask the user:** They can get their chat ID via @userinfobot on Telegram.

## Topic-Based Routing

Hermes **natively supports** topic-based routing for both DMs and groups. Each topic gets its own isolated session — no manual routing logic needed. Telegram sends `message_thread_id`/`thread_id` in the metadata automatically.

**DMs with topics:**
- DMs with topics do NOT support topic-based session isolation — private DMs between a user and a bot cannot create topics on Telegram
- Topics only work in groups/supergroups with "forum mode" enabled
- For isolated sessions in DMs, use Hermes's `dm_topics` config in `~/.hermes/config.yaml` instead

**Groups with topics (forum mode):**
- The group must have topics enabled first (Telegram group settings → create topic)
- Add the bot to the group via the Telegram UI (not via API)
- Each topic gets its own session automatically
- **Group chat ID** format: `-100` prefix followed by numeric ID (e.g., `-1002345678901`). Get it from Telegram Desktop (right-click group → info → chat ID).

**Do NOT propose workarounds** for threading unless you've confirmed the native feature is unavailable in this version.

## Configuration

### Config.yaml (`~/.hermes/config.yaml`)
```yaml
telegram:
  enabled: true              # set to true after setup
  reactions: false           # bot emojis reactions to received messages
  channel_prompts: {}        # channel-specific prompt overrides
  allowed_chats: ''          # comma-separated list of chat IDs (leave empty = allow all paired users)
```

### .env (`~/.hermes/.env`)
```bash
TELEGRAM_BOT_TOKEN=your-token-here
```

## Restricting Access

By default, any Telegram user who is **paired** can use the bot. To further restrict:

```yaml
# In config.yaml:
telegram:
  allowed_chats: "1234567890,9876543210"  # comma-separated chat IDs
```
This restricts access to specific chat IDs. Users not in this list (even if paired) are silently dropped.

## Commands & Features

- `/setdescription` — set bot description (send via BotFather)
- `/setabouttext` — set about section (via BotFather)
- `/setuserpic` — change profile picture (via BotFather)
- Bot can be added to groups — add it, mention @botusername, and respond in that group

## Troubleshooting

### Bots can't be invited via discord.gg links
Discord bot invites use OAuth2 URLs, not invite links. Telegram bots work differently — you give them the token and they connect.

### "Bot receives nothing" despite token being correct
- **Pairing not done:** `hermes pairing approve telegram <CODE>` is required for each user
- **enabled not true:** use the current profile-scoped key: `hermes --profile <profile> config set platforms.telegram.enabled true`
- **Gateway not restarted:** Changes require restart even after config update
- **Inherited home/allowed chat from cloned profile:** Clear `TELEGRAM_HOME_CHANNEL`, `TELEGRAM_HOME_CHANNEL_THREAD_ID`, `telegram.allowed_chats`, and `platforms.telegram.allowed_chats` until the new bot has its own chat. A `Bad Request: Chat not found` during startup commonly means the cloned profile tried to send to the old bot's home chat before the new bot was started by the user.
- **Inherited non-Telegram platforms from cloned profile:** Disable or clear Discord/WhatsApp settings if the specialist profile should only own Telegram. Otherwise gateway health can show token conflicts (`Discord bot token already in use`) or unpaired WhatsApp warnings that obscure the real Telegram status.
- **Status output includes recent health:** `hermes --profile <profile> gateway status` may show warnings from the previous run immediately after a restart. Verify with `hermes profile list`, `systemctl --user status hermes-gateway-<profile>`, and fresh `journalctl` lines.
- **Firewall/Network:** Telegram API (`api.telegram.org`) must be reachable
- **Bot not admin of group:** If the bot only sees @mentions, check if it's an admin (not just a member).

### "Bot only sees @mentions in groups" (CRITICAL BotFather gotcha)
All BotFather-created bots have `can_read_all_group_messages: false` by default. **This is a Telegram API restriction you cannot change on the bot after creation — no BotFather command enables it.** The bot will:
- ✓ Work perfectly in DMs
- ✓ Respond to @mentions in groups
- ✗ **NOT receive regular messages in groups** unless you add the bot as a group admin (Group Settings → Administrators → add bot as admin). Even then, it depends on the group type.

**If you need the bot to read all group messages without @mention:** you must add it as an admin and verify the bot gets the `can_read_all_group_messages` permission via `getChat` API. There is no BotFather way around this.

### "Config changes do nothing" (gag key pitfall)
`hermes config set` silently accepts any key but only writes valid ones. The config key for group chat authorization is `group_allowed_chats` (not `allowed_chats`). Valid keys:
- `platforms.telegram.allowed_chats` — chat-level authorization (response gate)
- `platforms.telegram.group_allowed_chats` — group-level authorization
- `platforms.telegram.dm_topics` — DM topic config array (for topic-based session isolation in DMs)

Use `hermes config edit` instead of guessing, or check the codebase for the correct field name.

### "Bot receives all messages from everyone"
- Set `allowed_chats` in config.yaml to restrict by chat ID
- Or manage per-user via pairing — only paired users work

### Token security
- Token grants full control of the bot — store only in `~/.hermes/.env`
- Telegram bot tokens use the HTTP API — no WebSocket required
- **Never** share the token in public channels or commits

### Gateway restart after changes
```bash
# Recommended for all Telegram config changes
systemctl --user restart hermes-gateway
```

### Verify configuration
```bash
# Check token is set
grep TELEGRAM_BOT_TOKEN ~/.hermes/.env

# Check enabled flag
grep -A5 "^telegram:" ~/.hermes/config.yaml

# Check gateway sees Telegram
hermes status | grep -i telegram
```

### Common Pitfalls
- **Forget the enable flag:** Setting the token alone is not enough — `gateway.telegram.enabled` must be `true`
- **Gateway not restarted:** Config changes live in memory; the gateway reads them at startup
- **Pairing required:** Without `hermes pairing approve telegram`, messages are silently dropped
- **allowed_chats vs pairing:** `allowed_chats` is an additional layer after pairing, not a replacement
- **Don't guess config keys:** Many Telegram config keys are not valid `hermes config set` keys — use `hermes config edit` or consult the codebase for the correct field name. Setting an invalid config key silently succeeds but does nothing.