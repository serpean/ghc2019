from lib.greedy import greedy
from os import makedirs, listdir
from shutil import rmtree


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


if __name__ == '__main__':
    main()
