from __future__ import annotations

from pathlib import Path
import re
from datetime import datetime


def parse_filenames_from_merged(merged_path: Path) -> list[str]:
    if not merged_path.exists():
        return []
    text = merged_path.read_text(encoding="utf-8", errors="ignore")
    return re.findall(r"^# FILENAME:\s*(.+)$", text, flags=re.MULTILINE)


def format_ts(ts: float) -> str:
    # Local time, readable
    return datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M")


def audio_dates_for(files: list[str]) -> list[tuple[str, str, str]]:
    results: list[tuple[str, str, str]] = []
    for name in files:
        num = Path(name).stem  # e.g., "New Recording 14"
        audio = Path("source_materials") / f"{num}.m4a"
        created = modified = ""
        if audio.exists():
            st = audio.stat()
            # macOS provides st_birthtime; fallback to st_mtime if absent
            created_ts = getattr(st, "st_birthtime", st.st_mtime)
            created = format_ts(created_ts)
            modified = format_ts(st.st_mtime)
        results.append((name, created, modified))
    return results


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    merged = root / "all_transcripts.txt"
    files = parse_filenames_from_merged(merged)
    if not files:
        # Fallback to transcripts directory
        files = [p.name for p in sorted((root / "transcripts").glob("New Recording *.txt"))]

    print(f"COUNT {len(files)}")
    for name, created, modified in audio_dates_for(files):
        print(f"{name} | created: {created or '-'} | modified: {modified or '-'}")


if __name__ == "__main__":
    main()




