# Hermes Update Breakage on Debian/Ubuntu

## The Problem

`hermes-update` (and `uv pip install --upgrade hermes-agent`) fails on Debian/Ubuntu systems because the system Python is externally managed. Two distinct failure modes:

### Failure Mode 1: Missing venv

```
error: Failed to inspect Python interpreter from active virtual environment at venv/bin/python3
  Caused by: Python interpreter not found at /home/realityrove/.hermes/hermes-agent/venv/bin/python3
```

The update process expects a venv at `~/.hermes/hermes-agent/venv/` but it's never been created or has been deleted.

### Failure Mode 2: --system on Externally-Managed Python

```
error: The interpreter at /usr is externally managed, and indicates the following:
  To install Python packages system-wide, try apt install python3-xyz
  If you wish to install a non-Debian-packaged Python package, create a virtual environment...
hint: Virtual environments were not considered due to the --system flag
```

This happens when `uv` is called with `--system` and the system Python reports itself as externally managed (Debian's README.venv check).

## Fix

### When venv is missing:

```bash
cd /home/realityrove/.hermes/hermes-agent
python3 -m venv venv
source venv/bin/activate
uv pip install --upgrade hermes-agent
```

### When --system fails on externally-managed python:

```bash
# Option A: Use a venv (recommended)
cd /home/realityrove/.hermes/hermes-agent
python3 -m venv venv
source venv/bin/activate
uv pip install --upgrade hermes-agent

# Option B: Override the check
uv pip install --break-system-packages --upgrade hermes-agent
```

### Option C: Use pip directly

```bash
pip3 install --user --upgrade hermes-agent
```

## Prevention

Always create the venv after initial install:

```bash
cd ~/.hermes/hermes-agent
python3 -m venv venv
```

If you're running Hermes from the repo (not pip), always activate the venv before running `hermes-update`.