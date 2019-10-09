import numpy as np


def read(file_path):
    """
    Reads the content from an input file and returns the size of the square matrix and the matrix itself.
    """
    content = []
    with open(file_path) as f:
        size = int(f.readline())
        for i in range(size):
            content.append(f.readline()[:-1].split(' '))

    return size, np.array(content)


def write(file_path, matrix):
    """
    Writes matrix to an output file using the required format.
    """
    with open(file_path, 'w') as f:
        f.write(f"{len(matrix)}\n")
        for array in matrix:
            f.write(str(array) + "\n")
