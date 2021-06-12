import pytest
import S5_time_it
from S5_time_it import *

def test_myprint():
    _, values = time_it(myprint, 'a', 'n', 'i', 'l', sep='', end= '***', repetiton=3)
    assert values == 'anil***'
    _, values = time_it(myprint, 'a', 'n', 'i', 'l',1, 2, 3, sep='!', end= "\\", repetiton=3)
    assert values == 'a!n!i!l!1!2!3!\\'

def test_square_pos():
    _, values = time_it(squared_power_list, 2, start=0, end=5, repetition = 1)
    assert values == [1, 2, 4, 8, 16, 32]

def test_square_mixed():
    _, values = time_it(squared_power_list, 2, start=0, end=3, repetition = 1)
    assert values == [2**0, 2**1, 2**2, 2**3]

def test_square_negative():
    with pytest.raises(Exception) as e_info:
        time_it(squared_power_list, -3, start=-1, end=3, repetition = 1)

def test_square_same_start_end():
    with pytest.raises(Exception) as e_info:
        time_it(squared_power_list, 2, start=5, end=5, repetition=1)

def test_square_start_gt_end():
    with pytest.raises(Exception) as e_info:
        time_it(squared_power_list, 2, start=7, end=5, repetition=1)

def test_square_start_gt_end_neg():
    with pytest.raises(Exception) as e_info:
        time_it(squared_power_list, 2, start=-2, end=-3, repetition=1)

def test_square_start_gt_end_zero():
    with pytest.raises(Exception) as e_info:
        time_it(squared_power_list, 2, start=3, end=0, repetition=1)

def test_square_start_not_int():
    with pytest.raises(Exception) as e_info:
        time_it(squared_power_list, 2, start=0.5, end=3, repetition=1)

def test_square_end_not_int():
    with pytest.raises(Exception) as e_info:
        time_it(squared_power_list, 2, start=3, end=3.5, repetition=1)

def test_polygon_area_triangle():
    _, values = time_it(polygon_area, 4, sides=3, repetition = 10)
    assert values == 6.93

def test_polygon_area_square():
    _, values = time_it(polygon_area, 4, sides=4, repetition = 10)
    assert values == 16

def test_polygon_area_pentagon():
    _, values = time_it(polygon_area, 10, sides=5, repetition = 10)
    assert values == 172.05

def test_polygon_area_hexagon():
    _, values = time_it(polygon_area, 9, sides=6, repetition = 10)
    assert values == 210.44

def test_polygon_area_gt6():
    with pytest.raises(Exception):
        time_it(polygon_area, 4, sides=7, repetition = 10)

def test_polygon_area_lt3():
    with pytest.raises(Exception):
        time_it(polygon_area, 2, sides=7, repetition = 10)

def test_polygon_area_0_length():
    with pytest.raises(Exception):
        time_it(polygon_area, 0, sides=4, repetition = 10)

def test_polygon_area_neg_length():
    with pytest.raises(Exception):
        time_it(polygon_area, -10, sides=4, repetition = 10)

def test_invalid_scale_temp():
    with pytest.raises(Exception):
        time_it(temp_converter, 100, temp_given_in='X', repetition=1000)

def test_posf_temp():
    _, values = time_it(temp_converter, 100, temp_given_in='f', repetition=1000)
    assert values == 37.78, 'Incorrect Temp'

def test_negf_temp():
    _, values = time_it(temp_converter, -100, temp_given_in='f', repetition=10)
    assert values == -73.33, 'Incorrect Temp'

def test_0f_temp():
    _, values = time_it(temp_converter, 0, temp_given_in='f', repetition=10)
    assert values == -17.78, 'Incorrect Temp'

def test_posk_temp():
    _, values = time_it(temp_converter, 100, temp_given_in='k', repetition=1000)
    assert values == -173.15, 'Incorrect Temp'

def test_negk_temp():
    _, values = time_it(temp_converter, 375, temp_given_in='k', repetition=10)
    assert values == 101.85, 'Incorrect Temp'

def test_0k_temp():
    _, values = time_it(temp_converter, 273.15, temp_given_in='k', repetition=10)
    assert values == 0, 'Incorrect Temp'

def test_100c_temp():
    _, values = time_it(temp_converter, 100, temp_given_in='c', repetition=10)
    assert values == 100, 'Incorrect Temp'

