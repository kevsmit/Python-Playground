# paycheck estimate

hours = float(input("Hours worked this week: "))
rate = float(input("Hourly pay ($): "))

regular = min(hours, 40)
overtime = max(hours - 40, 0)
pay = regular * rate + overtime * rate * 1.5

print(f"Regular hours: {regular:g}")
print(f"Overtime hours: {overtime:g}")
print(f"Estimated pay before taxes: ${pay:.2f}")
