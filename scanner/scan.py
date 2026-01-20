#scanner\scan.py
import os
from pathlib import Path
import pathspec

IGNORED_DIRS = {".git", "storage"}


def load_gitignore(path: Path) -> pathspec.PathSpec | None:
    gitignore = path / ".gitignore"
    if not gitignore.exists():
        return None

    patterns = gitignore.read_text().splitlines()
    return pathspec.PathSpec.from_lines("gitwildmatch", patterns)


def list_all_files(root_dir: str) -> list[str]:
    root_dir = Path(root_dir).resolve()
    files: list[str] = []

    # Stack of (directory_path, ignore_specs_active_here)
    ignore_stack: dict[Path, list[pathspec.PathSpec]] = {}

    for root, dirnames, filenames in os.walk(root_dir):
        root = Path(root)

        rel_root = root.relative_to(root_dir).as_posix()

        # Hard skip
        if root.name in IGNORED_DIRS:
            dirnames.clear()
            continue

        # Inherit ignore rules from parent
        parent = root.parent
        active_specs = list(ignore_stack.get(parent, []))

        # Load local .gitignore (if present)
        local_spec = load_gitignore(root)
        if local_spec:
            active_specs.append(local_spec)

        ignore_stack[root] = active_specs

        # Filter directories
        kept_dirs = []
        for d in dirnames:
            rel_path = (Path(rel_root) / d).as_posix() if rel_root != "." else d
            if not any(spec.match_file(rel_path) for spec in active_specs):
                kept_dirs.append(d)

        dirnames[:] = kept_dirs

        # Filter files
        for f in filenames:
            rel_path = (Path(rel_root) / f).as_posix() if rel_root != "." else f

            if any(spec.match_file(rel_path) for spec in active_specs):
                continue

            files.append(rel_path)

    return files


if __name__ == "__main__":
    result = list_all_files(r"D:\github\NeuroCode")
    print(result)
