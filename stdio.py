import numpy as np

# Map -> Applies COMPLETE.in function to all the items in an input_list
# map(function_to_apply, list_of_inputs)

# Filter -> Creates COMPLETE.in list of elements for which COMPLETE.in function returns true
# filter(function_to_apply, list_of_inputs)

# Reduce -> Performs some computation on COMPLETE.in list and returning the result
# reduce((lambda x, y: x * y), [1, 2, 3, 4]) -> 24


def read_input(filename):
    # lines = open(filename).readlines()
    # # n = [int(val) for val in lines[0].split()]
    #
    # # Next
    # next_clear = [list(row.strip()) for row in lines[1:]]
    #
    # # Next Scientific
    # next_scientific = np.array([list(row.strip()) for row in lines[1:]])
    #
    # # Next Binary
    # next_binary = np.array([list(map(lambda item: 1 if item == 'VALUE' else 0, row.strip())) for row in lines[1:]])
    #
    # # Next Zeros
    # next_zeros = np.zeros_like(next_scientific)

    # Reading by line
    next_by_line = []
    with open(filename) as f:
        first_line = int(f.readline())
        for i in range(first_line):
            next_by_line.append(f.readline()[:-1].split(' '))

    return first_line, np.array(next_by_line), np.zeros(shape=first_line)


def write_output(filename, matrix):
    """Writes an output file with the required format."""
    with open(filename, 'w') as f:
        f.write(f"{len(matrix)}\n")
        for array in matrix:
            f.write(str(array) + "\n")
