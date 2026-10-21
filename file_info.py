from pathlib import Path

path = Path(input("File to inspect: ").strip()).expanduser()
try:
    size = path.stat().st_size
except OSError as error:
    raise SystemExit(f"Could not read the file: {error}")

units = ["bytes", "KB", "MB", "GB", "TB"]
amount = float(size)
for unit in units:
    if amount < 1024 or unit == units[-1]:
        break
    amount /= 1024

print(f"Name: {path.name}")
print(f"Extension: {path.suffix or '(none)'}")
print(f"Size: {size:,} bytes")
print(f"Readable size: {amount:.2f} {unit}")
