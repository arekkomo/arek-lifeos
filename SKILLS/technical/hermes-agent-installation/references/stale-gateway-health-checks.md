# Stale Gateway Health Checks

## The Problem

When the user fixes configuration (missing API key, wrong endpoint, etc.) and the gateway doesn't pick it up, the error persists because the gateway has a **live snapshot of the old config** from its startup time. Old processes keep serving stale health/status messages even after the root cause is fixed.

## Diagnostic Checklist

1. **Check if gateway restarted recently:**
   ```bash
   grep -i "starting\|exiting\|shutdown" ~/.hermes/logs/gateway.log | tail -5
   ```
   The timestamp should be **after** your fix was applied.

2. **Check config state at the time of fix:**
   ```bash
   # Did the API key actually make it to .env?
   grep -i KEY ~/.hermes/.env | head -5
   
   # Does config.yaml have the right provider?
   grep -A3 "custom_providers" ~/.hermes/config.yaml
   ```

3. **Cross-reference timestamps:** If the gateway's last restart is **before** your fix time — the gateway is the problem, not your config.

4. **Restart and verify:**
   ```bash
   systemctl --user restart hermes-gateway
   sleep 5
   hermes doctor
   ```

## Common Root Causes

- **Gateway was started before user made fixes** — the most common cause
- **`.env` changes not visible** — Hermes reads `.env` at startup; mid-run `export` doesn't help
- **Config edits didn't save** — always verify the file content matches your expectation
- **Wrong config file edited** — profiles have their own `config.yaml` at `~/.hermes/profiles/<name>/config.yaml`

## When This Gets Confusing

This often creates a feedback loop:
1. User sees "no AI backend" error
2. User fixes `.env` — but gateway doesn't restart
3. User asks agent, agent runs `hermes doctor` which reads the **same stale gateway state**
4. Agent concludes "still broken" and suggests more fixes
5. User fixes again — still same stale gateway

**Solution in every session: restart the gateway before diagnosing, and always check the gateway's restart timestamp against your fix timestamp.**
