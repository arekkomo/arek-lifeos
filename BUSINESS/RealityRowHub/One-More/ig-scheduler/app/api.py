"""One More Instagram Scheduler — FastAPI app."""
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

# ── Config ─────────────────────────────────────────── #
PROJECT_ROOT = Path(__file__).parent.parent
MEDIA_ROOT   = PROJECT_ROOT / "Media" if (PROJECT_ROOT/"Media").exists() else \
               PROJECT_ROOT.parent.resolve() / "Media"
IG_POST_TIME_DEFAULT = "18:00"


# ── App ─────────────────────────────────────────── #
app = FastAPI(title="One More IG Scheduler")
app.mount("/static", StaticFiles(directory=str(PROJECT_ROOT / "static")), name="static")

from jinja2 import Environment, FileSystemLoader

_template_env = Environment(loader=FileSystemLoader(str(PROJECT_ROOT / "templates")))


def _render(template_name: str, **ctx) -> HTMLResponse:
    tpl = _template_env.get_template(template_name)
    return HTMLResponse(tpl.render(**ctx))


# ── Startup ───────────────────────────────────────── #

@app.on_event("startup")
async def startup():
    init_db()
    logger.info("Scheduler up — media root → %s", MEDIA_ROOT)


# ── Pages ──────────────────────────────────────────── #

def _fetch_rows(db):
    posts = db.execute(
        "SELECT p.*, COUNT(m.id) AS asset_count "
        "FROM posts p LEFT JOIN media_files m ON m.post_id=p.id GROUP BY p.id ORDER BY p.created_at DESC"
    )
    rows = []
    for r in posts:
        assets = db.execute("SELECT file_path, file_type FROM media_files WHERE post_id=?", (r["id"],))
        asset_list = [{"path": a["file_path"], "type": a["file_type"]} for a in assets]
        rows.append({**dict(r), "assets": asset_list})
    return rows


@app.get("/", response_class=HTMLResponse)
async def index():
    with get_db() as db:
        rows = _fetch_rows(db)
        status_counts = {}
        for s in ("detected", "draft", "scheduled", "published"):
            cnt = db.execute("SELECT COUNT(*) FROM posts WHERE status=?", (s,)).fetchone()[0]
            status_counts[s] = cnt
    return _render("index.html", rows=rows, status_counts=status_counts)


# ── HTMX partial ───────────────────────────────────── #

@app.get("/partials/schedule-grid", response_class=HTMLResponse)
async def schedule_grid_partial():
    with get_db() as db:
        rows = _fetch_rows(db)
    return _render("partials/schedule_grid.html", rows=rows)


# ── Mutations ─────────────────────────────────────── #

@app.post("/api/scan")
async def api_scan():
    with get_db() as db:
        result = scan_media(db, media_root=MEDIA_ROOT)
        db.commit()
    return {"scanned": True, **result}


@app.post("/api/posts/{post_id}/caption")
async def api_generate_caption(post_id: int):
    with get_db() as db:
        info = db.execute("SELECT * FROM posts WHERE id=?", (post_id,))
        p = info.fetchone()
        if not p:
            raise HTTPException(404, "Post not found")

        assets_raw = db.execute("SELECT file_path FROM media_files WHERE post_id=?", (post_id,))
        asset_paths = [Path(r["file_path"]) for r in assets_raw]

        caption = generate_caption(p["dish_name"], asset_paths)
        db.execute(
            "UPDATE posts SET status='draft', caption=? WHERE id=?",
            (caption, post_id),
        )
        db.commit()
    return {"post_id": post_id, "caption": caption}


@app.post("/api/posts/{post_id}/schedule")
async def api_schedule_post(post_id: int):
    with get_db() as db:
        p = db.execute("SELECT id FROM posts WHERE id=?", (post_id,)).fetchone()
        if not p:
            raise HTTPException(404, "Post not found")

        now = datetime.now(timezone.utc)
        h, m = map(int, IG_POST_TIME_DEFAULT.split(":"))
        target = now.replace(hour=h, minute=m, second=0, microsecond=0)
        if target <= now:
            target += timedelta(days=1)
        db.execute(
            "UPDATE posts SET status='scheduled', scheduled_at=? WHERE id=?",
            (target.isoformat(), post_id),
        )
        db.commit()
    return {"post_id": post_id, "scheduled_at": target.isoformat()}


@app.put("/api/posts/{post_id}/caption")
async def api_update_caption(post_id: int, request: Request):
    body = await request.json()
    new_cap = body.get("caption", "").strip()
    with get_db() as db:
        db.execute("UPDATE posts SET caption=? WHERE id=?", (new_cap, post_id))
        db.commit()
    return {"ok": True}


@app.delete("/api/posts/{post_id}")
async def api_delete_post(post_id: int):
    with get_db() as db:
        db.execute("DELETE FROM media_files WHERE post_id=?", (post_id,))
        db.execute("DELETE FROM posts WHERE id=?", (post_id,))
        db.commit()
    return {"ok": True}


# ── Media preview ─────────────────────────────── #

@app.get("/media/preview/{file_path:path}")
async def media_preview(file_path: str):
    full = Path(file_path).resolve()
    if not full.exists():
        raise HTTPException(404, "File not found")
    if not str(full).startswith(str(MEDIA_ROOT.resolve())) and \
       not str(full).startswith(str(PROJECT_ROOT.resolve())):
        raise HTTPException(403, "Not a project asset")
    ct = mimetypes.guess_type(str(full)) or ("application/octet-stream", None)
    return FileResponse(str(full), media_type=ct[0])
