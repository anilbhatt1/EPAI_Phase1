#main.py

print(f'_____Running {__name__} ____')

import module1

print('module1-print:', module1)

module1.pprint_dict('main.globals', globals())

import sys

print('sys.path:', sys.path)

print("Importing Module1 again just for fun")

import module1

del globals()['module1'] 

# globals()['module1'] = sys.modules['module1']
print('Imported module1 again after deletion')
import module1

module1.pprint_dict('main.globals', globals())