from stdio import read_input, write_output
import time

FILENAME_INPUT = 'input/COMPLETE.in'
FILENAME_OUTPUT_BASE = 'output/results'


def write(matrix):
    filename_output = FILENAME_OUTPUT_BASE + time.strftime("%H%M%S")
    write_output(filename_output, matrix)


def greedy():
    read_input(FILENAME_INPUT)
    # a, b, c, d, body = read_input(FILENAME_INPUT)
    # print(body)


greedy()
