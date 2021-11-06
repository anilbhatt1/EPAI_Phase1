import pytest
import math
import calculator as c
from calculator import derivatives as d

def test_cos():
    output = c.cos(90)
    assert output == round(math.cos(90),4), 'Cos value calculated incorrect'

def test_cos_non_num():
    output = c.cos('0')
    assert output == "Incorrect value format given - <class 'str'>. Give input as integer or float", 'Unexpected cos o/p'

def test_cos_neg():
    output = c.cos(-90)
    assert output == round(math.cos(-90),4), 'Cos value calculated incorrect'

def test_e():
    output = c.e(2)
    assert output == round(math.exp(2),4), 'e value incorrect'

def test_e_non_num():
    output = c.e('anil')
    assert output == "Incorrect value format given - <class 'str'>. Give input as integer or float", 'Unexpected e o/p'

def test_e_neg():
    output = c.e(-2)
    assert output == round(math.exp(-2),4), 'e value incorrect'

def test_log():
    output = c.log(10)
    assert output == math.log(10), 'log value incorrect'

def test_log_non_num():
    output = c.log('anil')
    assert output == "Incorrect value format given - <class 'str'>. Give input as +ve integer or +ve float", 'Unexpected log o/p'

def test_log_neg():
    output = c.log(-10)
    assert output == "log can be calculated only for +ve values. Non-postive value -10 given as input", 'Unexpected log o/p'

def test_relu_pos():
    output = c.relu(10)
    assert output == 10, 'relu value incorrect for +ve'

def test_relu_zero():
    output = c.relu(0)
    assert output == 0, 'relu value incorrect for 0'

def test_relu_neg():
    output = c.relu(-10)
    assert output == 0, 'relu value incorrect for -ve'

def test_relu_non_num():
    output = c.relu('anil')
    assert output == "Incorrect value format given - <class 'str'>. Give input as integer or float", 'Unexpected e o/p'

def test_sin():
    output = c.sin(90)
    assert output == round(math.sin(90),4), 'sin value calculated incorrect'

def test_sin_non_num():
    output = c.sin('0')
    assert output == "Incorrect value format given - <class 'str'>. Give input as integer or float", 'Unexpected sin o/p'

def test_sin_neg():
    output = c.sin(-90)
    assert output == round(math.sin(-90),4), 'sin value calculated incorrect'

def test_softmax():
    output = c.softmax(4,4,1)
    assert output == [0.49, 0.49, 0.02], 'softmax +ve o/p incorrect'

def test_softmax_neg():
    output = c.softmax(-4,4,1)
    assert output == [0, 0.95, 0.05], 'softmax -ve o/p incorrect'

def test_softmax_non_num():
    output = c.softmax(-4, 4, 'abc')
    assert output == 'Incorrect value format given - <class \'str\'> for "abc". Give input as integer or float', 'Unexpected softmax o/p'

def test_tan():
    output = c.tan(0)
    assert output == round(math.tan(0),4), 'tan value calculated incorrect'

def test_tan_non_num():
    output = c.tan('0')
    assert output == "Incorrect value format given - <class 'str'>. Give input as integer or float", 'Unexpected sin o/p'

def test_tan_neg():
    output = c.tan(-5)
    assert output == round(math.tan(-5),4), 'tan value calculated incorrect'

def test_tanh():
    output = c.tanh(0)
    assert output == round(math.tanh(0),4), 'tanh value calculated incorrect'

def test_tanh_non_num():
    output = c.tanh('0')
    assert output == "Incorrect value format given - <class 'str'>. Give input as integer or float", 'Unexpected sin o/p'

def test_tanh_neg():
    output = c.tanh(-5)
    assert output == round(math.tanh(-5),4), 'tanh value calculated incorrect'

def test_cos_der():
    output = d.cos_der(90)
    assert output == round(-math.sin(90),4), 'Cos Der value calculated incorrect'

def test_e_der():
    output = d.e_der(2)
    assert output == round(math.exp(2),4), 'e Der value incorrect'

def test_log_der():
    output = d.log_der(10)
    assert output == 1/10, 'log der value incorrect'

def test_relu_pos_der():
    output = d.relu_der(10)
    assert output == 1, 'relu der value incorrect for +ve'

def test_relu_zero_der():
    output = d.relu_der(0)
    assert output == 00, 'relu der value incorrect for 0'

def test_relu_neg_der():
    output = d.relu_der(-10)
    assert output == 0, 'relu der value incorrect for -ve'

def test_sin_der():
    output = d.sin_der(90)
    assert output == round(math.cos(90),4), 'sin der value calculated incorrect'

def test_softmax_der():
    output = d.softmax_der(4,4,1)
    assert len(output) == 3, 'softmax +ve o/p incorrect'
    assert len(output[0]) == 3, 'softmax +ve o/p incorrect'

def test_tan_der():
    output = d.tan_der(0)
    valid = 1 / math.cos(0) ** 2
    assert output == round(valid,4), 'tan der value calculated incorrect'

def test_tanh_der():
    output = d.tanh_der(0)
    valid = 1 - math.tanh(0) ** 2
    assert output == round(valid,4), 'tanh value calculated incorrect'
