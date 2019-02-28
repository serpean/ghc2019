from stdio import read_input, write_output
import time

FILENAME_INPUT = 'input/c_memorable_moments.txt'
FILENAME_OUTPUT_BASE = 'output/results'


def write(matrix):
    filename_output = FILENAME_OUTPUT_BASE + time.strftime("%H%M%S")
    write_output(filename_output, matrix)


def get_tags(matrix, id):
    return matrix[id][2:]


def get_next_common_tag(matrix, id, n, pictures, used):
    pass


def greedy():
    n, pictures, used = read_input(FILENAME_INPUT)
    res = [0]
    print(res)


greedy()
