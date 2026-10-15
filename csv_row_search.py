import csv
from pathlib import Path

path = Path(input("CSV file path: ").strip())
term = input("Word or phrase to find: ").strip().casefold()

if not path.is_file():
    print("That file does not exist.")
elif not term:
    print("Enter something to search for.")
else:
    try:
        with path.open(newline="", encoding="utf-8-sig") as file:
            rows = csv.DictReader(file)
            matches = 0
            for row in rows:
                if any(term in (value or "").casefold() for value in row.values()):
                    print(row)
                    matches += 1
                    if matches == 10:
                        print("Showing the first 10 matches.")
                        break
            if matches == 0:
                print("No matching rows found.")
    except (OSError, UnicodeError, csv.Error) as error:
        print(f"Could not read the CSV: {error}")
