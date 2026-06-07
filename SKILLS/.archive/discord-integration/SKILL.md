---
name: discord-integration
description: Manage Discord bot authentication, pairing channels, token rotation, and bot restart within Hermes. Includes bot token management, channel approval, and gateway restart.
---

# Discord Integration

## Token Management

### Update Bot Token
Hermes stores the Discord bot token in `~/.hermes/.env` under `DISCORD_BOT_TOKEN`.

```bash
# 1. Paste the bot token into .env (terminal)
echo "DISCORD_BOT_TOKEN=<new-token-here>" >> ~/.hermes/.env

# 2. Restart the gateway (systemd)
systemctl --user restart hermes-gateway

# 3. Verify
hermes status | grep -A5 "Discord"
```

**Note:** Discord bot tokens are **not** stored in `~/.hermes/config.yaml` — they go in `.env`. Config only has channel settings (require_mention, allowed_channels, free_response_channels, etc.).

### Token Format
Discord bot tokens start with `M...` (base64-like string, typically ~72 chars). Validate format before saving.

## Channel Pairing

### Approve a Channel
```bash
hermes pairing approve discord <CHANNEL_CODE>
```

Example: `hermes pairing approve discord SJMEXTZR`

This allows users from that Discord channel to interact with the bot. They'll be recognized automatically on their next message.

### Restarting for Changes
After updating tokens or configuration, always restart the gateway:
```bash
systemctl --user restart hermes-gateway
```

### Verification
Check status after restart:
```bash
hermes status
```

Discord should show ✓ configured when the token is valid.

### Common Pitfalls
- **Token in wrong file:** Discord bot tokens go in `.env`, NOT `config.yaml`. Config only stores channel settings.
- **Token format:** Bot tokens are base64-like strings starting with `M...`. If the string looks different (e.g., a short code), it may be a channel code, not a bot token.
- **Changes not taking effect:** Config/file changes require a gateway restart via `systemctl --user restart hermes-gateway`.
- **Channel codes vs tokens:** Channels have short codes (e.g., `SJMEXTZR` — 8 letters), tokens are long (70+ chars). Don't confuse them.