import shutil
from pathlib import Path

folder = Path(input("Folder or drive path (blank for current folder): ").strip() or ".").expanduser()

try:
    total, used, free = shutil.disk_usage(folder)
    gb = 1024 ** 3

    print(f"\nDrive: {folder.resolve()}")
    print(f"Total: {total / gb:.2f} GB")
    print(f"Used:  {used / gb:.2f} GB")
    print(f"Free:  {free / gb:.2f} GB")
    print(f"Used:  {used / total * 100:.1f}%")
except OSError as error:
    print(f"Could not check that path: {error}")
