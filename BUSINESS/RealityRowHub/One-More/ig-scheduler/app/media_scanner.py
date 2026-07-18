"""Media folder scanner — detect new files, register posts."""
from pathlib import Path

ALLOWED = {".jpg", ".jpeg", ".png", ".mp4", ".mov", ".webm"}

def scan(db, *, media_root: Path) -> dict[str, int]:
    """Walk Media root. Register new assets + create posts if novel."""
    count = {"posts": 0, "assets": 0}

    try:
        entries = sorted(media_root.iterdir())
    except FileNotFoundError:
        return count

    for entry in entries:
        if not entry.is_dir() or entry.name.startswith(("_", ".")):
            continue

        dish = entry.name

        rows = db.execute("SELECT file_path FROM media_files WHERE dish_name=?", (dish,))
        seen = {r["file_path"] for r in rows}

        new_assets: list[Path] = []
        for fpath in sorted(entry.iterdir()):
            if not fpath.is_file():
                continue
            if fpath.suffix.lower() not in ALLOWED:
                continue
            fp = str(fpath)
            if fp not in seen:
                new_assets.append(fpath)

        if not new_assets:
            continue

        # Existing draft/detected post?
        cur = db.execute("SELECT id FROM posts WHERE dish_name=? AND status IN ('detected','draft')", (dish,))
        existing = cur.fetchone()
        post_id = existing["id"] if existing else None

        for af in new_assets:
            ft = "video" if af.suffix in {".mp4", ".mov", ".webm"} else "photo"
            db.execute(
                "INSERT OR IGNORE INTO media_files (post_id, file_path, file_name, dish_name, file_type) VALUES (?,?,?,?,?)",
                (post_id, str(af), af.name, dish, ft),
            )

        # If no draft post existed, create one and backfill
        if post_id is None:
            cur2 = db.execute("INSERT INTO posts (status, dish_name) VALUES ('detected', ?)", (dish,))
            post_id = cur2.lastrowid or db.execute("SELECT last_insert_rowid()").fetchone()[0]
            for af in new_assets:
                db.execute(
                    "UPDATE media_files SET post_id=? WHERE file_path=?",
                    (post_id, str(af)),
                )
            count["posts"] += 1
        count["assets"] += len(new_assets)

    # Flush all changes before returning so next request can see them
    db.commit()

    return count
