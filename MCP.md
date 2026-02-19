# 📂 Smart File-Ops MCP: The Intelligent File System Orchestrator

**Smart File-Ops** is a high-performance server built on the **Model Context Protocol (MCP)**. It transforms local file management from a series of "blind" commands into a **context-aware** operation. By bridging the gap between raw system calls and Large Language Model (LLM) reasoning, it enables AI to organize, rename, and manage files with human-like understanding and surgical precision.

---

## 🔄 The Workflow: Intelligence in Action

The system follows a strict **"Scan -> Propose -> Approve -> Execute"** cycle to ensure maximum data integrity:

1.  **Indexing & Discovery:** The MCP scans the target directory, generating a metadata manifest (file types, sizes, timestamps).
2.  **Contextual Analysis:** For relevant files, the server extracts "smart snippets" (File headers, EXIF data, or PDF metadata) to provide the AI with context.
3.  **Strategic Mapping:** The AI analyzes the manifest and proposes a logical structure (e.g., "Consolidating all 2024 tax-related PDFs into a dedicated folder").
4.  **Execution Plan:** The server generates a JSON-based plan detailing every proposed move and name change.
5.  **Human-in-the-Loop Approval:** The LLM presents the plan to you. **No file is moved or modified without explicit user consent.**
6.  **Atomic Execution:** Upon approval, the server performs the operations, ensuring no data loss and maintaining a transaction log.



---

## 🏗 System Architecture

The server is engineered with a modular philosophy, separating intelligence from execution:

### 1. Scanner Core (Discovery)
* **Recursive Depth Control:** Smart scanning that prevents system lag by limiting recursion depth.
* **Signature-Based Identification:** Identifies files using "Magic Numbers" (binary signatures) rather than just extensions, preventing errors with mislabeled files.

### 2. Cognitive Sampling Layer (The "Eyes")
* **Intelligent Text Sampling:** Extracts the first 2KB of source code, Markdown, or plain text to identify project themes.
* **Advanced Media Extraction:** Utilizes `Pillow` to parse EXIF data from images (Camera model, GPS, Timestamp) for chronological or geographical sorting.
* **Document Parsing:** Leverages `PyPDF2` to read internal titles and metadata from official documents, distinguishing a "Utility Bill" from a "Legal Contract."

### 3. Safety & Integrity Layer
* **Path Sandboxing:** Restricts the AI to a user-defined "Whitelist" of directories, strictly blocking access to sensitive system folders.
* **Collision Resolver:** Automatically detects name conflicts in the destination and proposes unique indexing (e.g., `file_v2.pdf`) to prevent overwriting.
* **Atomic Transactions:** Ensures that if a move fails (e.g., disk full), the system halts safely without leaving partial or corrupted data.

---

## 🛠 Available Tools

| Tool | Description |
| :--- | :--- |
| `analyze_directory` | Generates a comprehensive directory map with metadata and content samples. |
| `propose_organization` | Requests the AI to draft an organizational strategy (Chronological, Categorical, or Project-based). |
| `smart_rename` | (Opt-in) Suggests and applies descriptive filenames based on internal file content. |
| `archive_intelligence` | Peeks inside ZIP archives and performs selective, organized extraction. |
| `transactional_move` | Executes a batch of file operations with built-in error handling and logging. |

---

## 🛡 Security & Privacy

* **Zero Cloud Egress:** Your actual file content never leaves your machine. Only small text summaries/metadata are shared with the LLM to facilitate decision-making.
* **Local Execution:** The server runs within your local user environment, inheriting your existing permission levels.
* **Full Accountability:** Every "destructive" action (Rename, Move, Delete) requires a manual confirmation in the chat interface.

---

## ⚙️ Configuration & Installation

### 1. Prerequisites
* **Python 3.10+**
* **Dependencies:** `pip install mcp-sdk psutil pillow pypdf2`

### 2. Integration with MCP Clients (e.g., Claude Desktop)
Add the following configuration to your `config.json` file:

```json
{
  "mcpServers": {
    "smart-file-ops": {
      "command": "python",
      "args": ["/path/to/your/server.py"],
      "env": {
        "ALLOWED_ROOT": "C:/Users/YourName/Documents/FilesToOrganize",
        "ENABLE_RENAME": "true",
        "LOG_LEVEL": "INFO"
      }
    }
  }
}
```

---

## 📝 Use Case Scenarios (Examples)

* **Automated Downloads Cleanup:** > "Scan my Downloads folder. Identify all invoices, rename them by vendor and date, and move them to my 'Finance' folder."
* **Project Consolidation:** > "Find all Python files across these three folders that relate to 'Project X' and organize them into a clean directory structure."
* **Smart Archive Management:** > "Check the ZIP file I just downloaded. If it contains images, extract them to 'Photos/New', otherwise, list the contents and wait for my instructions."