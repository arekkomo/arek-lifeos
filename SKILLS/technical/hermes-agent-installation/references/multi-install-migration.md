# Multi-Install Migration — Consolidating to a Single Venv

## When to Run This

You have hermes running from multiple sources (system-pip, venv, docker) and need to consolidate into one authoritative install.

## Step 1: Inventory All Installs

```bash
# Which python runs the dashboard?
ps aux | grep "hermes dashboard" | grep -v grep

# Which python runs the gateway?
ps aux | grep "hermes_cli.main gateway" | grep -v grep

# Any Docker hermes containers?
docker ps --format "table {{.Names}}\t{{.Image}}" | grep -i hermes

# List all hermes-related files
ls ~/.local/bin/hermes 2>/dev/null
ls ~/.hermes/hermes-agent/venv/bin/hermes 2>/dev/null
ls /usr/local/bin/hermes 2>/dev/null
pip3 show hermes-agent 2>/dev/null | grep Location
```

## Step 2: Audit Versions

```bash
echo "=== System-pip version ==="
pip3 show hermes-agent 2>/dev/null | grep Version

echo "=== Venv version ==="
cd ~/.hermes/hermes-agent && source venv/bin/activate && pip show hermes-agent 2>/dev/null | grep Version

echo "=== Gateway running version ==="
ps aux | grep "hermes_cli.main gateway" | grep -v grep
```

If versions differ, features may work in one component but not another.

## Step 3: Ensure Venv is Ready

```bash
# Create/verify venv
cd ~/.hermes/hermes-agent
python3 -m venv venv 2>/dev/null || true  # skip if exists
source venv/bin/activate

# Install uv and dashboard deps
pip install uv fastapi uvicorn

# Install hermes from source
pip install -e .
```

## Step 4: Update the Gateway to Use the Venv

If the gateway systemd service uses a wrong interpreter:

```bash
# Check current service file
systemctl --user show hermes-gateway | grep ExecStart
cat ~/.config/systemd/user/hermes-gateway.service
```

Update the ExecStart to point at the venv python, and ensure it runs hermes from venv:

```ini
[Service]
ExecStart=/home/realityrove/.hermes/hermes-agent/venv/bin/python -m hermes_cli.main gateway run --replace
```

Then:
```bash
systemctl --user daemon-reload
systemctl --user restart hermes-gateway
```

## Step 5: Choose What Runs the Dashboard

**Option A: Run from the venv directly** (dashboard + gateway same install)

```bash
hermes dashboard --host 0.0.0.0 --port 9119 --insecure
```

**Option B: Run dashboard as a separate systemd service**

Create `~/.config/systemd/user/hermes-dashboard.service`:

```ini
[Unit]
Description=Hermes Agent Dashboard
After=network.target

[Service]
Type=simple
ExecStart=/home/realityrove/.hermes/hermes-agent/venv/bin/python -m hermes_cli.main dashboard --host 0.0.0.0 --port 9119 --insecure
Restart=always
RestartSec=10

[Install]
WantedBy=default.target
```

```bash
systemctl --user daemon-reload
systemctl --user enable --now hermes-dashboard
```

> Note: Dashboard is typically run manually, not as a systemd service. If auto-start is needed, copy the example above.

## Step 6: Remove Conflicting Installs

```bash
# Uninstall the old system-pip copy
pip3 uninstall hermes-agent -y --break-system-packages

# Remove old binaries
rm -f ~/.local/bin/hermes
rm -f /usr/local/bin/hermes

# Remove any abandoned venvs (never used)
rm -rf ~/.venvs/hermes

# Clean up editable artifacts
rm -f ~/.local/lib/python3.12/site-packages/__editable__*.pth
rm -f ~/.local/lib/python3.12/site-packages/__editable___hermes_agent_*_finder.py
rm -f ~/.local/lib/python3.12/site-packages/__pycache__/__editable__*.cpython-*.pyc
```

## Step 7: Verify

```bash
# Confirm single install
pip3 show hermes-agent | grep Location
ps aux | grep "hermes dashboard" | grep -v grep
ps aux | grep "hermes_cli.main gateway" | grep -v grep
hermes --version

# Gateway still responds to messages?
# Dashboard shows latest version?
```

## Session Reference

Session on 2026-06-05 consolidated three conflicting installs (system-pip, venv, unused `~/.venvs/hermes`) into a single `~/.hermes/hermes-agent/venv` authoritative install. Dashboard runs manually from venv; gateway runs via systemd. Alias added to `~/.bashrc`: `alias hermes="/home/realityrove/.hermes/hermes-agent/venv/bin/hermes"`.
