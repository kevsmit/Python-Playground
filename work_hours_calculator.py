# work hours calculator

hours = float(input("Hours worked: "))
break_minutes = int(input("Break length in minutes: "))

paid_hours = hours - (break_minutes / 60)

print(f"Paid hours: {paid_hours:.2f}")
