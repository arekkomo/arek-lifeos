# SSH Pitfalls & Server Maintenance Quick Reference

## SSH Connection Drops

### `netplan apply` kills SSH over WiFi
`sudo netplan apply` restarts network interfaces. If connected via WiFi (`wlP*`), the interface gets reset and SSH drops mid-command with "Operation timed out" / "Broken pipe".

**Prevention:**
- Always SSH into wired IP when doing netplane (e.g., `ssh realityrove@10.0.0.61` for enP7s7 on DGX Spark)
- Or start `tmux` before running netplane: `tmux && sudo netplane apply` (survives disconnects)
- Check your connection: `ip route | grep default` — if it shows `dev wlP9s9`, don't run netplane

### Enable SSH Keepalive
Prevents idle connections from silently dropping. Add to `~/.ssh/config`:
```
Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
```
Sends a keepalive ping every 60 seconds (3 allowed failures).

## Firmware Management

### Check firmware updates
```bash
fwupdmgr get-upgrades    # list available updates
fwupdmgr update          # apply all updates
```

### Suppress upload prompts
When prompted about uploading firmware reports, press `y` to disable future prompts.
Alternatively: `fwupdmgr disable-upload`

## Zombie Process Check
If your system prompt mentions zombie processes, check:
```bash
ps aux | grep ' Z'
```
Occasional zombies are normal (init reaps them). Persistent ones may indicate a misbehaving service.
