"""Turn a CSV file into a markdown table.

Numbers get right aligned, everything else left aligned.
"""

import csv
import sys


def is_number(text):
    try:
        float(text.replace(",", ""))
        return True
    except ValueError:
        return False


def read_rows(path):
    with open(path, newline="") as f:
        rows = [row for row in csv.reader(f) if row]
    if not rows:
        raise SystemExit("file is empty")
    width = max(len(r) for r in rows)
    # pad short rows so every row has the same number of cells
    return [r + [""] * (width - len(r)) for r in rows]


def make_table(rows):
    header, body = rows[0], rows[1:]
    cols = len(header)

    widths = [max(len(r[i].strip()) for r in rows) for i in range(cols)]
    widths = [max(w, 3) for w in widths]

    # a column counts as numeric if every non-blank value is a number
    numeric = []
    for i in range(cols):
        values = [r[i].strip() for r in body if r[i].strip()]
        numeric.append(bool(values) and all(is_number(v) for v in values))

    def fmt(row):
        cells = []
        for i, cell in enumerate(row):
            cell = cell.strip().replace("|", "\\|")
            if numeric[i]:
                cells.append(cell.rjust(widths[i]))
            else:
                cells.append(cell.ljust(widths[i]))
        return "| " + " | ".join(cells) + " |"

    divider = []
    for i in range(cols):
        if numeric[i]:
            divider.append("-" * (widths[i] - 1) + ":")
        else:
            divider.append("-" * widths[i])

    lines = [fmt(header), "| " + " | ".join(divider) + " |"]
    lines += [fmt(r) for r in body]
    return "\n".join(lines)


def main():
    if len(sys.argv) != 2:
        print("usage: python table_maker.py file.csv")
        sys.exit(1)
    print(make_table(read_rows(sys.argv[1])))


if __name__ == "__main__":
    main()
