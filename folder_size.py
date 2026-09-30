from pathlib import Path

folder_text = input("Folder to measure (blank for current folder): ").strip()
folder = Path(folder_text or ".")

if not folder.is_dir():
    print("That folder does not exist.")
else:
    total_bytes = 0
    file_count = 0

    for item in folder.rglob("*"):
        if item.is_file():
            try:
                total_bytes += item.stat().st_size
                file_count += 1
            except OSError:
                print(f"Skipped: {item}")

    print(f"Files counted: {file_count}")
    print(f"Total size: {total_bytes / (1024 * 1024):.2f} MB")
