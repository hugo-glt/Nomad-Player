from pathlib import Path


def validate_library_path(path: str) -> Path:
    library_path = Path(path)
    if not library_path.exists():
        raise ValueError(f"The specified path does not exist: {library_path}")
    if not library_path.is_dir():
        raise ValueError(f"The specified path is not a directory: {library_path}")
    return library_path