def test_invalid_speed():
    with pytest.raises(Exception) as e_info:
        time_it(speed_converter, -100, dist='m', time='s', repetition=100)

def test_kmhr_kmday_dist():
    _ , values = time_it(speed_converter, 100, dist='km', time='day', repetition=100)
    assert values == 239.98, 'Incorrect Speed'

def test_kmhr_kmhr_dist():
    _ , values = time_it(speed_converter, 100, dist='km', time='hr', repetition=100)
    assert values == 100.0, 'Incorrect Speed'   

def test_kmhr_kmmin_dist():
    _ , values = time_it(speed_converter, 100, dist='km', time='min', repetition=100)
    assert values == 1.67, 'Incorrect Speed'
    
def test_kmhr_kms_dist():
    _ , values = time_it(speed_converter, 100, dist='km', time='s', repetition=100)
    assert values == 0.03, 'Incorrect Speed'
    
def test_kmhr_kmms_dist():
    _ , values = time_it(speed_converter, 100, dist='km', time='ms', repetition=100)
    assert values == 0.0, 'Incorrect Speed'
    
def test_kmhr_mday_dist():
    _ , values = time_it(speed_converter, 100, dist='m', time='day', repetition=100)
    assert values == 239980.8, 'Incorrect Speed'
    
def test_kmhr_mhr_dist():
    _ , values = time_it(speed_converter, 100, dist='m', time='hr', repetition=100)
    assert values == 100000.0, 'Incorrect Speed'
    
def test_kmhr_mmin_dist():
    _ , values = time_it(speed_converter, 100, dist='m', time='min', repetition=100)
    assert values == 1666.67, 'Incorrect Speed'
    
def test_kmhr_ms_dist():
    _ , values = time_it(speed_converter, 100, dist='m', time='s', repetition=100)
    assert values == 27.78, 'Incorrect Speed'
    
def test_kmhr_mms_dist():
    _ , values = time_it(speed_converter, 100, dist='m', time='ms', repetition=100)
    assert values == 0.03, 'Incorrect Speed'
    
def test_kmhr_ftday_dist():
    _ , values = time_it(speed_converter, 100, dist='ft', time='day', repetition=100)
    assert values == 787338.61, 'Incorrect Speed'
    
def test_kmhr_fthr_dist():
    _ , values = time_it(speed_converter, 100, dist='ft', time='hr', repetition=100)
    assert values == 328084.0, 'Incorrect Speed'
    
def test_kmhr_ftmin_dist():
    _ , values = time_it(speed_converter, 100, dist='ft', time='min', repetition=100)
    assert values == 5468.07, 'Incorrect Speed'
    
def test_kmhr_fts_dist():
    _ , values = time_it(speed_converter, 100, dist='ft', time='s', repetition=100)
    assert values == 91.13, 'Incorrect Speed'
    
def test_kmhr_ftms_dist():
    _ , values = time_it(speed_converter, 100, dist='ft', time='ms', repetition=100)
    assert values == 0.09, 'Incorrect Speed'
    
def test_kmhr_yrdday_dist():
    _ , values = time_it(speed_converter, 100, dist='yrd', time='day', repetition=100)
    assert values == 262445.4, 'Incorrect Speed'
    
def test_kmhr_yrdhr_dist():
    _ , values = time_it(speed_converter, 100, dist='yrd', time='hr', repetition=100)
    assert values == 109361.0, 'Incorrect Speed'
    
def test_kmhr_yrdmin_dist():
    _ , values = time_it(speed_converter, 100, dist='yrd', time='min', repetition=100)
    assert values == 1822.68, 'Incorrect Speed'
    
def test_kmhr_yrds_dist():
    _ , values = time_it(speed_converter, 100, dist='yrd', time='s', repetition=100)
    assert values == 30.38, 'Incorrect Speed'
    
def test_kmhr_yrdms_dist():
    _ , values = time_it(speed_converter, 100, dist='yrd', time='ms', repetition=100)
    assert values == 0.03, 'Incorrect Speed'

def test_invalid_dist_speed():
    with pytest.raises(Exception):
        time_it(speed_converter, 100, dist='miles', time='ms', repetition=100)


def test_invalid_time_speed():
    with pytest.raises(Exception):
        time_it(speed_converter, 100, dist='m', time='minutes', repetition=100)
