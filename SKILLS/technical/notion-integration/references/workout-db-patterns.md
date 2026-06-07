---
name: workout-db-patterns
description: "Patterns for querying Notion workout/fitness/log databases reliably — schema inspection, pagination, and filter traps."
---

# Notion Workout Database Query Patterns

## Schema Inspection (ALWAYS first)

**Before querying or writing, inspect column types. Notion's API requires exact match.**

```bash
TOKEN='$'curl -s https://api.notion.com/v1/databases/<DB_ID> \
  -H "Authorization: Bearer $TOKEN" \
  -H "Notion-Version: 2022-06-28" | python3 -c "
import sys, json
db = json.load(sys.stdin)
for name, prop in db.get('properties', {}:items():
    print(f'{name}: {prop.get('type')}')"
```

Common type traps:
- `Exercise` or `Name` → always `title` type (rich_text in title object)
- `Equipment` → usually `select` (single) NOT `multi_select`
- `Muscle Group` → often `multi_select`
- Numbers are `number` type — values can be `null` for empty cells

## Pagination (cursor-based)

**Notion API returns max 100 results per page. You MUST follow the `next_cursor` for complete results.**

```python
import urllib.request, json

TOKEN='<token>'
DB_ID = '<database-uuid>'

headers = {
    'Authorization': 'Bearer ' + TOKEN,
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json'
}

all_results = []
start_cursor = None

while True:
    body = json.dumps({'page_size': 100, 'start_cursor': start_cursor}).encode()
    req = urllib.request.Request(
        f'https://api.notion.com/v1/databases/{DB_ID}/query',
        headers=headers,
        data=body
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read())
    
    all_results.extend(data.get('results', []))
    
    if not data.get('has_more'):
        break
    start_cursor = data.get('next_cursor')

# all_results now contains every page
```

## Filtering Gotchas

- **Date filters fail silently** if the date column name doesn't match EXACTLY (check schema first)
- **Empty date columns** will cause the filter to exclude that row entirely
- **Multiple date fields** exist in some DBs (Created vs Date vs Updated) — query the right one
- **Filter by `Session ID`** is useful for grouping exercises into sessions

## Parsing Exercise Name (title type)

```python
# Title type values are nested lists: [[{'plain_text': '...', ...}], ...]
exercises = props.get('Exercise', {}).get('title', [])
title = exercises[0].get('plain_text', '(no title)') if exercises else '(none)'
```

## Coach Session Report Workflow

When generating a Coach session report:
1. Query workout DB for date range
2. Group by `Session ID` to identify distinct workouts
3. Summarize each workout separately (exercise → sets/weight)
4. Compare session-to-session progression (PR tracking)
5. Report completion count vs expected (e.g., 3/5 days this week)
6. **ALWAYS anchor dates to the session's current date** — don't assume day labels (Mon/Tue/Wed) match the user's actual day

## Common Workout DB Columns (Arek's setup)

| Column | Type | Notes |
|---|---|---|
| Exercise | title | Main identifier |
| Date | date | Not Created — a custom date field |
| Day Type | select | Push A / Pull A / Arms, etc. |
| Total Sets | number | |
| Session ID | rich_text | Groups exercises into sessions |
| PR | checkbox | |
| Muscle Group | multi_select | Can be empty |
| Notes | rich_text | |
| Set N Weight (lbs) | number | null for warmup |
| Set N Reps | number | null for warmup |
