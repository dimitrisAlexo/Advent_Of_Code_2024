import re


def result_of_controlled_multiplications(filename):
    mul_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')  # Matches valid mul(X,Y)
    control_pattern = re.compile(r"do\(\)|don't\(\)")  # Matches do() and don't()

    total = 0
    enabled = True  # Multiplications start enabled

    with open(filename, 'r') as file:
        for line in file:
            for token in re.finditer(f'{control_pattern.pattern}|{mul_pattern.pattern}', line):
                match = token.group()
                if match == "do()":
                    enabled = True
                elif match == "don't()":
                    enabled = False
                else:
                    x, y = mul_pattern.match(match).groups()
                    if enabled:
                        total += int(x) * int(y)

    print("Sum of enabled multiplications:", total)
    return total


result_of_controlled_multiplications('input.txt')
