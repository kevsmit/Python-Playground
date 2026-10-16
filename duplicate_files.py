from pathlib import Path
import hashlib
folder = Path(input("Folder to check: ").strip()).expanduser()
if not folder.is_dir():
    raise SystemExit("That folder does not exist.")
by_size = {}
for file in folder.rglob("*"):
    if file.is_file():
        try:
            by_size.setdefault(file.stat().st_size, []).append(file)
        except OSError:
            pass
by_hash = {}
for files in by_size.values():
    if len(files) < 2:
        continue
    for file in files:
        try:
            digest = hashlib.sha256()
            with file.open("rb") as source:
                for chunk in iter(lambda: source.read(65536), b""):
                    digest.update(chunk)
            by_hash.setdefault(digest.hexdigest(), []).append(file)
        except OSError:
            print(f"Could not read: {file}")
groups = [files for files in by_hash.values() if len(files) > 1]
print(f"Found {len(groups)} duplicate groups.")
for files in groups:
    print("\n" + "\n".join(map(str, files)))
