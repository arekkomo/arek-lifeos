---
name: notion-integration
domain: technical
version: 3.0
description: Connect Notion MCP server to Hermes via OAuth. Includes setup, configuration, CLI commands, and troubleshooting.
updated: 2026-05-31
---

# Notion Integration (Hermes)

> **Status:** Active  
> **Last Updated:** 2026-05-31

## Notion Auth Systems

Notion has **three separate auth systems** that are often confused:

| System | Location in UI | Token format | Use case |
|--------|------------|--------------|----------|
| **Connections** (OAuth) | Settings & Members → Connections tab | `ntn_xxx` | Notion MCP, OAuth apps |
| **Integrations** (tokens) | Settings & Members → Integrations page | `secret_xxx` or `ntn_xxx` | API tokens, bot tokens |
| **People** | Settings & Members → People tab | N/A | Human members ONLY |

**CRITICAL:** Connections and Integrations live under their own tabs — NEVER under People. You cannot manage them from the People tab.

## Notion MCP Server — Setup

### 1. Get OAuth token from Notion
Go to https://mcp.notion.com in browser, sign in with Notion, and copy the access token. This creates a **Connection** automatically.

### 2. Add the MCP server to Hermes
**Recommended approach (CLI):**
```bash
hermes mcp add notion --url https://mcp.notion.com/mcp
```

Interactive prompts:
- Name: confirm "Notion MCP"
- "Does this server require authentication?": **Y**
- Auth method: **token**
- Token value: paste `ntn_...` token exactly

**Manual config.yaml approach:**
Append to `~/.hermes/config.yaml`:
```yaml
mcp_servers:
  notion:
    name: Notion MCP
    url: https://mcp.notion.com/mcp
    transport: streamable_http
    auth:
      token: env:NOTION_MCP_TOKEN
```
**⚠️ CRITICAL:** Do NOT wrap this under a `config:` key. It goes directly under `mcp_servers:` at the top level.

### 3. Create .env with the token
```bash
echo "NOTION_MCP_TOKEN=ntn_xx..." >> ~/.hermes/.env
chmod 600 ~/.hermes/.env
```

### 4. Ensure MCP HTTP transport is available
If connection fails with "requires HTTP transport but mcp.client.streamable_http is not available":
```bash
pip3 install --upgrade mcp --break-system-packages
```

### 4a. Install Hermes MCP extras (BUNDLED PYTHON CLIENT)
Hermes **bundles its own MCP Python client** — it does NOT use the system `mcp` pip package.
To enable MCP transport in Hermes, install the MCP extras:
```bash
pip3 install 'hermes-agent[mcp]' --break-system-packages
```
Without this, Hermes will report "requires HTTP transport but mcp.client.streamable_http is not available" regardless of the system `mcp` version. Verifying the install:
```bash
python3 -c "import hermes.agent.mcp; print('MCP support available')"
```

### 4b. Alternative: Use npx/stdio-based Notion MCP (when hosted streamable_http fails)
If `https://mcp.notion.com/mcp` returns 401 but the token works against Notion REST (`/v1/users/me`), use the official local stdio server. This works with a Notion integration/API token stored in `.env`.

Config shape verified with Hermes:
```yaml
mcp_servers:
  notion:
    command: npx
    args:
      - -y
      - '@notionhq/notion-mcp-server'
      - --transport
      - stdio
    env:
      NOTION_TOKEN: ${NOTION_MCP_TOKEN}
      OPENAPI_MCP_HEADERS: '{"Authorization":"Bearer ${NOTION_MCP_TOKEN}","Notion-Version":"2022-06-28"}'
    enabled: true
    name: Notion MCP (local stdio)
    timeout: 120
    connect_timeout: 60
```

Verify:
```bash
hermes mcp test notion
hermes --profile coach mcp test notion
```
Expected: `Transport: stdio → npx`, `✓ Connected`, and Notion API tools discovered.

### 5. Test the connection
```bash
hermes mcp test          # Tests connectivity
hermes mcp list          # Shows tools/status
```
If "notion" shows as **✗ disabled**, the MCP version is too old or auth failed.

