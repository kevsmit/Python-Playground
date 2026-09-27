from datetime import datetime, timedelta

print("Shift end time")
start_text = input("Start time (HH:MM, 24-hour clock): ")
hours_text = input("Hours worked: ")

try:
    start = datetime.strptime(start_text, "%H:%M")
    hours = float(hours_text)

    if hours <= 0 or hours > 24:
        print("Enter a shift length between 0 and 24 hours.")
    else:
        end = start + timedelta(hours=hours)
        print(f"Your shift ends at {end.strftime('%I:%M %p')}.")
        if end.date() > start.date():
            print("That's the next day.")
except ValueError:
    print("Use HH:MM for the time and a number for hours.")
