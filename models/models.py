from pydantic import BaseModel

# מודל לשם קובץ ישן וחדש
class RenameFileIn(BaseModel):
    old_name: str
    new_name: str
    dir_path: str

# מודל לקלט של סריקת תיקיות
class ScanFilesIn(BaseModel):
    dir_path: str
    max_preview_length: int = 100

# מודל לקלט של העברת קבצים לתוך תיקיות
class MoveFilesIn(BaseModel):
    dir_path: str
    file_types_map: dict
