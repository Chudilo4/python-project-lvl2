# file<render.py>


from package.include.check_dict_value import check_dict_value


def render(value, depth=0):
    step = '    '
    ident = step * depth
    delet_step = '  - '
    add_step = '  + '
    txt = "{"
    for i in value:
        if i[2] == 'del':
            txt += '\n' + f'{ident}{delet_step}{i[0]}: {check_dict_value(i[1], step, depth+1)}'
        elif i[2] == 'not change':
            txt += '\n' + f'{ident}{step}{i[0]}: {check_dict_value(i[1], step, depth+1)}'
        elif i[2] == 'add':
            txt += '\n' + f'{ident}{add_step}{i[0]}: {check_dict_value(i[3], step, depth+1)}'
        elif i[2] == 'changed':
            txt += '\n' + f'{ident}{delet_step}{i[0]}: {check_dict_value(i[1], step, depth+1)}'
            txt += '\n' + f'{ident}{add_step}{i[0]}: {check_dict_value(i[3], step, depth+1)}'
        elif i[2] == 'have children':
            txt += '\n' + f'{ident}{step}{i[0]}: {render(i[4], depth + 1)}'
    txt += '\n' + f'{ident}}}'
    return txt