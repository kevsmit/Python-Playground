import getpass
import string

COMMON = {"password", "123456", "12345678", "qwerty", "letmein", "abc123", "111111", "iloveyou", "admin", "welcome"}


def check(pw):
    tips = []
    score = 0

    if len(pw) >= 12:
        score += 2
    elif len(pw) >= 8:
        score += 1
    else:
        tips.append("make it at least 8 characters")

    groups = [
        (string.ascii_lowercase, "a lowercase letter"),
        (string.ascii_uppercase, "an uppercase letter"),
        (string.digits, "a number"),
        (string.punctuation, "a symbol"),
    ]
    for chars, name in groups:
        if any(c in chars for c in pw):
            score += 1
        else:
            tips.append("add " + name)

    if pw.lower() in COMMON:
        score = 0
        tips.insert(0, "this is a very common password, pick something else")

    if score <= 2:
        label = "weak"
    elif score <= 4:
        label = "ok"
    else:
        label = "strong"
    return label, score, tips


def main():
    pw = getpass.getpass("Password to check (hidden): ")
    label, score, tips = check(pw)
    print(f"Strength: {label} ({score}/6)")
    for t in tips:
        print(" -", t)


if __name__ == "__main__":
    main()
