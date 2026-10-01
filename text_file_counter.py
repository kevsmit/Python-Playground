from pathlib import Path

path_text = input("Text file to count: ").strip()
path = Path(path_text)

if not path.is_file():
    print("That file does not exist.")
else:
    try:
        text = path.read_text(encoding="utf-8")
        words = text.split()
        lines = text.splitlines()
        print(f"Words: {len(words)}")
        print(f"Characters: {len(text)}")
        print(f"Lines: {len(lines)}")
    except (OSError, UnicodeError):
        print("Could not read that file as UTF-8 text.")
