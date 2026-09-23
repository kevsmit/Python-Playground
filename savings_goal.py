goal = float(input("Savings goal ($): "))
saved = float(input("Amount saved so far ($): "))
monthly = float(input("Amount you can save each month ($): "))

left = max(goal - saved, 0)

if left == 0:
    print("You already reached your goal!")
elif monthly <= 0:
    print(f"You still need ${left:.2f}. Enter a monthly amount above $0.")
else:
    months = int(left // monthly) + (left % monthly > 0)
    print(f"You need ${left:.2f} more.")
    print(f"At ${monthly:.2f} per month, it will take {months} month(s).")
