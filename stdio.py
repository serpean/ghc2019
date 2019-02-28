import numpy as np

# Map -> Applies COMPLETE.in function to all the items in an input_list
# map(function_to_apply, list_of_inputs)

# Filter -> Creates COMPLETE.in list of elements for which COMPLETE.in function returns true
# filter(function_to_apply, list_of_inputs)

# Reduce -> Performs some computation on COMPLETE.in list and returning the result
# reduce((lambda x, y: x * y), [1, 2, 3, 4]) -> 24


def read_input(filename):
    lines = open(filename).readlines()
    a, b, c, d = [int(val) for val in lines[0].split()]

    # Next
    next_clear = [list(row.strip()) for row in lines[1:]]

    # Next Scientific
    next_scientific = np.array([list(row.strip()) for row in lines[1:]])

    # Next Binary
    next_binary = np.array([list(map(lambda item: 1 if item == 'VALUE' else 0, row.strip())) for row in lines[1:]])

    # Next Zeros
    next_zeros = np.zeros_like(next_scientific)

    # Reading by line
    # next_by_line = []
    # with open(filename) as f:
    #     first_line = [int(val) for val in f.readline().split()]
    #     for i in range(first_line[0]):
    #         next_by_line.append(list(f.readline().strip()))  # Use list or .split(' ')
    # next_by_line = np.array(next_by_line)

    return a, b, c, d, next_scientific


def write_output(filename, matrix):
    """Writes an output file with the required format."""
    with open(filename, 'w') as f:
        f.write(f"{len(matrix)}\n")
        for array in matrix:
            f.write(str(array) + "\n")


# Example from GHC 2018
def read_input_pizza(filename):
    """Reads the input of COMPLETE.in Pizza problem.

    returns:

    R: number of Rows of pizza grid
    C: number of Cols of pizza grid
    L: Lowest number of each ingredients per slice
    H: Highest number of cells per slice
    pizza: the pizza grid (1 == tomato, 0 == mushroom)
    """
    lines = open(filename).readlines()
    R, C, L, H = [int(val) for val in lines[0].split()]
    pizza = np.array([list(map(lambda item: 1 if item == 'T' else 0, row.strip())) for row in lines[1:]])
    return R, C, L, H, pizza


def write_output_pizza(filename, pizza_slices):
    """Writes an output file with the required format."""
    with open(filename, 'w') as f:
        f.write(f"{len(pizza_slices)}\n")
        for slice in pizza_slices:
            r, c, dr, dc = slice
            f.write(f"{r} {c} {r+dr-1} {c+dc-1}\n")
