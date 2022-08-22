
import json
import yaml
from package.include.render import render
from package.include.generate_diff import generate_diff
from package.include.check_dict_value import check_dict_value
from package.include.check_things_value import check_things_value

def test():
    f = open('tests/fixtures/test_json', 'r')
    f2 = open('tests/fixtures/test_yaml.txt', 'r')
    test_json = generate_diff(json.load(open('tests/fixtures/file3.json')),
                              json.load(open('tests/fixtures/file4.json')))
    with open('tests/fixtures/file3.yaml') as data:
        f3_yaml = yaml.load(data, Loader=yaml.SafeLoader)
    with open('tests/fixtures/file4.yaml') as data2:
        f4_yaml = yaml.load(data2, Loader=yaml.SafeLoader)
    test_yaml = generate_diff(f3_yaml, f4_yaml)


    assert render(test_json) == f.read()
    assert render(test_yaml) == f2.read()
