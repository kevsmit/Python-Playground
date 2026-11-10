"""Small stats helper for a list of daily temperatures."""
import sys


def summarize(temps):
    """Return min, max, average and the biggest day-to-day jump."""
    if not temps:
        raise ValueError("no temperatures given")
    biggest_jump = 0.0
    for prev, cur in zip(temps, temps[1:]):
        biggest_jump = max(biggest_jump, abs(cur - prev))
    return {
        "min": min(temps),
        "max": max(temps),
        "average": sum(temps) / len(temps),
        "biggest_jump": biggest_jump,
    }


def main():
    if len(sys.argv) > 1:
        raw = sys.argv[1:]
    else:
        raw = input("Enter temperatures separated by spaces: ").split()
    try:
        temps = [float(x) for x in raw]
        stats = summarize(temps)
    except ValueError as err:
        print("Problem:", err)
        return
    print(f"Days:         {len(temps)}")
    print(f"Lowest:       {stats['min']:.1f}")
    print(f"Highest:      {stats['max']:.1f}")
    print(f"Average:      {stats['average']:.1f}")
    print(f"Biggest jump: {stats['biggest_jump']:.1f}")


if __name__ == "__main__":
    main()
