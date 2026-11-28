import sys
from collections import deque
from string import ascii_lowercase

WORDS = """
cold cord card ward warm word worm wore core care cars bars bats cats
cots dots dogs cogs logs lots lost most mist list lint line fine fire
hire here hare hard herd head heal heat beat bear dear deer seed feed
fled flea flew flaw claw clay play plan plane slow glow grow crow crew
""".split()


def neighbors(word, words):
    for i in range(len(word)):
        for c in ascii_lowercase:
            if c != word[i]:
                new = word[:i] + c + word[i + 1:]
                if new in words:
                    yield new


def ladder(start, end, words):
    words = set(words) | {end}
    queue = deque([[start]])
    seen = {start}
    while queue:
        path = queue.popleft()
        if path[-1] == end:
            return path
        for nxt in neighbors(path[-1], words):
            if nxt not in seen:
                seen.add(nxt)
                queue.append(path + [nxt])
    return None


def load_words(path):
    with open(path) as f:
        return [w.strip().lower() for w in f if w.strip()]


def main():
    if len(sys.argv) < 3:
        print("usage: python ladder.py START END [wordlist.txt]")
        return
    start, end = sys.argv[1].lower(), sys.argv[2].lower()
    if len(start) != len(end):
        print("words need to be the same length")
        return
    words = load_words(sys.argv[3]) if len(sys.argv) > 3 else WORDS
    words = [w for w in words if len(w) == len(start)]
    path = ladder(start, end, words)
    if path:
        print(" -> ".join(path))
        print(f"{len(path) - 1} steps")
    else:
        print("no ladder found")


if __name__ == "__main__":
    main()
