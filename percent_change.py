print("Percentage change calculator")

try:
    old = float(input("Starting value: "))
    new = float(input("New value: "))

    if old == 0:
        print("Starting value cannot be zero for percentage change.")
    else:
        change = new - old
        percent = change / abs(old) * 100
        print(f"Change: {change:+,.2f}")
        print(f"Percentage change: {percent:+.2f}%")
except ValueError:
    print("Please enter numbers only.")
