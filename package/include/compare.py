# file <gendiff.py>


def compare(f, f2):
    diff = []
    value = ''
    new_value = ''
    children = []
    list_key = f | f2
    status = ''
    for key in sorted(list_key):
        name = key
        if key not in f:
            new_value = f2.get(key)
            status = 'add'
        elif key not in f2:
            value = f.get(key)
            status = 'del'
        elif isinstance(f[key], dict) and isinstance(f2[key], dict):
            children = compare(f.get(key), f2.get(key))
            status = 'have children'
        elif (key in f and key in f2) and (f[key] == f2[key]):
            value = f.get(key)
            status = 'not change'
        else:
            value = f.get(key)
            new_value = f2.get(key)
            status = 'changed'
        element = [name, value, status, new_value, children]
        diff.append(element)
    return diff
