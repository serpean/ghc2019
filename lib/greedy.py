from .io import read, write
from random import randint
import numpy as np


def get_slide_tags(pictures_matrix, slides_list, slide_id):
    """
    Returns the list of tags hosted by a slide.
    """
    tags = []
    for picture in slides_list[slide_id]:
        for tag in pictures_matrix[picture][2:]:
            tags.append(tag)
    return tags


def have_common_tags(pictures_matrix, slides_list, slide_id_1, slide_id_2):
    """
    Returns true if two slides have tags in common.
    """
    tags_slide_1 = get_slide_tags(pictures_matrix, slides_list, slide_id_1)
    tags_slide_2 = get_slide_tags(pictures_matrix, slides_list, slide_id_2)
    return not set(tags_slide_1).isdisjoint(tags_slide_2)


def get_next_valid_slide(pictures_matrix, slides_list, slide_id, used_slides_list):
    """
    Returns the first valid slide found that has not been used and has tags in common with the passed slide or None if
    there are not valid slides available left.
    """

    # First target slide id is selected using a random approach
    target_slided_id = randint(0, len(slides_list)-1)  # Note: Far better resolution for random. Chaos means equality ;D

    # A number saving the number of checked slides is stored to prevent an infinite search of valid pictures
    checked_slides = 0

    # Keep searching while there are still some slides available left
    while checked_slides < len(slides_list):
        if not used_slides_list[target_slided_id]:
            if have_common_tags(pictures_matrix, slides_list, slide_id, target_slided_id):
                return target_slided_id

        # If the current target slide is not valid, just try the next one
        target_slided_id = ((target_slided_id + 1) % (len(slides_list)))
        checked_slides += 1

    # Return None if there are not valid slides available left
    return None


def sort_pictures(pictures_matrix, size):
    """
    Sort pictures matrix to separate its elements between the horizontal and the vertical ones
    """
    horizontal_pictures_list = []
    vertical_pictures_list = []
    for i in range(size):
        if pictures_matrix[i][0] == 'H':
            horizontal_pictures_list.append(i)
        else:
            vertical_pictures_list.append(i)
    return horizontal_pictures_list, vertical_pictures_list


def generate_slides_list(horizontal_pictures_list, vertical_pictures_list):
    """
    Generate a list of valid slides (1 Slide = 1 Horizontal pictures || 2 Vertical pictures).

    Horizontal pictures are stored in the order they appear and vertical pictures are united following the pattern of
    one picture and the picture that results of adding half of the length of the vertical pictures list to the first
    picture id.

    Note: It is not good and could be improved by trying to merge pictures that hove nothing to do, improving the total
    number of tags. However, we did not had time for it.
    """
    slides = []
    for i in range(len(horizontal_pictures_list)):
        slides.append([horizontal_pictures_list[i]])
    for i in range(int(len(vertical_pictures_list)/2)):
        slides.append([vertical_pictures_list[i], vertical_pictures_list[i+(int(len(vertical_pictures_list)/2))]])
    return slides


def greedy(input_file_path, output_file_path):
    """
    Resolves the problem in a greedy approach.
    """
    # Read input file and get matrix of pictures and its size
    size, pictures_matrix = read(input_file_path)

    # Sort pictures matrix to separate its elements between the horizontal and the vertical ones
    horizontal_pictures_list, vertical_pictures_list = sort_pictures(pictures_matrix, size)

    # Generate a list of valid slides (1 Slide = 1 Horizontal pictures || 2 Vertical pictures)
    slides_list = generate_slides_list(horizontal_pictures_list, vertical_pictures_list)

    # Generate a zeroes list of the same size of the slides list to represent the used ones
    used_slides_list = np.zeros(shape=len(slides_list))

    # Start by the first slide and mark it as used. Note: This is hardly the best solution, but it works pretty well
    current_slide_id = 0
    used_slides_list[current_slide_id] = 1

    # Set first slide as initial valid value and find next valid slides to add to the ordered slides list
    ordered_slides_list = [slides_list[current_slide_id]]
    while True:
        current_slide_id = get_next_valid_slide(pictures_matrix, slides_list, current_slide_id, used_slides_list)

        # If there is no valid next slide, break. In this greedy approach, we did not wanted to have ramifications
        if not current_slide_id:
            break

        # If there is a new valid slide, mark it as used and repeat the process
        ordered_slides_list.append(slides_list[current_slide_id])
        used_slides_list[current_slide_id] = 1

    # Write the solution to output/name_of_the_input_file
    write(output_file_path, ordered_slides_list)
