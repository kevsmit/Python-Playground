print("Recipe scaler")

try:
    original = float(input("Original servings: "))
    wanted = float(input("Servings you want: "))
    if original <= 0 or wanted <= 0:
        print("Servings must be greater than zero.")
    else:
        scale = wanted / original
        print("Enter each ingredient's amount and name. Press Enter with no amount to finish.")
        while True:
            amount_text = input("Amount: ").strip()
            if not amount_text:
                break
            amount = float(amount_text)
            name = input("Ingredient and unit (for example, cups of flour): ").strip()
            print(f"Use {amount * scale:g} {name}")
except ValueError:
    print("Use numbers for servings and ingredient amounts.")
