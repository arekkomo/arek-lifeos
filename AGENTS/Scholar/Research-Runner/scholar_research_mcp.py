#!/usr/bin/env python3
"""Constrained Phase 1 research MCP server for Scholar.

This server intentionally exposes one read-only tool. It cannot execute caller
commands, read browser profiles, access credentials, or change the source set.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

from mcp.server.fastmcp import FastMCP

ROOT = Path(__file__).resolve().parent
RUNNER = ROOT / "phase1_research.py"
PLANS = ROOT / "plans" / "mcp"
RUNS = ROOT / "runs"
ALLOWED_SOURCES = ["hackernews", "polymarket", "github", "digg", "arxiv", "techmeme", "grounding"]
REPO_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")

mcp = FastMCP("scholar-research")


def _clean_topic(value: str, name: str, maximum: int = 240) -> str:
    value = " ".join(value.split())
    if not value or len(value) > maximum:
        raise ValueError(f"{name} must be between 1 and {maximum} characters.")
    return value


def _make_plan(topic: str, intent: str, focus: str) -> dict:
    queries = [
        {
            "label": "primary",
            "search_query": topic,
            "ranking_query": f"What credible developments and discussion signals about {topic} appeared in the last 30 days?",
            "sources": ALLOWED_SOURCES,
            "weight": 1.0,
        }
    ]
    if focus:
        queries.append(
            {
                "label": "focus",
                "search_query": f"{topic} {focus}",
                "ranking_query": f"What recent evidence is most useful about {topic} and {focus}?",
                "sources": ALLOWED_SOURCES,
                "weight": 0.7,
            }
        )
    return {
        "intent": intent,
        "freshness_mode": "balanced_recent",
        "cluster_mode": "none",
        "subqueries": queries,
    }


@mcp.tool()
def research_phase1(
    topic: str,
    github_repo: str = "",
    focus: str = "",
    intent: Literal["breaking_news", "product", "comparison", "how_to", "opinion", "prediction", "factual", "concept"] = "concept",
) -> dict:
    """Run isolated, read-only research across Phase 1's fixed source allowlist.

    Coverage is always partial until `source_status` confirms sources completed.
    Reddit, X, browser cookies, credentials, social scrapers, and arbitrary shell
    execution are unavailable by design. Use `github_repo` only as owner/repo.
    """
    topic = _clean_topic(topic, "topic")
    focus = _clean_topic(focus, "focus", 160) if focus else ""
    github_repo = github_repo.strip()
    if github_repo and not REPO_RE.fullmatch(github_repo):
        raise ValueError("github_repo must be exactly owner/repository.")
    if not RUNNER.is_file():
        raise RuntimeError("Phase 1 runner is unavailable.")

    PLANS.mkdir(parents=True, exist_ok=True)
    RUNS.mkdir(parents=True, exist_ok=True)
    run_id = f"{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}-{uuid.uuid4().hex[:8]}"
    plan_path = PLANS / f"{run_id}.json"
    output_path = RUNS / f"{run_id}.json"
    plan_path.write_text(json.dumps(_make_plan(topic, intent, focus), indent=2) + "\n", encoding="utf-8")

    command = [
        sys.executable,
        str(RUNNER),
        topic,
        "--plan-file",
        str(plan_path),
        "--output",
        str(output_path),
    ]
    if github_repo:
        command.extend(["--github-repo", github_repo])

    completed = subprocess.run(
        command,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=180,
        check=False,
    )
    if completed.returncode != 0 or not output_path.is_file():
        # Do not relay arbitrary upstream output; the trusted wrapper retains its logs locally.
        raise RuntimeError("Phase 1 research did not complete. No result was returned.")

    report = json.loads(output_path.read_text(encoding="utf-8"))
    results = []
    allowed_items = [item for item in report.get("results", []) if item.get("source") in ALLOWED_SOURCES]
    for item in allowed_items[:20]:
        results.append(
            {
                "source": item.get("source"),
                "title": item.get("title"),
                "url": item.get("url"),
                "published_at": item.get("published_at"),
                "engagement": item.get("engagement", {}),
                "summary": (item.get("summary") or "")[:700],
            }
        )
    raw_source_status = report.get("source_status", {})
    source_status = {source: raw_source_status.get(source, "not-returned") for source in ALLOWED_SOURCES}
    return {
        "coverage": "partial",
        "window_days": report.get("window_days", 30),
        "source_status": source_status,
        "result_count": len(results),
        "results": results,
        "limitations": [
            "Reddit, X/Twitter, browser cookies, credentials, and social scrapers are disabled.",
            "Do not claim a community-wide or exhaustive discussion digest from this result.",
            "Use the cited URLs as evidence and state unavailable/no-result sources explicitly.",
        ],
    }


if __name__ == "__main__":
    mcp.run()
