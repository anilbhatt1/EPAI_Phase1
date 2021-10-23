# run.py

print(f'loading run.py: __name__ = {__name__}')

# import module1

import timing

code = '[x**2 for x in range(1_0000)]'

result = timing.timeit(code, 100)
print(result)