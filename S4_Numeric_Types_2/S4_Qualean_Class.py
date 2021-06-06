'''
Write a Qualean class that is inspired by Boolean+Quantum concepts. We can assign it only 3 possible real states. True, False, and
Maybe (1, 0, -1) but it internally picks an imaginary state. The moment you assign it a real number, it immediately finds an
imaginary number random.uniform(-1, 1) and multiplies with it and stores that number internally after using Bankers rounding to
10th decimal place.
It implements these functions (with exactly the same names)
    and, or, repr, str, add, eq, float, ge, gt, invertsign, le, lt, mul, sqrt, bool
Your task is to write the above class, and then write all the functions.
Then you need to write a test file, that tests all of the functions mentioned above + the other basic ones you have seen in
the tests till now. Your unit test file must contain at least 25 tests, and they must not be repetitive. Some of the tests it must implement are:
    q + q + q ... 100 times = 100 * q
    q.sqrt() = Decimal(q).sqrt
    sum of 1 million different qs is very close to zero (use isclose)
    q1 and q2 returns False when q2 is not defined as well and q1 is False
    q1 or q2 returns True when q2 is not defined as well and q1 is not false
'''

import random
import math

class Qualean:
    def __init__(self, user_input):
        if user_input in [-1, 0, 1]:
            self.user_input = user_input
            self.q = self.__transform__()
        else:
            raise Exception(" You can create Qualean object only for 3 numbers - 1, 0, -1")

    def __transform__(self):
        return round((self.user_input * random.uniform(-1, 1)), 10)

    def __str__(self):
        return f'Qualean Number :{int(self.user_input)}'

    def __repr__(self):
        return str(self.user_input)

    def __add__(self, value):
        return self.q + value

    def __eq__(self, value):
        return self.q == value

    def __float__(self):
        return self.q

    def __ge__(self, value):
        return self.q >= value

    def __gt__(self, value):
        return self.q > value

    def __invertsign__(self):
        return -1 * self.q

    def __le__(self, value):
        return self.q <= value

    def __lt__(self, value):
        return self.q < value

    def __mul__(self, value):
        return self.q * value

    def __sqrt__(self):
        if self.q >= 0:
            return math.sqrt(self.q)
        else:
            return math.sqrt(self.__invertsign__())

    def __bool__(self):
        return self.q != 0

    def get_item(self):
        return self.q

    def __and__(self, other_obj):
        if not bool(self.q):  #if self.q (i.e. value of qualean) itself is zero, no need to check further. Return false
            return False
        else:
            if isinstance(other_obj, Qualean) and other_obj.q != 0: #if other_obj is also boolean & its value is not 0,then check further
                return bool(self.q and other_obj.q)
            else:
                return False

    def __or__(self, other_obj):
        if bool(self.q):
            return True
        else:
            if isinstance(other_obj, Qualean) and other_obj.q != 0:
                return True
            else:
                return False
