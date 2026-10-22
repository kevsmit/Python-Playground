"""Think of a number and the computer guesses it using binary search."""


def guess_number(low, high, answer_is):
    """Find the number by repeatedly guessing the middle of the range.

    answer_is(guess) must return "higher", "lower" or "correct".
    Returns the number and how many guesses it took.
    """
    guesses = 0
    while low <= high:
        guess = (low + high) // 2
        guesses += 1
        reply = answer_is(guess)
        if reply == "correct":
            return guess, guesses
        if reply == "higher":
            low = guess + 1
        else:
            high = guess - 1
    return None, guesses


def ask_player(guess):
    while True:
        reply = input(f"Is it {guess}? (higher / lower / correct): ").strip().lower()
        if reply in ("higher", "lower", "correct"):
            return reply
        print("Please type higher, lower or correct.")


def main():
    low, high = 1, 100
    print(f"Think of a number between {low} and {high}. I will try to guess it.")
    number, guesses = guess_number(low, high, ask_player)
    if number is None:
        print("Hmm, those answers don't add up. Did you change your number?")
    else:
        print(f"Got it! Your number is {number}. It took me {guesses} guesses.")


if __name__ == "__main__":
    main()
