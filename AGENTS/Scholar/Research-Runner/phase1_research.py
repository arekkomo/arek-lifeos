#!/usr/bin/env python3
"""Run Last30Days in an isolated, no-cookie/no-Reddit Phase 1 mode.

This wrapper intentionally does not invoke the upstream setup wizard. It
runs only an explicit source allowlist and starts the engine with a sanitized
environment, so Scholar never receives browser, cookie, shell, or credential
access merely to request research.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ENGINE = ROOT / "vendor" / "last30days-skill" / "skills" / "last30days" / "scripts" / "last30days.py"
RUNS = ROOT / "runs"
SOURCES = "hackernews,polymarket,github,digg,arxiv,techmeme,grounding"
# Defense in depth: explicit --search is the allowlist, and this disables every
# source that could use social cookies, scraping, external paid data, or a local corpus.
EXCLUDED = (
    "reddit,x,youtube,tiktok,instagram,bluesky,truthsocial,threads,pinterest,"
    "trustpilot,xiaohongshu,linkedin,perplexity,dripstack,stocktwits,corpus,jobs"
)


def sanitized_environment() -> dict[str, str]:
    """Pass minimal runtime state; deliberately omit all ambient API keys/tokens."""
    keep = ("PATH", "HOME", "LANG", "LC_ALL", "TERM", "TMPDIR", "XDG_CACHE_HOME", "XDG_CONFIG_HOME")
    env = {key: os.environ[key] for key in keep if os.environ.get(key)}
    env.update(
        {
            "FROM_BROWSER": "off",
            "EXCLUDE_SOURCES": EXCLUDED,
            "INCLUDE_SOURCES": "",
            "LAST30DAYS_DEFAULT_SEARCH": SOURCES,
            "LAST30DAYS_MEMORY_DIR": str(RUNS),
            # Prevent the runner from treating a caller's native search setting as authority.
            "LAST30DAYS_NATIVE_SEARCH": "",
        }
    )
    return env


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Phase 1 research with an explicit safe source allowlist.")
    parser.add_argument("topic", help="Research topic; the upstream engine uses its standard 30-day time window.")
    parser.add_argument("--deep", action="store_true", help="Use the engine's deeper result profile.")
    parser.add_argument("--output", type=Path, help="Optional exact JSON output file path.")
    args = parser.parse_args()

    if not ENGINE.is_file():
        parser.error(f"Pinned upstream engine is missing: {ENGINE}")

    RUNS.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    output = args.output or RUNS / f"{stamp}-phase1.json"
    output.parent.mkdir(parents=True, exist_ok=True)

    command = [
        sys.executable,
        str(ENGINE),
        args.topic,
        "--no-browser-cookies",
        "--search",
        SOURCES,
        "--emit=json",
        "--output",
        str(output),
        "--save-dir",
        str(RUNS),
    ]
    if args.deep:
        command.append("--deep")

    print("Phase 1 source allowlist:", SOURCES, file=sys.stderr)
    print("Hard-disabled:", EXCLUDED, file=sys.stderr)
    result = subprocess.run(command, env=sanitized_environment(), text=True)
    if result.returncode == 0:
        print(f"RESULT_JSON={output}")
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
