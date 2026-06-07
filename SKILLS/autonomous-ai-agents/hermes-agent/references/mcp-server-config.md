# MCP Server Configuration — Pitfall Reference

## Notion MCP Auth Format (Critical)

Current `tools/mcp_tool.py` treats `auth` as a string only (`oauth` is special-cased) and sends HTTP credentials via the `headers:` map. It interpolates `${ENV_VAR}` placeholders from the active profile's `.env`.

**Wrong** (causes `AttributeError: 'dict' object has no attribute 'lower'`):

```yaml
mcp_servers:
  notion:
    url: https://mcp.notion.com/mcp
    auth:
      token: env:NOTION_MCP_TOKEN
    transport: streamable_http
    enabled: true
    name: Notion MCP
```

**Also wrong / ineffective** (no Authorization header is sent, usually 401):

```yaml
mcp_servers:
  notion:
    url: https://mcp.notion.com/mcp
    auth: token
    transport: streamable_http
```

**Correct shape for a bearer token**:

```yaml
mcp_servers:
  notion:
    url: https://mcp.notion.com/mcp
    headers:
      Authorization: "Bearer ${NOTION_MCP_TOKEN}"
    transport: streamable_http
    enabled: true
    name: Notion MCP
```

If this still returns `401 Unauthorized`, the config shape is no longer the blocker; the token is invalid/revoked/not accepted for the Notion MCP workspace/auth flow. Verify with `hermes mcp test notion` under the relevant profile.

**Symptoms of config/auth issues**:
- Nested `auth:` dict → `AttributeError: 'dict' object has no attribute 'lower'`
- `auth: token` without headers → `401 Unauthorized` because no bearer header is sent
- Correct bearer header but `401` → token/workspace/auth problem, not a YAML-copy problem
- Check `profiles/<profile>/logs/errors.log` for the exact traceback from `mcp_tool.py`
