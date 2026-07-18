"""Media folder scanner — detect new files, register posts."""
import logging
from pathlib import Path

logger = logging.getLogger("one-more.scheduler")

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".mp4", ".mov", ".webm"}

def _is_media(filename: str) -> bool:
    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS

async def scan(db, *, media_root: Path):
    """Walk Media root. Register new assets + create posts if novel."""
    count_new = {"posts": 0, "assets": 0}

    try:
        entries = sorted(media_root.iterdir())
    except FileNotFoundError:
        logger.warning("Media root %s not found — nothing to scan", media_root)
        return count_new

    for entry in entries:
        if not entry.is_dir():
            continue
        if entry.name.startswith("_") or entry.name.startswith("."):
            continue  # skip hidden/temp folders

        dish = entry.name

        # What files are already seen?
        rows = await db.execute("SELECT file_path FROM media_files WHERE dish_name=?", (dish,))
        seen_paths: set[str] = {r["file_path"] for r in rows}

        new_assets: list[Path] = []
        for fpath in sorted(entry.iterdir()):
            if not fpath.is_file():
                continue
            if not _is_media(fpath.name):
                continue
            fp_str = str(fpath)
            if fp_str not in seen_paths:
                new_assets.append(fpath)

        if not new_assets:
            continue

        # Does a draft/detected post for this dish already exist?
        cur = await db.execute(
            "SELECT id FROM posts WHERE dish_name=? AND status IN ('detected','draft')",
            (dish,),
        )
        existing = await cur.fetchone()
        post_id = existing["id"] if existing else None

        for af in new_assets:
            is_video = af.suffix in {".mp4", ".mov", ".webm"}
            await db.execute(
                "INSERT INTO media_files (post_id, file_path, file_name, dish_name, file_type) VALUES (?,?,?,?,?)",
                (post_id, str(af), af.name, dish, "video" if is_video else "photo"),
            )

        # If no draft post existed, create one and backfill post_ids
        if post_id is None:
            cur2 = await db.execute(
                "INSERT INTO posts (status, dish_name) VALUES ('detected', ?)",
                (dish,),
            )
            new_post_id = cur2.lastrowid
            for af in new_assets:
                await db.execute(
                    "UPDATE media_files SET post_id=? WHERE file_path=?",
                    (new_post_id, str(af)),
                )
            count_new["posts"] += 1
        count_new["assets"] += len(new_assets)

    return count_new
