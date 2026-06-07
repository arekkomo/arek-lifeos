---
name: hermes-agent-installation
domain: technical
version: 1.2
description: Installing, repairing, and troubleshooting Hermes Agent installation — broken wheels, editable pth persistence, platform module checks, config reload pitfalls, and dependency fixes.
updated: 2026-06-06
---

# Hermes Agent Installation & Repair

> **Status:** Active  
> **Last Updated:** 2026-06-06

## Critical Workflow: Check Docs Before Troubleshooting

**When facing ANY setup/config/troubleshooting issue:**

1. **ALWAYS load hermes-agent skill first** — `skill_view(name='hermes-agent')`
2. **Check the skill's `references/` directory** for relevant troubleshooting guides  
3. **Read the docs folder** in the hermes-agent repo for the specific feature you're working on
4. Check logs (`~/.hermes/logs/gateway.log`, profile logs) for exact error messages
5. Only THEN try fixes

**Why this matters:** Guessing commands leads to wrong fixes and endless loops. The docs have the authoritative commands and known pitfalls for every feature.

**Failure signals:** If the user says "check docs first" or "are you going in circles" — immediately stop guessing, load the skill, and read the docs carefully.

## Broken Wheel Detection

When `pip install hermes-agent[messaging]` completes but platform adapters fail to load:

**Check the wheel integrity:**
```bash
cat /home/realityrove/.local/lib/python3.12/site-packages/hermes_agent-*.dist-info/RECORD
```

If RECORD contains only metadata lines (RECORD, WHEEL, METADATA, etc.) with zero `.py` entries, the wheel is corrupted — it contains no source code despite completing successfully.

**Fix:** Clone from git and install directly:
```bash
cd /tmp
git clone https://github.com/nousresearch/hermes-agent.git
cd hermes-agent
pip install --break-system-packages .[messaging]
```

## Editable pth File Persistence

When uninstalling a package, the editable pth file and finder module remain behind and continue redirecting imports.

**Symptoms:**
- Package uninstalled but `pip list` still shows it
- Gateway platform code finds files from wrong directory (e.g., `/tmp/`)
- Editable pth path pointing to transient locations

**Always clean up after uninstall:**
```bash
# Uninstall first
pip uninstall hermes-agent -y --break-system-packages

# Then remove leftover editable artifacts
rm -f /home/realityrove/.local/lib/python3.12/site-packages/__editable__*.pth
rm -f /home/realityrove/.local/lib/python3.12/site-packages/__editable___hermes_agent_*_finder.py
rm -f /home/realityrove/.local/lib/python3.12/site-packages/__pycache__/__editable__*.cpython-*.pyc

# Now install fresh
pip install --break-system-packages .[messaging]
```

## Platform Module Availability Check

After a fresh install, verify platform modules are importable:
```bash
/usr/bin/python3 -c "import gateway.platforms.whatsapp; print('OK')"
/usr/bin/python3 -c "import gateway.platforms.discord; print('OK')"
```

If either fails with `ModuleNotFoundError`:
1. Check the package path: `/home/realityrove/.local/lib/python3.12/site-packages/gateway/platforms/`
2. Verify the gateway platform files exist (whatsapp.py, discord.py)
3. Reinstall the package — missing platform modules indicate an incomplete install

## Common Dependency Fixes

**`No module named 'aiohttp'`** (gateway crashes on WhatsApp platform init):
```bash
/usr/bin/python3 -m pip install --break-system-packages aiohttp
```

**`ModuleNotFoundError: No module named 'hermes_agent'`**:
The PyPI wheel's top-level module name is `agent`, not `hermes_agent`. Gateway imports still use `hermes_agent`. After a fresh install from source:
```bash
/usr/bin/python3 -c "import agent; print('OK')"  # Should work
/usr/bin/python3 -c "import hermes_agent; print('OK')"  # May still fail
```
The gateway handles this internally via its plugin system if installed correctly.

## Installation Verification Checklist

After any hermes-agent install:
1. `[ ]` Wheel contains source: `RECORD` has `.py` entries (not just metadata)
2. `[ ]` No leftover editable pth: no `__editable__*.pth` files remain
3. `[ ]` Platform modules importable: `gateway.platforms.whatsapp` and `gateway.platforms.discord` import without error
4. `[ ]` All platform dependencies present: aiohttp, discord.py, discord.py[voice], brotlicffi
5. `[ ]` Gateway can load platforms: `hermes status` shows configured platforms
6. `[ ]` Bridge processes running: `ps aux | grep whatsapp-bridge` shows your bridge

