from datetime import date, timedelta

try:
    start = date.fromisoformat(input("Start date (YYYY-MM-DD): ").strip())
    end = date.fromisoformat(input("End date (YYYY-MM-DD): ").strip())
except ValueError:
    raise SystemExit("Please enter valid dates in YYYY-MM-DD format.")

if end < start:
    raise SystemExit("The end date must be on or after the start date.")

days = (end - start).days + 1
weeks, remainder = divmod(days, 7)
weekdays = weeks * 5
for offset in range(remainder):
    if (start + timedelta(days=offset)).weekday() < 5:
        weekdays += 1

print(f"Weekdays: {weekdays}")
print("Both dates are included. Holidays are not excluded.")
