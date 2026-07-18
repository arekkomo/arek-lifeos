"""Synchronous SQLite database layer with schema init."""
import sqlite3
from contextlib import contextmanager
from pathlib import Path

DB_DIR = Path(__file__).parent.parent / "instance"
SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS media_files (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id     INTEGER REFERENCES posts(id) ON DELETE SET NULL,
    file_path   TEXT    NOT NULL UNIQUE,
    file_name   TEXT    NOT NULL,
    dish_name   TEXT    NOT NULL,
    file_type   TEXT    DEFAULT 'photo',
    created_at  TIMESTAMP DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS posts (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    status        TEXT    DEFAULT 'detected',
    dish_name     TEXT    NOT NULL,
    caption       TEXT    DEFAULT '',
    notes         TEXT    DEFAULT '',
    scheduled_at  TIMESTAMP,
    created_at    TIMESTAMP DEFAULT (datetime('now')),
    posted_at     TIMESTAMP,
    ig_media_id   TEXT
);

CREATE INDEX IF NOT EXISTS idx_posts_status ON posts(status);
CREATE INDEX IF NOT EXISTS idx_dish_status ON posts(dish_name, status);
"""

@contextmanager
def get_db():
    """Yield a synchronous sqlite3 connection with Row factory."""
    DB_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_DIR / "schedule.db"))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    """Ensure schema exists (call once at startup)."""
    with get_db() as conn:
        conn.executescript(SCHEMA_SQL)
        conn.commit()