## Port & Bridge Path Diagnostics

See: `references/platform-module-detection.md` for platform discovery path bugs.

## Server Maintenance Pitfalls

See: `references/server-maintenance-pitfalls.md` for SSH disconnect patterns (netplan over WiFi kills connections), SSH keepalive setup, firmware update workflows, and zombie process checks.

## Hybrid Install Pitfall: Gateway vs Dashboard Version Mismatch

Hermes can end up as a **hybrid install** — gateway running from a venv copy of hermes-agent, dashboard running from the system-pip copy. These can have **different versions** and different platform dependencies.

**Symptom:** Features work in dashboard but not in gateway (or vice versa). Gateway log shows import errors despite dashboard UI showing "up to date."

**Verify:** Run both checks:
```bash
# venv copy
cd ~/.hermes/hermes-agent && source venv/bin/activate && pip show hermes-agent | grep Version
# system-pip copy (dashboard)
pip3 show hermes-agent | grep Version
```

If versions differ, the dashboard UI's "Update" button only updates one of them. You need to update **both**:
```bash
# Update venv copy
cd ~/.hermes/hermes-agent && source venv/bin/activate && pip install --upgrade hermes-agent
# Update system-pip copy (dashboard)
uv pip install --upgrade hermes-agent
```

**Always restart the gateway after updating.** The gateway snapshots config at startup and won't pick up new code until restarted:
```bash
systemctl --user restart hermes-gateway
```

### Dashboard Update Button Fails on Debian (System Pip Copy)

The dashboard runs from `~/.local/bin/hermes` (system-pip copy), which on Debian blocks `uv pip install --system`.

**Symptom:** Clicking "Update" in the Dashboard UI shows:
> "error: No virtual environment found... Virtual environments were not considered due to the --system flag"

**Root cause:** The dashboard's update button uses `uv pip install --system` which Debian rejects. The gateway may be on the latest version (venv copy), but the dashboard's system-pip copy is stale.

**Fix: Update the system-pip copy directly:**
```bash
# Update ONLY the dashboard's copy (system pip):
/usr/bin/python3 -m pip install --break-system-packages --user --upgrade hermes-agent

# Verify:
/home/realityrove/.local/bin/hermes --version
```

**Verify dashboard is now current:** Refresh the dashboard UI — it should show the latest version and no "Update available" banner.

> **Note:** The "Update available: 88 commits behind" message is a known quirk of `uv pip install --system` on Debian. It's misleading — PyPI shows the latest release version, so if that matches, you're up to date. This will be fixed server-side eventually.

### Update via Terminal (Direct Pip Installs)

If hermes is installed directly via pip (not inside a venv), `hermes update` may hang waiting for interactive confirmation you can't see over SSH/remote sessions.

**Fast fix — no interaction needed:**
```bash
uv pip install --upgrade hermes-agent
```

This works non-interactively and doesn't hit the Debian externally-managed Python restriction since `uv` manages its own resolver. After updating, **restart the Dashboard** if it was running:
```bash
hermes dashboard --port 9119
```

**Verify:** `pip show hermes-agent | grep Version`

**Debian workaround if above still fails (e.g. `uv` insists on a venv):**
```bash
/usr/bin/python3 -m pip install --break-system-packages --user --upgrade hermes-agent
```
This explicitly bypasses the externally-managed check and installs to `~/.local/` rather than `/usr/`.

### Consolidating Hybrid Install to Single Venv

When you have a hybrid setup (system-pip for dashboard + venv for gateway) and want to migrate everything to the authoritative venv:

**Steps:**
1. `uv pip install fastapi uvicorn` in the venv (for the dashboard web framework)
2. `cd ~/.hermes/hermes-agent && source venv/bin/activate && pip install -e .` (reinstall from source into venv)
3. Update systemd service (`hermes-gateway.service` and optionally `hermes-dashboard.service`) to use `venv/bin/python` instead of `/usr/bin/python3`
4. Update `~/.bashrc` alias: `alias hermes="/home/realityrove/.hermes/hermes-agent/venv/bin/hermes"`
5. Uninstall the system-pip copy: `pip uninstall hermes -y` (removes `~/.local/bin/hermes`)
6. Restart both services

