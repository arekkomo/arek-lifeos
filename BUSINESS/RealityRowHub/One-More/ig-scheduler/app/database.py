"""Async SQLite database layer with schema init."""
import aiosqlite
from pathlib import Path

DB_DIR = Path(__file__).parent.parent / "instance"
SCHEMA_SQL = """
-- media_files: one row per asset discovered in Media/<dish>/
CREATE TABLE IF NOT EXISTS media_files (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id     INTEGER REFERENCES posts(id) ON DELETE SET NULL,
    file_path   TEXT    NOT NULL UNIQUE,
    file_name   TEXT    NOT NULL,
    dish_name   TEXT    NOT NULL,
    file_type   TEXT    DEFAULT 'photo',  -- photo | video
    created_at  TIMESTAMP DEFAULT (datetime('now')),
    scheduled   BOOLEAN DEFAULT 0
);

-- posts: queued content (one or more media_files + caption)
CREATE TABLE IF NOT EXISTS posts (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    status        TEXT    DEFAULT 'detected',  -- detected | draft | scheduled | published
    dish_name     TEXT    NOT NULL,
    caption       TEXT    DEFAULT '',
    notes         TEXT    DEFAULT '',
    scheduled_at  TIMESTAMP,
    created_at    TIMESTAMP DEFAULT (datetime('now')),
    posted_at     TIMESTAMP,
    ig_media_id   TEXT    NULL  -- Instagram media ID after publication
);

-- index for fast status lookups
CREATE INDEX IF NOT EXISTS idx_posts_status ON posts(status);
CREATE INDEX IF NOT EXISTS idx_dish_status ON posts(dish_name, status);
"""

async def get_db():
    """Return a new async sqlite connection."""
    DB_DIR.mkdir(parents=True, exist_ok=True)
    conn = await aiosqlite.connect(str(DB_DIR / "schedule.db"))
    conn.row_factory = aiosqlite.Row
    return conn

async def init_db():
    """Ensure schema exists."""
    async with (await get_db()) as conn:
        await conn.executescript(SCHEMA_SQL)
        await conn.commit()
