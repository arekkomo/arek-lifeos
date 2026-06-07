# Hybrid Install Diagnosis

## When a component is running from what?

On Debian with externally-managed Python, hermes can end up installed in multiple locations:

1. **System pip** (`~/.local/bin/hermes`) — the dashboard UI uses this.
2. **Venv** (`~/.hermes/hermes-agent/venv/bin/python`) — the gateway uses this.
3. **Docker** — if hermes runs in a container, check with `docker ps | grep hermes`.

## Quick check script

```bash
echo "=== Which python runs hermes? ==="
which hermes
hermes --version 2>/dev/null || hermes_cli --version 2>/dev/null || true

echo "=== Is the dashboard using venv or pip? ==="
ps aux | grep "hermes dashboard" | grep -v grep

echo "=== Is the gateway using venv or pip? ==="
ps aux | grep "hermes_cli.main gateway" | grep -v grep

echo "=== Any Docker containers? ==="
docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Status}}" | grep -i hermes || echo "no docker containers"

echo "=== venv version ==="
cd ~/.hermes/hermes-agent && source venv/bin/activate && pip show hermes-agent 2>/dev/null | grep Version

echo "=== system pip version ==="
pip3 show hermes-agent 2>/dev/null | grep Version
```
