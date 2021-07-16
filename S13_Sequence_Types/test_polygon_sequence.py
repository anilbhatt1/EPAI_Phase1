import pytest
import polygon
from polygon import polygon
import polygon_sequence
from polygon_sequence import poly_seq
from datetime import datetime, date
from random import randint, uniform
from io import StringIO
import sys
import time
import inspect
import os
import re

p1 = polygon(6, 10)
def test_polygon_repr():
    assert repr(p1) == 'Regular Polygon class having 6 sides, circumradius = 10',"REPR for polygon not proper"

def test_polygon_int_angle():
    assert round(p1.int_angle,4) == 120.0, "Internal angle incorrect"

def test_polygon_edge_len():
    assert round(p1.edge_len,4) == 10, 'Edge length incorrect'

def test_polygon_apothem():
    assert round(p1.apothem,4) == 8.6603, 'Apothem incorrect'

def test_polygon_area():
    assert round(p1.area,4) == 259.8076, 'Area incorrect'

def test_polygon_perimeter():
    assert round(p1.perimeter,4) == 60.0, "Perimeter Incorrect"

rect = polygon(15, 10)
rect1 = polygon(15,10)
def test_polygon_eq():
    assert rect == rect1, "Polygon Equality test failed"

rect2 = polygon(4, 10)
def test_polygon_gt():
    assert rect > rect2, "Polygon gt test failed"

rect3 = polygon(30, 10)
def test_polygon_lt():
    assert rect < rect3, "Polygon lt test failed"

def test_polygon_invalid_circumradius():
    with pytest.raises(ValueError):
        train = polygon(3, -10.5)

def test_polygon_lessthan_3sides():
    with pytest.raises(ValueError):
        train = polygon(2, 10.5)

def test_polygon_invalid_sides():
    with pytest.raises(ValueError):
        train = polygon(2.5, 10.5)

s1 = poly_seq(6, 10)
def test_polyseq_length():
    assert len(s1) == 6, 'Invalid length for poly sequence'

def test_polyseq_idx_0_1():
    assert s1[0][1] == 0, 'Invalid area-perimeter ratio for side 0'
    assert s1[1][1] == 0, 'Invalid area-perimeter ratio for side 1'

def test_polyseq_idx_2():
    assert round(s1[2][1],4) == 2.5, 'Inavlid area-perimeter ratio for index 2'

def test_polyseq_idx_2():
    assert round(s1[5][1],4) == 4.3301, 'Inavlid area-perimeter ratio for index 5'

def test_polyseq_idx_minus1():
    assert round(s1[-1][1],4) == 4.3301, 'Inavlid area-perimeter ratio for -1 index'

def test_polyseq_idx_minus1():
    with pytest.raises(ValueError):
        s1[-99]

def test_polyseq_idx_highindx():
    with pytest.raises(ValueError):
        s1[99]

def test_polyseq_repr():
    assert repr(s1) == 'poly_seq class instance : Largest Polygon class in the sequence has 6 sides with a common circumradius = 10', "REPR for polygon not proper"

s2 = poly_seq(edges=25, radius=10)
def test_polyseq_maxefficient():
    assert s2.max_efficient == 'Polygon with max efficiency for circumradius of 10 is one with 25 sides & Area-perimeter ratio for the same is 4.9606',\
                                "Max-efficient Failed"
