print("Download time estimate")

try:
    size_gb = float(input("File size in GB: "))
    speed_mbps = float(input("Download speed in Mbps: "))

    if size_gb < 0 or speed_mbps <= 0:
        print("Use a nonnegative file size and speed greater than zero.")
    else:
        seconds = size_gb * 8_000 / speed_mbps
        hours, remainder = divmod(round(seconds), 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"Estimated time: {hours}h {minutes}m {seconds}s")
        print("Actual downloads can take longer due to overhead or slow servers.")
except ValueError:
    print("Please enter numbers only.")
