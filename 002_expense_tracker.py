# expense tracker - day 1

expenses = []

print("Expense Tracker")
print("----------------")

while True:
    name = input("Expense name (or 'done'): ")

    if name.lower() == "done":
        break

    amount = float(input("Amount: $"))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added!\n")

total = 0

print("\nYour Expenses")
print("-------------")

for expense in expenses:
    print(f"{expense['name']}: ${expense['amount']:.2f}")
    total += expense["amount"]

print(f"\nTotal spent: ${total:.2f}")
