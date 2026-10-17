from datetime import datetime
from pathlib import Path
import time

folder = Path(input("Folder to check: ").strip()).expanduser()
if not folder.is_dir():
    raise SystemExit("That folder does not exist.")

try:
    days = int(input("Show files older than how many days? "))
    if days < 0:
        raise ValueError
except ValueError:
    raise SystemExit("Please enter zero or a positive whole number.")

cutoff = time.time() - days * 24 * 60 * 60
old_files = []
for file in folder.rglob("*"):
    try:
        if file.is_file() and file.stat().st_mtime < cutoff:
            old_files.append(file)
    except OSError:
        print(f"Could not check: {file}")

print(f"Found {len(old_files)} older files.")
for file in sorted(old_files):
    changed = datetime.fromtimestamp(file.stat().st_mtime)
    print(f"{changed:%Y-%m-%d}  {file}")
