from collections import Counter
from pathlib import Path

folder_text = input("Folder to check (leave blank for current folder): ").strip()
folder = Path(folder_text or ".")

if not folder.is_dir():
    print("That folder does not exist.")
else:
    extensions = Counter(
        file.suffix.lower() or "[no extension]"
        for file in folder.iterdir()
        if file.is_file()
    )

    if not extensions:
        print("No files found in that folder.")
    else:
        for extension, count in extensions.most_common():
            print(f"{extension}: {count}")
