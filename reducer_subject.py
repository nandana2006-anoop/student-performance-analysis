
#!/usr/bin/env python3
import sys

current_subject = None
total_marks = 0.0
total_students = 0
pass_count = 0
fail_count = 0

def print_result(subject, total, count, passed, failed):
    if count > 0:
        average = total / count
        print(
            f"{subject}\tAverage: {average:.2f}"
            f"\tPass count: {passed}"
            f"\tFail count: {failed}"
            f"\tTotal students: {count}"
        )

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        subject, marks, result = line.split("\t")
        marks = float(marks)
    except ValueError:
        continue

    if current_subject is not None and subject != current_subject:
        print_result(
            current_subject, total_marks, total_students,
            pass_count, fail_count
        )
        total_marks = 0.0
        total_students = 0
        pass_count = 0
        fail_count = 0

    current_subject = subject
    total_marks += marks
    total_students += 1

    if result == "Pass":
        pass_count += 1
    else:
        fail_count += 1

if current_subject is not None:
    print_result(
        current_subject, total_marks, total_students,
        pass_count, fail_count
    )
