import numpy as np


def is_safe(report):

    diffs = np.diff(report)

    # Check if the report is already safe
    if all(1 <= abs(d) <= 3 for d in diffs) and (all(d > 0 for d in diffs) or all(d < 0 for d in diffs)):
        return True

    # Try removing one level at a time and check if it becomes safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]  # Remove one level
        modified_diffs = np.diff(modified_report)

        if all(1 <= abs(d) <= 3 for d in modified_diffs) and (
                all(d > 0 for d in modified_diffs) or all(d < 0 for d in modified_diffs)):
            return True

    return False


def assess_safety_with_dampener(filename):
    safe_count = 0

    with open(filename, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe(report):
                safe_count += 1

    print("Number of safe reports with dampener:", safe_count)
    return safe_count


assess_safety_with_dampener('input.txt')
