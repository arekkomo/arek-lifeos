# Session Notes

## Session 2026-06-04: Dashboard Deployment on Spark

### Context
- User runs Hermes on a DGX Spark machine (server at 10.0.61)
- User accesses from Mac laptop on same LAN
- User tried the Hermes Desktop App (Apple) — it bundles its own full gateway/agent, can't skip to connect to an existing instance
- User needed the standalone dashboard accessible from Mac

### What Worked
1. Source is at `~/.hermes/hermes-agent/web/` with npm/node_modules already installed
2. Built with `cd ~/.hermes/hermes-agent/web && npm run build`
3. Dashboard started with `python3 -m hermes_cli.main dashboard --host 0.0.0.0 --port 9119 --insecure --no-open`
4. Server binds to 0.0.0.0 (all interfaces) for LAN access

### Pitfalls Found (now in SKILL.md)
- The `--skip-build` flag FAILED because web_dist wasn't pre-built
- Default host is localhost only — must explicitly set `--host` for LAN access
- `--insecure` is required to bypass OAuth gate when no providers are configured

### Environment
- Ollama at 10.0.15:11434 (custom_provider for Qwen 3.6)
- Gateway running on :8080 (Telegram/Discord)
- Dashboard on :9119 (new deployment)
- User: realityrove
