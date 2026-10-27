#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)

for row in reader:
    try:
        if len(row) < 4:
            continue

        if row[0].strip().lower() == "student_id":
            continue

        student_id = row[0].strip()
        math = float(row[1])
        english = float(row[2])
        science = float(row[3])

        if not student_id:
            continue

        if not all(0 <= mark <= 100 for mark in [math, english, science]):
            continue

        average = (math + english + science) / 3

        if average >= 85:
            category = "Top Students"
        elif average >= 35:
            category = "Other Students"
        else:
            category = "Weak Students"

        print(f"{category}\t{student_id}\t{math:.2f}\t{english:.2f}\t{science:.2f}\t{average:.2f}")

    except (ValueError, TypeError, IndexError):
        continue
