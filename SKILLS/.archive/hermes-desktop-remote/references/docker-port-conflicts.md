# Docker Port Conflicts on Spark/DGX

## Common collision on Spark

| Port   | Service      | What it is                                  |
|--------|--------------|---------------------------------------------|
| 8080   | SearXNG (Docker) | Privacy metasearch engine (not Herme)   |
| 12000  | open-webui (Docker) | Chat UI for Ollama                       |
| 9119   | hermes dashboard | Real Hermes gateway target for Desktop app |

## Detection

```bash
# List all Docker containers and their port mappings
docker ps --format '{{.Names}} {{.Image}} {{.Ports}}'

# Check which process owns a port
ss -tlnp | grep :<port>
```

## Root cause

SearXNG and open-webui run as Docker containers and grabbed ports that might otherwise seem available. They started ~4 days into Spark's lifetime (pulled from Docker Hub). Docker containers bind to `0.0.0.0` and will silently hijack ports.

## Prevention

- Always run `docker ps --format '{{.Names}} {{.Ports}}'` before troubleshooting port conflicts
- Use `ss -tlnp` to verify which process owns a port
- Never assume a port is free just because no local process (non-Docker) owns it
