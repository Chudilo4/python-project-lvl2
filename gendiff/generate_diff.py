# file<diff.py>


from package.include.compare import compare
from package.include.plain import plain
from package.include.render import stylish
from package.include.out_json import format_json
import json
import yaml


def generate_diff(file_path1, file_path2, format_name=stylish):
    if '.json' in file_path1 and '.json' in file_path2:
        f1 = json.load(open(file_path1))
        f2 = json.load(open(file_path2))
    elif '.yaml' in file_path1 and '.yaml' in file_path2:
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
