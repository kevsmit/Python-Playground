import json
from pathlib import Path

path = Path(input("JSON file to check: ").strip()).expanduser()
try:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
except json.JSONDecodeError as error:
    raise SystemExit(
        f"Invalid JSON on line {error.lineno}, column {error.colno}: {error.msg}"
    )
except (OSError, UnicodeError) as error:
    raise SystemExit(f"Could not read the file: {error}")

print("Valid JSON.")
print(f"Top-level type: {type(data).__name__}")
if isinstance(data, dict):
    print(f"Keys: {len(data)}")
elif isinstance(data, list):
    print(f"Items: {len(data)}")
