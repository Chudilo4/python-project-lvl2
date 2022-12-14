# file<gendiff.py>


from gendiff.include.compare import compare
from gendiff.include.plain import plain
from gendiff.include.render import stylish
from gendiff.include.out_json import format_json
import json
import yaml


def generate_diff(file_path1, file_path2, format_name=stylish):
    if '.json' in file_path1:
        f1 = json.load(open(file_path1))
        f2 = json.load(open(file_path2))
    elif '.yaml' in file_path1 or '.yml' in file_path1:
        with open(file_path1) as data:
            f1 = yaml.load(data, Loader=yaml.SafeLoader)
        with open(file_path2) as data2:
            f2 = yaml.load(data2, Loader=yaml.SafeLoader)
    diff = compare(f1, f2)
    if format_name == 'plain':
        return plain(diff).strip()
    if format_name == 'stylish':
        return stylish(diff).strip()
    if format_name == 'json':
        return format_json(diff).strip()
    return stylish(diff).strip()
