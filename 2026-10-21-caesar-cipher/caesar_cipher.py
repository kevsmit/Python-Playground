"""Encode or decode text with a Caesar cipher."""
import sys


def shift_text(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)


def main():
    mode = input("Encode or decode? (e/d): ").strip().lower()
    text = input("Text: ")
    shift = int(input("Shift (1-25): "))
    if mode == "d":
        shift = -shift
    print(shift_text(text, shift))


if __name__ == "__main__":
    if "--test" in sys.argv:
        assert shift_text("Hello, World!", 3) == "Khoor, Zruog!"
        assert shift_text("Khoor, Zruog!", -3) == "Hello, World!"
        print("ok")
    else:
        main()
