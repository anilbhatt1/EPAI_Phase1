def f_string_print(fn:'Function')->'Function':
    """
    This is a closure to print the result of the function which is
    passed as an argument .
    """
    def inner(*args,**kwargs):
        output = fn(*args,**kwargs)
        print(f'Function: {fn.__name__}, Arguments:{args} and Output:{output}')
        return output
    return inner