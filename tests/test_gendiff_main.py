from package.gendiff_json import generate_diff_json
from package.gendiff_yaml import generate_diff_yaml


def test():
    f = open('tests/fixtures/test_json.txt', 'r')
    f2 = open('tests/fixtures/test_yaml.txt', 'r')
    test_json = generate_diff_json('tests/fixtures/file1.json',
                                   'tests/fixtures/file2.json')
    test_yaml = generate_diff_yaml('tests/fixtures/file3.yaml',
                                   'tests/fixtures/file4.yaml')
    assert test_json == f.read()
    assert test_yaml == f2.read()
