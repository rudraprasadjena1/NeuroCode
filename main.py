#main.py
from scanner.scan import list_all_files
from scanner.hashh import hash_file
from scanner.cache import load_index, save_index, load_metadata, save_metadata
from parser.python_parser import parse_python_file
import os

repo_root = r"D:\github\NeuroCode"

old_index = load_index()
old_metadata = load_metadata()

new_index = {}
new_metadata = dict(old_metadata)  # copy existing

files = list_all_files(repo_root)

new = modified = unchanged = 0

for rel_path in files:
    full_path = os.path.join(repo_root, rel_path)
    h = hash_file(full_path)
    new_index[rel_path] = h

    is_changed = False

    if rel_path not in old_index:
        new += 1
        is_changed = True
    elif old_index[rel_path] != h:
        modified += 1
        is_changed = True
    else:
        unchanged += 1

    # Only parse changed Python files
    if is_changed and rel_path.endswith(".py"):
        functions, imports, calls = parse_python_file(full_path)

        new_metadata[rel_path] = {
            "functions": functions,
            "imports": imports,
            "calls":calls
        }

# Remove deleted files from metadata
deleted_files = set(old_index.keys()) - set(new_index.keys())
for f in deleted_files:
    new_metadata.pop(f, None)

deleted = len(deleted_files)

save_index(new_index)
save_metadata(new_metadata)

print(f"Files: {len(files)}")
print(f"New: {new}")
print(f"Modified: {modified}")
print(f"Unchanged: {unchanged}")
print(f"Deleted: {deleted}")
