# file<check_things_value.py>


def check_things_value(value):
    if value is False:
        result = 'false'
    elif value is True:
        result = 'true'
    elif value is None:
        result = 'null'
    else:
        result = value
    return result
