def count_x_mas(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file]

    rows = len(grid)
    cols = len(grid[0])
    counter = 0

    def is_valid_x_mas(x, y):
        # Out of bounds check
        part1 = False
        part2 = False
        if (((x - 1 >= 0) and (y - 1 >= 0)) and ((x + 1 < rows) and (y + 1 < cols))):
            # Top right to bottom left
            if grid[x - 1][y - 1] == "M" and grid[x + 1][y + 1] == "S":
                part1 = True
            if grid[x - 1][y - 1] == "S" and grid[x + 1][y + 1] == "M":
                part1 = True

            # Top left to bottom right
            if grid[x - 1][y + 1] == "M" and grid[x + 1][y - 1] == "S":
                part2 = True
            if grid[x - 1][y + 1] == "S" and grid[x + 1][y - 1] == "M":
                part2 = True

        return part1 and part2

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "A":
                if is_valid_x_mas(x, y):
                    counter += 1

    print("Total occurrences of X-MAS:", counter)
    return counter


count_x_mas('input.txt')
