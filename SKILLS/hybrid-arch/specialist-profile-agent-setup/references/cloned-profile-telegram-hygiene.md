# Cloned profile hygiene for dedicated Telegram specialist bots

When a specialist profile is created by cloning `default`, the gateway can be active but not useful because inherited platform state points at the old agent.

## Symptoms

- `hermes profile list` / systemd show the specialist gateway as running.
- Bot receives messages but logs show `Unauthorized user: <id> on telegram`.
- Shutdown/restart logs show `telegram.error.BadRequest: Chat not found` because the cloned `TELEGRAM_HOME_CHANNEL` points to another bot/chat.
- `gateway status` reports Discord/WhatsApp warnings even after config keys were disabled.
- Telegram `sendMessage` to the user can return `403 Forbidden` if the user has not started or has blocked the bot; do not use that alone as proof the gateway is broken.

## Fix pattern

1. Verify actual receipt in service logs:

```bash
journalctl --user -u hermes-gateway-<name> -n 300 --no-pager | grep -iE 'telegram|unauthorized|pair|error'
```

2. Seed profile-scoped approval if Arek's Telegram ID is known and no pairing code is shown:

```json
{
  "8178908137": {
    "user_name": "Arek Komorowski",
    "approved_at": 1780789180.0
  }
}
```

Save as:

```text
~/.hermes/profiles/<name>/pairing/telegram-approved.json
```

Set mode `0600`.

3. Add allowlist when gateway is denying all unauthorized users:

```bash
TELEGRAM_ALLOWED_USERS=8178908137
```

This may need to be written to the profile `.env` directly if `hermes config set TELEGRAM_ALLOWED_USERS ...` only updates `config.yaml` in the current Hermes version.

4. Remove inherited platform env variables from the profile `.env`:

```text
DISCORD_BOT_TOKEN
DISCORD_HOME_CHANNEL
DISCORD_HOME_CHANNEL_THREAD_ID
DISCORD_ALLOWED_USERS
WHATSAPP_MODE
WHATSAPP_ALLOWED_USERS
WHATSAPP_ENABLED
TELEGRAM_HOME_CHANNEL
TELEGRAM_HOME_CHANNEL_THREAD_ID
```

Keep the specialist's own `TELEGRAM_BOT_TOKEN`.

5. Disable unrelated platforms in config:

```bash
hermes --profile <name> config set platforms.discord.enabled false
hermes --profile <name> config set platforms.whatsapp.enabled false
hermes --profile <name> config set telegram.allowed_chats ''
hermes --profile <name> config set platforms.telegram.allowed_chats ''
```

6. Disable cloned MCP servers that are not required for first contact:

```bash
hermes --profile <name> config set mcp_servers.linear.enabled false
hermes --profile <name> config set mcp_servers.graphthulhu.enabled false
hermes --profile <name> config set mcp_servers.notion.enabled false
```

7. Restart and verify from fresh logs:

```bash
systemctl --user restart hermes-gateway-<name>
sleep 3
hermes --profile <name> pairing list
hermes --profile <name> gateway status
journalctl --user -u hermes-gateway-<name> --since 'now - 2 minutes' --no-pager
```

8. Ask Arek to send a new `hi` in the dedicated bot DM. Only then call the setup verified.
