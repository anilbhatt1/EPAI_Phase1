from faker import Faker
from collections import namedtuple
from statistics import mode, mean
from datetime import datetime, date
from time import perf_counter
import string
import random
from random import randint, uniform

# Using namedtuple, calculate the largest blood type
def common_blood_type(all_named_tup:namedtuple)-> (str, datetime):
    start = perf_counter()
    common_grp = mode(list(map(lambda profile: profile[5], all_named_tup)))
    end = perf_counter()
    return common_grp, end-start

# Using namedtuple, calculate the mean-current_location
def mean_current_loc(all_named_tup:namedtuple)-> (tuple, datetime):
    start = perf_counter()
    x_mean = mean(list(map(lambda profile:profile[4][0], all_named_tup)))
    y_mean = mean(list(map(lambda profile:profile[4][1], all_named_tup)))
    end = perf_counter()
    mean_loc = (x_mean, y_mean)
    return mean_loc, end-start

# Using namedtuple, calculate the oldest_person_age
def oldest_person_age(all_named_tup:namedtuple) -> (float, int):
    start = perf_counter()
    oldest_dob = min(list(map(lambda profile:profile[-1], all_named_tup)))
    current_dt = date.today()
    end = perf_counter()
    return round((current_dt - oldest_dob).days/365, 2), end-start

# Using namedtuple, calculate the average age
def average_age(all_named_tup:namedtuple) -> (float, int):
    start = perf_counter()
    current_dt = date.today()
    avg_age = mean(list(map(lambda profile:(current_dt - profile[-1]).days/365, all_named_tup)))
    end = perf_counter()
    return round(avg_age, 2), end-start

# Using dictionary, Get most common blood-group
def common_blood_type_d(all_dict):
    start = perf_counter()
    common_grp = mode(list(map(lambda profile: profile['blood_group'], all_dict.values())))
    end = perf_counter()
    return common_grp, end-start

# Using dictionary, calculate the mean-current_location
def mean_current_loc_d(all_dict):
    start = perf_counter()
    x_mean = mean(list(map(lambda profile:profile['current_location'][0], all_dict.values())))
    y_mean = mean(list(map(lambda profile:profile['current_location'][1], all_dict.values())))
    end = perf_counter()
    mean_loc = (x_mean, y_mean)
    return mean_loc, end-start

# Using dictionary, calculate the oldest_person_age
def oldest_person_age_d(all_dict):
    start = perf_counter()
    oldest_dob = min(list(map(lambda profile:profile['birthdate'], all_dict.values())))
    current_dt = date.today()
    end = perf_counter()
    return round((current_dt - oldest_dob).days/365, 2), end-start

# Using dictionary, calculate the average age
def average_age_d(all_dict):
    start = perf_counter()
    current_dt = date.today()
    avg_age = mean(list(map(lambda profile:(current_dt - profile['birthdate']).days/365, all_dict.values())))
    end = perf_counter()
    return round(avg_age, 2), end-start

def stock_market_valu(top_100:'namedtuple()') -> (float, float, float):

    open_value  = round(sum(list(map(lambda comp : comp[2], top_100))), 4)
    high_value  = round(sum(list(map(lambda comp : comp[3], top_100))), 4)
    close_value = round(sum(list(map(lambda comp : comp[4], top_100))), 4)
    return open_value, high_value, close_value



