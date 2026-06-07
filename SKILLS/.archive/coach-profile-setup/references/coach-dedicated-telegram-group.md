# Coach dedicated Telegram group migration

Session learning from migrating Coach out of the Emily/default Telegram group into a dedicated Coach profile + bot + group.

## Preferred target state
- Default/Emily gateway owns the general Arek & Co group.
- Coach runs as a separate Hermes profile at `~/.hermes/profiles/coach`.
- Coach profile has its own gateway service, e.g. `hermes-gateway-coach.service`.
- Coach uses its own Telegram bot (e.g. `@Coach_arco_bot`) and a dedicated Coach-only Telegram group.
- Telegram topics inside the Coach group represent Coach subdomains: Training, Nutrition, Sleep/recovery, Body composition, Health/labs, General check-ins.

## Why this is better than topic-level skill routing
Topic skill binding inside the default group can make a topic *behave* like Coach, but it is not a true profile boundary. Dedicated bot/group gives clean isolation for:
- profile config and model;
- skill set;
- memory/session store;
- pairing database;
- logs;
- service lifecycle.

This matches Arek's preference for direct specialist-agent communication and avoids central routing/context bloat when the domain is obvious.

## Migration checklist
1. Create the Coach Telegram bot in BotFather and configure the token under the Coach profile, not default.
2. Install/enable a separate user service for Coach gateway: `hermes --profile coach gateway run --replace`.
3. Confirm both services can be active independently:
   - `systemctl --user is-active hermes-gateway.service`
   - `systemctl --user is-active hermes-gateway-coach.service`
4. Confirm Coach profile pairing separately:
   - `HERMES_HOME=/home/realityrove/.hermes/profiles/coach hermes pairing list`
5. Remove old default-group Coach routing. Current config path is `platforms.telegram.extra.group_topics`; old `telegram.group_topics` entries are stale.
6. Create new Coach Telegram group, add the Coach bot, and send a test message.
7. Verify logs:
   - Coach log should show `inbound message` for the new group chat ID under `~/.hermes/profiles/coach/logs/gateway.log`.
   - Agent log should show `model=qwen3.6:latest provider=custom platform=telegram` for the Coach session.
   - A healthy turn eventually logs `response ready` in the Coach gateway log.
8. Remove the Coach bot from the old Emily/default group to prevent the Coach gateway from still seeing old group traffic.

## Pitfalls
- If `hermes pairing list` is run without `HERMES_HOME=~/.hermes/profiles/coach`, it checks the default profile, not Coach.
- A message can be correctly routed to Coach but still not receive a fast response if the Coach behavior prompt triggers tool-heavy investigation for simple greetings. Treat that as a prompt/tool-discipline problem, not a routing problem.
- Bot token presence may not appear directly in `config.yaml`; avoid exposing secrets. Verify via service status and successful Telegram connection/logs instead.
- Notion MCP can be running as a child process of the Coach gateway; do not confuse MCP status with Telegram routing status.

## Behavior discipline fix for simple-message tool loops
When the new Coach group is correctly routed but a trivial message like `hi` causes many model/tool calls, patch Coach's profile-level behavior instead of changing routing.

Recommended profile prompt additions:
- In `~/.hermes/profiles/coach/SOUL.md`, add a **Response Discipline** section: default to a direct Coach reply; do not inspect files, search history, query Notion, run code, or use tools for simple conversational messages; greetings/setup checks/light check-ins get 1–3 sentence replies starting with `**Coach:**`.
- In `~/.hermes/profiles/coach/SKILL.md`, add **Tool Discipline**: tools only for explicit log/retrieve/update/compare/analyze requests involving health data, images, notes, or databases.

Recommended Coach config hardening:
```yaml
agent:
  disabled_toolsets:
    - terminal
    - code_execution
    - cronjob
    - delegation

tool_loop_guardrails:
  warnings_enabled: true
  hard_stop_enabled: true
  warn_after:
    exact_failure: 1
    same_tool_failure: 2
    idempotent_no_progress: 1
  hard_stop_after:
    exact_failure: 2
    same_tool_failure: 3
    idempotent_no_progress: 2

command_allowlist: []
```

Restart and verify:
```bash
systemctl --user restart hermes-gateway-coach.service
# If stuck in deactivating because an old turn is draining, force only the Coach service:
systemctl --user kill --signal=SIGKILL hermes-gateway-coach.service || true
systemctl --user reset-failed hermes-gateway-coach.service || true
systemctl --user start hermes-gateway-coach.service

HERMES_HOME=/home/realityrove/.hermes/profiles/coach hermes chat -q 'hi' --profile coach --quiet
```
A healthy verification is a single short `**Coach:**` response and an agent log line with `tool_turns=0`.

## Minimal verification commands
```bash
systemctl --user is-active hermes-gateway-coach.service
HERMES_HOME=/home/realityrove/.hermes/profiles/coach hermes status --all
HERMES_HOME=/home/realityrove/.hermes/profiles/coach hermes pairing list
python3 - <<'PY'
from pathlib import Path
p=Path('/home/realityrove/.hermes/profiles/coach/logs/gateway.log')
for line in p.read_text(errors='replace').splitlines()[-120:]:
    if 'inbound message' in line or 'response ready' in line:
        print(line[:900])
PY
```
