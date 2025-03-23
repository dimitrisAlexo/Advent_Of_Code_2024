import numpy as np


def assess_safety(filename):
    safe_count = 0

    with open(filename, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))

            diffs = np.diff(report)  # Compute differences between adjacent levels

            # Check if all differences are within the allowed range (1 to 3 in absolute value)
            if not all(1 <= abs(d) <= 3 for d in diffs):
                continue

            # Check if strictly increasing or strictly decreasing
            if all(d > 0 for d in diffs) or all(d < 0 for d in diffs):
                safe_count += 1

    print("Number of safe reports:", safe_count)
    return safe_count


assess_safety('input.txt')
