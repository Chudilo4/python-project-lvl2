# file<render.py>


from package.include.check_dict_value import check_dict_value


def stylish(value, depth=0):
    step = '    '
    ident = step * depth
    delet_step = '  - '
    add_step = '  + '
    txt = "{\n"
    for i in value:
        if i[2] == 'del':
            txt += f'{ident}{delet_step}{i[0]}: {check_dict_value(i[1], step, depth+1)}' + '\n'
        elif i[2] == 'not change':
            txt += f'{ident}{step}{i[0]}: {check_dict_value(i[1], step, depth+1)}' + '\n'
        elif i[2] == 'add':
            txt += f'{ident}{add_step}{i[0]}: {check_dict_value(i[3], step, depth+1)}' + '\n'
        elif i[2] == 'changed':
            txt += f'{ident}{delet_step}{i[0]}: {check_dict_value(i[1], step, depth+1)}' + '\n'
            txt += f'{ident}{add_step}{i[0]}: {check_dict_value(i[3], step, depth+1)}' + '\n'
        elif i[2] == 'have children':
            txt += f'{ident}{step}{i[0]}: {stylish(i[4], depth + 1)}'
    txt += f'{ident}}}\n'
    return txt
