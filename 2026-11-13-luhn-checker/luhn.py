import sys


def luhn_valid(number):
    digits = [int(c) for c in number if c.isdigit()]
    if len(digits) < 2:
        return False

    total = 0
    # go from the right, double every second digit
    for i, d in enumerate(reversed(digits)):
        if i % 2 == 1:
            d = d * 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def check_digit(partial):
    # find the digit that makes partial + digit pass
    for d in range(10):
        if luhn_valid(partial + str(d)):
            return d


def main():
    if len(sys.argv) < 2:
        examples = ["4539 1488 0343 6467", "4539 1488 0343 6468", "79927398713"]
        for n in examples:
            print(f"{n:<22} {'valid' if luhn_valid(n) else 'invalid'}")
        print("\nusage: python luhn.py <number>")
        print("       python luhn.py --digit <number without last digit>")
        return

    if sys.argv[1] == "--digit" and len(sys.argv) > 2:
        partial = "".join(c for c in " ".join(sys.argv[2:]) if c.isdigit())
        print(f"check digit: {check_digit(partial)}")
        return

    number = " ".join(sys.argv[1:])
    print("valid" if luhn_valid(number) else "invalid")


if __name__ == "__main__":
    main()
