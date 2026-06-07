# Desktop App Remote Connection Reference

## Session Token Pitfall (2026-06-04)

**CRITICAL: Session tokens are machine-scoped.** Tokens extracted from the dashboard on Spark (localhost) cannot be reused from a remote Desktop app on the user's Mac, even on the same LAN. The token is tied to the machine that received the page.

**Correct procedure:**

1. Open `http://<spark-ip>:9119` in the **remote browser** (Mac, not Spark)
2. Open DevTools → Network tab → reload page
3. Click the HTML document request → Response tab
4. Find `__HERMES_SESSION_TOKEN__="..."` and copy the full value between quotes
5. Paste into Desktop App's "Session token" field
6. Click "Save and reconnect"

**Never** try to extract the token from the server's own browser or curl endpoint — the per-machine session-scoped token won't work remotely. You must extract it from the browser on the remote machine.

## Port Identification Quick Reference

| Port | Service | Desktop App Should Use? |
|------|---------|-------------------------|
| 9119 | Hermes Dashboard/Gateway | **YES** — the target |
| 8080 | SearXNG (metasearch) | **NO** — wrong service entirely |
| 11434 | Ollama | **NO** — model inference only |
| 3000 | Open WebUI | **NO** — separate service |

**Rule of thumb:** If the URL resolves to SearXNG or any non-Hermes service, the Desktop app's connection buttons will grey out silently with no useful error. Always verify the service responds before trying to connect.
