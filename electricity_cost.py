try:
    watts = float(input("Device watts: "))
    hours = float(input("Hours used per day: "))
    rate = float(input("Electricity price per kWh: $"))
    if watts < 0 or hours < 0 or rate < 0:
        raise ValueError
except ValueError:
    raise SystemExit("Please enter zero or positive numbers.")

daily_kwh = watts * hours / 1000
daily_cost = daily_kwh * rate
monthly_cost = daily_cost * 30
yearly_cost = daily_cost * 365

print(f"Daily energy use: {daily_kwh:.2f} kWh")
print(f"Daily cost: ${daily_cost:.2f}")
print(f"30-day cost: ${monthly_cost:.2f}")
print(f"Yearly cost: ${yearly_cost:.2f}")
