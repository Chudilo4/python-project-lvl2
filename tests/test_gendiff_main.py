from package.gendiff import generate_diff


def test_generate_diff():
    f = open('tests/fixtures/text.txt', 'r')
    assert generate_diff('tests/fixtures/file1.json',
                         'tests/fixtures/file2.json') == f.read()
