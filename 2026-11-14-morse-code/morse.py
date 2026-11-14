import sys

MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--", "'": ".----.",
    "/": "-..-.", "-": "-....-", "@": ".--.-.", ":": "---...",
}
BACK = {v: k for k, v in MORSE.items()}


def to_morse(text):
    words = []
    for word in text.upper().split():
        letters = [MORSE[c] for c in word if c in MORSE]
        if letters:
            words.append(" ".join(letters))
    return " / ".join(words)


def from_morse(code):
    words = []
    for word in code.strip().split("/"):
        letters = [BACK.get(sym, "?") for sym in word.split()]
        if letters:
            words.append("".join(letters))
    return " ".join(words)


def looks_like_morse(text):
    return all(c in ".-/ " for c in text.strip())


def main():
    if len(sys.argv) < 2:
        for sample in ["SOS", "Hello World", "... --- ..."]:
            if looks_like_morse(sample):
                print(f"{sample!r} -> {from_morse(sample)}")
            else:
                print(f"{sample!r} -> {to_morse(sample)}")
        return

    text = " ".join(sys.argv[1:])
    if looks_like_morse(text):
        print(from_morse(text))
    else:
        print(to_morse(text))


if __name__ == "__main__":
    main()
