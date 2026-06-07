# Notion Workout Log retrieval notes

Session-derived durable pattern for Coach fitness tracking.

## Data location
- Notion database title: `Workout Log`
- Purpose: Daily exercise tracking — sets, reps, weight per exercise per session.
- Shape: one Notion page/row per exercise, grouped into sessions by `Session ID`.

## Important properties
- `Date`
- `Session ID`
- `Day Type`
- `Exercise`
- `Muscle Group`
- `Total Sets`
- `Set 1 Weight (lbs)`, `Set 1 Reps`
- `Set 2 Weight (lbs)`, `Set 2 Reps`
- `Set 3 Weight (lbs)`, `Set 3 Reps`
- `Set 4 Weight (lbs)`, `Set 4 Reps`
- `PR`
- `Notes`

## Retrieval workflow
1. Use Notion search for `Workout Log` to discover the database if needed.
2. Pull recent entries sorted by `Date` descending.
3. Group rows by the latest `Session ID` rather than treating each page as a whole workout.
4. Render a concise summary:
   - Date and day type
   - Session ID
   - Total logged sets
   - PRs flagged
   - Per-exercise bullets with set/weight/reps

## MCP fallback pitfall
The Notion MCP can successfully retrieve database schema while `query_data_source` may return `invalid_request_url` for a database ID returned by search. If that happens, treat it as a wrapper/version mismatch, not a Notion auth failure. Use the Notion REST database query endpoint directly with the configured Notion token as a fallback.

Minimal REST shape:

```json
{
  "sorts": [{"property": "Date", "direction": "descending"}],
  "page_size": 20
}
```

Endpoint:

```text
POST https://api.notion.com/v1/databases/<database_id>/query
Authorization: Bearer <token>
Notion-Version: 2022-06-28
Content-Type: application/json
```
