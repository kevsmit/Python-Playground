"""Roll some dice many times and show how often each total comes up."""
import random
import sys


def roll(num_dice, sides):
    return sum(random.randint(1, sides) for _ in range(num_dice))


def simulate(num_dice, sides, rolls):
    counts = {}
    for _ in range(rolls):
        total = roll(num_dice, sides)
        counts[total] = counts.get(total, 0) + 1
    return counts


def main():
    num_dice = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    sides = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    rolls = int(sys.argv[3]) if len(sys.argv) > 3 else 1000
    counts = simulate(num_dice, sides, rolls)
    for total in sorted(counts):
        pct = counts[total] / rolls * 100
        print(f"{total:>3}: {'#' * round(pct)} {pct:.1f}%")


if __name__ == "__main__":
    main()
