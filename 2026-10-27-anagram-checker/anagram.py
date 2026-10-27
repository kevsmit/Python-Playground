"""Check whether two words or phrases are anagrams of each other."""

import sys
from collections import Counter


def normalize(text):
    """Lowercase the text and keep only letters and digits."""
    return Counter(ch for ch in text.lower() if ch.isalnum())


def is_anagram(a, b):
    return normalize(a) == normalize(b)


def main():
    if len(sys.argv) == 3:
        first, second = sys.argv[1], sys.argv[2]
    else:
        first = input("First word or phrase: ")
        second = input("Second word or phrase: ")

    if is_anagram(first, second):
        print(f'"{first}" and "{second}" are anagrams.')
    else:
        print(f'"{first}" and "{second}" are not anagrams.')


if __name__ == "__main__":
    main()
