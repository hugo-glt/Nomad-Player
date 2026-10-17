from pathlib import Path

# Error message for path input validation
def validate_library_path(path: str) -> Path:
    library_path = Path(path)
    if not library_path.exists():
        raise ValueError(f"The specified path does not exist: {library_path}")
    if not library_path.is_dir():
        raise ValueError(f"The specified path is not a directory: {library_path}")
    return library_path

def display_audio_files(library_path):
    path= Path(library_path)

    if path.is_dir():
        mp3_files = [file for file in path.iterdir()
                    if file.is_file() and file.suffix.lower() == ".mp3"]
