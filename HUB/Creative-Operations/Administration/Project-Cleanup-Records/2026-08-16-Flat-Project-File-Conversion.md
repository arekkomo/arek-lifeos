---
title: Flat Project File Conversion
summary: Converted all CREATIVE project folders to the RRHub-compatible flat file schema.
created: 2026-08-16
---

# Flat Project File Conversion — 2026-08-16

## Result

- Flattened all non-episodic project folders; the sole permitted nested structure is `Imma-Nyala/EPISODES/EP01/` for episode-specific files.
- Classified and normalized 55 Markdown project files.
- Added matching RRHub/Vault metadata to every file: `type`, `title`, `project`, `stage`, `version`, and `updated`.
- All RRHub writing elements now use only: `song`, `script`, `scene_breakdown`, `shot_breakdown`, or `note`.

## Content decisions

- **Fog:** retained `fog_song.md` as the canonical lyrics-plus-Suno file; retired the duplicate lyric-only copy and retained separate production notes.
- **Little M:** merged its final lyric draft and Suno style prompt into `little-m_song.md`; retained research as production notes.
- **MEOW:** returned the stray Little M copy to the MEOW project as `meow_song_v02.md`; created a clearly marked placeholder `meow_script.md` so its existing shot breakdown has an RRHub source element.
- **Chaotic Baking:** preserved the `.bak` script as `chaotic-baking_script_v01.md` and retained the current script as canonical.

## Verification

- 55 files checked: all have valid shared metadata and a permitted RRHub `type`.
- No non-episodic project subfolders remain; `Imma-Nyala/EPISODES/EP01/` is the valid episodic exception.
- Legacy subfolder links inside project notes were updated to flat-file links.
