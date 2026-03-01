"""
Path validation and security checks for file operations.
Ensures that file operations are restricted to safe, allowed directories.
"""

import os
from typing import List


class PathValidator:
    """Validates file paths for security and safety."""
    
    def __init__(self, allowed_directories: List[str] = None):
        """
        Initialize the path validator with a list of allowed directories.
        
        Args:
            allowed_directories: List of directories that operations are allowed in
        """
        self.allowed_directories = allowed_directories or []
    
    def is_path_safe(self, requested_path: str) -> bool:
        """
        Check if a requested path is within the allowed directories.
        
        Args:
            requested_path: The path to validate
            
        Returns:
            True if path is safe and within allowed directories, False otherwise
        """
        if not self.allowed_directories:
            return False
        
        target_path = os.path.abspath(requested_path)
        for allowed_dir in self.allowed_directories:
            allowed_abs = os.path.abspath(allowed_dir)
            if target_path.startswith(allowed_abs + os.sep) or target_path == allowed_abs:
                return True
        return False
    
    def add_allowed_directory(self, directory: str) -> None:
        """
        Add a directory to the list of allowed directories.
        
        Args:
            directory: Path to allow
        """
        abs_path = os.path.abspath(directory)
        if abs_path not in self.allowed_directories:
            self.allowed_directories.append(abs_path)
    
    def remove_allowed_directory(self, directory: str) -> None:
        """
        Remove a directory from the list of allowed directories.
        
        Args:
            directory: Path to disallow
        """
        abs_path = os.path.abspath(directory)
        if abs_path in self.allowed_directories:
            self.allowed_directories.remove(abs_path)
