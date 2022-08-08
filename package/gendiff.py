# file <gendiff.py>


import json


def generate_diff(file1, file2):
    f = json.load(open(file1))
    f2 = json.load(open(file2))
    txt = '{'
    list_json_set = list(set(f).union(set(f2)))
    list_json_set.sort()
    for i in list_json_set:
        if i in f.keys():
            if f[i] in f2.values():
                txt += f'\t\n   {i}: {str(f[i]).lower()}'
                continue
            txt += f'\t\n - {i}: {str(f[i]).lower()}'
        if i in f2.keys():
            txt += f'\t\n + {i}: {str(f2[i]).lower()}'
    txt += "\n}"
    return txt
