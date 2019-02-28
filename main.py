from stdio import read_input, write_output
import time

FILENAME_INPUT = 'input/a_example.txt'
FILENAME_OUTPUT_BASE = 'output/results'


def remove_newline(name):
    if name[-2:] == '\n':
        return name[:-2]
    return name


def create_hash(pics):
    result = {}
    i = 0
    while i < len(pics):
        j = 2
        while j < len(pics[i]):
            result[remove_newline(pics[i][j])] = i
            j = j+1
        i=i+1
    return result


def write(matrix):
    filename_output = FILENAME_OUTPUT_BASE + time.strftime("%H%M%S")
    write_output(filename_output, matrix)


def greedy():
    n, pictures = read_input(FILENAME_INPUT)
    #print(pictures)
    print(create_hash(pictures))


greedy()
