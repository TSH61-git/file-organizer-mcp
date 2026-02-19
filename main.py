from __future__ import annotations
import asyncio
from mcp.server.fastmcp import FastMCP
from services.file_service import FileService
from models.models import RenameFileIn, ScanFilesIn, MoveFilesIn

# Initialization
mcp = FastMCP("Organizer")
file_service = FileService()

# --- Tools ---

@mcp.tool()
async def scan_files(dir_path: str, max_preview_length: int = 500) -> dict:
    """
    Comprehensive directory scanner for listing files and retrieving content previews.
    
    Use this tool to understand the file structure of a given path, identify file types, 
    and read the beginning of text-based files. It supports various formats including 
    source code, logs, and data files.
    
    Args:
        dir_path: The absolute path to the directory (must be within the allowed whitelist).
        max_preview_length: Number of characters to read from each file (default is 500).
    """
    input_data = ScanFilesIn(dir_path=dir_path, max_preview_length=max_preview_length)
    files_info = await asyncio.to_thread(file_service.scan_files, input_data)
    return {"ok": True, "files": files_info}

@mcp.tool()
async def rename_file(old_name: str, new_name: str, dir_path: str) -> dict:
    """
    Renames a single file within a specified directory.
    
    Use this tool for organizational tasks such as correcting typos, adding timestamps, 
    or updating file versioning. Ensure the new name includes the correct file extension.
    
    Args:
        old_name: The current name of the file.
        new_name: The desired new name for the file.
        dir_path: The directory where the file is located.
    """
    input_data = RenameFileIn(old_name=old_name, new_name=new_name, dir_path=dir_path)
    result = await asyncio.to_thread(file_service.rename_file, input_data)
    return result

@mcp.tool()
async def move_files(dir_path: str, file_types_map: dict) -> dict:
    """
    Automatically organizes files into subdirectories based on their file extensions.
    
    Use this tool to clean up cluttered directories. For example, providing 
    {'jpg': 'Photos', 'pdf': 'Docs'} will move all .jpg files to a 'Photos' folder 
    and .pdf files to a 'Docs' folder. Subdirectories are created automatically if they don't exist.
    
    Args:
        dir_path: The source directory to organize.
        file_types_map: A dictionary mapping extensions (keys) to folder names (values).
    """
    input_data = MoveFilesIn(dir_path=dir_path, file_types_map=file_types_map)
    result = await asyncio.to_thread(file_service.move_files, input_data)
    return result

if __name__ == "__main__":
    mcp.run()