**Verify after:**
```bash
# Both should point to the same venv
which hermes                    # Should be in venv
hermes --version                # Should show consistent version
hermes status                   # Gateway should start cleanly
```

### Dashboard Stops After Update

**Symptom:** Desktop app shows "cannot connect" or reverts to `127.0.0.1:9119` despite entering a remote URL. Curl confirms `10.0.0.61:9119` returns HTTP 200 — network is fine.

**Root cause:** An outdated Desktop app silently reverts to localhost fallback when the remote URL fails to apply or persist. This is NOT a network failure.

**Fix:** **Always update the Desktop app binary first.** Then re-enter the Remote URL + fresh session token from the browser dashboard (`Ctrl+U` → search `HERMES_SESSION_TOKEN`).

## Dashboard Stops After Update

After a hermes update (git pull + pip install), the **Dashboard process is killed** — the Desktop app is essentially the Dashboard in Electron form, so it will show "cannot reach gateway" after any update.

**Always restart the Dashboard after updating:**
```bash
hermes dashboard --port 9119
```

If you need remote access:
```bash
# SSH tunnel (safer):
ssh -L 9119:127.0.0.1:9119 user@spark
hermes dashboard --port 9119

# Or direct bind on trusted network:
hermes dashboard --host 0.0.0.0 --port 9119 --insecure
```

> **See:** `hermes-gateway` skill → the `hermes-gateway` skill's desktop remote connection reference for full remote setup guide.

## Changes Not Taking Effect Without Restart

Hermes Gateway **does not reload config or `.env` on-the-fly**. It takes a snapshot of `config.yaml` and `.env` at startup. If you fix a configuration issue but the problem persists, the gateway is likely still running with the **old snapshot**.

**Symptom:** You fixed `config.yaml` or `.env`, but `hermes doctor` or DM messages still show the same errors.

**Fix:** Restart the gateway:
```bash
systemctl --user restart hermes-gateway    # or: hermes gateway restart
```

**Verification after restart:**
1. Check gateway logs for a new startup entry: `grep "Starting\|Gateway" ~/.hermes/logs/gateway.log | tail -3`
2. Confirm the new timestamp matches your fix time
3. Re-run `hermes doctor` — it should now show success

**See:** `references/stale-gateway-health-checks.md` for the full diagnostic checklist.

## Profile, MCP, and Local Provider Troubleshooting

This skill is now the umbrella for Hermes installation/repair plus common profile, MCP, and local-provider setup failures. The former narrow skills have been preserved as reference files:

- `references/hermes-profile-troubleshooting.md`
- `references/notion-mcp-setup.md`
- `references/ollama-troubleshooting.md`
- `references/ollama-troubleshooting-hermes-model-recommendations.md`

### Profile diagnostics

When a named profile fails to start or does not load expected skills/tools:

1. Check old profile processes: `pgrep -fa 'hermes.*<profile>'`.
2. Check the profile config and `.env` under `~/.hermes/profiles/<name>/`.
3. Confirm profile skills are listed in profile `config.yaml`; use `/reload-skills` or restart the gateway after edits.
4. For MCP servers, verify the auth format exactly matches the Hermes docs; Notion MCP auth has historically required `auth: "token"` as a string, not a nested dict.

### Notion MCP setup

Use Notion MCP when Hermes needs workspace/database access through Notion's remote MCP server. Distinguish Notion auth systems before debugging:

- **Connections/OAuth** (`ntn_...`) are for Notion MCP and OAuth apps.
- **Legacy integrations** (`secret_...`) are for the Notion API/bot-token style.
- `mcp.notion.com` may return 404 before authentication; create/connect the Notion connection first.

### Ollama/local provider issues

Ollama issues belong to the Hermes provider/installation class because most failures are config or process mismatch, not model reasoning failures. Diagnose with:

```bash
curl -s http://localhost:11434/api/tags | python -m json.tool
curl -s -d '{"model":"qwen3.6:latest","prompt":"Say hello","stream":false}' http://localhost:11434/api/generate
hermes doctor
grep -E "error|fail|timeout|provider" ~/.hermes/logs/gateway.log | tail -15
```

Common fixes: restart gateway after config changes, ensure `providers:` names match `custom_providers`, and verify Hermes points at the actual Ollama endpoint/port.
