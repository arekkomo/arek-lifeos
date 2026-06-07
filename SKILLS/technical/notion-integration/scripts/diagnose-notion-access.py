"""Diagnostic: discover all accessible databases and pages from a Notion OAuth integration.

USAGE:
  python3 scripts/diagnose-notion-access.py

What it does:
  1. Calls GET /users/me to verify auth and workspace name
  2. Calls POST /search to enumerate all accessible databases and pages
  3. For each database, calls GET /databases/{id} to get display name + schema
  4. For each database, calls POST /databases/{id}/query to check if pages are accessible
  5. Outputs results to stdout and saves them to <working_dir>/notion_accessible_dbs_detail.json

AUTHENTICATED AS:
  Read token from /home/realityrove/secret_notion.txt on line 14.
  Change the path if your secret file is elsewhere.
"""
import json
import requests

# ── Config ─────────────────────────────────────────────────────
with open('/home/realityrove/secret_notion.txt') as f:
    token = f.read().strip()
TOKEN_PATH = '/home/realityrove/secret_notion.txt'

headers = {
    'Authorization': f'Bearer {token}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json',
}

def get_db_name(db_full):
    """Extract display name from a database object (handles list or str)."""
    name_field = db_full.get('name')
    if name_field and isinstance(name_field, list):
        return next((c.get('plain_text', '') for c in name_field if c.get('plain_text')), 'unnamed')
    if name_field and isinstance(name_field, str):
        return name_field
    return 'unnamed'

# ── Auth check ──────────────────────────────────────────────────
me_resp = requests.get('https://api.notion.com/v1/users/me', headers=headers, timeout=15)
me = me_resp.json()
print(f"Authenticated as: {me.get('type', '?')} | Workspace: {me.get('workspace_name', '?')}")
print(f"Bot ID: {me.get('bot', {}).get('owner', {}).get('workspace', {}).get('id', '?')}")
print(f"Integration ID: {me_resp.json()['bot']['id']}")
print()

# ── Enumerate accessible items ──────────────────────────────────
search_resp = requests.post('https://api.notion.com/v1/search', headers=headers, json={}, timeout=15)
search_result = search_resp.json()

dbs = [i for i in search_result.get('results', []) if i.get('object') == 'database']
pages = [i for i in search_result.get('results', []) if i.get('object') == 'page']

all_data = {}

for i, db in enumerate(dbs):
    db_id = db['id']
    db_full = requests.get(f'https://api.notion.com/v1/databases/{db_id}', headers=headers, timeout=15).json()
    db_name = get_db_name(db_full)
    props = db_full.get('properties', {})
    
    # Query pages in DB (limit 3 for sample)
    q = requests.post(f'https://api.notion.com/v1/databases/{db_id}/query', headers=headers, json={'limit': 3}, timeout=15).json()
    result_count = q.get('result_count', '?')
    has_more = q.get('has_more', False)
    sample_pages = q.get('results', [])
    
    page_names = []
    for p in sample_pages:
        titles = p.get('properties', {}).get('title', [])
        name = ' '.join(t.get('plain_text', '') for t in titles if t.get('plain_text')) or '[unnamed]'
        page_names.append(name)
    
    entry = {
        'name': db_name,
        'id': db_id,
        'archived': db_full.get('archived', False),
        'result_count': result_count,
        'has_more': has_more,
        'properties': {k: v.get('type') for k, v in props.items()},
        'sample_pages': page_names or ['(empty)'],
    }
    all_data[db_id] = entry
    
    status = 'ARCHIVED' if db_full.get('archived') else 'ACTIVE'
    print(f"[{i+1}] {db_name} [{status}] ({result_count} pages in DB, more={has_more})")
    print(f"     ID: {db_id}")
    print(f"     Properties ({len(props)}):")
    for k, v in list(props.items())[:10]:
        print(f"       • {k}: {v}")
    if len(props) > 10:
        print(f"       ... and {len(props)-10} more")
    print(f"     Sample pages:")
    for p in page_names or ['(empty)']:
        print(f"       - {p}")
    print()

# ── Diagnostics ────────────────────────────────────────────────
print("=" * 60)
print("DIAGNOSIS")
print("=" * 60)

dbs_with_pages = sum(1 for d in all_data.values() if d['sample_pages'] and d['sample_pages'] != ['(empty)'])
dbs_empty = sum(1 for d in all_data.values() if d['sample_pages'] == ['(empty)'])

if dbs_with_pages > 0:
    print(f"✓ {dbs_with_pages} database(s) have visible pages → integration has full access")
if dbs_empty > 0:
    print(f"✗ {dbs_empty} database(s) have zero visible pages → may need page-level sharing")
if pages:
    print(f"✓ {len(pages)} standalone pages accessible outside databases")
    
print("\nFull JSON saved to notion_accessible_dbs_detail.json")
with open('notion_accessible_dbs_detail.json', 'w') as f:
    json.dump(all_data, f, indent=2, default=str)
