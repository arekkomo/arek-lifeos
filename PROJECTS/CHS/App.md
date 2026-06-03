---
title: CHS App (chs-hub)
category: project
summary: Technical documentation for the CHS quoting, invoicing, and project management web app.
tags: [CHS, app, nextjs, sqlite, n8n, tech]
updated: 2026-05-09
---

# CHS App — chs-hub

## Overview

**Name:** chs-hub  
**Version:** 0.2.0  
**Type:** Internal business management tool for Robert (not client-facing)  
**Local dev URL:** http://localhost:3000  
**Production URL:** http://10.0.0.15:3002 (PM2 on local server `realityrove@10.0.0.15`)  
**Code path:** `/Users/arekkomorowski/Projects/CHS`

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Next.js 16.2.2 (App Router) |
| Language | TypeScript |
| UI | shadcn/ui + Tailwind CSS v4 |
| State / Forms | React Hook Form + Zod |
| ORM | Drizzle ORM |
| Database | SQLite (`chs.db` via better-sqlite3) |
| PDF generation | @react-pdf/renderer (in-app) |
| Automation | n8n webhooks (document generation + email) |
| Process manager | PM2 (`chs-hub` process) |
| Package manager | pnpm |

---

## Features (v0.2.0)

### Contacts
- Store clients and contractors
- Fields: name, address, city, postCode, phone, email, relationship (client / contractor), notes

### Projects
- Full lifecycle: `quote → in_progress → paused → done → canceled`
- Per-project hourly rate (default $60/hr) and GST rate (default 5%)
- Completion percentage tracking
- Project templates (save a project structure for reuse)

### Tasks
- Nested task tree (parent tasks + subtasks)
- Per-task: hours, assignee, due date, status, sort order
- Statuses: not_started / in_progress / done / archived / omit
- Tasks feed directly into quote/invoice labour calculations

### Materials
- Per-project material line items
- Fields: item name, price, quantity, status (quote / purchased / omit), date
- Feed into quote/invoice materials section

### Quotes
- Quote number, issue date, expiry date
- Status: not_issued → issued → sent → paid
- PDF generation (two methods — see below)
- Email delivery via n8n

### Invoices
- Same structure as quotes
- Status: not_issued → issued → sent → paid
- PDF generation + email delivery

### Settings
- Company name, phone, email, address
- n8n webhook URLs (quote, invoice, email)

---

## PDF & Email Architecture

Two PDF generation methods:

1. **In-app (React PDF):** `@react-pdf/renderer` renders PDFs server-side — used for direct download / print preview
2. **n8n webhook:** App POSTs structured payload to n8n → n8n generates styled PDF → returns `docUrl`

Email delivery:
- App renders PDF via React PDF → base64 encodes → POSTs to n8n email webhook
- n8n sends email with PDF attachment to client
- Quote/Invoice status auto-updates to `sent` on success

**n8n webhook URLs** (stored in Settings):
- `n8n_webhook_quote` — quote document generation
- `n8n_webhook_invoice` — invoice document generation
- `n8n_webhook_email` — email delivery (quotes + invoices)

---

## Deployment

**Production server:** `realityrove@10.0.0.15` (DGX Spark on local network)  
**Deploy command:** `./deploy.sh` from project root  
**What deploy.sh does:**
1. rsync to `~/CHS/` on prod (excludes node_modules, .next, .git)
2. SSHs in, clears `.next` cache, runs `pnpm build`, restarts PM2
3. Verifies version string appears in built JS

> ⚠️ Never rsync to `~/chs-hub/` — that directory exists but PM2 doesn't serve from it

---

## Data Model (simplified)

```
contacts ──────────────────────────┐
                                   │
projects ──── project_contacts ────┘ (many-to-many, role: client | assigned)
    │
    ├── tasks (nested, parent_task_id)
    ├── materials
    ├── quotes ──── contacts (clientId)
    └── invoices ── contacts (clientId)

settings (key/value store)
```

---

## Known Contact Info (from code)

- **Phone:** +1.604.767.6437
- **Email:** creativehmsolutions@gmail.com

---

## Planned Features / Roadmap

> Add future feature requests here as they are defined.

- [ ] ~~Public deployment~~ — deferred, local network is sufficient for now
- [ ] Client portal or quote acceptance flow
- [ ] Payment tracking / integration
- [ ] Photo attachments per project
- [ ] Expense receipts linked to materials
- [ ] Reporting / revenue dashboard

---

## Development Notes

- Built and maintained by Arek (Claude Code project)
- Database is a local SQLite file — no cloud DB, no auth layer currently
- Production runs on the DGX Spark at home — not internet-accessible without VPN/tunnel
- A static website draft exists at `/website/chs_home.html` in the repo (see [[Website-Plan]])
