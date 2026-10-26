try:
    people = int(input("Number of people: "))
    hourly_pay = float(input("Average hourly pay: $"))
    minutes = float(input("Meeting length in minutes: "))
    if people <= 0 or hourly_pay < 0 or minutes < 0:
        raise ValueError
except ValueError:
    raise SystemExit("Enter a positive number of people and non-negative amounts.")

hours = minutes / 60
total_cost = people * hourly_pay * hours
person_hours = people * hours

print(f"Total meeting cost: ${total_cost:,.2f}")
print(f"Total staff time: {person_hours:.2f} person-hours")
print(f"Cost per minute: ${total_cost / minutes:,.2f}" if minutes else "Cost per minute: $0.00")
