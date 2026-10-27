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
        math = float(columns[1])
        english = float(columns[2])
        science = float(columns[3])
    except ValueError:
        continue

    for subject, marks in [
        ("Math", math),
        ("English", english),
        ("Science", science)
    ]:
        result = "Pass" if marks >= 35 else "Fail"
        print(f"{subject}\t{marks}\t{result}")
