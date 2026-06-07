---
name: Notion MCP — Setup Reference
---

# Notion MCP Server — Official Setup

## Overview
Notion hosts an official remote MCP server at: **https://mcp.notion.com**
- No local installation required
- OAuth-based auth (browser flow)
- ~16 tools: database query, page create/update, search, block manipulation, etc.
- Uses streamable HTTP transport

## Step-by-Step Setup

### 1. Get Your Connection Token
Go to your Notion workspace → **Settings & Members → Connections** tab (NOT Integrations)
Create a new Connection → this generates an OAuth token for the MCP server.

### 2. Access the MCP Server
Open https://mcp.notion.com in your browser:
- Click "Add" or "Connect"
- Log in with your Notion account
- Authorize the connection
- You get: **access token + server URL**

### 3. Configure Hermes
In your `mcp_servers.yaml` or `config.yaml`:
```yaml
mcp_servers:
  - name: notion
    url: https://mcp.notion.com/mcp
    headers:
      Authorization: "Bearer <your-access-token>"
```

### 4. Verify
Run `/reload-mcp` in Hermes → check that MCP tools are loaded.

## Important Notes
- Notion has TWO auth systems: Integrations (API tokens) and Connections (OAuth)
- Connections are managed at Settings & Members → Connections tab
- People tab is for humans only — integrations/connections never appear there
- If you get 400 on /v1/search with OAuth tokens, use POST with JSON body instead
- You do NOT need to share pages individually when using MCP — it handles workspace access automatically
