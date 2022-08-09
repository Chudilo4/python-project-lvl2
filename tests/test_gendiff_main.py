from package.gendiff import generate_diff


def test_generate_diff():
    f = open('tests/text.txt', 'r')
    assert generate_diff('tests/file1.json', 'tests/file2.json') == f.read()
