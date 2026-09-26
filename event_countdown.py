from datetime import date

print("Days until an event")
name = input("What are you counting down to? ").strip()
date_text = input("Event date (YYYY-MM-DD): ").strip()

try:
    event_date = date.fromisoformat(date_text)
    days_left = (event_date - date.today()).days

    if days_left > 0:
        print(f"{days_left} day(s) until {name or 'your event'}!")
    elif days_left == 0:
        print(f"{name or 'Your event'} is today!")
    else:
        print(f"{name or 'Your event'} was {-days_left} day(s) ago.")
except ValueError:
    print("Enter a real date in YYYY-MM-DD format.")
