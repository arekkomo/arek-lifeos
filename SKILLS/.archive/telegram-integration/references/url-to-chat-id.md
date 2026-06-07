# Telegram URLs → Chat IDs

## URL Formats and Their IDs

### t.me/c/SUPERGROUP_ID/THREAD_ID
- Format: `https://t.me/c/<id>/<thread_id>`
- The `c` prefix means it's a **supergroup with topics**
- API chat ID: `-100<id>` (prepend `-100` to the path segment)
- Thread/topic ID: the last path segment
- Example: `https://t.me/c/3827588279/2`
  - Chat ID: `-1003827588279`
  - Thread/topic ID: `2`

### t.me/SUPERGROUP_INVITE
- Format: `https://t.me/+<invite_code>` (group invite link)
- Not useful for chat ID — you need Desktop client to see the ID

### t.me/username
- Format: `https://t.me/username` (channel, group, or bot)
- The username is enough for messaging but NOT for config
- Use Desktop → right-click → info → scroll to chat ID

### t.me/BOT_USERNAME or /start?start=
- For DMs: user ID = number in BotFather output or from @userinfobot

## Key Mapping

| URL pattern | API value | Prefix |
|---|---|---|
| `t.me/c/NNNNN/TTT` | `-100NNNNN` | `-100` |
| Group invite `t.me/+X` | Must find via app info | None |
| `t.me/u/@username` | Use app info → chat ID | None |
| Bot `t.me/@username` | User ID from BotFather | None |
| DM from @userinfobot | `123456789` | Plain number |

## Common Mistakes

- **Using the raw URL number without `-100` prefix** for supergroups → API returns 404
- **Confusing thread_id with chat_id** — they're separate: chat_id groups the messages, thread_id separates topics
- **Assuming t.me/c/NNN always works as `-100NNN`** — verify via gateway logs or app info; legacy groups may differ
- **Skipping the gateway logs** — they contain the exact chat_id and thread_id for each inbound message
