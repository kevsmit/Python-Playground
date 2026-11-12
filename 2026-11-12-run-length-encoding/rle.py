import sys


def encode(text):
    if not text:
        return ""
    out = []
    current = text[0]
    count = 1
    for ch in text[1:]:
        if ch == current:
            count += 1
        else:
            out.append(f"{count}{current}")
            current = ch
            count = 1
    out.append(f"{count}{current}")
    return "".join(out)


def decode(text):
    out = []
    num = ""
    for ch in text:
        if ch.isdigit():
            num += ch
        else:
            if not num:
                raise ValueError(f"missing count before '{ch}'")
            out.append(ch * int(num))
            num = ""
    if num:
        raise ValueError("encoded text ends with a number")
    return "".join(out)


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ("encode", "decode"):
        print("usage: python rle.py encode|decode TEXT")
        print()
        sample = "AAABBBCCCCD"
        packed = encode(sample)
        print(f"example: {sample} -> {packed} -> {decode(packed)}")
        return

    mode, text = sys.argv[1], " ".join(sys.argv[2:])
    try:
        result = encode(text) if mode == "encode" else decode(text)
    except ValueError as e:
        print(f"error: {e}")
        sys.exit(1)
    print(result)


if __name__ == "__main__":
    main()
