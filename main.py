from stdio import read_input, write_output
import time

FILENAME_INPUT = 'input/a_example.txt'
FILENAME_OUTPUT_BASE = 'output/results'


def create_hash(pics):
    result = {}
    i = 0
    while i < len(pics):
        j = 2
        while j < len(pics[i]):
            if pics[i][j] not in result:
                result[pics[i][j]] = []
            result[pics[i][j]].append(i)
            j = j+1
        i=i+1
    return result


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
    hash = create_hash(pictures)


greedy()
