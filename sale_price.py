print("Sale price calculator")

try:
    price = float(input("Original price: $"))
    discount = float(input("Discount percentage: "))
    tax = float(input("Sales tax percentage: "))

    if price < 0 or not 0 <= discount <= 100 or tax < 0:
        print("Check your numbers and try again.")
    else:
        after_discount = price * (1 - discount / 100)
        total = after_discount * (1 + tax / 100)
        print(f"Price after discount: ${after_discount:.2f}")
        print(f"Total after tax: ${total:.2f}")
except ValueError:
    print("Please enter numbers only.")
