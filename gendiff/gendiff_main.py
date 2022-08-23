# file <gendiff_main.py>


from gendiff.generate_diff import generate_diff
from gendiff.include.parser import parser


def main():
    file1, file2, format_diff = parser()
    diff = generate_diff(file1, file2, format_diff)
    print(diff)


if __name__ == '__main__':
    main()
