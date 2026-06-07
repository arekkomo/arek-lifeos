# Pairing Mechanism

Hermes uses a **pairing** system for all messaging platforms to prevent unauthorized users from interacting with the bot.

## General Pattern

```bash
hermes pairing approve <platform> <PAIRING_CODE>
```

- **Pairing codes** are typically 8-character alphanumeric strings  
- Each user/chat gets their own pairing code  
- After approval, that user is recognized automatically on their next message  
- Check current pairings: `hermes pairing list`

## Platform-Specific Notes

### Telegram
- Codes appear in BotFather when a user first messages the bot
- Also appears in gateway logs at `~/.hermes/logs/gateway.log`
- Can get chat ID via @userinfobot on Telegram
- For a DM, the 8-char code is the pairing code — use it as-is

### Discord
- Channel codes (8 letters) used for approving channels
- `hermes pairing approve discord <CODE>`

### WhatsApp
- Phone numbers / chat IDs used as pairing codes
- Also requires bridge allowlist in `.env`

## Key Points
- **Pairing is required on ALL platforms** — it's not optional
- Messages from unpaired users are silently dropped
- Pairing is per-user, not global (except for `allowed_chats` which acts as a secondary filter)
- After pairing a user, no restart needed — they work immediately on their next message