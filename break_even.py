try:
    fixed_costs = float(input("Fixed costs: $"))
    price = float(input("Selling price per item: $"))
    item_cost = float(input("Cost per item: $"))
    if fixed_costs < 0 or price < 0 or item_cost < 0:
        raise ValueError
except ValueError:
    raise SystemExit("Please enter zero or positive numbers.")

profit_per_item = price - item_cost
if profit_per_item <= 0:
    raise SystemExit("The selling price must be higher than the cost per item.")

units = int(-(-fixed_costs // profit_per_item))
revenue = units * price
print(f"Profit per item: ${profit_per_item:,.2f}")
print(f"Break-even quantity: {units} items")
print(f"Revenue at break-even: ${revenue:,.2f}")
