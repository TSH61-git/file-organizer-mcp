# 📁 **File Management MCP Project**

> 🔧 A lightweight Python project demonstrating a simple file management system using the
> Model Context Protocol (MCP). It provides directory scanning, file renaming, and
> organization features with security checks and reusable utilities.

---

## 🚀 What This Project Does

This repository implements a small application that allows users to perform
file-system operations in a controlled way.  Core capabilities include:

- 🔍 **Scanning directories** and previewing file contents.
- ✏️ **Renaming files** within an approved path.
- 📂 **Moving files** to specific subfolders based on their extensions.
- ✅ All operations are guarded by a path validator to keep actions within
  allowed directories, preventing unauthorized access.

These features are exposed via a set of MCP tools so they can be integrated
into larger systems through HTTP or other protocol endpoints.

---

## 📂 Project Structure

```
EX1_MCP/
├── fastmcp.json          # MCP configuration
├── main.py               # Entry point (if any)
├── models/
│   └── models.py         # Pydantic input models for the tools
├── services/
│   ├── file_service.py   # Core file operation logic
│   └── path_validator.py # Security helper to keep paths safe
├── utils/
│   ├── utils.py          # Generic misc helpers
│   └── validation.py     # Input/filename/directory validators
├── settings.py           # Environment settings loader
├── logs/                 # Empty folder reserved for log files
└── README.md             # This documentation
```

▫️ **models/** – defines the shape of inputs (`RenameFileIn`, `ScanFilesIn`,
`MoveFilesIn`) using Pydantic.

▫️ **services/** – contains business logic. `file_service` performs operations
and asks `path_validator` whether a directory is allowed.

▫️ **utils/** – miscellaneous helpers including path and string validation.

▫️ **settings.py** – convenience code for reading `.env` values.

---

## 🛠 MCP Tools Available

These methods are suitable as endpoints in an MCP server:

| Tool Name      | Description                                  |
|---------------|----------------------------------------------|
| `scan_files`  | Walk a directory and return file previews.   |
| `rename_file` | Change the name of a file safely.            |
| `move_files`  | Organize files into folders by extension.    |

Each tool expects one of the Pydantic models from `models/models.py` as
input and returns either structured results or simple error messages.

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone <repo-url> EX1_MCP
   cd EX1_MCP
   ```

2. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1    # Windows PowerShell
   ```

3. Install dependencies (if any are listed in `pyproject.toml` or manually):
   ```bash
   pip install -r requirements.txt  # or `poetry install` if using Poetry
   ```

4. Optionally set environment variables in a `.env` file adjacent to
   `settings.py`.

---

## ▶️ Usage

### As a library
Import the services and call them directly:

```python
from services.file_service import FileService
from models.models import ScanFilesIn

svc = FileService(allowed_directories=[r"C:\Users\User\Downloads\TRY"])
result = svc.scan_files(ScanFilesIn(dir_path=r"C:\Users\User\Downloads\TRY"))
print(result)
```

### As an MCP server
Configure an MCP server (e.g., using `fastmcp.json`) and register the
`FileService` methods as tools. Example `fastmcp.json` already points
at `services/file_service.py`. Run the MCP host and call tools via HTTP
per the MCP protocol.

### Logging
Any runtime logging can be written to the `logs/` directory. It's currently
empty but reserved for future use.

---

## 📝 Notes

- 🛡️ Path validation is central: only directories listed in
  `allowed_directories` may be manipulated.
- 📦 The project is minimal and intended as a demonstration or starter
  template for building MCP-based file utilities.

---

## 🤝 Contributing

Feel free to open issues or submit pull requests. Suggestions for new tools or
additional validation are welcome!
