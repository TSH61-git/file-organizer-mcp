"""
Data models for file operations.
Defines Pydantic models for input validation of file-related operations.
"""

from pydantic import BaseModel


class RenameFileIn(BaseModel):
    """Model for file renaming operation input."""
    old_name: str
    new_name: str
    dir_path: str


class ScanFilesIn(BaseModel):
    """Model for directory scanning operation input."""
    dir_path: str
    max_preview_length: int = 100


class MoveFilesIn(BaseModel):
    """Model for file moving/organization operation input."""
    dir_path: str
    file_types_map: dict
