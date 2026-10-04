print("Subscription total")
monthly_total = 0.0

while True:
    name = input("Subscription name (blank to finish): ").strip()
    if not name:
        break

    try:
        price = float(input(f"{name} price: $"))
        period = input("Monthly or yearly? (m/y): ").strip().lower()
        if price < 0 or period not in ("m", "y"):
            print("Enter a nonnegative price and m or y. Item skipped.")
            continue
        monthly_total += price if period == "m" else price / 12
    except ValueError:
        print("Enter a number for the price. Item skipped.")

print(f"Monthly total: ${monthly_total:.2f}")
print(f"Yearly total: ${monthly_total * 12:.2f}")
