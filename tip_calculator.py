# small tip calculator

bill = float(input("Bill total: $"))
tip_percent = float(input("Tip percent: "))
people = int(input("Number of people: "))

tip = bill * (tip_percent / 100)
total = bill + tip
per_person = total / people

print(f"Tip: ${tip:.2f}")
print(f"Total: ${total:.2f}")
print(f"Each person pays: ${per_person:.2f}")
