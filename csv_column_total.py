import csv
from pathlib import Path

path = Path(input("CSV file path: ").strip())
column = input("Number column to add: ").strip()

if not path.is_file():
    print("That file does not exist.")
else:
    total = 0.0
    count = 0
    try:
        with path.open(newline="", encoding="utf-8-sig") as file:
            rows = csv.DictReader(file)
            if column not in (rows.fieldnames or []):
                print(f"Column not found. Available: {', '.join(rows.fieldnames or [])}")
            else:
                for row in rows:
                    try:
                        total += float(row[column])
                        count += 1
                    except (ValueError, TypeError):
                        pass
                print(f"Added {count} values: {total:,.2f}")
    except (OSError, UnicodeError, csv.Error) as error:
        print(f"Could not read the CSV: {error}")
