import pytest
from Polygons2 import Polygons2

p1 = Polygons2(6,10)
def test_Polygons_len():
    assert len(p1) == 4,"Length for polygon not proper"

def test_Polygons_iterable():
    lst = ['Sides = 3, Radius = 10, Eff_ratio = 2.5',
           'Sides = 4, Radius = 10, Eff_ratio = 3.54',
           'Sides = 5, Radius = 10, Eff_ratio = 4.05',
           'Sides = 6, Radius = 10, Eff_ratio = 4.33']

    result_lst = []
    for i in p1:
        result_lst.append(i)

    for idx in range(len(lst)):
        assert result_lst[idx] == lst[idx],f'Message mismatch in {idx}'

def test_Polygons_next():
    iter1 = iter(p1)
    lst = ['Sides = 3, Radius = 10, Eff_ratio = 2.5',
           'Sides = 4, Radius = 10, Eff_ratio = 3.54',
           'Sides = 5, Radius = 10, Eff_ratio = 4.05',
           'Sides = 6, Radius = 10, Eff_ratio = 4.33']

    for idx in range(len(lst)):
        assert lst[idx] == next(iter1), f'Next Iter mismatch in {idx}'

def test_exception_next():
    iter1 = iter(p1)
    for idx in range(4):
        next(iter1)

    with pytest.raises(StopIteration):
        next(iter1)
