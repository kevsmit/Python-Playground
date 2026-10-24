from pathlib import Path
import hashlib

path = Path(input("File to hash: ").strip()).expanduser()
if not path.is_file():
    raise SystemExit("That file does not exist.")

digest = hashlib.sha256()
try:
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(65536), b""):
            digest.update(chunk)
except OSError as error:
    raise SystemExit(f"Could not read the file: {error}")

print(f"SHA-256: {digest.hexdigest()}")
