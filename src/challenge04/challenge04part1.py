import numpy as np


def count_xmas(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file]

    grid = np.array(grid)
    rows, cols = grid.shape
    target = "XMAS"
    length = len(target)
    count = 0

    directions = [
        (1, 0),  # Vertical down
        (0, 1),  # Horizontal right
        (1, 1),  # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (-1, 0),  # Vertical up
        (0, -1),  # Horizontal left
        (-1, -1),  # Diagonal up-left
        (-1, 1)  # Diagonal up-right
    ]

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if all(0 <= r + i * dr < rows and 0 <= c + i * dc < cols and grid[r + i * dr, c + i * dc] == target[i]
                       for i in range(length)):
                    count += 1

    print("Total occurrences of XMAS:", count)
    return count


count_xmas('input.txt')
