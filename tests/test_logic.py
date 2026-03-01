import pytest
import os
from utils.validation import is_valid_filename, is_empty_string
from services.path_validator import PathValidator

# --- בדיקות עבור utils/validation.py ---

def test_is_valid_filename():
    assert is_valid_filename("valid_name.txt") is True
    assert is_valid_filename("invalid/name.txt") is False
    assert is_valid_filename("test?file.py") is False

def test_is_empty_string():
    assert is_empty_string("") is True
    assert is_empty_string("   ") is True
    assert is_empty_string("content") is False

# --- בדיקות עבור services/path_validator.py ---

def test_path_validation_logic():
    # משתמש בנתיב אבסולוטי של התיקייה הנוכחית
    current_dir = os.path.abspath(os.getcwd())
    validator = PathValidator(allowed_directories=[current_dir])
    
    # בדיקה שנתיב בתוך התיקייה המורשית מאושר
    test_file = os.path.join(current_dir, "test.txt")
    assert validator.is_path_safe(test_file) is True # שימוש בשם הנכון: is_path_safe

def test_path_validation_security():
    current_dir = os.path.abspath(os.getcwd())
    validator = PathValidator(allowed_directories=[current_dir])
    
    # בדיקה שנתיב מחוץ לתיקייה (כמו תיקיית מערכת) נחסם
    assert validator.is_path_safe(r"C:\Windows\System32") is False

def test_empty_allowed_list():
    # בדיקה שאם אין רשימת מורשים, הכל נחסם
    validator = PathValidator(allowed_directories=[])
    assert validator.is_path_safe(os.getcwd()) is False