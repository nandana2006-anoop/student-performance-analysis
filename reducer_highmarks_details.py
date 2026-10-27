#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.rstrip("\n")
    if not line:
        continue

    parts = line.split("\t")
    if len(parts) != 6:
        continue

    category, student_id, math, english, science, average = parts

    print(
        f"{student_id}\t{math}\t{english}\t{science}\t"
        f"{average}\t{category}"
    )
