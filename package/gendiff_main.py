# file <gendiff_main.py>


import argparse
import json
import yaml
from package.include.render import render
from package.include.generate_diff import generate_diff

def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output',)
    args = parser.parse_args()
    if '.json' in args:
        f = json.load(open(args.first_file))
        f2 = json.load(open(args.second_file))
        diff = generate_diff(f, f2)
        print(render(diff))
    else:
        with open(args.first_file) as data:
            f = yaml.load(data, Loader=yaml.SafeLoader)
        with open(args.second_file) as data2:
            f2 = yaml.load(data2, Loader=yaml.SafeLoader)
        diff = generate_diff(f, f2)
        print(render(diff))


if __name__ == '__main__':
    main()
