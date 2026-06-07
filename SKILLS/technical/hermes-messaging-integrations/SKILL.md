---
name: hermes-messaging-integrations
description: "Class-level Hermes messaging integrations playbook: set up, configure, pair, restrict, and troubleshoot Telegram, Discord, and WhatsApp gateway channels."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [hermes, messaging, telegram, discord, whatsapp, gateway, integration]
    related_skills: [hermes-gateway, hermes-agent-installation]
---

# Hermes Messaging Integrations

## Overview

Use this umbrella skill when configuring or troubleshooting Hermes messaging platforms: Telegram, Discord, and WhatsApp. The shared class is: put secrets in the right place, enable the platform in gateway config, restart the gateway/bridge, pair or approve the channel/user, then verify inbound and outbound messages with logs.

Legacy full playbooks and session-specific notes are kept under `references/`:

- `references/telegram-integration.md`
- `references/discord-integration.md`
- `references/whatsapp-integration.md`
- `references/whatsapp-troubleshooting.md`
- `references/telegram-integration-pairing-mechanism.md`
- `references/telegram-integration-topic-target-format.md`
- `references/telegram-integration-url-to-chat-id.md`
- `references/whatsapp-integration-diagnostic-patterns.md`
- `references/whatsapp-integration-eaddrinuse-diagnostics.md`

## Universal Workflow

1. **Load Hermes docs/skills first** for current commands if behaviour changed.
2. **Separate secrets from config:** tokens/API keys belong in `~/.hermes/.env` via `hermes config set ...`; routing/channel settings belong in `~/.hermes/config.yaml`.
3. **Enable the platform** under gateway config and restart the gateway.
4. **Pair or approve the endpoint** before assuming messages are dropped.
5. **Verify both directions:** send a message from the platform, check gateway logs, then use Hermes send tools or platform-specific CLI/API to reply.
6. **Preserve topic/thread targeting:** when the source platform supports topics/threads, use the full target format including topic/thread IDs.

## Telegram

Use Telegram for lightweight mobile command/chat access and topic-based specialist routing.

Core setup:

```bash
hermes config set TELEGRAM_BOT_TOKEN <botfather-token>
hermes config set gateway.telegram.enabled true
hermes gateway restart
```

Important notes:

- Create the bot in BotFather; token format looks like `123456789:ABC...`.
- Dedicated Hermes profiles should normally get dedicated BotFather bots/tokens, not reuse the default profile token.
- User/channel pairing is required before messages are trusted.
- Topic delivery must preserve the topic/thread component: `telegram:<chat_id>:<topic_id>`.
- For URL-derived chat IDs and topic quirks, read `references/telegram-integration-url-to-chat-id.md` and `references/telegram-integration-topic-target-format.md`.

## Discord

Use Discord when Hermes needs to participate in servers/channels/threads.

Core setup:

```bash
hermes config set DISCORD_BOT_TOKEN <discord-bot-token>
hermes config set gateway.discord.enabled true
hermes gateway restart
hermes pairing approve discord <CHANNEL_CODE>
```

Important notes:

- Discord bot token is a secret; store it in `.env`, not as plain YAML channel config.
- Gateway config controls channel allowlists, mention requirements, and free-response channels.
- If a channel does not respond, first check pairing/approval and bot permissions in the guild.

## WhatsApp

Use WhatsApp when the user wants Hermes reachable through WhatsApp Web via the Node bridge.

Core diagnostics before changing config:

```bash
ps aux | grep whatsapp-bridge | grep -v grep
ps aux | grep "bridge.js --port" | grep -v grep
grep bridge_port ~/.hermes/config.yaml
curl -s http://127.0.0.1:<bridge_port>/health
```

Important notes:

- WhatsApp has a gateway process plus a Node bridge; both must agree on the bridge port.
- Config often needs both `whatsapp.bridge_port` and `whatsapp.extra.bridge_port` to match the actual bridge process.
- Common failures are stale QR/session, allowlist mismatch, bridge not running, and `EADDRINUSE` port conflicts.
- The bridge script lives in the Hermes Agent install/repo, not inside this skill package; if older instructions mention `the WhatsApp bridge.js file in the Hermes Agent repo`, resolve that path from the Hermes Agent installation.

## Troubleshooting Checklist

- [ ] `hermes gateway restart` completed after config changes
- [ ] `~/.hermes/.env` contains the token/key and `config.yaml` contains non-secret channel settings
- [ ] Pairing/approval is done for the exact user/channel/topic
- [ ] Gateway logs show platform adapter startup without auth errors
- [ ] Platform-specific bridge/process is running where required (WhatsApp)
- [ ] Delivery target preserves chat/thread/topic IDs

## Common Pitfalls

1. **Editing `.env` manually when `hermes config set` exists.** Prefer the CLI so reload semantics and quoting are handled consistently.
2. **Confusing gateway port with dashboard port.** Messaging adapters talk through gateway service/config; the web dashboard is a separate admin UI.
3. **Dropping topic/thread IDs.** A bare platform chat target may lose Telegram topic or Discord thread routing.
4. **Assuming WhatsApp is a pure token integration.** It depends on a live bridge and Web session, so process and port diagnostics matter.
