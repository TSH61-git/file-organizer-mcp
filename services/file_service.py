# services/file_service.py
"""
File service for handling file operations like scanning, renaming, and organizing.
"""

import os
import shutil
from models.models import RenameFileIn, ScanFilesIn, MoveFilesIn
from services.path_validator import PathValidator


class FileService:
    """Service for handling file operations with security checks."""

    def __init__(self, allowed_directories=None):
        """
        Initialize FileService with allowed directories.
        
        Args:
            allowed_directories: List of directories where operations are allowed.
                                If None, defaults to a predefined list.
        """
        if allowed_directories is None:
            allowed_directories = [os.path.abspath(r"C:\Users\User\Downloads\TRY")]
        
        self.path_validator = PathValidator(allowed_directories)


    def scan_files(self, input: ScanFilesIn):
        """Scan files in a directory with preview of contents."""
        if not self.path_validator.is_path_safe(input.dir_path):
            return "שגיאה: הגישה לתיקייה זו חסומה מטעמי אבטחה. ניתן לגשת רק לתיקיות המוגדרות מראש."
        
        dir_path = input.dir_path
        max_preview_length = input.max_preview_length

        files_info = []
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file)[1]

                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()[:max_preview_length]
                except Exception:
                    content = "Unable to read content"

                files_info.append({
                    "file_name": file,
                    "file_extension": file_extension,
                    "content_preview": content
                })

        return files_info

    def rename_file(self, input: RenameFileIn):
        """Rename a file in a safe directory."""
        if not self.path_validator.is_path_safe(input.dir_path):
            return "שגיאה: הגישה לתיקייה זו חסומה מטעמי אבטחה. ניתן לגשת רק לתיקיות המוגדרות מראש."
        
        old_name = input.old_name
        new_name = input.new_name
        dir_path = input.dir_path

        old_path = os.path.join(dir_path, old_name)
        new_path = os.path.join(dir_path, new_name)

        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            return {"ok": True, "message": f"Renamed {old_name} to {new_name}"}
        elif os.path.exists(new_path):
            return {"ok": False, "error": "כבר קיים קובץ בשם הזה, שנה שם אחר כדי למנוע דריסה"}
        else:
            return {"ok": False, "error": "File not found"}

    def move_files(self, input: MoveFilesIn):
        """Move files to subdirectories based on their file types."""
        if not self.path_validator.is_path_safe(input.dir_path):
            return "שגיאה: הגישה לתיקייה זו חסומה מטעמי אבטחה. ניתן לגשת רק לתיקיות המוגדרות מראש."
        
        dir_path = input.dir_path
        file_types_map = input.file_types_map

        for ext, subfolder in file_types_map.items():
            subfolder_path = os.path.join(dir_path, subfolder)
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)

            for file in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file)
                if os.path.isfile(file_path) and file.endswith(ext):
                    shutil.move(file_path, os.path.join(subfolder_path, file))

        return {"ok": True, "message": "Files successfully moved."}
