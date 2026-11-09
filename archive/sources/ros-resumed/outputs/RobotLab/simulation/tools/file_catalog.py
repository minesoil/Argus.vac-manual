"""Read-only file listings for the Windows launcher; paths arrive as JSON stdin."""

import json
import os
from pathlib import Path
import sys
import time


def catalog(request):
    root = Path(request["path"])
    query = request.get("query", "").casefold().strip()
    entries, errors = [], []

    def entry(path):
        try:
            stat = path.lstat()
            entries.append(
                {
                    "name": path.name,
                    "path": str(path),
                    "folder": path.is_dir(),
                    "link": path.is_symlink(),
                    "size": stat.st_size,
                    "modified": stat.st_mtime,
                }
            )
        except OSError as exc:
            errors.append(f"{path}: {exc.strerror}")

    if not root.is_dir():
        raise ValueError(f"Folder unavailable: {root}")
    if query:
        deadline = time.monotonic() + 45

        def problem(exc):
            errors.append(f"{exc.filename}: {exc.strerror}")

        for folder, dirs, files in os.walk(root, onerror=problem, followlinks=False):
            if time.monotonic() > deadline:
                errors.append(
                    "Search stopped after 45 seconds; results are partial. Choose a smaller folder."
                )
                break
            for name in dirs + files:
                if query in name.casefold():
                    entry(Path(folder) / name)
    else:
        for path in root.iterdir():
            entry(path)
    entries.sort(
        key=lambda item: (not item["folder"], item["name"].casefold(), item["path"])
    )
    return {"entries": entries, "errors": errors, "path": str(root), "query": query}


if __name__ == "__main__":
    try:
        print(json.dumps(catalog(json.load(sys.stdin))))
    except Exception as exc:
        print(json.dumps({"entries": [], "errors": [str(exc)]}))
        sys.exit(1)
