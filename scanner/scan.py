#scanner\scan.py
import os
from pathlib import Path
import pathspec

IGNORED_DIRS = {".git", "storage"}


def load_gitignore_spec(root_dir: str) -> pathspec.PathSpec:
    gitignore_path = Path(root_dir) / ".gitignore"
    if not gitignore_path.exists():
        return pathspec.PathSpec.from_lines("gitwildmatch", [])

    patterns = gitignore_path.read_text().splitlines()
    return pathspec.PathSpec.from_lines("gitwildmatch", patterns)


def list_all_files(root_dir: str) -> list[str]:
    root_dir = os.path.abspath(root_dir)
    spec = load_gitignore_spec(root_dir)

    files: list[str] = []

    for root, dirnames, filenames in os.walk(root_dir):

        # Get path relative to repo root
        rel_root = os.path.relpath(root, root_dir).replace("\\", "/")

        # Skip .git completely
        if rel_root in IGNORED_DIRS:
            dirnames.clear()
            continue

        # Filter ignored directories
        dirnames[:] = [
            d for d in dirnames
            if not spec.match_file(f"{rel_root}/{d}" if rel_root != "." else d)
        ]

        # Filter ignored files
        for name in filenames:
            rel_path = f"{rel_root}/{name}" if rel_root != "." else name
            rel_path = rel_path.replace("\\", "/")

            if not spec.match_file(rel_path):
                files.append(rel_path)


    return files


all_files = list_all_files(r"D:\github\NeuroCode")
print(all_files)
