"""Find free time slots in a day given a list of busy meetings."""

import sys

DAY_START = "09:00"
DAY_END = "17:00"

SAMPLE = [
    ("09:30", "10:15"),
    ("10:00", "11:00"),
    ("12:00", "13:00"),
    ("14:30", "15:00"),
    ("14:45", "15:30"),
]


def to_minutes(t):
    h, m = t.split(":")
    return int(h) * 60 + int(m)


def to_clock(mins):
    return f"{mins // 60:02d}:{mins % 60:02d}"


def merge(slots):
    slots = sorted(slots)
    merged = []
    for start, end in slots:
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def free_slots(busy, day_start, day_end, min_length=0):
    free = []
    current = day_start
    for start, end in merge(busy):
        if start > current:
            free.append((current, min(start, day_end)))
        current = max(current, end)
        if current >= day_end:
            break
    if current < day_end:
        free.append((current, day_end))
    return [(s, e) for s, e in free if e - s >= min_length and e > s]


def read_file(path):
    busy = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            start, end = line.split("-")
            busy.append((start.strip(), end.strip()))
    return busy


def main():
    args = sys.argv[1:]
    min_length = 0
    if "--min" in args:
        i = args.index("--min")
        min_length = int(args[i + 1])
        del args[i:i + 2]

    busy = read_file(args[0]) if args else SAMPLE
    busy_mins = [(to_minutes(s), to_minutes(e)) for s, e in busy]

    print(f"Day: {DAY_START} - {DAY_END}")
    print("Busy:")
    for s, e in merge(busy_mins):
        print(f"  {to_clock(s)} - {to_clock(e)}")

    slots = free_slots(busy_mins, to_minutes(DAY_START), to_minutes(DAY_END), min_length)
    print("Free:")
    if not slots:
        print("  nothing, sorry")
    for s, e in slots:
        print(f"  {to_clock(s)} - {to_clock(e)}  ({e - s} min)")


if __name__ == "__main__":
    main()
