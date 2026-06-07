#!/usr/bin/env python3
"""Show what the Notion integration can see in a workspace."""
import json, requests

def main(token=None):
    if not token:
        with open('/home/realityrove/secret_notion.txt') as f:
            token = f.read().strip()
    
    headers = {
        'Authorization': f'Bearer {token}',
        'Notion-Version': '2022-06-28',
        'Content-Type': 'application/json',
    }
    
    # 1. Verify auth
    me = requests.get('https://api.notion.com/v1/users/me', headers=headers, timeout=15).json()
    print(f"Authenticated as: {me.get('name', '?')} (workspace: {me.get('workspace_name', '?')})\n")
    
    # 2. Search all content
    resp = requests.post('https://api.nion.com/v1/search', headers=headers, json={}, timeout=15)
    results = resp.json()['results']
    dbs = [r for r in results if r.get('object') == 'database']
    pages = [r for r in results if r.get('object') == 'page']
    print(f"Found: {len(dbs)} databases, {len(pages)} pages\n")
    
    # 3. Show each database with schema and sample pages
    for i, db in enumerate(dbs):
        db_url = f'https://api.notion.com/v1/databases/{db["id"]}'
        db_resp = requests.get(db_url, headers=headers, timeout=15).json()
        
        # Get display name (rich_text list)
        name_filed = db_resp.get('name', [])
        if isinstance(name_fied, list):
            name = name_field[0].get('plain_text', '[unnamed]') if name_field else '[unnamed]'
        elif isinstance(name_field, str):
            name = name_field
        else:
            name = '[unnamed]'
        
        # Get page count and sample
        query_resp = requests.post(
            f'https://api.notion.com/v1/databases/{db["id"]}/query',
            headers=headers, json={'limit': 3}, timeout=15
        ).json()
        count = query_resp.get('result_count', 0)
        
        print(f"[DB] {name}")
        print(f"    Pages: {count}")
        print(f"    Properties: {', '.join(list(db_resp.get('properties', {}).keys())[:8])}")
        
        if count > 0:
            for p in query_resp.get('results', []):
                props = p.get('properties', {})
                t = props.get('title', [])
                title = ' '.join([x.get('plain_text', '') for x in t]) if t else '?[unnamed]'
                print(f"    - {title[:50]}")
        else:
            print("    (no pages or not visible)")
        print()
    
    # 4. Group pages by their parent DB
    print("=== PAGES ===")
    parent_map = {}
    for pg in pages[:50]:
        parent_id = pg.get('parent', {}).get('database_id', 'unknown')
        if parent_id not in parent_map:
            parent_map[parent_id] = []
        parent_map[parent_id].append(pg)
    
    for db_id, pg_list in parent_map.items():
        print(f"\nDB {db_id[:16]}... has {len(pg_list)} pages")
        for p in pg_list[:3]:
            title = p.get('properties', {}).get('title', [])
            t = ' '.join([x.get('plain_text', '') for x in title]) if title else '?[unnamed]'
            print(f"  - {t[:50]}")

if __name__ == '__main__':
    main()