import math
from ..utils import f_string_print

@f_string_print
def tanh(value):
    if isinstance(value, int) or isinstance(value, float):
        pass
    else:
        return f'Incorrect value format given - {type(value)}. Give input as integer or float'

    result = math.tanh(value)

    return round(result, 4)

@f_string_print
def tanh_der(value):
    if isinstance(value, int) or isinstance(value, float):
        pass
    else:
        return f'Incorrect value format given - {type(value)}. Give input as integer or float'

    result = 1 - math.tanh(value) ** 2

    return round(result, 4)