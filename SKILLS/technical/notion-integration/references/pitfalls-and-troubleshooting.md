# Pitfalls and Troubleshooting — Notion integration with OAuth tokens

## Two-level sharing required (DB schema + individual pages)
Adding the integration as a connection to a database only grants schema access — you'll see column names, property types, and database metadata but **zero pages**. 

After sharing the DB (3 dots → Add connections → integration name), you must also open each page inside it and click "Add connections" for the integration. Without per-page sharing, all `POST /databases/{db_id}/query` calls return `{"results": []}`.

## Database display names missing from search results
Database `name` fields are `null`, `[]`, or `""` in `/search` POST results. The only way to get display names is:
```python
for db in all_db_results:
    full_db = requests.get(f'https://api.notion.com/v1/databases/{db["id"]}', headers=headers)
    full_db_name = full_db.json()['name']  # may be list or str
```
Cache these calls — `/databases/{id}` is rate-limited more aggressively than `/search`.

## `name` field can be array or string
Some integrations return `db.name` as a rich_text array: `[{"plain_text": "Name", ...}]`
OAuth tokens sometimes return a plain string: `"My Database"`.

Defensive access pattern:
```python
name_field = db.get('name')
if name_field and isinstance(name_field, list):
    db_name = next((c.get('plain_text', '') for c in name_field if c.get('plain_text')), 'unnamed')
elif name_field and isinstance(name_field, str):
    db_name = name_field
else:
    db_name = 'unnamed'
```

## Pagination: `has_more` not `result_count`
`/search` POST returns:
- `results`: list of items (max 100 per page)
- `has_more`: boolean, use `cursor` parameter to fetch next page
- NO `result_count` key — it exists on `/databases/{id}/query` but not on `/search`

## `result_count` vs `has_more` confusion
- `GET /databases/{id}` — returns `result_count` (integer)
- `POST /databases/{id}/query` — returns `result_count` (integer) + `has_more` (boolean)
- `POST /search` — returns `has_more` (boolean) — NO `result_count`
- Always check which endpoint you called before accessing pagination keys

## Agent naming — "Hermes Bridge"
This is the display name to search for when manually adding connections. If it doesn't appear, the integration may have a different name in the workspace. Check with `GET /users/me` to verify the workspace name.

## Connections vs People — critical distinction
**Hermes Bridge appears under Connections (Integrations), NOT under People.**
This is a common trap. In Notion UI:
- **Settings → People** shows human members only
- **Connections (or Integrations) tab** shows API integrations/bots
- You cannot add or modify connection permissions from the People tab

### Permission models for connections
Depending on your Notion org policy and how the integration was created:

1. **Database-level sharing** (per-database): Open database → "..." → "Add connections" → your integration name
2. **Workspace-level sharing** (all pages): Some Notion setups allow setting a connection's permission to "Can edit" or "Full access" for the entire workspace. Look for this option under:
   - **Settings → Connections → [integration name] → Permissions**
   - Or **Settings → Members → Connections tab → [integration name]**
3. **Per-page sharing**: Open each page → "Share" → scroll to "Integrations" section → add your integration

**If workspace-level sharing isn't available**, fall back to per-database or per-page sharing. Check with your Notion admin or plan tier what's supported.

## Rate limiting pattern
- `/search` — ~500 RPM for the workspace
- `/databases/{id}` — ~100 RPM for the workspace
- Individual API calls within 100 RPM for a specific database/page
- Practical limit: batch 20+ requests with 1s pauses between batches
