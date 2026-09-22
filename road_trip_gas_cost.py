# Estimate the gas cost for a road trip.
miles = float(input("Trip distance in miles: "))
mpg = float(input("Your car's miles per gallon: "))
price = float(input("Gas price per gallon: $"))

if miles < 0 or mpg <= 0 or price < 0:
    print("Enter a positive MPG and non-negative distance and price.")
else:
    gallons = miles / mpg
    cost = gallons * price
    print(f"Estimated gas needed: {gallons:.1f} gallons")
    print(f"Estimated trip cost: ${cost:.2f}")
