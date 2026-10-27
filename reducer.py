#!/usr/bin/env python3
import sys

current_key = None
total = 0.0
count = 0
passes = 0
fails = 0

def emit(key, total, count, passes, fails):
    if key is None:
        return

    if key == "PASS_STATUS":
        print(f"PASS_COUNT\t{passes}")
        print(f"FAIL_COUNT\t{fails}")
    elif count:
        print(f"{key}_AVERAGE\t{total / count:.2f}")

for line in sys.stdin:
    line = line.rstrip("\n")
    parts = line.split("\t", 1)

    if len(parts) != 2:
        continue

    key, value = parts

    if key != current_key:
        emit(current_key, total, count, passes, fails)
        current_key = key
        total = 0.0
        count = 0
        passes = 0
        fails = 0

    if key == "PASS_STATUS":
        if value == "PASS":
            passes += 1
        elif value == "FAIL":
            fails += 1
    else:
        try:
            total += float(value)
            count += 1
        except ValueError:
            continue

emit(current_key, total, count, passes, fails)
