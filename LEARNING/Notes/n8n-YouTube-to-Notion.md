---
title: n8n Workflow — YouTube → Notion Pipeline
category: note
summary: Automated workflow for capturing YouTube video metadata (title, description, tags) and syncing it to Notion via API webhook
tags: [automation, n8n, youtube, workflow-automation, content-capture]
sources: 1
updated: 2026-07-04
---

# n8n Workflow — YouTube → Notion Pipeline

**Automated pipeline for capturing YouTube video metadata and syncing to Notion database.** Designed for content research workflows where video sources need to be catalogued automatically.

## How It Works (n8n Implementation)

### Step 1: Trigger
- **YouTube Trigger** → polls channel for new uploads, or **Webhook** → receives data from other sources
- Also supports manual trigger for ad-hoc entries

### Step 2: Data Extraction
- **HTTP Request** node pulls URL-encoded form data containing YouTube video metadata (title, description, tags)
- Extracts core fields needed for database entry

### Step 3: Notion API
- Passes extracted data to Notion's REST API via Webhook integration
- Creates new page record in the target Notion database with all captured metadata

## Configuration Notes
- Requires n8n instance (self-hosted or cloud) running
- Notion Integration token needed for authentication (stored as n8n credential)
- Custom YouTube channel feed URL in trigger node configuration
- Webhook endpoint URL must be accessible publicly if triggered externally

> ⚠️ Use-case: Research pipeline — automatically capture interesting YouTube content without manual entry. Integrate with `[[Synthesia-NaturalAvatars]]` workflow for full video content capture to knowledge base.

## Access
This is an operational workflow — check your n8n instance configuration for deployment details. See [n8n documentation](https://docs.n8n.io/) for webhook and Notion integration guide.

```
## [2026-07-04] ingest | YouTube→Notion Workflow
Captured substantive content (5.5KB) from Notion dump as operational workflow note. Source: raw/dtb_export_archive_2026-07-04/YouTube-To-Notion.md
```
