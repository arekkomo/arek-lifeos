---
name: gateway-remote-access
domain: system
version: 1.0
description: Connect local GUI clients (Hermes Desktop App, MCP clients, any GUI) to a remote Hermes gateway running on a server. Covers SSH tunneling, port forwarding, and verifying gateway network binding.
updated: 2026-06-04
tags: [gateway, ssh, tunnel, remote, desktop, client, networking]
---

# Gateway Remote Access

Connect any local GUI or CLI client to a Hermes gateway running on a remote server. The gateway holds all state (Telegram/Discord connections, skills, memory, cron jobs, model config); the client is just a thin frontend.

## When This Pattern Applies

- New Hermes Desktop App on a different machine than the gateway
- Remote CLI access (SSH session running `hermes chat`)
- Connecting MCP clients or IDE plugins to a remote gateway
- Any GUI tool that talks to the Hermes gateway API

## Prerequisites

1. Gateway must be **listening on a LAN-binding address** (not `127.0.0.1` only)
2. SSH access to the gateway server must be available
3. No firewall blocking the gateway port

## Step-by-Step

### 1. Verify Gateway is LAN-Accessible

On the gateway server:
```bash
ss -tlnp | grep <gateway_port>
```
- Look for `0.0.0.0:<port>` or `[::]:<port>` binding — **not** `127.0.0.1:<port>`
- Default Hermes gateway port is `8080`

If bound to `127.0.0.1`, check `config.yaml` for `gateway.host` or `network.bind` settings. Set to `0.0.0.0` to allow LAN connections.

### 2. Create SSH Tunnel from Client Machine

On the **client** machine (Mac, Windows, another Linux):
```bash
ssh -fNL <local_port>:127.0.0.1:<remote_gateway_port> <user>@<server_host>
```

Example (Mac → DGX Spark):
```bash
ssh -fNL 9090:10.0.0.61:8080 realityrove@10.0.0.61
```

- `-f` — background mode
- `-N` — no command (tunnel only)
- `-L <local>:<remote_host>:<remote_port>` — forward mapping

**If the gateway is on the same host as SSH** (most common), use:
```bash
ssh -fNL <local_port>:127.0.0.1:<remote_gateway_port> <user>@<server_host>
```
The tunnel connects to `127.0.0.1` on the **server side**, which is correct — SSH forwards it there.

### 3. Verify Tunnel Works

```bash
# Check gateway responds through tunnel
curl http://localhost:<local_port>/api/status
```

### 4. Configure the Client

Point the Desktop app (or any GUI client) to: `ws://127.0.0.1:<local_port>`

## Persistent Tunnel on macOS

Add to `~/.ssh/config` on the **client** machine:
```ssh-config
Host <alias>
    HostName <server_host_or_ip>
    User <username>
    LocalForward <local_port> 127.0.0.1:<remote_gateway_port>
    ExitOnForwardFailure yes
    ServerAliveInterval 60
    ServerAliveCountMax 3
```

Then: `ssh -fN <alias>`

The `ServerAliveInterval` prevents the tunnel from dying on idle connections.

## Troubleshooting

### Gateway shows `127.0.0.1:<port>` in `ss -tlnp`
The gateway is only listening on loopback. Check `config.yaml` for `gateway.host` or `network.bind` settings. May need to set it to `0.0.0.0` (the default in most installs).

### Tunnel drops after a few minutes
Missing keepalive. Add `ServerAliveInterval 60` to SSH config. Firewall or NAT timeout may also kill idle connections.

### Client reports connection refused
Verify the gateway host/port in the tunnel command matches where the gateway is actually listening. Check `ss -tlnp` on the server for the correct port.

### Gateway port shows `::` (IPv6) but client uses IPv4
The `[::]:8080` binding covers both IPv6 and IPv4. Should work fine. If not, explicitly bind to `0.0.0.0`.

## Important

- **All state stays on the server.** Session context, skills, memory, tool state, and messaging platform integrations remain on the gateway server. The tunnel is purely a transport for the client connection.
- **The LLM model provider** (Ollama, OpenRouter, etc.) is configured on the server and does not need to be accessible from the client.
- **Do NOT expose the gateway port directly to the internet.** Always use SSH tunneling or a VPN.

## Related Skills

- `hermes-agent` — general Hermes gateway setup and config
- `hermes-gateway` — gateway management (start/stop, health checks)
