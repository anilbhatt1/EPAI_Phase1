import pytest
import time
from datetime import datetime, timezone
from functools import wraps, singledispatch, lru_cache
from decimal import Decimal
from html import escape
import Decorators_Assignment
from Decorators_Assignment import *
import inspect
import re
from io import StringIO
import sys

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(Decorators_Assignment, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(Decorators_Assignment)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_odd_it_even():
    @odd_it
    def adder(a: int, b: int) -> int:
        return a + b
    if datetime.now().second % 2 != 0:
        assert adder(1, 2) != None
    else:
        assert adder(1, 2) == None

def test_odd_secs():
    if datetime.now().second % 2 != 0:
        f1 = fn_odd_secs()
        assert f1 == f'Ran'

def test_even_secs():
    if datetime.now().second % 2 == 0:
        f1 = fn_odd_secs()
        assert f1 == None

# Capturing the console output for logger as it would be printing out to the consolve
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

def test_logger():

    @logger
    def combine(var1: str, var2: int) -> str:
        '''
        This is the writeup for function named - combine.
        This is a function that takes 2 variables var1 which is str and var2 which is int.
        Function is decorated to keep a log of time at which it is invoked.
        Function will return a string combining var1 and var2.
        '''
        result = f'{var1} and {var2} are input supplied'
        return result

    with Capturing() as output:
        combine('red', 1)

    print(f'output : {output}')

    # assert that logging data has the name of the function and "called at" details
    assert any(["function_name" and "called at" in o for o in output])
    # Function Execution time title
    assert any(["Execution time" in o for o in output])
    # Function description title
    assert any(["Function description" in o for o in output])
    # Function's doc strings are actually passed on
    assert "This is the writeup for function named - combine" in combine.__doc__
    # Function annotation title
    assert any(["Function annotation" in o for o in output])
    # Function annotation title
    assert any(["Function description" in o for o in output])
    # that annotations are printing details on variables and returned values
    assert any(["var1" and "var2" and "return" and "int" and "str" in o for o in output])
    # that function's name is same as the name of the function!
    assert "combine" == combine.__name__

India = Country('India', 'Delhi', '1.3B', '$3.05 t')
def test_log_class():
    time_now = datetime.now(timezone.utc)
    f1 = India.debug_info()
    check = [' Object belongs to the class: Country',
             f' Id of object : {hex(id(India))}',
             f' Object was called at : {time_now} UTC']
    assert len(f1) == 3, 'Invalid Length'
    for i in range(3):
        assert f1[i] == check[i], f'Assertion failed at item {i}'

def test_access_rights_function():

	def func(*args):
		return args

	assert len(decorator_factory('high')(func)()) == 4, 'high needs access to 4 functions'

	assert len(decorator_factory('mid')(func)()) == 3, 'mid needs access to 3 functions'

	assert len(decorator_factory('low')(func)()) == 2, 'low needs access to 2 functions'

	assert len(decorator_factory('no')(func)()) == 1, 'no needs access to 1 function'

	assert decorator_factory('random')(func)() == "Improper access keyword set"

def test_authenticate_function():
	@authenticate("secret")
	def my_func(user_pwd):
		return "Amazing!"

	with pytest.raises(TypeError) as execinfo:
		my_func()

	assert my_func("random") == "Wrong Password", ''

	assert my_func("secret") == "Amazing!"

def test_timed_function():
	@timed(10)
	def func(*args):
		time.sleep(0.2)
		pass

	with Capturing() as output:
		func()

	assert any(["Avg" or "Average" in o for o in output])
	assert any(["0.2" or "0.3" in o for o in output])
	assert any(["10" in o for o in output])

'''
from session8 import *
from datetime import datetime
import pytest
from io import StringIO 
import sys
import time
import inspect
import os

README_CONTENT_CHECK_FOR = [
    "and",
    "or",
    "repr",
    "str",
    "add",
    "eq",
    "float",
    "ge",
    "gt",
    "invert",
    "le",
    "lt",
    "mul",
    "sqrt",
    "bool",
    "init"
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    # Returns pass if used four spaces for each level of syntactically \
    # significant indenting.
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_odd_it_even():
    @odd_it
    def adder(a: int, b: int) -> int:
        return a + b
    if datetime.now().second % 2 != 0:
    	assert adder(1, 2) != None
    else:
    	assert adder(1, 2) == None

# Capturing the console output for logger as it would be printing out to the consolve


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

def test_logger():

	@logger
	def function_name(var1: str, var2: int) -> str:
		"""
		This is a function's writeup
		This is a function's writeup
		This is a function's writeup
		This is a function's writeup
		This is a function's writeup
		"""
		return 'output'

	with Capturing() as output:
		function_name('red', 1)

	# assert that logging data has
	# the name of the function and "called at" details
	assert any(["function_name" and "called at" in o for o in output])
	# Function Execution time title
	assert any(["Execution time" in o for o in output])
	# Function description title
	assert any(["Function description" in o for o in output])
	# Function's doc strings are actually passed on
	assert "This is a function's writeup" in function_name.__doc__
	# Function annotation title
	assert any(["Function annotation" in o for o in output])
	# Function annotation title
	assert any(["Function description" in o for o in output])
	# that annotations are printing details on variables and returned values
	assert any(["var1" and "var2" and "return" and "int" and "str" in o for o in output])
	# that function's name is same as the name of the function!
	assert "function_name" == function_name.__name__


def test_access_rights_function():

	def func(*args):
		return args

	assert len(decorator_factory('high')(func)()) == 4

	assert len(decorator_factory('mid')(func)()) == 3

	assert len(decorator_factory('low')(func)()) == 2

	assert len(decorator_factory('no')(func)()) == 1

	assert decorator_factory('random')(func)() == "Improper access keyword set"



def test_authenticate_function():
	@authenticate("secret")
	def my_func():
		return "Amazing!"

	with pytest.raises(TypeError) as execinfo:
		my_func()

	assert my_func("random") == "Wrong Password"

	assert my_func("secret") == "Amazing!"


def test_timed_function():
	@timed(10)
	def func(*args):
		time.sleep(0.2)
		pass

	with Capturing() as output:
		func()

	assert any(["Avg" or "Average" in o for o in output])
	assert any(["0.2" or "0.3" in o for o in output])
	assert any(["10" in o for o in output])
'''
