# file <gendiff_main.py>


import argparse
from package.gendiff_json import generate_diff_json
from package.gendiff_yaml import generate_diff_yaml


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output',)
    args = parser.parse_args()
    if '.json' in args:
        diff = generate_diff_json(args.first_file, args.second_file)
        print(diff)
    else:
        diff2 = generate_diff_yaml(args.first_file, args.second_file)
        print(diff2)


if __name__ == '__main__':
    main()
