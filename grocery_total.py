# grocery total calculator

prices = []

while True:
    price = input("Item price (or press Enter to finish): ")
    if price == "":
        break
    prices.append(float(price))

print(f"Total: ${sum(prices):.2f}")
