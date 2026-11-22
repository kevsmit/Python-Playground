# Free Time Finder

Give it a list of meetings and it tells you what gaps are left in the
work day (9 to 5). Overlapping meetings get merged together first.

Uses a built-in example if you don't give it a file.

## Run

    python free_time.py
    python free_time.py meetings.txt
    python free_time.py meetings.txt --min 30

`--min` hides gaps shorter than that many minutes.

File is one meeting per line:

    09:30-10:15
    12:00-13:00
    # lines starting with # are skipped
