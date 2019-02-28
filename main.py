from stdio import read_input, write_output
from random import randint
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

def separateArray(pics, variable):
    i = 0
    result = []
    while i < len(pics):
        if pics[i][0] == variable:
            j = 2
            aux = [[i]]
            app = []
            while j < len(pics[i]):
                app.append(pics[i][j])
                j = j + 1
            aux.append(app)
            result.append(aux)
        i = i + 1
    return result


def merge_v(p1, p2):
    #input [[id], [cat, dog, beach]]
    common=set(p1[1]).union(set(p2[1]))
    return list([p1[0]+p2[0],list(common)])

def random_merge_v_array(h_array, v_array):
    if(len(v_array)<2):
        return h_array
    value_in=v_array[0]
    value_in
    value_ran=v_array[randint(1, len(v_array)-1)]
    h_array.append(merge_v(value_in, value_ran))
    v_array.remove(value_in)
    v_array.remove(value_ran)
    return random_merge_v_array(h_array, v_array)


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
    #hash = create_hash(pictures)
    vertical = separateArray(pictures, 'V')
    horizontal = separateArray(pictures, 'H')
    mez=random_merge_v_array(horizontal, vertical)
    print(mez)


greedy()
