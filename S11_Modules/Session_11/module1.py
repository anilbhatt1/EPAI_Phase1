#module1

print(f'_______Running {__name__} _____')

def pprint_dict(header, d):
    print('\n\n -------------------------')
    print(f'*** {header} ***')
    for key, value in d.items():
        print(key, value)
    print('---------------------------\n\n')
    
#lets use this function to print globals dict
pprint_dict('module1.globals', globals())

print(f'__________________End of {__name__}__________')
