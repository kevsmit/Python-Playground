"""Count how often each word appears in a piece of text."""
import re
import sys
from collections import Counter


def count_words(text):
    words = re.findall(r"[a-z']+", text.lower())
    return Counter(words)


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            text = f.read()
    else:
        text = input("Enter some text: ")

    counts = count_words(text)
    for word, n in counts.most_common(10):
        print(f"{word:<15} {n}")


if __name__ == "__main__":
    main()
