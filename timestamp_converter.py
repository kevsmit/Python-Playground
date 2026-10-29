from datetime import datetime, timezone


def main():
    choice = input("Convert (1) timestamp to date or (2) date to timestamp? ").strip()
    try:
        if choice == "1":
            stamp = float(input("Unix timestamp: "))
            date = datetime.fromtimestamp(stamp, timezone.utc)
            print("UTC:", date.strftime("%Y-%m-%d %H:%M:%S"))
        elif choice == "2":
            value = input("UTC date and time (YYYY-MM-DD HH:MM:SS): ").strip()
            date = datetime.strptime(value, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
            print("Unix timestamp:", int(date.timestamp()))
        else:
            print("Choose 1 or 2.")
    except (ValueError, OSError, OverflowError):
        print("Invalid input or timestamp.")


if __name__ == "__main__":
    main()
