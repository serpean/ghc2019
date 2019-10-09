from lib.stdio import read_input, write_output
from random import randint

import time

# FILENAME = 'c_memorable_moments.txt'
FILENAME = 'd_pet_pictures.txt'
FILENAME_INPUT = 'input/' + FILENAME
FILENAME_OUTPUT_BASE = 'output/' + FILENAME


def create_hash(pics):
    result = {}
    for pic in pics:
        for tag in pic[1]:
            if tag not in result:
                result[tag] = []
            result[tag] = result[tag] + pic[0]


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


def get_tags(pictures, id):
    return pictures[id][2:]


def have_common_tags(pictures, id1, id2):
    tags1 = get_tags(pictures, id1)
    tags2 = get_tags(pictures, id2)
    return len(list(set(tags1).intersection(tags2)))


def get_next_common_tag(pictures, id, n, used):
    i = randint(0, n-1)  # Far better resolution
    l = 0

    # FIXME FIRST MERGE SLIDES TAGS
    # while l < n:
    #     if not used[i]:
    #         if have_common_tags(pictures, id, i[0]):
    #             return i
    #     i = ((i + 1) % n)
    #     l += 1
    # return None


def separate_h_v(pictures, n):
    h = []
    v = []
    for i in range(n):
        if pictures[i][0] == 'H':
            h.append(i)
        else:
            v.append(i)
    return h, v


def generate_slides(h, v):
    slides = []
    for i in range(len(h)):
        slides.append([h[i]])
    for i in range(int(len(v)/2)):
        slides.append([v[i], v[i+1]])
    return slides


def greedy_all_pictures_equal():
    n, pictures, used = read_input(FILENAME_INPUT)
    next_common = 0
    used[next_common] = 1
    res = [next_common]
    while True:
        next_common = get_next_common_tag(pictures, next_common, n, used)
        if not next_common:
            break
        res.append(next_common)
        used[next_common] = 1
    write(res)


def greedy():
    n, pictures, used = read_input(FILENAME_INPUT)
    horizontal = separateArray(pictures, 'H')
    vertical = separateArray(pictures, 'V')
    mez = random_merge_v_array(horizontal, vertical)
    print(create_hash(mez))
    scoreNum = countDuplicates(mez)
    print(scoreNum)
    #h, v = separate_h_v(pictures, n)
    #slides = generate_slides(h, v)
    #next_common = 0
    #used = np.zeros_like(slides)
    #used[next_common] = 1
    #res = [next_common]
    #while True:
    #    next_common = get_next_common_tag(pictures, slides[next_common], n, used)
    #    if not next_common:
    #        break
    #    res.append(next_common)
    #    used[next_common] = 1
    ## write(res)
    #print(res)

greedy()
