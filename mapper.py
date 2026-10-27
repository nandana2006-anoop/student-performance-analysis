#!/usr/bin/env python3
import csv
import sys

reader = csv.reader(sys.stdin)

for row in reader:
    if not row or row[0].strip().lower() == "student_id":
        continue

    try:
        student_id = row[0].strip()
        marks = [float(x) for x in row[1:4]]

        if len(marks) != 3:
            continue
        if any(mark < 0 or mark > 100 for mark in marks):
            continue

        for subject, mark in zip(
            ["MATH", "ENGLISH", "SCIENCE"], marks
        ):
            print(f"{subject}\t{mark}")

        average = sum(marks) / 3
        status = "PASS" if average >= 40 else "FAIL"
        print(f"PASS_STATUS\t{status}")

    except (ValueError, IndexError):
        print("Skipping invalid row", file=sys.stderr)
