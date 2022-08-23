# file <gendiff_main.py>


from package.include.diff import generate_diff
from package.include.parser import parser


def main():
    file1, file2, format_diff = parser()
    diff = generate_diff(file1, file2, format_diff)
    print(diff)


if __name__ == '__main__':
    main()
