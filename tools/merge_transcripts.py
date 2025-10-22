from pathlib import Path


def collect_transcripts(transcripts_dir: Path) -> list[Path]:
    """Return sorted list of transcript files matching 'New Recording *.txt'."""
    files = sorted(transcripts_dir.glob('New Recording *.txt'))
    return files


def merge_transcripts(files: list[Path], output_path: Path) -> None:
    """Merge transcript files into one text file with clear separators."""
    output_lines: list[str] = []
    for file_path in files:
        output_lines.append('---\n')
        output_lines.append(f'# FILENAME: {file_path.name}\n')
        output_lines.append('---\n')
        content = file_path.read_text(encoding='utf-8', errors='ignore')
        output_lines.append(content)
        if not content.endswith('\n'):
            output_lines.append('\n')
        output_lines.append('\n')
    output_path.write_text(''.join(output_lines), encoding='utf-8')


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    transcripts_dir = project_root / 'transcripts'
    output_path = project_root / 'all_transcripts.txt'

    transcripts_dir.mkdir(exist_ok=True)
    files = collect_transcripts(transcripts_dir)
    if not files:
        print('[WARN] No transcripts found matching pattern: New Recording *.txt')
        output_path.write_text('', encoding='utf-8')
        return

    merge_transcripts(files, output_path)
    print(f'[DONE] Merged {len(files)} files → {output_path}')


if __name__ == '__main__':
    main()








