"""Figure out who owes who after a group trip or dinner.

Give it a CSV file with columns: name,amount,description
Each row is something one person paid for the whole group.
"""

import csv
import sys


def load_expenses(path):
    expenses = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            name = row["name"].strip()
            amount = float(row["amount"])
            expenses.append((name, amount))
    return expenses


def balances(expenses):
    paid = {}
    for name, amount in expenses:
        paid[name] = paid.get(name, 0) + amount

    total = sum(paid.values())
    share = total / len(paid)
    return {name: round(amt - share, 2) for name, amt in paid.items()}, total, share


def settle(bal):
    # people who are owed money and people who owe money
    owed = sorted([[n, b] for n, b in bal.items() if b > 0], key=lambda x: -x[1])
    owes = sorted([[n, -b] for n, b in bal.items() if b < 0], key=lambda x: -x[1])

    payments = []
    i = j = 0
    while i < len(owes) and j < len(owed):
        amount = min(owes[i][1], owed[j][1])
        if amount >= 0.01:
            payments.append((owes[i][0], owed[j][0], round(amount, 2)))
        owes[i][1] -= amount
        owed[j][1] -= amount
        if owes[i][1] < 0.01:
            i += 1
        if owed[j][1] < 0.01:
            j += 1
    return payments


def main():
    if len(sys.argv) != 2:
        print("usage: python bill_splitter.py expenses.csv")
        sys.exit(1)

    expenses = load_expenses(sys.argv[1])
    if not expenses:
        print("no expenses found")
        return

    bal, total, share = balances(expenses)
    print(f"Total spent: ${total:.2f}")
    print(f"Each person: ${share:.2f}")
    print()

    for name, b in sorted(bal.items()):
        if b > 0:
            print(f"  {name} is owed ${b:.2f}")
        elif b < 0:
            print(f"  {name} owes ${-b:.2f}")
        else:
            print(f"  {name} is even")
    print()

    payments = settle(bal)
    if not payments:
        print("Everyone is square.")
    for frm, to, amt in payments:
        print(f"{frm} pays {to} ${amt:.2f}")


if __name__ == "__main__":
    main()
