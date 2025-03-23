import numpy as np


def compute_total_distance(filename):
    # Load the two columns from the file
    left_column, right_column = np.loadtxt(filename, unpack=True, dtype=int)

    # Sort both columns
    left_column.sort()
    right_column.sort()

    # Compute elementwise distances
    distances = np.abs(left_column - right_column)

    # Compute the total distance
    total_distance = np.sum(distances)

    print("Total Distance:", total_distance)

    return total_distance


# Call the function with the input file
compute_total_distance('input.txt')
