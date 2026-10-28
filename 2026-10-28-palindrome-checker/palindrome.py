"""Check whether a word or phrase reads the same forwards and backwards."""

import sys


def clean(text):
    """Lowercase the text and keep only letters and digits."""
    return [ch for ch in text.lower() if ch.isalnum()]


def is_palindrome(text):
    chars = clean(text)
    return chars == chars[::-1]


def main():
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = input("Word or phrase: ")

    if is_palindrome(text):
        print(f'"{text}" is a palindrome.')
    else:
        print(f'"{text}" is not a palindrome.')


if __name__ == "__main__":
    main()
