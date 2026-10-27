
#!/usr/bin/env python3
import sys

current_category = None
student_count = 0
total_marks_sum = 0.0
average_sum = 0.0

def print_result(category, count, marks_sum, avg_sum):
    if category is not None and count > 0:
        print(
            f"{category}\tStudents: {count}"
            f"\tAverage total marks: {marks_sum / count:.2f}"
            f"\tAverage student average: {avg_sum / count:.2f}"
        )

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        category, student_id, total, average = line.split("\t")
        total = float(total)
        average = float(average)
    except ValueError:
        continue

    if current_category is not None and category != current_category:
        print_result(
            current_category, student_count,
            total_marks_sum, average_sum
        )
        student_count = 0
        total_marks_sum = 0.0
        average_sum = 0.0

    current_category = category
    student_count += 1
    total_marks_sum += total
    average_sum += average

if current_category is not None:
    print_result(
        current_category, student_count,
        total_marks_sum, average_sum
    )

