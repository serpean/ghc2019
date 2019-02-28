from stdio import read_input, write_output
from random import randint
import numpy as np
import time

# FILENAME = 'c_memorable_moments.txt'
FILENAME = 'd_pet_pictures.txt'
FILENAME_INPUT = 'input/' + FILENAME
FILENAME_OUTPUT_BASE = 'output/' + FILENAME


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
    h, v = separate_h_v(pictures, n)
    slides = generate_slides(h, v)
    next_common = 0
    used = np.zeros_like(slides)
    used[next_common] = 1
    res = [next_common]
    while True:
        next_common = get_next_common_tag(pictures, slides[next_common], n, used)
        if not next_common:
            break
        res.append(next_common)
        used[next_common] = 1
    # write(res)
    print(res)

greedy()
