import math

print("Bike rental price comparison")

try:
    minutes = int(input("How many minutes will you ride? "))
    hourly_rate = float(input("Price per hour: $"))
    minute_rate = float(input("Price per minute: $"))

    if minutes <= 0 or hourly_rate < 0 or minute_rate < 0:
        print("Use a positive ride length and nonnegative prices.")
    else:
        hours_charged = math.ceil(minutes / 60)
        hourly_cost = hours_charged * hourly_rate
        minute_cost = minutes * minute_rate
        print(f"Hourly plan ({hours_charged} hour(s)): ${hourly_cost:.2f}")
        print(f"Per-minute plan: ${minute_cost:.2f}")
        if hourly_cost == minute_cost:
            print("Both plans cost the same.")
        else:
            cheaper = "hourly" if hourly_cost < minute_cost else "per-minute"
            print(f"The {cheaper} plan is cheaper.")
except ValueError:
    print("Please enter numbers only.")
