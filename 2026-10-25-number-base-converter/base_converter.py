"""Convert a whole number between binary, octal, decimal and hex."""

import sys

DIGITS = "0123456789ABCDEF"


def to_base(number, base):
    """Turn a non-negative int into a string in the given base (2-16)."""
    if number == 0:
        return "0"
    result = ""
    while number > 0:
        result = DIGITS[number % base] + result
        number //= base
    return result


def from_base(text, base):
    """Turn a string in the given base back into an int."""
    total = 0
    for char in text.upper():
        value = DIGITS.find(char)
        if value == -1 or value >= base:
            raise ValueError(f"'{char}' is not valid in base {base}")
        total = total * base + value
    return total


def main():
    if len(sys.argv) != 3:
        print("Usage: python base_converter.py <number> <from_base>")
        print("Example: python base_converter.py FF 16")
        return
    try:
        base = int(sys.argv[2])
        if not 2 <= base <= 16:
            raise ValueError("base must be between 2 and 16")
        number = from_base(sys.argv[1], base)
    except ValueError as err:
        print(f"Error: {err}")
        return
    print(f"Decimal: {number}")
    print(f"Binary:  {to_base(number, 2)}")
    print(f"Octal:   {to_base(number, 8)}")
    print(f"Hex:     {to_base(number, 16)}")


if __name__ == "__main__":
    main()
