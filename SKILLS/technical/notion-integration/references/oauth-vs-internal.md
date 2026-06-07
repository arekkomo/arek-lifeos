# Notion OAuth vs Internal Integration — Practical Notes

> **Session:** 2026-05-31
> **Topic:** Token types and how they behave differently with Notion API

## Why This Matters

The Notion integration skill stores a token, but the type of token determines what works and what doesn't.

## Internal Integration Secret (`secret-xxx`)

**Created at:** Notion → My Integrations → New Integration
**Scope:** Workspace-level by default
**Token start:** `secret-`
**Behavior:**
- `/users/me` → Returns the integration bot
- `/search` → Works immediately, returns ALL workspace content
- Page sharing: No manual sharing needed — all workspace pages are visible
- Best for: Agent tools that need broad workspace access

## OAuth Access Token (`ntn_xxx`)

**Created at:** Notion → My Integrations → Create OAuth App → get token via browser
**Scope:** User-level, one page at a time
**Token start:** `ntn_` 
**Behavior:**
- `/users/me` → Returns "Obsidian Hermes Bridge" (bot user) — **confirms auth works**
- `/search` → May return 400 even with valid token
- Page sharing: Each page/database must be manually shared with the integration via "Share" → "Add connections"
- Best for: User-facing tools that need controlled access

## The 400 on /search Pattern

**What happens:**
1. POST to `/users/me` succeeds (token authenticates)
2. POST to `/search` returns `400 invalid_request_url`

**Root cause:** Not OAuth failure — either:
- No pages shared with the integration (so no content is visible to search)
- Query parameter format wrong for the token type

**How to verify:**
1. Call `/users/me` — if it returns your bot name, token is valid
2. Open a page in Notion → "Share" → scroll to bottom — see if your integration is listed
3. Click "Add connections" → search your integration → add it
4. Retry search

## Sharing Pages with Integration

> **⚠️ Important:** The integration appears under **Connections** in Notion settings, NOT under People. If you're looking in the People tab, you won't find it.

For any page or database you want the agent to access:
1. Open the page/database in Notion
2. Click **"⋮" (More options)** or **"Share"** button
3. Scroll to **Integrations** section (may say "Add connections")
4. Search your integration name ("Hermes Bridge" or "Obsidian Hermes Bridge")
5. Confirm

This is per-page/per-database. Check your Notion plan/admin for workspace-level permission options.

## Workspace-level Permission Options

For OAuth apps, permissions can be granted at three levels:
1. **Database-level**: Add connection to the database itself
2. **Workspace-level**: Notion Admin settings → Connections → [integration] → set permission to "Can edit" (if available)
3. **Page-level**: Share individual pages (last resort)

If workspace-level isn't available through the UI, check your Notion plan tier — some tiers restrict connection permission scope.

## Checklist for New Integration Setup

- [ ] Integration created in Notion → My Integrations
- [ ] Token copied (verify it starts with `secret-` or `ntn_`)
- [ ] Workspace-level access granted (for Internal Integration secrets)
- [ ] Each page/database shared with the integration
- [ ] Token verified: `GET /users/me` returns bot name
- [ ] Test search: `GET /search` returns expected results
- [ ] Test write: `POST /pages` with database ID confirms write access

---