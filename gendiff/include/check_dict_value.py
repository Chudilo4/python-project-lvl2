# file<check_dict_value.py


from gendiff.include.check_things_value import check_things_value
import itertools


def check_dict_value(value, replacer, depth):
    def iter_(current_value, dept):
        if not isinstance(current_value, dict):
            return str(check_things_value(current_value))

        deep_indent_size = dept + 1
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * dept
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return iter_(value, depth)