## Pitfalls

### CLI commands
- `hermes mcp add` requires `--url` flag — `--name` does NOT exist
- Run `hermes mcp add <name> --url <endpoint>`
- There is NO `hermes mcp reload subcommand` — config changes take effect on next tool use
- Use `hermes mcp test` to verify connection state

### Config structure
- MCP config must be directly under `mcp_servers: notion:`, NOT under `mcp_servers: config: notion:`
- Do NOT overwrite `~/.hermes/config.yaml` or `~/.hermes/.env` directly — use `hermes mcp configure` or `echo >>`
- **`hermes mcp configure <name>` is interactive-only (requires TTY).** It does NOT accept `--enable`, `--disable`, or other flags. To toggle `enabled:` in config.yaml, use terminal file editing instead.
- **`hermes mcp serve` serves ALL configured MCP servers — no server-name arg.** Running `hermes mcp serve notion` fails with "unrecognized arguments: notion".

### env variable loading
- `~/.hermes/.env` files do NOT auto-load in shell
- Must export manually BEFORE running MCP commands: `export NOTION_MCP_TOKEN=***`
- The config `token: env:NOTION_MCP_TOKEN` only works if the env var is set in the same session

### Notion permissions
- MCP Connection is DIFFERENT from Integration — Connection uses OAuth, Integration uses API tokens
- Connection grants workspace-wide access; Integrations need per-page sharing
- "Add connections" on individual databases only grants schema access, not page content access

### Package management
- **Do NOT use `docker exec`** for package installs — user runs Hermes directly on host (Spark machine), not in Docker
- Use `pip3 install --break-system-packages` on the host for MCP upgrades
- **Do NOT rely on system-wide `pip install mcp` to fix Hermes MCP issues.** Hermes bundles its own MCP client implementation and does not use the system `mcp` pip package. If you see `mcp.client.streamable_http is not available` despite `mcp>=1.25` installed system-wide, the fix is to upgrade Hermes itself (not pip), or use an alternative transport mode (e.g., `npx`/stdio-based MCP servers like `@notionhq/notion-mcp-server`).

### Silent token revocation — MCP test passes but real calls fail
**Symptom:** `hermes mcp test <name>` returns "✓ Connected" but real API calls (curl, API scripts) return 401 "API token is invalid." **The MCP test only validates the transport layer, NOT credentials.**
- The npx stdio transport establishes a connection without checking the OAuth token
- Token validity is only confirmed on the first actual API call
- **Always verify with a real API call after setup:** `curl https://api.notion.com/v1/users/me -H "Authorization: Bearer <token>"` before assuming auth works

### Enabling MCP servers via terminal
Since `hermes mcp configure` is interactive-only, use terminal to enable/disable:
```bash
# Enable via python
python3 -c "
import yaml
with open('/home/realityrove/.hermes/config.yaml', 'r') as f:
    config = yaml.safe_load(f)
config['mcp_servers']['<name>']['enabled'] = True
with open('/home/realityrove/.hermes/config.yaml', 'w') as f:
    yaml.dump(config, f, default_flow_style=False)
"
```

### Database IDs are full 32-char UUIDs — never use 8-char shorthand
Old shorthand like `175b4695` is **incomplete** and will always return 404.
Real format: `175b4695-a24d-8069-81f3-e5dcac3348d6` (8-dash-hyphen-separated).
**Always use the full UUID.** When in doubt, discover the correct IDs via `/search` (see below).

### ALWAYS query database schema before writing — property names and types must match exactly
Notion validates every property. Assumed names cause `validation_error` 400s.
**Before writing ANY page, query the DB schema first:**
```python
req = urllib.request.Request(f"https://api.notion.com/v1/databases/{db_id}")
req.add_header("Authorization", f"Bearer {token}")
req.add_header("Notion-Version", "2022-06-28")
with urllib.request.urlopen(req, timeout=10) as resp:
    db = json.loads(resp.read())
for name, prop in db.get("properties", {}).items():
    print(f"{name}: {prop.get('type')}")
```
Common traps:
- `Exercise Name` is `title` type (not `rich_text`)
- `Equipment` is `select` (not `multi_select`)
- `Muscle Group` is `multi_select` (not `select`)
- `Version` is `number` (not `rich_text`)
- Field names have exact casing and spaces — they are NOT sanitized
Check for every database — schemas vary per-DB.

