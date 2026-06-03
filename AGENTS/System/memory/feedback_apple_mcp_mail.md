---
name: apple-mcp tool status
description: Status of apple-mcp tools — mail disabled, reminders fixed via manual source patch
type: feedback
originSessionId: 71527be7-a757-4430-b410-da4830126107
---
**Mail:** Never call `mcp__apple-mcp__mail`. Arek uses Gmail via browser, not Apple Mail. Permanently off-limits.

**Reminders:** Fixed 2026-05-05 via manual patch to the apple-mcp source. The original code intentionally returned empty arrays for all read operations ("not implemented for performance"). Patched `utils/reminders.ts` with working AppleScript and rebuilt with bun. Search and read now work — all 4 reminders (Will, Power of attorney, Apply for Nexus, Pay VES Membership Dues) are accessible via search. The `list` summary count shows low due to sequential AppleScript timing, but search is fully functional. If CoWork updates and overwrites the npm cache, the fix will need to be reapplied. ⚠️ Note (2026-05-11): `Arek&Co/reminders-fix.ts` no longer exists at vault root — if the tool breaks again after a CoWork update, Arek will need to rebuild the patch from scratch (re-patch `utils/reminders.ts` in the apple-mcp source with working AppleScript and rebuild with bun).

**How to apply:** Use `mcp__apple-mcp__reminders` with `search` operation for reliable reads. Avoid relying on the `list` count. If the tool breaks again after a CoWork update, alert Arek — the recovery file is gone and the fix needs to be rebuilt.
