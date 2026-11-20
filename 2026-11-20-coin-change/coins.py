# Coin change: find the fewest coins that add up to an amount.
# Shows the greedy answer next to the best answer, since greedy
# doesn't always win with odd coin sets.

import sys


def greedy(amount, coins):
    used = []
    for c in sorted(coins, reverse=True):
        while amount >= c:
            amount -= c
            used.append(c)
    return used if amount == 0 else None


def fewest(amount, coins):
    # best[i] = shortest list of coins that makes i
    best = [None] * (amount + 1)
    best[0] = []
    for i in range(1, amount + 1):
        for c in coins:
            if c <= i and best[i - c] is not None:
                option = best[i - c] + [c]
                if best[i] is None or len(option) < len(best[i]):
                    best[i] = option
    return best[amount]


def show(label, coins_used):
    if coins_used is None:
        print(f"{label}: can't be made")
    else:
        print(f"{label}: {len(coins_used)} coins -> {sorted(coins_used, reverse=True)}")


def main():
    if len(sys.argv) < 2:
        print("usage: python coins.py AMOUNT [coin coin ...]")
        print("example: python coins.py 63 1 5 10 25")
        return

    amount = int(sys.argv[1])
    coins = [int(x) for x in sys.argv[2:]] or [1, 5, 10, 25]
    coins = sorted(set(c for c in coins if c > 0))

    print(f"Amount: {amount}  Coins: {coins}")
    show("Greedy", greedy(amount, coins))
    show("Best  ", fewest(amount, coins))


if __name__ == "__main__":
    main()
