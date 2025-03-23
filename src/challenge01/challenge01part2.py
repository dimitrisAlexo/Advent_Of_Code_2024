import numpy as np
from collections import Counter


def compute_similarity_score(filename):
    # Load the two columns from the file
    left_column, right_column = np.loadtxt(filename, unpack=True, dtype=int)

    # Count occurrences in the right list
    right_counts = Counter(right_column)

    similarity_score = sum(num * right_counts[num] for num in left_column)

    print("Similarity Score:", similarity_score)

    # Compute similarity score
    return similarity_score


compute_similarity_score('input.txt')
