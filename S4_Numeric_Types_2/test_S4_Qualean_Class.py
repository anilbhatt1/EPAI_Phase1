import pytest
import S4_Qualean_Class as qual
import random
import math

def test_str():
    choice = random.choice([-1, 0, 1])
    q_num = qual.Qualean(choice)
    assert q_num.__str__() == 'Qualean Number :' + str(int(choice))
    #print(f'q_num.__str__():{q_num.__str__() }')

def test_repr():
    choice = random.choice([-1, 0, 1])
    q_num = qual.Qualean(choice)
    assert q_num.__repr__() == str(choice)

def test_add():
    choice = random.choice([-1, 0, 1])
    q_num = qual.Qualean(choice)
    num = random.randint(0,100)
    assert q_num.__add__(num) == q_num.q + num
    #print(f'num : {num}, choice:{choice}, q_num.q : {q_num.q}, sum : {q_num.q + num}')

def test_eq():
    choice = random.choice([-1, 0, 1])
    q_num = qual.Qualean(choice)
    num = round(random.uniform(-1, 1), 10)
    assert q_num.__eq__(num) == (q_num.q == num)
    #print(f'q_num.q :{q_num.q}, num :{num}, q_num.__eq__(num) :{q_num.__eq__(num)}')
    num2 = q_num
    assert q_num.__eq__(num2.q) == True
    #print(f'q_num.q :{q_num.q}, num2 :{num2.q}, (q_num.q == num2.q) :{(q_num.q == num2.q)}')

def test_float():
    choice = random.choice([-1, 0, 1])
    q_num = qual.Qualean(choice)
    assert q_num.__float__() == q_num.q

def test_ge():
    choice = random.choice([-1, 0, 1])
    q_num = qual.Qualean(choice)
    num = round(random.uniform(-3, -2), 10)
    #print(f'q_num.q : {q_num.q}, num:{num}, q_num.__ge__(num) :{q_num.__ge__(num)}')
    assert q_num.__ge__(num) == True
    num = round(random.uniform(2, 3), 10)
    assert q_num.__ge__(num) == False
    q_num = qual.Qualean(0)
    num = 0
    assert q_num.__ge__(num) == True

def test_gt():
    choice = random.choice([-1, 0, 1])
    q_num = qual.Qualean(choice)
    num = round(random.uniform(-3, -2), 10)
    #print(f'q_num.q : {q_num.q}, num:{num}, q_num.__ge__(num) :{q_num.__ge__(num)}')
    assert q_num.__gt__(num) == True
    num = round(random.uniform(2, 3), 10)
    assert q_num.__gt__(num) == False
    q_num = qual.Qualean(0)
    num = 0
    assert q_num.__gt__(num) == False

def test_invertsign():
    choice = random.choice([-1, 0, 1])
    q_num = qual.Qualean(choice)
    assert q_num.__invertsign__() == -1 * q_num.q
    q_num = qual.Qualean(0)
    assert q_num.__invertsign__() == 0

def test_le():
    choice = random.choice([-1, 0, 1])
    q_num = qual.Qualean(choice)
    num = round(random.uniform(-3, -2), 10)
    #print(f'q_num.q : {q_num.q}, num:{num}, q_num.__ge__(num) :{q_num.__ge__(num)}')
    assert q_num.__le__(num) == False
    num = round(random.uniform(2, 3), 10)
    assert q_num.__le__(num) == True
    q_num = qual.Qualean(0)
    num = 0
    assert q_num.__le__(num) == True

def test_lt():
    choice = random.choice([-1, 0, 1])
    q_num = qual.Qualean(choice)
    num = round(random.uniform(-3, -2), 10)
    #print(f'q_num.q : {q_num.q}, num:{num}, q_num.__ge__(num) :{q_num.__ge__(num)}')
    assert q_num.__lt__(num) == False
    num = round(random.uniform(2, 3), 10)
    assert q_num.__lt__(num) == True
    q_num = qual.Qualean(0)
    num = 0
    assert q_num.__lt__(num) == False

def test_mul():
    choice = random.choice([-1, 0, 1])
    q_num = qual.Qualean(choice)
    num = round(random.uniform(-3, -2), 10)
    assert q_num.__mul__(num) == q_num.q * num
    num = 0
    assert q_num.__mul__(num) == 0
    q_num = qual.Qualean(0)
    num = round(random.uniform(-3, -2), 10)
    assert q_num.__mul__(num) == 0

def test_sqrt():
    choice = random.choice([-1, 0, 1])
    q_num = qual.Qualean(choice)
    if q_num.q >=0:
        assert q_num.__sqrt__() == math.sqrt(q_num.q)
    else:
        assert q_num.__sqrt__() == math.sqrt(-1 * q_num.q)
    q_num = qual.Qualean(0)
    assert q_num.__sqrt__() == 0

def test_bool():
    choice = random.choice([-1, 1])
    q_num = qual.Qualean(choice)
    assert q_num.__bool__() == True
    q_num = qual.Qualean(0)
    assert q_num.__bool__() == False

def test_getitem():
    choice = random.choice([-1, 0, 1])
    q_num = qual.Qualean(choice)
    assert q_num.get_item() == q_num.q

def test_and():
    choice = random.choice([-1, 1])
    q_num = qual.Qualean(choice)
    num = 2
    assert q_num.__and__(num) == False
    choice2 = random.choice([-1, 1])
    q_num2 = qual.Qualean(choice2)
    assert q_num.__and__(q_num2) == True
    q_num3 = qual.Qualean(0)
    assert q_num.__and__(q_num3) == False
    q_num = qual.Qualean(0)
    assert q_num.__and__(q_num2) == False
    assert q_num.__and__(q_num3) == False

def test_or():
    choice = random.choice([-1, 1])
    q_num = qual.Qualean(choice)
    num = 2
    assert q_num.__or__(num) == True
    choice2 = random.choice([-1, 1])
    q_num2 = qual.Qualean(choice2)
    assert q_num.__or__(q_num2) == True
    q_num3 = qual.Qualean(0)
    assert q_num.__or__(q_num3) == True
    q_num = qual.Qualean(0)
    assert q_num.__or__(q_num2) == True
    assert q_num.__or__(q_num3) == False



