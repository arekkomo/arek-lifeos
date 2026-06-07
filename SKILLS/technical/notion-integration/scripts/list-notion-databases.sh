#!/usr/bin/env bash
# List all accessible Notion databases for the current OAuth token.
# Usage: source .env if needed, then run this script.
#
# Requires: curl, AND either NOTION_MCP_TOKEN or MCP_NOTION_API_KEY
#           set in environment (from ~/.hermes/.env).

set -euo pipefail

TOKEN="${NOTION_MCP_TOKEN:-${MCP_NOTION_API_KEY:-}}"

if [ -z "$TOKEN" ]; then
    echo "ERROR: No Notion token found. Set NOTION_MCP_TOKEN or MCP_NOTION_API_KEY." >&2
    exit 1
fi

curl -s https://api.notion.com/v1/search \
  -H "Authorization: Bearer $TOKEN" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{"filter":{"property":"object","value":"database"}}' \
  | python3 -c "
import sys, json
data = json.load(sys.stdin)
dbs = data.get('results', [])
print(f'Accessible databases in Notion: {len(dbs)}')
for db in dbs:
    name_parts = db.get('title', [])
    name = next((p.get('plain_text') for p in name_parts), '[NO TITLE]')
    dbid = db.get('id', '?')
    print(f'  - {name} (ID: {dbid})')
"
