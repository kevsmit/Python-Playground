"""Print the first N Fibonacci numbers."""
import sys


def fibonacci(n):
    """Return a list with the first n Fibonacci numbers."""
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


def main():
    if len(sys.argv) > 1:
        raw = sys.argv[1]
    else:
        raw = input("How many Fibonacci numbers? ")
    try:
        n = int(raw)
    except ValueError:
        print("Please enter a whole number.")
        return
    if n < 0:
        print("Please enter a number that is 0 or more.")
        return
    print(", ".join(str(x) for x in fibonacci(n)))


if __name__ == "__main__":
    main()
