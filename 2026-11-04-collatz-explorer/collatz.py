"""Collatz sequence explorer.

Pick a starting number. If it's even, halve it; if it's odd, triple it and
add one. Repeat until you reach 1.
"""
import sys


def collatz(n):
    """Return the full Collatz sequence starting at n."""
    if n < 1:
        raise ValueError("n must be a positive integer")
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq


def longest_under(limit):
    """Return (start, steps) for the start below limit with the most steps."""
    best = (1, 0)
    for start in range(1, limit):
        steps = len(collatz(start)) - 1
        if steps > best[1]:
            best = (start, steps)
    return best


def main():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = int(input("Start number: "))
    seq = collatz(n)
    print(" -> ".join(map(str, seq)))
    print(f"Steps: {len(seq) - 1}, peak value: {max(seq)}")
    start, steps = longest_under(1000)
    print(f"Longest chain under 1000 starts at {start} ({steps} steps)")


if __name__ == "__main__":
    main()
