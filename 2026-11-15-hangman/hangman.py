import random
import sys

WORDS = [
    "python", "keyboard", "giraffe", "blanket", "rocket", "pickle",
    "lantern", "pumpkin", "volcano", "sandwich", "penguin", "compass",
]

GALLOWS = [
    "",
    "  O",
    "  O\n  |",
    "  O\n /|",
    "  O\n /|\\",
    "  O\n /|\\\n /",
    "  O\n /|\\\n / \\",
]

MAX_MISSES = len(GALLOWS) - 1


def show_word(word, guessed):
    return " ".join(c if c in guessed else "_" for c in word)


def play(word):
    guessed = set()
    misses = 0

    while misses < MAX_MISSES:
        print()
        print(GALLOWS[misses])
        print(show_word(word, guessed))
        print(f"misses left: {MAX_MISSES - misses}")

        guess = input("guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("just one letter please")
            continue
        if guess in guessed:
            print("already tried that")
            continue

        guessed.add(guess)
        if guess in word:
            if all(c in guessed for c in word):
                print(f"\nyou got it: {word}")
                return True
        else:
            misses += 1
            print("nope")

    print()
    print(GALLOWS[misses])
    print(f"out of guesses, the word was {word}")
    return False


def main():
    word = sys.argv[1].lower() if len(sys.argv) > 1 else random.choice(WORDS)
    try:
        play(word)
    except (KeyboardInterrupt, EOFError):
        print(f"\nbye, the word was {word}")


if __name__ == "__main__":
    main()
