# Bridge Log JSON Diagnostic Patterns

When WhatsApp says "no reply" but the bridge *appears* connected, the bridge log's JSON events tell you exactly what's wrong.

## Common JSON Events & What They Mean

### {event: "ignored", reason: "self_chat_mode_rejects_non_self"}
**Meaning:** Bridge is in self-chat mode but you're trying to send a message to someone else. Normal — not an error.

### {event: "ignored", reason: "allowlist_mismatch", chatId: "XXXXXX@lid"}
**Meaning:** The sender is NOT in `WHATSAPP_ALLOWED_USERS` in `.env`.
**Fix:** Add the sender's phone number to `WHATSAPP_ALLOWED_USERS` in `~/.hermes/.env`, then restart gateway.

### {reason: "device_removed", type: "conflict"}
```
{"tag":"conflict","attrs":{"type":"device_removed"}}
❌ Logged out. Delete session and restart to re-authenticate.
```
**Meaning:** A *new* WhatsApp pair happened (via `hermes whatsapp`), which revoked the old session. Also happens if WhatsApp detects the session on a different device.
**Fix:** 
1. `rm -rf ~/.hermes/whatsapp/session`
2. `hermes whatsapp` to create a fresh session and re-scan QR code.

### {"level":40, "msg":"Timeout in AwaitingInitialSync, forcing state to Online..."}
**Meaning:** Bridge connected but WhatsApp's sync took a while. The session *is* online — not a real timeout. Normal on first connect. **Ignore this message.**

### {"level":50, ... "reasonNode":{"tag":"stream:error"}}
**Meaning:** Stream/connection was forcibly closed. Usually a network issue or WhatsApp server-side. If it keeps repeating, check your internet or try re-pairing.

## Other JSON Patterns

- **`"code":"401"`** in stream:error → Auth failure. Delete session and re-pair.
- **`"reasonNode":{"tag":"conflict"}`** → Another device took over. Delete session and re-pair.

## Quick Diagnostic Commands

```bash
# Show all JSON error-like events
grep -E '"reason"|"event"' ~/.hermes/whatsapp/bridge.log | python3 -m json.tool 2>/dev/null | grep -v -B1 "^--$" | grep -E "event.*reason|level.*[40-50]"

# Show only the last 5 events
tail -100 ~/.hermes/whatsapp/bridge.log | grep -E '{"event"|"reason"' | tail -5

# Check if bridge is connected (not just "listening")
grep "connected" ~/.hermes/whatsapp/bridge.log | tail -1
```

## Key Rule

**"Connected" in the log ≠ "working for you."** The bridge can be connected but still drop your messages because of:
1. Port mismatch (config vs actual bridge port)
2. Allowlist not including your sender number
3. Wrong bridge user (another Linux user's bridge, not yours)

Always verify all three in sequence.