# file<plain.py>


from gendiff.include.check_things_value import check_things_value


def plain(diff, level=0, addr=[]):
    result = ''
    for i in diff:
        while level < len(addr):
            addr.pop()
        if level == len(addr):
            addr.append(i[0])
        if i[2] == 'add':
            result += f'Property \'{".".join(addr)}\' was added '
            result += f'with value: {check_plain_val(i[3])}\n'
        elif i[2] == 'del':
            result += f'Property \'{".".join(addr)}\' was removed\n'
        elif i[2] == 'changed':
            result += f'Property \'{".".join(addr)}\' was updated. From '
            result += f'{check_plain_val(i[1])} to {check_plain_val(i[3])}\n'
        elif i[2] == 'have children':
            result += plain(i[4], level + 1, addr)
    return result


def check_plain_val(value):
    if type(value) is dict:
        result = '[complex value]'
    else:
        result = check_things_value(value)
        if result not in ('false', 'null', 'true') and type(result) != int:
            result = f"'{result}'"
    return result
