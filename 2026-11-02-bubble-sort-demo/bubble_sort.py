"""Bubble sort demo that prints each pass so you can watch it work."""
import sys


def bubble_sort(items):
    items = list(items)
    for end in range(len(items) - 1, 0, -1):
        swapped = False
        for i in range(end):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True
        print(f"After pass {len(items) - end}: {items}")
        if not swapped:
            break
    return items


def main():
    if len(sys.argv) > 1:
        numbers = [int(x) for x in sys.argv[1:]]
    else:
        numbers = [5, 2, 9, 1, 7, 3]
    print(f"Start: {numbers}")
    print(f"Sorted: {bubble_sort(numbers)}")


if __name__ == "__main__":
    main()
