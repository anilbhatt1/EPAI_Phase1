import math
from ..utils import f_string_print

@f_string_print
def relu(value):
    if isinstance(value, int) or isinstance(value, float):
        pass
    else:
        return f'Incorrect value format given - {type(value)}. Give input as integer or float'

    if value <= 0:
        relu_result = 0
    else:
        relu_result = value

    return relu_result

@f_string_print
def relu_der(value):
    if isinstance(value, int) or isinstance(value, float):
        pass
    else:
        return f'Incorrect value format given - {type(value)}. Give input as integer or float'

    if value <= 0:
        relu_result = 0
    else:
        relu_result = 1

    return relu_result