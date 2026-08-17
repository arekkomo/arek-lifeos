#!/usr/bin/env python3
"""One-way, idempotent Notion → typed Creative Library import.

Writes imported material into type-based CREATIVE/Library folders and keeps sync
metadata here in HUB. Curated captures and project folders are never overwritten.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import UTC, datetime
from pathlib import Path

OPERATIONS = Path(__file__).resolve().parent
VAULT = Path('/home/realityrove/Obsidian/Arek&Co')
LIBRARY = VAULT / 'CREATIVE/Library'
SYSTEM_PROMPTS = OPERATIONS.parent / 'System-Prompts'
SYSTEM_PROMPT_SLUGS = {
    'personal-assistant-system-prompt',
    'claude-systems-project-system-prompt',
    'creative-studio-system-prompt',
    'rrhub-port-migration-3000-3001-8700-8701',
}
DOMAIN_TARGETS = {
    'Writing': LIBRARY / 'Ideas-and-Concepts' / 'Notion-Import',
    'Shows': LIBRARY / 'Story-Design' / 'Notion-Import' / 'Shows',
    'Scenes': LIBRARY / 'Story-Design' / 'Notion-Import' / 'Scenes',
    'Sequences': LIBRARY / 'Story-Design' / 'Notion-Import' / 'Sequences',
    'Shots': LIBRARY / 'Production-Assets' / 'Notion-Import' / 'Shots',
    'Characters': LIBRARY / 'Production-Assets' / 'Notion-Import' / 'Characters',
    'Locations': LIBRARY / 'Production-Assets' / 'Notion-Import' / 'Locations',
    'Props': LIBRARY / 'Production-Assets' / 'Notion-Import' / 'Props',
    'Styles': LIBRARY / 'Production-Assets' / 'Notion-Import' / 'Styles',
    'Prompts': LIBRARY / 'Visual-Prompt-Reference' / 'Notion-Import',
}
ENV = Path('/home/realityrove/.hermes/.env')
DATABASES = {
    'Shows': '185b4695-a24d-8034-a533-ed1699342ada',
    'Scenes': '29ab4695-a24d-8070-b7dd-dfd8ddc85899',
    'Shots': '29ab4695-a24d-8037-8bd7-e5213ae7bd23',
    'Locations': '187b4695-a24d-8048-a850-da27d34ac4ab',
    'Characters': '187b4695-a24d-80b1-9d7a-c877b0caa4ba',
    'Props': '187b4695-a24d-80bb-a3e3-edaec1102553',
    'Styles': '187b4695-a24d-8064-9926-ec5d064de335',
    'Sequences': '1e4b4695-a24d-801a-9065-edfcef946e7a',
    'Writing': '175b4695-a24d-8069-81f3-e5dcac3348d6',
    'Prompts': '2d9b4695-a24d-809e-afdf-c999b7fe7f2e',
}
EXPECTED_NOT_SHARED = {}


def token() -> str:
    value = os.environ.get('NOTION_API_KEY') or os.environ.get('MCP_NOTION_API_KEY')
    if value:
        return value
    if ENV.exists():
        match = re.search(r'^(?:MCP_NOTION_API_KEY|NOTION_API_KEY)\s*=\s*["\']?([^\s"\']+)', ENV.read_text(), re.M)
        if match:
            return match.group(1)
    raise RuntimeError('No Notion API token found; set NOTION_API_KEY or repair ~/.hermes/.env.')


def request(path: str, method: str = 'GET', payload: dict | None = None) -> dict:
    headers = {
        'Authorization': f'Bearer {token()}',
        'Notion-Version': '2022-06-28',
        'Content-Type': 'application/json',
    }
    req = urllib.request.Request(
        f'https://api.notion.com/v1/{path}',
        data=json.dumps(payload).encode() if payload is not None else None,
        headers=headers,
        method=method,
    )
    with urllib.request.urlopen(req, timeout=60) as response:
        return json.load(response)


def plain(rich_text: list[dict] | None) -> str:
    return ''.join(item.get('plain_text', '') for item in rich_text or [])


def slug(text: str) -> str:
    value = re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
    return value[:90] or 'untitled'


def title_of(properties: dict) -> str:
    for prop in properties.values():
        if prop.get('type') == 'title':
            return plain(prop.get('title'))
    return 'Untitled'


def scalar_properties(properties: dict) -> dict:
    """Retain source properties intact, without relying on a database-specific schema."""
    result = {}
    for name, prop in properties.items():
        kind = prop.get('type')
        value = prop.get(kind)
        if kind in {'title', 'rich_text'}:
            result[name] = plain(value)
        elif kind == 'select':
            result[name] = (value or {}).get('name')
        elif kind in {'multi_select', 'relation', 'people'}:
            result[name] = [item.get('name') or item.get('id') for item in value or []]
        elif kind == 'date':
            result[name] = value
        elif kind in {'checkbox', 'number', 'url', 'email', 'phone_number'}:
            result[name] = value
        else:
            result[name] = value
    return result


def list_pages(database_id: str) -> list[dict]:
    pages, cursor = [], None
    while True:
        body = {'page_size': 100}
        if cursor:
            body['start_cursor'] = cursor
        data = request(f'databases/{database_id}/query', 'POST', body)
        pages.extend(data.get('results', []))
        if not data.get('has_more'):
            return pages
        cursor = data.get('next_cursor')


def children(page_id: str) -> list[dict]:
    blocks, cursor = [], None
    while True:
        suffix = f'?page_size=100&start_cursor={cursor}' if cursor else '?page_size=100'
        data = request(f'blocks/{page_id}/children{suffix}')
        blocks.extend(data.get('results', []))
        if not data.get('has_more'):
            return blocks
        cursor = data.get('next_cursor')


def block_text(block: dict) -> str:
    kind = block.get('type', '')
    data = block.get(kind, {})
    text = plain(data.get('rich_text'))
    if kind.startswith('heading_'):
        return '#' * int(kind[-1]) + ' ' + text
    if kind == 'bulleted_list_item':
        return '- ' + text
    if kind == 'numbered_list_item':
        return '1. ' + text
    if kind == 'quote':
        return '> ' + text
    if kind == 'to_do':
        return f"- [{'x' if data.get('checked') else ' '}] {text}"
    if kind == 'code':
        return f"```{data.get('language', '')}\n{text}\n```"
    if kind == 'divider':
        return '---'
    return text


def write_page(domain: str, page: dict) -> Path:
    properties = page.get('properties', {})
    title = title_of(properties)
    source_id = page['id']
    target_dir = SYSTEM_PROMPTS if domain == 'Prompts' and slug(title) in SYSTEM_PROMPT_SLUGS else DOMAIN_TARGETS[domain]
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / f'{slug(title)}--{source_id.replace("-", "")[:8]}.md'
    try:
        body = '\n\n'.join(filter(None, (block_text(b) for b in children(source_id))))
    except urllib.error.HTTPError as exc:
        body = f'> ⚠️ Notion block export unavailable (HTTP {exc.code}); page properties are preserved below.'
    frontmatter = {
        'title': title,
        'category': 'notion-creative-mirror',
        'notion_page_id': source_id,
        'notion_url': page.get('url'),
        'notion_last_edited': page.get('last_edited_time'),
        'source_database': domain,
        'synced_at': datetime.now(UTC).isoformat(),
    }
    yaml = '\n'.join(f'{key}: {json.dumps(value, ensure_ascii=False)}' for key, value in frontmatter.items())
    content = f'---\n{yaml}\n---\n\n# {title}\n\n{body}\n\n## Notion Properties\n\n```json\n{json.dumps(scalar_properties(properties), ensure_ascii=False, indent=2)}\n```\n'
    target.write_text(content)
    return target


def main() -> None:
    OPERATIONS.mkdir(parents=True, exist_ok=True)
    SYSTEM_PROMPTS.mkdir(parents=True, exist_ok=True)
    for target_dir in DOMAIN_TARGETS.values():
        target_dir.mkdir(parents=True, exist_ok=True)
    report = {
        'synced_at': datetime.now(UTC).isoformat(),
        'direction': 'Notion → Obsidian (one way)',
        'root': str(LIBRARY),
        'databases': {},
        'not_shared_or_unavailable': EXPECTED_NOT_SHARED,
        'notes': [
            'Curated CREATIVE/Library entries are not overwritten.',
            'Notion assets/files are retained as source property metadata; external binary downloads are not mirrored.',
            'Re-run this script to refresh edited pages. Files are deterministic by Notion page ID.',
        ],
    }
    for domain, database_id in DATABASES.items():
        try:
            pages = list_pages(database_id)
            files = [str(write_page(domain, page).relative_to(VAULT)) for page in pages]
            report['databases'][domain] = {'database_id': database_id, 'count': len(files), 'files': files}
        except urllib.error.HTTPError as exc:
            report['databases'][domain] = {
                'database_id': database_id,
                'count': 0,
                'status': 'unavailable',
                'http_status': exc.code,
            }
        time.sleep(0.35)
    (OPERATIONS / 'SYNC-REPORT.json').write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
    total = sum(item['count'] for item in report['databases'].values())
    unavailable = [name for name, item in report['databases'].items() if item.get('status') == 'unavailable']
    suffix = f'; unavailable: {", ".join(unavailable)}' if unavailable else ''
    print(f'Synced {total} Notion records across {len(DATABASES) - len(unavailable)} creative databases to {LIBRARY}{suffix}')

if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, urllib.error.HTTPError, urllib.error.URLError) as exc:
        print(f'Sync failed: {exc}', file=sys.stderr)
        raise SystemExit(1)
