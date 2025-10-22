#!/usr/bin/env python3
import os
from pathlib import Path
import sys

# Ensure ffmpeg is available via imageio-ffmpeg
try:
    import imageio_ffmpeg as iio
    ffmpeg_path = iio.get_ffmpeg_exe()
    ffmpeg_dir = str(Path(ffmpeg_path).parent)
    os.environ["PATH"] = ffmpeg_dir + os.pathsep + os.environ.get("PATH", "")
except Exception as e:
    print(f"[WARN] imageio-ffmpeg not available: {e}", file=sys.stderr)

from faster_whisper import WhisperModel

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "source_materials"
OUT_DIR = PROJECT_ROOT / "transcripts"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Model configuration
MODEL_SIZE = os.environ.get("WHISPER_MODEL", "small")  # tiny/base/small/medium/large-v3
COMPUTE_TYPE = os.environ.get("WHISPER_COMPUTE", "auto")  # auto / float16 / int8
LANG = os.environ.get("WHISPER_LANG", "ru")

print(f"[INFO] Loading model: {MODEL_SIZE} (compute={COMPUTE_TYPE})")
model = WhisperModel(MODEL_SIZE, device="auto", compute_type=COMPUTE_TYPE)

m4a_files = sorted(SRC_DIR.glob("*.m4a"))
if not m4a_files:
    print(f"[INFO] No .m4a files found in {SRC_DIR}")
    sys.exit(0)

for audio_path in m4a_files:
    out_txt = OUT_DIR / f"{audio_path.stem}.txt"
    if out_txt.exists():
        print(f"[SKIP] {audio_path.name} -> already exists: {out_txt.name}")
        continue
    print(f"[INFO] Transcribing: {audio_path.name} -> {out_txt.name}")
    segments, info = model.transcribe(str(audio_path), beam_size=1, language=LANG, vad_filter=True)

    with out_txt.open("w", encoding="utf-8") as f:
        f.write(f"# Transcript for {audio_path.name}\n")
        f.write(f"# Language: {info.language}, prob={info.language_probability:.2f}\n\n")
        for seg in segments:
            start = seg.start
            end = seg.end
            text = seg.text.strip()
            f.write(f"[{start:>7.2f} - {end:>7.2f}] {text}\n")

print(f"[DONE] Transcripts saved to {OUT_DIR}")




