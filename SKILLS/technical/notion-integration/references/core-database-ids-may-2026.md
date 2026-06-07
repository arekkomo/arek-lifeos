# Core Notion Database IDs

> **Discovered:** 2026-06-01  
> **Source:** Notion API workspace discovery via OAuth connection  
> **Note:** IDs are full NOT truncated (NOT `175b4695` - must use full UUID strings like `175b4695-a24d-8069-81f3-e5dcac3348d6`)

## Agent-Referenced Databases

| Database Name | Full UUID | Purpose |
|---------------|-----------|---------|
| dtb Knowledge | `171b4695-a24d-8014-8354-cee9f58d98fc` | Agent knowledge base (source material reading) |
| dtb Writing | `175b4695-a24d-8069-81f3-e5dcac3348d6` | Project status, creative pipeline |
| Projects | `171b4695-a24d-81b7-aa0a-d36ac7909fd6` | Strategic project tracking |
| Tasks | `171b4695-a24d-8176-9486-e3708c6cd0b0` | Task management |

## Discovery Command

To discover all accessible databases in your workspace:
```bash
hermes mcp run discovery notion
```

## Full Workspace List (as of 2026-06-01)

The workspace "Arek's Notion" (workspace_id: `1a77942b-3a01-4fa6-9057-b1cd7af3f11f`) currently has 26 accessible databases:

- Exercise Library, Body Measurements, Calorie Tracker, Workout Log (fitness tracking)
- dtb Writing, dtb Knowledge, dtb Prompts, dtb Shows, dtb Scenes, dtb Shots, dtb Locations, dtb Characters, dtb Props, dtb Styles, VFX companies (creative pipeline)
- Projects, Tasks (project management)
- Arek & Co — Dashboard Priorities (dashboard)
- Multiple duplicate "Shots" and unnamed databases (cleanup candidates)
