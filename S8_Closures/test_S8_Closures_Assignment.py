import pytest
import types
#import S8_Closures
import S8_Closures_Assignment as S8

def test_check_doc_good():

    # zero
    f1 = S8.check_doc(S8.assign_b)
    assert f1 == 'Insufficient documentation'

    # Less than 50
    f1 = S8.check_doc(S8.assign_b)
    assert f1 == 'Insufficient documentation'
    
    # Good > 50
    f1 = S8.check_doc(S8.add)
    assert f1 == 'Have enough documentation'

    #Not a function
    x = 8
    f1 = S8.check_doc(x)
    assert f1 == 'Not a function'

def test_fibonacci():

    # Generating 2
    fib = S8.next_fib()
    r = fib()
    r = fib()
    assert r == 'Next fibonacci number is 2', 'Not correct number'

    # Generating 8
    r = fib()
    r = fib()
    assert r =='Next fibonacci number is 5', 'Not correct number'

    #Checking list
    lst = [1,2,3,5,8,13]
    fib = S8.next_fib()
    for i in lst:
        r = fib()
        assert r == 'Next fibonacci number is ' + str(i), 'Not correct number'

def test_ctr_only_func_as_arg():
    test_dict = {'add':10, 'mul':10, 'div':10}
    ctr_add = S8.ctr_dict_fn_only_arg(S8.add)
    ctr_mul = S8.ctr_dict_fn_only_arg(S8.mul)
    ctr_div = S8.ctr_dict_fn_only_arg(S8.div)
    for i in range(10):
        ctr_add(1, 2)
        ctr_mul(5, 2)
        ctr_div(6, 2)
    assert test_dict == S8.cnt_dict

def test_ctr_dict_func_as_arg():

    global fn_dict
    fn_dict = {}
    ctr_add = S8.ctr_dict(S8.add, fn_dict)
    ctr_mul = S8.ctr_dict(S8.mul, fn_dict)
    ctr_div = S8.ctr_dict(S8.div, fn_dict)

    r = ctr_add(1,2)
    assert r == 3, 'Incorrect addition'
    assert fn_dict['add'] == 1, 'Incorrect add counter'

    r = ctr_mul(5,2)
    assert r == 10, 'Incorrect multiply'
    assert fn_dict['mul']  == 1, 'Incorrect mul counter'

    r = ctr_div(10,2)
    assert r == 5, 'Incorrect division'
    assert fn_dict['div']  == 1, 'Incorrect div counter'

    for i in range(10):
        ctr_add(1, 2)
        ctr_mul(5, 2)
        ctr_div(10,2)
    assert fn_dict['add'] == 11, 'Add counter not cumulating correctly'
    assert fn_dict['mul'] == 11, 'Mul counter not cumulating correctly'
    assert fn_dict['div'] == 11, 'Div counter not cumulating correctly'

# This is to test if ctr_dict works for other functions & dictionaries
def test_ctr_another_dict():
    global fn_dict2
    fn_dict2 = {}
    ctr_a = S8.ctr_dict(S8.assign_a, fn_dict2)
    ctr_b = S8.ctr_dict(S8.assign_b, fn_dict2)

    for i in range(10):
        ctr_a(i)
        ctr_b(i)

    assert fn_dict2['assign_a'] == 10, 'assign_a counter not cumulating correctly'
    assert fn_dict2['assign_b'] == 10, 'assign_b counter not cumulating correctly'
