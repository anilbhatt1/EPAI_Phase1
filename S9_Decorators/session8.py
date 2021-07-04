from functools import wraps
from datetime import datetime
from time import perf_counter

# Decorator that allows to run a function only at odd seconds, else prints out "We're even!"
def odd_it(fn: "Function"):
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

# The same logger that we coded in the class
# it will be tested against a function that will be sent 2 parameters, and 
# it would return some random string. 
def logger(fn: "Function"):
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



# start with a decorator_factory that takes an argument one of these strings, 
# high, mid, low or no
# then write the decorator that has 4 free variables
# based on the argument set by the factory call, give access to 4, 3, 2 or 1 arguments
# to the function being decorated from var1, var2, var3, var4
# YOU CAN ONLY REPLACE "#potentially missing code" LINES WITH MULTIPLE LINES BELOW
# KEEP THE REST OF THE CODE SAME
def decorator_factory(access:str):
	# Based on the privilege_lvl with which a particular function is decorated,
	# this decorator will give the list of access available to that particular function
	# 4 privilege levels are available for decoration - 'high', 'medium', 'low', 'no'
	def dec_privilege(fn):
		access_var = {'high': ('add', 'remove', 'modify', 'view'), 'mid': ('add', 'modify', 'view'),
					  'low': ('modify', 'view'), 'no': ('view',)}

		def inner(*args, **kwargs):
			if access in access_var.keys():
				return access_var[access]
			else:
				return "Improper access keyword set"

		return inner

	return dec_privilege


# The authenticate function. Start with a dec_factory that sets the password. It's inner
# will not be called with "password", *args, **kwargs on the fn
def authenticate(set_password):
	"""
	This decorator factory accepts a user_password. Any function decorated with this decorator has to supply a
	password. Function will be allowed to execute only if user supplied password matches with the system password
	set inside  'dec_authenticate'.
	"""

	def dec_authenticate(fn: 'function'):
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


# The timing function
def timed(reps):
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


