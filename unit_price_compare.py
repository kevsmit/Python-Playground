print("Compare unit prices")

try:
    first_price = float(input("First item's price: $"))
    first_amount = float(input("First item's size (same unit for both): "))
    second_price = float(input("Second item's price: $"))
    second_amount = float(input("Second item's size: "))

    if min(first_price, second_price) < 0 or min(first_amount, second_amount) <= 0:
        print("Prices must be at least zero and sizes must be greater than zero.")
    else:
        first_unit = first_price / first_amount
        second_unit = second_price / second_amount
        print(f"First: ${first_unit:.2f} per unit")
        print(f"Second: ${second_unit:.2f} per unit")
        if first_unit == second_unit:
            print("They cost the same per unit.")
        else:
            print("The first item is cheaper." if first_unit < second_unit else "The second item is cheaper.")
except ValueError:
    print("Please enter numbers only.")
