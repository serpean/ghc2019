from .io import read, read_results


def get_slide_tags(pictures_matrix, slide):
    """
    Returns the list of tags hosted by a slide.
    """

    tags = []
    for picture in slide:
        for tag in pictures_matrix[picture][2:]:
            tags.append(tag)
    return tags


def rate_transition(pictures_matrix, current_slide, next_slide):
    """
    Rates the transition between two slices according to the problem requirements.
    """
    current_slide_tags = get_slide_tags(pictures_matrix, current_slide)
    next_slide_tags = get_slide_tags(pictures_matrix, next_slide)

    common_tags = len(list(set(current_slide_tags).intersection(next_slide_tags)))
    first_but_not_second_tags = len(set(current_slide_tags) - set(next_slide_tags))
    second_but_not_first_tags = len(set(next_slide_tags) - set(current_slide_tags))

    return min(common_tags, min(first_but_not_second_tags, second_but_not_first_tags))


def calculate_score(input_file_path, output_file_path):
    """
    Returns the score of a solution based on the sum of the score of all the transitions involved.
    """
    _, pictures_matrix = read(input_file_path)
    slides_list = read_results(output_file_path)

    score = 0

    current_slide = slides_list[0]
    for i in range(1, len(slides_list)):
        next_slide = slides_list[i]

        score += rate_transition(pictures_matrix, current_slide, next_slide)

        current_slide = next_slide

    return score
