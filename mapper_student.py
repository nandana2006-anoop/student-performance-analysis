#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    columns = line.split(",")

    if columns[0].strip().lower() in ("student_id", "student id"):
        continue

    if len(columns) < 4:
        continue

    try:
        student_id = columns[0].strip()
        math = float(columns[1])
        english = float(columns[2])
        science = float(columns[3])
    except ValueError:
        continue

    marks = [math, english, science]

    if any(mark < 0 or mark > 100 for mark in marks):
        continue

    total = sum(marks)
    average = total / 3

    if average >= 85:
        category = "Top Students"
    elif average < 30:
        category = "Weak Students"
    else:
        category = "Average Students"

    print(f"{category}\t{student_id}\t{total:.2f}\t{average:.2f}")
