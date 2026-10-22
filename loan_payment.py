try:
    principal = float(input("Loan amount: $"))
    yearly_rate = float(input("Annual interest rate (%): "))
    years = int(input("Loan length in years: "))
    if principal <= 0 or yearly_rate < 0 or years <= 0:
        raise ValueError
except ValueError:
    raise SystemExit("Enter positive numbers and a non-negative interest rate.")

months = years * 12
monthly_rate = yearly_rate / 100 / 12
if monthly_rate == 0:
    payment = principal / months
else:
    payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** -months)

total = payment * months
print(f"Monthly payment: ${payment:,.2f}")
print(f"Total paid: ${total:,.2f}")
print(f"Total interest: ${total - principal:,.2f}")
