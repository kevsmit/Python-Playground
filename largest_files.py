from pathlib import Path

folder_text = input("Folder to scan (blank for current folder): ").strip()
folder = Path(folder_text or ".")

if not folder.is_dir():
    print("That folder does not exist.")
else:
    files = []
    for item in folder.rglob("*"):
        if item.is_file():
            try:
                files.append((item.stat().st_size, item))
            except OSError:
                print(f"Skipped: {item}")

    if not files:
        print("No files found.")
    else:
        print("Five largest files:")
        for size, path in sorted(files, reverse=True)[:5]:
            print(f"{size / (1024 * 1024):.2f} MB - {path}")
