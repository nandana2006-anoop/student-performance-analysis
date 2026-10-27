#!/usr/bin/env python3
import sys

current_category = None
count = 0
total_average = 0.0

def emit(category, count, total):
    if category is not None and count > 0:
        print(f"{category}\tStudents: {count}\tAverage marks: {total / count:.2f}")

for line in sys.stdin:
    parts = line.rstrip("\n").split("\t")

    if len(parts) != 6:
        continue

    category = parts[0]

    try:
        average = float(parts[5])
    except ValueError:
        continue

    if current_category is not None and category != current_category:
        emit(current_category, count, total_average)
        count = 0
        total_average = 0.0

    current_category = category
    count += 1
    total_average += average

if current_category is not None:
    emit(current_category, count, total_average)
