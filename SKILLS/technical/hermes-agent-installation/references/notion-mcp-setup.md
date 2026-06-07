---
name: notion-mcp-setup
domain: technical
version: 1.0
description: Set up Notion MCP integration with Hermes Agent - covering OAuth tokens, environment variables, and CLI configuration.
updated: 2026-05-31
---

# Notion MCP Setup with Hermes

> **Status:** Active
> **Last Updated:** 2026-05-31

## Purpose

Configure Notion's remote MCP server with Hermes Agent for workspace-wide database access.

## Notion Auth Systems - Critical Distinction

| System | Location | Token format | Use case |
|--------|----------|--------------|----------|
| **Connections (OAuth)** | Settings & Members → **Connections** tab | `ntn_xxx` | Notion MCP, OAuth apps |
| **Integrations (legacy)** | Settings & Members → **Integrations** | `secret_xxx` | API tokens, bots |
| **People** | Settings & Members → **People** tab | N/A | Human members only |

**CRITICAL: Integrations appear under Integrations, NOT People. Cannot manage from People tab.**

## Setup Workflow

### Step 1: Create Notion Connection
1. Open Notion workspace → **Settings & Members → Connections tab**
2. Create new **Connection** for Notion MCP server
3. OAuth will prompt browser authentication

**⚠️ Note:** `mcp.notion.com` returns 404 for unauthenticated users. Must create a Connection first.

### Step 2: Add MCP Server via CLI
```bash
hermes mcp add notion --url https://mcp.notion.com/mcp
```
- When prompted: Confirm name as "Notion MCP"
- Auth method: Choose **token**
- Paste your `ntn_xxx` token from the Connection flow

### Step 3: Verify Connection
```bash
hermes mcp test
hermes mcp list
```

## Environment Setup

```bash
# Add token to .env
echo "NOTION_MCP_TOKEN=ntn_xxxtoken" >> ~/.hermes/.env
chmod 600 ~/.hermes/.env

# Alternative: add to config.yaml (requires manual edit)
# nano ~/.hermes/config.yaml
```

## Troubleshooting

### Config.yaml Protection
- Config file is protected by Hermes from direct tool writes
- Use manual editor or `hermes mcp configure` CLI commands only
- Never attempt to write via API tools in automated flows

### MCP Server Not Found
- Verify connection created in Notion first
- Check URL is `https://mcp.notion.com/mcp` (not just `https://mcp.notion.com`)
- Token format must be `ntn_xxx` (OAuth connection, not integration)

### "Must specify URL" Error
- When using `hermes mcp add`, always include both `--url` and server name
- Syntax: `hermes mcp add <name> --url <endpoint_url>`

### Database Schema ≠ Page Content
- Connection grants schema access to all databases
- Page access must be added separately for each database
- Some databases may need individual sharing to the connection

## Useful Commands
```bash
hermes mcp status                    # Check all MCP connections
hermes mcp list                      # List registered MCP servers
hermes mcp test                      # Test authentication
hermes mcp configure <server_name>   # Update connection details
```

## Reference
- https://mcp.notion.com/mcp
- https://developers.notion.com/guides/get-started/authorization