## Agent Integration Map

### Director
- dtb Writing: read/write (project status, creative pipeline)
- dtb Knowledge: read (source material for creative work)

### Strategist
- Project tracking databases (read/write)
- VES/AMPAS membership DB (read/write)
- RealityRowHub strategic DB (read/write)

### Accountant
- Financial tracking tables (read/write)
- Budgeting DB (read/write)
- Net worth DB (read/write)

### Coach
- Health tracking tables (read/write)
- Sleep/recovery DB (read/write)

### Connector
- Event calendar DB (read/write)
- Social calendar (read/write)
- Contact tracking tables (read/write)

### Operator
- Dashboard sync (read/write)
- Briefing delivery (write/write)
- Input routing (read/write)

### Scholar
- Source library DB (read/write)
- Literature DB (read/write)
- Knowledge base sync (write/write)

## Notion API Usage (Direct)

- **OAuth token format:** `ntn_xxx`
- **Internal Integration format:** `secret_xxx`
- **Search:** POST `/search` with JSON body `{"message": {"message": "text"}}` — NOT GET
- **Databases:** GET/POST `/v1/databases/{db_id}` and `/v1/databases/{db_id}/query`
- **Pages:** GET/POST/PATCH `/v1/pages/{page_id}`
- **Blocks:** POST `/v1/blocks/{block_id}/children`
- **Database Schema Discovery:** ALWAYS query `GET /v1/databases/{db_id}` before writing pages — property names, types, and options vary per database. Do NOT assume property names match database names.
- **Discovery:** Run `hermes-skill scripts/list-notion-databases.sh` to discover all accessible DBs and their 32-char UUID IDs.

## Troubleshooting

### Database Schema Access ≠ Page Content Access
Adding a connection to a database grants schema access only, not page content. Both must be shared:
- **Schema access:** open database → ⋮ → Add connections → integrate
- **Page access:** open page → Share → add integration → prompt "Also share all N pages?" → confirm
- For OAuth tokens, page sharing is MANDATORY per-database when using Integration tokens (not Connections)

### OAuth `ntn_` token returns 400 on /search
**Symptom:** Token authenticates to `/users/me` but returns `400 invalid_request_url` on search.
**Fix:** Use POST with JSON body, not GET with query params.

### Internal (`secret-xxx`) vs OAuth (`ntn_xxx`)
| Feature | Internal (`secret-xxx`) | OAuth (`ntn_xxx`) |
|---------|-----|-----|
| Scope | Workspace-level by default | User-level |
| Page access | Auto-grants all content | Must share each page individually |
| Setup | Easier for broad access | More granular |
| Use case | Agent tools | User-facing integrations |

### Retrieving Database Names
```python
name_field = db.get('name')
if isinstance(name_field, list) and name_field:
    db_name = name_field[0].get('plain_text', '[unnamed]')
elif isinstance(name_field, str):
    db_name = name_field
else:
    db_name = '[unnamed]'
```

### Writing Works When Pages Appear Empty
Page creation can succeed while querying returns 0 pages. Integration can CREATE but not READ yet. Always test write to confirm access.

### Notion validation errors come through as JSON strings — need double-parsing
When a Notion API returns a 400 validation error, `HTTPError.read()` returns a **JSON string** (bytes), NOT a parsed dict. You must do `json.loads(e.read().decode())` to access the message. Common mistake: treating `e.read()` as a dict directly — it's bytes. Pattern:

```python
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        ...
except urllib.error.HTTPError as e:
    error_body = json.loads(e.read().decode())
    print(error_body['message'])  # the actual Notion validation message
```

The error message itself can be very long and list all failed fields (e.g. "body.properties.Version.title should be defined, instead was `undefined`."). **Extract just the first line** of the message for readability.