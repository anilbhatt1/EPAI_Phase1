import types

def check_doc(fn):
    """
    This function is used to check if a given function has doc-string length of more than 50.
    This is a closure.
    """
    length = 50
    def check_len()-> str:
        """
        This function checks if given argument is a function & sends response after checking docstring length.
        'length' is a free variable.
        """
        nonlocal length
        if not isinstance(fn, types.FunctionType):
            return f'Not a function'
        elif len(fn.__doc__) < length:
            return f'Insufficient documentation'
        else:
            return f'Have enough documentation'
    return check_len()

def next_fib():
    """
    This function is used to generate the next fibonacci number in the sequence. Fibonacci numbers
    are 0,1,1,2,3,5,8,13,21...
    This is a closure.
    """
    fib_1, fib_2 = 0, 1
    def gen_next()->(str, int):
        """
        This function takes free variables fib_1 and fib_2 and generates the next fibonacci number in sequence.
        fib_1 and fib_2 are stored with new numbers also.
        """
        nonlocal fib_1
        nonlocal fib_2
        fib_3 = fib_1 + fib_2
        fib_1, fib_2 = fib_2, fib_3
        return f'Next fibonacci number is {fib_2}'
    return gen_next

def add(valu1:int, valu2:int)-> int:
    """
    This function accepts 2 integer values and returns sum of both.
    """
    return valu1 + valu2

def mul(valu1:int, valu2:int)-> int:
    """
    This function accepts 2 integer values and returns product of both.
    """
    return valu1 * valu2

def div(valu1:int, valu2:int)-> int:
    """
    This function accepts 2 integer values and returns quotient of both.
    """
    return valu2 and valu1/valu2

# To test docstring count == 0
def assign_a(valu):
    a = valu
    return a

# To test docstring count < 50
def assign_b(valu):
    """
    Assigns value to b
    """
    b = valu
    return b

cnt_dict = {'add':0, 'mul':0, 'div':0}
def ctr_dict_fn_only_arg(fn):
    """
    This is a function that accepts another function. Then it updates a dictionary that keeps couunt of each function
    being called.
    This is a closure.
    """
    cnt = cnt_dict[fn.__name__]
    def update(*args, **kwargs)->(int, dict):
        """
        This function accepts another function, executes that function and also increases the counter.
        If there is no entry for a particular function, entry for the same is created in dictionary and
        then counter is updated.
        """
        nonlocal cnt
        cnt += 1

        cnt_dict[fn.__name__] = cnt
        return fn(*args, **kwargs)

    return update


def ctr_dict(fn, func_dict)->(int, dict):
    """
    This is a function that accepts another function & dictionary that is used to keep track of how many times that particular
    function (supplied as argument) is called.
    This is a closure.
    """
    def update(*args, **kwargs)->(int, dict):
        """
        This function accepts another function, executes that function and also increases the counter.
        If there is no entry for a particular function, entry for the same is created in dictionary and
        then counter is updated.
        """
        if not fn.__name__ in func_dict.keys():
            func_dict[fn.__name__] = 0

        func_dict[fn.__name__] += 1
        return fn(*args, **kwargs)

    return update
