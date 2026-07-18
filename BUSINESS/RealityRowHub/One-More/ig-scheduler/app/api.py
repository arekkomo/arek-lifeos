"""One More Instagram Scheduler — main FastAPI app."""
from __future__ import annotations
import logging
import mimetypes
from datetime import datetime, timedelta, timezone
from pathlib import Path

from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse

from .database import get_db, init_db
from .media_scanner import scan as scan_media
from .caption import generate_caption

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("one-more.scheduler")

# ── Config ──────────────────────────────────────────────── #
PROJECT_ROOT = Path(__file__).parent.parent
MEDIA_ROOT   = Path(
    PROJECT_ROOT / "Media" if (PROJECT_ROOT/"Media").exists()
    else PROJECT_ROOT.parent.resolve() / "Media"  # also try parent (BUSINESS level)
)

IG_POST_TIME_DEFAULT = "18:00"
OPENAI_API_KEY       = ""  # loaded from env at startup

def _load_env():
    """Lightweight .env loader (no python-dotenv dep)."""
    global OPENAI_API_KEY, MEDIA_ROOT
    env_path = PROJECT_ROOT / ".env"
    if not env_path.exists():
        return
    d = {}
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            d[k.strip()] = v.strip().strip('"').strip("'")
    OPENAI_API_KEY = d.get("OPENAI_API_KEY", "")

# ── App factory ─────────────────────────────────────────── #

app = FastAPI(title="One More IG Scheduler")

# Static: images, styles, favicon
app.mount("/static", StaticFiles(directory=str(PROJECT_ROOT / "static")), name="static")


@app.on_event("startup")
async def startup():
    _load_env()
    await init_db()
    logger.info("Scheduler started — media root → %s", MEDIA_ROOT)


# ── Templates (server-side Jinja + HTMX swaps) ───────────── #

from jinja2 import Environment, FileSystemLoader

_template_env = Environment(
    loader=FileSystemLoader(str(PROJECT_ROOT / "templates")),
)
_template_env.globals.update({  # helpers available in templates
    "datetime": datetime,
})


def _render(template_name: str, **ctx):
    tpl = _template_env.get_template(template_name)
    return tpl.render(**ctx)


# ── Pages ─────────────────────────────────────────────────── #

@app.get("/", response_class=HTMLResponse)
async def index():
    async with await get_db() as db:
        posts = await db.execute(
            "SELECT p.*, COUNT(m.id) AS asset_count "
            "FROM posts p LEFT JOIN media_files m ON m.post_id=p.id GROUP BY p.id ORDER BY p.created_at DESC"
        )
        rows = []
        for r in await posts.fetchall():
            # grab primary asset path
            assets = await db.execute("SELECT file_path, file_type FROM media_files WHERE post_id=?", (r["id"],))
            asset_rows = await assets.fetchall()
            rows.append({**dict(r), "assets": [{"path": a["file_path"], "type": a["file_type"]} for a in asset_rows]})

        # summary counts by status
        status_counts = {}
        for s in ("detected", "draft", "scheduled", "published"):
            cur = await db.execute("SELECT COUNT(*) FROM posts WHERE status=?", (s,))
            row = await cur.fetchone()
            status_counts[s] = row["COUNT(*)"]

        return _render("index.html", rows=rows, status_counts=status_counts)


# ── HTMX partials ─────────────────────────────────────────── #

@app.get("/partials/schedule-grid")
async def schedule_grid():
    """Return just the table body — swapped via HTMX."""
    async with await get_db() as db:
        posts = await db.execute(
            "SELECT p.*, COUNT(m.id) AS asset_count "
            "FROM posts p LEFT JOIN media_files m ON m.post_id=p.id GROUP BY p.id ORDER BY p.created_at DESC"
        )
        rows = []
        for r in await posts.fetchall():
            assets = await db.execute("SELECT file_path, file_type FROM media_files WHERE post_id=?", (r["id"],))
            asset_rows = await assets.fetchall()
            rows.append({**dict(r), "assets": [{"path": a["file_path"], "type": a["file_type"]} for a in asset_rows]})
    return _render("partials/schedule_grid.html", rows=rows)


# ── Mutations ───────────────────────────────────────── ──── #

@app.post("/api/scan")
async def api_scan():
    """Manually trigger folder scan."""
    async with await get_db() as db:
        result = await scan(db, media_root=MEDIA_ROOT)
    return {"scanned": True, **result}


@app.post("/api/posts/{post_id}/caption")
async def api_generate_caption(post_id: int):
    """Generate caption for a post (detected → draft)."""
    async with await get_db() as db:
        info = await db.execute("SELECT * FROM posts WHERE id=?", (post_id,))
        p = (await info.fetchone())
        if not p:
            raise HTTPException(404, "Post not found")

        assets_raw = await db.execute("SELECT file_path FROM media_files WHERE post_id=?", (post_id,))
        asset_paths = [Path(r["file_path"]) for r in await assets_raw.fetchall()]

        caption = await generate_caption(p["dish_name"], asset_paths, api_key=OPENAI_API_KEY)

        await db.execute(
            "UPDATE posts SET status='draft', caption=? WHERE id=?",
            (caption, post_id),
        )
    return {"post_id": post_id, "caption": caption}


@app.post("/api/posts/{post_id}/schedule")
async def api_schedule_post(post_id: int):
    """Mark a post as scheduled at DEFAULT_POST_TIME next slot."""
    async with await get_db() as db:
        info = await db.execute("SELECT * FROM posts WHERE id=?", (post_id,))
        p = (await info.fetchone())
        if not p:
            raise HTTPException(404, "Post not found")

        now = datetime.now(timezone.utc)
        h, m = map(int, IG_POST_TIME_DEFAULT.split(":"))
        target = now.replace(hour=h, minute=m, second=0, microsecond=0)
        if target <= now:
            target += timedelta(days=1)
        await db.execute(
            "UPDATE posts SET status='scheduled', scheduled_at=? WHERE id=?",
            (target.isoformat(), post_id),
        )
    return {"post_id": post_id, "scheduled_at": p["scheduled_at"] if not p else target.isoformat()}


@app.post("/api/posts/{post_id}/edit_caption")
async def api_edit_caption(post_id: int, request: Request):
    """User-edited caption override."""
    body = await request.json()
    caption = body.get("caption", "").strip()
    async with await get_db() as db:
        await db.execute(
            "UPDATE posts SET caption=? WHERE id=?",
            (caption, post_id),
        )
    return {"ok": True}


@app.post("/api/posts/{post_id}/delete")
async def api_delete_post(post_id: int):
    """Remove a post + associated media refs."""
    async with await get_db() as db:
        await db.execute("DELETE FROM media_files WHERE post_id=?", (post_id,))
        await db.execute("DELETE FROM posts WHERE id=?", (post_id,))
    return {"ok": True}


# ── Media preview ──────────────────────────────────────── #

@app.get("/media/preview/{file_path:path}")
async def media_preview(file_path: str):
    """Serve a local asset for preview in the UI."""
    full = Path(file_path).resolve()
    if not full.exists():
        raise HTTPException(404, "File not found")
    # Safety: only serve under known Media roots
    if not str(full).startswith(str(MEDIA_ROOT.resolve())) and not str(full).startswith(str(PROJECT_ROOT.resolve())):
        raise HTTPException(403, "Not a project asset")
    content_type = mimetypes.guess_type(str(full)) or ("application/octet-stream", None)
    return FileResponse(str(full), media_type=content_type[0])
