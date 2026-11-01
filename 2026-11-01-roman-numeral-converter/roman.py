"""Convert between integers and Roman numerals."""
import sys

PAIRS = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
         (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
         (5, "V"), (4, "IV"), (1, "I")]


def to_roman(n):
    if not 1 <= n <= 3999:
        raise ValueError("number must be between 1 and 3999")
    out = ""
    for value, symbol in PAIRS:
        while n >= value:
            out += symbol
            n -= value
    return out


def from_roman(s):
    s = s.upper()
    total = 0
    for value, symbol in PAIRS:
        while s.startswith(symbol):
            total += value
            s = s[len(symbol):]
    if s:
        raise ValueError("invalid Roman numeral")
    return total


def convert(text):
    if text.isdigit():
        return to_roman(int(text))
    return str(from_roman(text))


if __name__ == "__main__":
    for item in sys.argv[1:] or ["1994", "MMXXVI", "42"]:
        try:
            print(f"{item} -> {convert(item)}")
        except ValueError as err:
            print(f"{item} -> error: {err}")
