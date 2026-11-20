# Coin Change

Works out the fewest coins needed to make an amount. It prints the
greedy answer (always grab the biggest coin) and the actual best answer,
so you can see the cases where greedy gets it wrong.

Default coins are 1, 5, 10, 25 if you don't give any.

## Run

    python coins.py 63
    python coins.py 6 1 3 4

Example:

    Amount: 6  Coins: [1, 3, 4]
    Greedy: 3 coins -> [4, 1, 1]
    Best  : 2 coins -> [3, 3]
