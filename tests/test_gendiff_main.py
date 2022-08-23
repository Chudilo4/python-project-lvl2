
import json
import yaml
from package.include.render import stylish
from package.include.compare import compare
from package.include.plain import plain
from package.include.out_json import format_json

def test_stylish_json():
    f = open('tests/fixtures/test_json.txt', 'r')
    test_json = compare(json.load(open('tests/fixtures/file3.json')),
                        json.load(open('tests/fixtures/file4.json')))
    assert stylish(test_json) == f.read()


def test_stylish_yaml():
    f = open('tests/fixtures/test_yaml.txt', 'r')
    with open('tests/fixtures/file3.yaml') as data:
        f1_yaml = yaml.load(data, Loader=yaml.SafeLoader)
    with open('tests/fixtures/file4.yaml') as data2:
        f2_yaml = yaml.load(data2, Loader=yaml.SafeLoader)
    test_yaml = compare(f1_yaml, f2_yaml)
    assert stylish(test_yaml) == f.read()


def test_plain_json():
    test_json = compare(json.load(open('tests/fixtures/file3.json')),
                        json.load(open('tests/fixtures/file4.json')))
    result = plain(test_json)
    f = open('tests/fixtures/test_format.txt')
    assert result == f.read()


def test_out_json():
    test_json = compare(json.load(open('tests/fixtures/file1.json')),
                        json.load(open('tests/fixtures/file2.json')))
    result = format_json(test_json).strip()
    with open('tests/fixtures/test_out_json.txt') as f:
        assert result + '\n' == f.read()



