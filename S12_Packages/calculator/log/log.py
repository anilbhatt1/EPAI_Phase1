import math
from ..utils import f_string_print

@f_string_print
def log(value):
    if isinstance(value, int) or isinstance(value, float):
        pass
    else:
        return f'Incorrect value format given - {type(value)}. Give input as +ve integer or +ve float'

    if value > 0:
        result = math.log(value)
        return result
    else:
        return f'log can be calculated only for +ve values. Non-postive value {value} given as input'


@f_string_print
def log_der(value):
    if isinstance(value, int) or isinstance(value, float):
        pass
    else:
        return f'Incorrect value format given - {type(value)}. Give input as +ve integer or +ve float'

    if value > 0:
        result = 1 / value
        return result
    else:
        return f'Derivative log can be calculated only for +ve values. Non-postive value {value} given as input'