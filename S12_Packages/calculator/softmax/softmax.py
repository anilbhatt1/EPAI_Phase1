import math
from ..utils import f_string_print

@f_string_print
def softmax(*args):
    exp_sum = 0
    softmax_list = []

    for logits in args:
        if isinstance(logits, int) or isinstance(logits, float):
            pass
        else:
            return f'Incorrect value format given - {type(logits)} for "{logits}". Give input as integer or float'

        exp_sum += math.exp(logits)

    for logits in args:
        softmax_value = round((math.exp(logits) / exp_sum), 2)
        softmax_list.append(softmax_value)

    return softmax_list


@f_string_print
def softmax_der(*args):
    exp_sum = 0
    softmax_list = []

    for logits in args:
        if isinstance(logits, int) or isinstance(logits, float):
            pass
        else:
            return f'Incorrect value format given - {type(logits)} for "{logits}". Give input as integer or float'

        exp_sum += math.exp(logits)

    for logits in args:
        softmax_value = (math.exp(logits) / exp_sum)
        softmax_list.append(softmax_value)

    softmax_all_deriv_list = []

    for inp_idx, _ in enumerate(args):

        softmax_indiv_deriv_list = []

        for sm_idx, sm_value in enumerate(softmax_list):

            if sm_idx == inp_idx:  # Partial derivative
                sm_diff = sm_value * (1 - sm_value)
            else:
                sm_diff = -1 * sm_value * softmax_list[inp_idx]

            softmax_indiv_deriv_list.append(round(sm_diff, 2))

        softmax_all_deriv_list.append(softmax_indiv_deriv_list)

    return softmax_all_deriv_list