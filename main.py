from lib.greedy import greedy
from lib.utils import calculate_score
from os import makedirs, listdir
from shutil import rmtree


def show_scores():
    print('----------  SCORES ----------')
    total = 0
    for output_file in listdir('output/'):
        score = calculate_score('input/' + output_file, 'output/' + output_file)
        total += score
        print(output_file, score)

    print('\nTotal', total)


def main():
    # Delete old results if exist
    rmtree('output/', True)

    # Create output folder
    makedirs('output/')

    # For each file in the input folder
    for input_file in listdir('input/'):

        # Create an output file related
        output_file = 'output/' + input_file.split('/')[-1]

        # Run the greedy approach
        greedy('input/' + input_file, output_file)

    show_scores()


if __name__ == '__main__':
    main()
