# file <gendiff.py>


import yaml


def generate_diff_yaml(file1, file2):
    with open(file1) as data:
        f = yaml.load(data, Loader=yaml.SafeLoader)
    with open(file2) as data2:
        f2 = yaml.load(data2, Loader=yaml.SafeLoader)
    txt = '{'
    list_yaml_set = list(set(f).union(set(f2)))
    list_yaml_set.sort()
    for i in list_yaml_set:
        if i in f.keys():
            if f[i] in f2.values():
                txt += f'\n    {i}: {str(f[i]).lower()}'
                continue
            txt += f'\n  - {i}: {str(f[i]).lower()}'
        if i in f2.keys():
            txt += f'\n  + {i}: {str(f2[i]).lower()}'
    txt += "\n}"
    return txt
