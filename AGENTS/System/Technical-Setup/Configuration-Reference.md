# Configuration Reference
> Maintained by: System
> Installation notes customized for your specific hardware

## DGX Spark — System Configuration

### OS & Core Software (preinstalled)
- **OS:** NVIDIA DGX OS (optimized for AI workloads)
- **Runtime:** CUDA, cuDNN, NVIDIA Container Runtime
- **Containers:** Docker + NGC (NVIDIA container registry)
- **Frameworks:** PyTorch, TRT-LLM (preinstalled)
- **Reference:** https://build.nvidia.com/spark

### Access Methods
- **Local:** Keyboard/mouse/monitor direct
- **Remote:** SSH, NVIDIA Sync, or remote desktop (same network)
- **Hybrid:** Both simultaneously supported

### System Updates
- **Primary method:** DGX Dashboard (recommended — ensures driver/firmware compatibility)
- **Manual fallback** (terminal):
  ```
  sudo apt update && sudo apt dist-upgrade
  sudo fwupdmgr refresh && sudo fwupdmgr upgrade
  sudo reboot
  ```
- **Pre-update checklist:** stable power, save all work, close running models
- **Edition:** Founders Edition (update procedure may differ from OEM units)
- **Dashboard docs:** https://docs.nvidia.com/dgx/dgx-spark/dgx-dashboard.html

### ComfyUI Setup
- **CUDA version:** [Fill in — check with `nvcc --version`]
- **Python version:** [Fill in — check with `python3 --version`]
- **ComfyUI path:** [Fill in]
- **Models location:** [Fill in]
- **Custom nodes:** [List installed]

---

## MacBook — Development Setup
- **OS:** macOS Tahoe 26.3.1
- **Package manager:** Homebrew
- **Node version:** [Fill in — `node --version`]
- **Python version:** [Fill in — `python3 --version`]
- **Key paths:** [Fill in]

---

## n8n Setup
- **Instance:** [Self-hosted / Cloud]
- **URL:** [Fill in]
- **Key workflows:** [List active workflows]

---

## API Keys & Services
> DO NOT store actual keys here — note what services are configured only
- Anthropic API: Configured
- [Other services]: [Status]

---

## CoWork MCP Connectors

### apple-mcp (installed 2026-04-29)
- **Source:** https://github.com/supermemoryai/apple-mcp
- **Install:** `npx -y install-mcp apple-mcp --client claude`
- **Tools active:** Calendar, Contacts, Maps, Messages, Notes, Reminders
- **Disabled (do not use):** Mail — Arek uses Gmail in browser, not Apple Mail
- **Relevant agents:** Operator (Reminders, Messages), Connector (Contacts), Director (Calendar)

### Apple Notes MCP (separate connector)
- Native Apple Notes read/write — overlaps with apple-mcp notes tool
- Prefer this for Notes operations (more stable, already integrated)

### Google Calendar MCP (separate connector)
- Overlaps with apple-mcp calendar tool
- Prefer this for Calendar operations

## Last Updated
2026-04-29
