import os

def is_valid_directory(dir_path: str) -> bool:
    return os.path.isdir(dir_path)
