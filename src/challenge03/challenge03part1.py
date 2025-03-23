import re


def result_of_multiplications(filename):
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")  # Regular expression to match valid mul(X,Y) patterns
    total = 0

    with open(filename, 'r') as file:
        for line in file:
            matches = pattern.findall(line)
            for x, y in matches:
                total += int(x) * int(y)

    print("Sum of all valid multiplications:", total)
    return total


result_of_multiplications('input.txt')
