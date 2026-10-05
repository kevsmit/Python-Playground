conversions = {
    "1": ("miles", "kilometers", 1.60934),
    "2": ("kilometers", "miles", 1 / 1.60934),
    "3": ("pounds", "kilograms", 0.453592),
    "4": ("kilograms", "pounds", 1 / 0.453592),
    "5": ("feet", "meters", 0.3048),
    "6": ("meters", "feet", 1 / 0.3048),
}

print("Unit converter")
for key, (source, target, _) in conversions.items():
    print(f"{key}. {source} to {target}")

choice = input("Choose a conversion (1-6): ").strip()
if choice not in conversions:
    print("Please choose a number from 1 to 6.")
else:
    try:
        amount = float(input("Amount: "))
        source, target, factor = conversions[choice]
        print(f"{amount:g} {source} = {amount * factor:.2f} {target}")
    except ValueError:
        print("Please enter a number.")
