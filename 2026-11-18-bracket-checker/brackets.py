import sys

PAIRS = {")": "(", "]": "[", "}": "{"}


def check(text):
    """Return None if brackets are balanced, otherwise an error message."""
    stack = []
    for i, ch in enumerate(text):
        if ch in "([{":
            stack.append((ch, i))
        elif ch in PAIRS:
            if not stack:
                return f"unexpected '{ch}' at position {i}"
            opener, pos = stack.pop()
            if opener != PAIRS[ch]:
                return f"'{opener}' at position {pos} closed by '{ch}' at position {i}"
    if stack:
        opener, pos = stack[-1]
        return f"'{opener}' at position {pos} is never closed"
    return None


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            text = f.read()
    else:
        text = input("Enter some text: ")

    problem = check(text)
    if problem:
        print("Not balanced:", problem)
    else:
        print("Balanced!")


if __name__ == "__main__":
    main()
