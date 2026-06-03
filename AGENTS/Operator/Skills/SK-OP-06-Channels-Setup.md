# SK-OP-06 — Claude Code Channels Setup

Connect Arek & Co to Telegram, Discord, or iMessage so you can fire tasks from your phone.

**Status:** Not yet configured
**Requires:** Bun runtime (not yet installed), Claude Pro/Max subscription ✅

---

## Step 1 — Install Bun

Run this in Terminal:

```bash
curl -fsSL https://bun.sh/install | bash
```

Verify: `bun --version`

---

## Option A — Telegram (Recommended)

Most reliable. Works on all devices. Creates a private bot only you control.

### 1. Create your bot

Open Telegram → search **BotFather** → send `/newbot`
- Give it a name (e.g. "Arek Operator")
- Username must end in `bot` (e.g. `arekoperator_bot`)
- Copy the token BotFather gives you

### 2. Install the plugin

In a Claude Code session:

```
/plugin marketplace add anthropics/claude-plugins-official
/plugin install telegram@claude-plugins-official
/reload-plugins
```

### 3. Configure your token

```
/telegram:configure <paste-token-here>
```

### 4. Start Claude Code with channel enabled

```bash
claude --channels plugin:telegram@claude-plugins-official
```

### 5. Pair your account

- Open Telegram → send any message to your bot
- Bot replies with a pairing code
- Back in Claude Code: `/telegram:access pair <code>`
- Lock it down: `/telegram:access policy allowlist`

**Done.** Message your bot from any device → Arek & Co responds.

---

## Option B — iMessage (Easiest — no bot needed)

macOS only. Uses your existing Messages app. No external service.

### 1. Grant Full Disk Access

**System Settings → Privacy & Security → Full Disk Access → add Terminal (or iTerm)**

### 2. Install plugin

```
/plugin install imessage@claude-plugins-official
/reload-plugins
```

### 3. Start with channel

```bash
claude --channels plugin:imessage@claude-plugins-official
```

### 4. Test

Text yourself from any Apple device → Claude responds.

Click **OK** when macOS asks if Terminal can control Messages.

---

## Option C — Discord

### 1. Create bot

- Go to [discord.com/developers/applications](https://discord.com/developers/applications)
- New Application → Bot section → Reset Token → copy it
- Enable **Message Content Intent** under Privileged Gateway Intents
- OAuth2 → URL Generator → scope: `bot` + permissions: View/Send/Read Messages, Attach Files, Add Reactions
- Open generated URL to invite bot to your server

### 2. Install & configure

```
/plugin install discord@claude-plugins-official
/reload-plugins
/discord:configure <token>
```

### 3. Start with channel

```bash
claude --channels plugin:discord@claude-plugins-official
```

### 4. Pair

- DM your bot in Discord → it replies with a pairing code
- `/discord:access pair <code>`
- `/discord:access policy allowlist`

---

## Running persistently (optional)

For always-on access while your Mac is awake, run Claude in a persistent terminal session:

```bash
# In iTerm or Terminal, keep a dedicated tab:
claude --channels plugin:telegram@claude-plugins-official
```

Or add it to a scheduled startup via launchd if you want it to auto-start.

---

## What you can do from phone once connected

- "Morning briefing" → get your daily brief pushed back
- "Add task: [x]" → routes to appropriate agent
- "What's on my plate today?" → Operator checks reminders/calendar
- "Journal" → runs journal session remotely
- Any capture (idea, link, voice note) → Operator routes it

---

## Source

[Claude Code Channels Docs](https://docs.anthropic.com/en/docs/claude-code/channels)
