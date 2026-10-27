import csv
from pathlib import Path

path = Path(input("CSV file path: ").strip())
if not path.is_file():
    print("File not found.")
    raise SystemExit(1)

first_seen = {}
duplicates = []

with path.open(newline="", encoding="utf-8-sig") as file:
    for line_number, row in enumerate(csv.reader(file), start=1):
        row_key = tuple(row)
        if row_key in first_seen:
            duplicates.append((line_number, first_seen[row_key]))
        else:
            first_seen[row_key] = line_number

if duplicates:
    print("Duplicate rows found:")
    for line_number, first_line in duplicates:
        print(f"Line {line_number} repeats line {first_line}.")
else:
    print("No duplicate rows found.")
