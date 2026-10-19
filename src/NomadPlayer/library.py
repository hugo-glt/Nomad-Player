from pathlib import Path

SUPPORTED_EXTENSIONS = {".mp3", ".flac", ".wav", ".ogg", ".m4a"}

# Error message for path input validation
def validate_library_path(path: str) -> Path:
    library_path = Path(path)
    if not library_path.exists():
        raise ValueError(f"The specified path does not exist: {library_path}")
    if not library_path.is_dir():
        raise ValueError(f"The specified path is not a directory: {library_path}")
    return library_path

def scan_audio_files(library_path: Path) -> list[Path]:
    return [
        file for file in library_path.rglob("*")
        if file.is_file() and file.suffix.lower() in SUPPORTED_EXTENSIONS
    ]
