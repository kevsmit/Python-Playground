from pathlib import Path

folder_text = input("Folder to search (blank for current folder): ").strip()
search_text = input("Part of the filename to find: ").strip().casefold()
folder = Path(folder_text or ".")

if not folder.is_dir():
    print("That folder does not exist.")
elif not search_text:
    print("Enter something to search for.")
else:
    matches = 0
    try:
        for item in folder.rglob("*"):
            if item.is_file() and search_text in item.name.casefold():
                print(item)
                matches += 1
                if matches == 20:
                    print("Showing the first 20 matches.")
                    break
        if matches == 0:
            print("No matching files found.")
    except OSError as error:
        print(f"Could not finish the search: {error}")
