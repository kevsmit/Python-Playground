import random
import sys

DIGITS = "123456"
LENGTH = 4
MAX_TURNS = 10


def score(secret, guess):
    exact = sum(s == g for s, g in zip(secret, guess))
    common = sum(min(secret.count(d), guess.count(d)) for d in set(guess))
    return exact, common - exact


def read_guess():
    while True:
        guess = input("guess: ").strip()
        if len(guess) == LENGTH and all(c in DIGITS for c in guess):
            return guess
        print(f"need {LENGTH} digits, each from {DIGITS[0]} to {DIGITS[-1]}")


def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else None
    rng = random.Random(seed)
    secret = "".join(rng.choice(DIGITS) for _ in range(LENGTH))

    print(f"I picked a {LENGTH} digit code using {DIGITS[0]}-{DIGITS[-1]} (repeats allowed).")
    print(f"You get {MAX_TURNS} tries. + = right digit right spot, - = right digit wrong spot.\n")

    for turn in range(1, MAX_TURNS + 1):
        guess = read_guess()
        exact, close = score(secret, guess)
        print(f"  {turn:>2}: {guess}  {'+' * exact}{'-' * close}")
        if exact == LENGTH:
            print(f"got it in {turn}!")
            return
    print(f"out of tries, the code was {secret}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nbye")
