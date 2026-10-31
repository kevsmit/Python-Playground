print("Temperature converter")
choice = input("Convert (1) Celsius to Fahrenheit or (2) Fahrenheit to Celsius: ").strip()

if choice not in ("1", "2"):
    raise SystemExit("Please choose 1 or 2.")

try:
    temperature = float(input("Temperature: "))
except ValueError:
    raise SystemExit("Please enter a valid number.")

if choice == "1":
    converted = temperature * 9 / 5 + 32
    print(f"{temperature:g}°C = {converted:.1f}°F")
else:
    converted = (temperature - 32) * 5 / 9
    print(f"{temperature:g}°F = {converted:.1f}°C")
