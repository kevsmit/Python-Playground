import math

print("Paint calculator")
width = float(input("Wall width in feet: "))
height = float(input("Wall height in feet: "))
coats = int(input("How many coats? "))
coverage = float(input("Square feet covered by one gallon (check the can): "))

if width <= 0 or height <= 0 or coats <= 0 or coverage <= 0:
    print("Please enter numbers greater than zero.")
else:
    area = width * height * coats
    gallons = area / coverage
    quarts = math.ceil(gallons * 4)
    print(f"You need about {gallons:.2f} gallons, or {quarts} quart(s).")
