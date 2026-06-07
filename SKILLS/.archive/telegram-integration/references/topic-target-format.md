# Posting to Telegram Topics — Target Format

When sending to a specific topic (thread) in a group, use the target format:

```
telegram:<chat_id>:<topic_id>
```

Examples from live use:
- `telegram:-1003827588279:145` → group `-1003827588279`, topic `145`
- Topic IDs come from the Telegram URL: `https://t.me/c/<chat_numeric_id>/<topic_id>`

To find your topic ID:
1. Open the topic in Telegram Desktop
2. URL shows `https://t.me/c/3827588279/145` — the last number is the topic ID
3. Or long-press the topic name and share its info

## Topic-Based Agent Routing Pattern

For multi-agent setup using group topics:
1. Create a topic per agent (long-press group name → Edit Topics → New Topic)
2. Name each topic descriptively (e.g., 🏋️ Coach, 💰 Finance)
3. Get each topic ID from the URL
4. Wire up routing by documenting which topic ID maps to which Hermes profile
5. Messages in each topic auto-route to the correct session via Hermes native topic isolation
6. No @-mention needed — the thread itself defines the context
