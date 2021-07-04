import time
from datetime import datetime, timezone
from functools import wraps, singledispatch, lru_cache
from decimal import Decimal
from html import escape

## Allows a function to run only on odd seconds
def odd_it(fn: 'function')->'function':
    """
    Decorator to ensure that function that it decorates runs only on odd seconds.
    """
    from datetime import datetime
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        secs = datetime.now().second
        if secs % 2 == 0:
            result = None
        else:
            result = fn(*args, **kwargs)
        return result
    return inner

@odd_it
def fn_odd_secs():
    """
    This is a simple function that simply passes. This is decorated in such a way that it is supposed to run only on odd seconds.
    """
    return 'Ran'

## Logging for functions
def logger(fn:'function')->'function':
    """
    Decorator that keeps log of time at which function that it decorates is invoked."
    """
    from datetime import datetime, timezone
    from functools import wraps
    from time import perf_counter

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        time_called = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        end = perf_counter()
        time_took = end - start
        str1 = f'Function name {fn.__name__} was called at {time_called} and result is **{result}**.'
        str2 = f'Function description is {fn.__doc__}.'
        str3 = f'Function annotation is {fn.__annotations__} and Execution time is {time_took}.'
        msg = str1 + str2 + str3
        print(f'Log: {msg}')
        return msg
    return inner

@logger
def add(a:str, b:int)->str:
    """
    This is a function's writeup.
    This is a function that takes 2 variables var1 which is str and var2 which is int.
    Function is decorated to keep a log of time at which it is invoked.
    Function will return a string combining var1 and var2
    """
    result = f'{a} and {b} are input supplied'
    return result

##Logging for class objects
def info(obj:'object')->list:
    """
    This function accepts an object that belongs to a class as argument and returns a log of info related to this object
    """
    logs = []
    logs.append(f' Object belongs to the class: {obj.__class__.__name__}')
    logs.append(f' Id of object : {hex(id(obj))}')
    logs.append(f' Object was called at : {datetime.now(timezone.utc)} UTC')
    return logs

def dec_debug(cls):
    """
    This decorator will decorate a class. Any object instantiated from the class can get a log info
    by calling obj.debug_info()
    """
    cls.debug_info = info
    return cls

@dec_debug
class Country():
    """
    Creates a class called country in such a way that object created is callable.
    Also decorated by dec_debug so that obj.debug_info() can return the log details of the object.
    """
    def __init__(self, name, capital, population, GDP):
        self.name = name
        self.capital = capital
        self.population = population
        self.GDP = GDP

    def __call__(self):
        return f'Country is {self.name}'

##Authenticate - Will allow to run a function only once authenticated
def authenticate(set_password:str)->'function':
    """
    This decorator factory accepts a user_password. Any function decorated with this decorator has to supply a
    password. Function will be allowed to execute only if user supplied password matches with the system password
    set inside  'dec_authenticate'.
    """
    def dec_authenticate(fn:'function'):

        def inner(*args, **kwargs):
            if len(args) == 0:
                raise TypeError
            elif set_password == args[0]:
                result = fn(*args, **kwargs)
                return result
            else:
                return f'Wrong Password'
        return inner
    return dec_authenticate

@authenticate('secret')
def div(a:int, b:int) -> float:
    """
    This function is to divide 2 given numbers. Decorated with dec_factory, hence supplying a password of 'anil'.
    """
    return a/b

@authenticate('Buddha-Smiling')
def remainder(a:int, b:int) -> int:
    """
    This function is to divide 2 given numbers and give its remainder. Decorated with dec_factory,
    hence supplying a password of 'Buddha-Smiling'.
    """
    return a%b

##Timer - This decorator should run a function 'n' number of times and give back the average time took
def timed(reps:int)-> 'function':
    """
    Decorator to calculate average elapsed run time for a function. Through 'repeat' parameter this decorator
    has capability to execute the function 'repeat' number of times.
    """
    def dec_timed(fn:'function'):
        total_elapsed = 0
        total_cnt = 0

        from functools import wraps
        from time import perf_counter
        @wraps(fn)
        def inner(*args, **kwargs):
            nonlocal total_elapsed
            nonlocal total_cnt
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)
                total_cnt += 1
            avg_time = total_elapsed / total_cnt
            print(f'Function - {fn.__name__} accepted {args} argument, ran {reps} times & took avg of {avg_time} secs.')
            return result
        return inner

    return dec_timed

@timed(1000)
def add_new(a:int, b:int) -> int:
    """
    This is a function that adds 2 integers and is decorated to keep a lof of time at which it is invoked.
    """
    return a + b

##Provides privilege access (has 4 parameters, based on privileges (high, mid, low, no), gives access to all 4, 3, 2 or 1 params)
user_list = {'Amit':'All', 'Amir':'Medical', 'Anil':'Dental', 'Sachin':'Vision'}

def dec_factory(privilege_lvl:str) -> 'function':
    def dec_privilege(fn):
        access = {'high': ('add', 'remove', 'modify', 'view'),'mid': ('add', 'modify', 'view'),'low': ('view'),'no': ()}

        def inner(*args, **kwargs):
            available_fns = access[privilege_lvl]
            if fn.__name__ in available_fns:
                result = fn(*args, **kwargs)
            else:
                result = f'Function **{fn.__name__}** is not available for privilige level **{privilege_lvl}**'
            return result

        return inner

    return dec_privilege

@dec_factory('high')
def add(user_input):
    name, coverage = user_input
    if name in user_list:
        response = f'{name} already exists, please use modify'
    else:
        user_list[name] = coverage
        response = f'{name} added with coverage : {coverage} in user list'
    return response

'''
Start with a decorator_factory that takes an argument one of these strings, high, mid, low or no. 
Then write the decorator that has 4 free variables  based on the argument set by the factory call, 
give access to 4, 3, 2 or 1 arguments to the function being decorated from var1, var2, var3, var4
'''
def decorator_factory(privilege_lvl:str)->'function':
    # Based on the privilege_lvl with which a particular function is decorated,
    # this decorator will give the list of access available to that particular function
    # 4 privilege levels are available for decoration - 'high', 'medium', 'low', 'no'
    def dec_privilege(fn):
        access = {'high':('add', 'remove', 'modify', 'view'), 'mid':('add', 'modify', 'view'), 'low':('modify', 'view'),'no':('view',)}
        def inner(*args, **kwargs):
            if privilege_lvl in access.keys():
                return access[privilege_lvl]
            else:
                return "Improper access keyword set"
        return inner
    return dec_privilege

@decorator_factory('low')
def dummy2(*args):
    return args