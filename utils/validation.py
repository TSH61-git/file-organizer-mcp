"""
Validation utilities for the application.
Provides general-purpose validation functions for various data types and paths.
"""

import os
from typing import Any


def is_valid_directory(dir_path: str) -> bool:
    """
    Check if the provided path is a valid directory.
    
    Args:
        dir_path: Path to check
        
    Returns:
        True if path exists and is a directory, False otherwise
    """
    return os.path.isdir(dir_path)


def is_valid_file(file_path: str) -> bool:
    """
    Check if the provided path is a valid file.
    
    Args:
        file_path: Path to check
        
    Returns:
        True if path exists and is a file, False otherwise
    """
    return os.path.isfile(file_path)


def is_empty_string(value: str) -> bool:
    """
    Check if a string is empty or contains only whitespace.
    
    Args:
        value: String to check
        
    Returns:
        True if string is empty or whitespace, False otherwise
    """
    return not value or not value.strip()


def is_valid_filename(filename: str) -> bool:
    """
    Check if a filename is valid (no illegal characters).
    
    Args:
        filename: Filename to validate
        
    Returns:
        True if filename is valid, False otherwise
    """
    illegal_chars = r'<>:"/\|?*'
    return not any(char in filename for char in illegal_chars)
