import pytest
import namedtuples
from namedtuples import *
from faker import Faker
from collections import namedtuple
from statistics import mode, mean
from datetime import datetime, date
from time import perf_counter
import string
import random
from random import randint, uniform
from io import StringIO
import sys
import time
import inspect
import os
import re

README_CONTENT_CHECK_FOR = [
    "common_blood_type",
    "mean_current_loc",
    "oldest_person_age",
    "average_age",
    "common_blood_type_d",
    "mean_current_loc_d",
    "oldest_person_age_d",
    "average_age_d",
    "stock_market_valu"
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 300, "Make your README.md file interesting! Add atleast 300 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(namedtuples)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(namedtuples, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


generate = Faker()
# Using the Faker library to get 10000 random profiles.
indiv_profile = namedtuple('indiv_profile', generate.profile().keys())
# Creating a namedtuple named 'indiv_profile' that will have fields same as fake profile we generate via Faker module
collect_profile = namedtuple('collect_profile', 'info')
# Creating a namedtuple named 'collect_profile' that has a field named 'info'.This will be used to collect the profiles inside 'all_profiles'

# Collecting 10_000 profiles inside 'all_profiles'
for i in range(10_000):
    indiv = indiv_profile(**generate.profile())
    if i == 0:
        all_profiles = collect_profile(indiv)
    else:
        all_profiles += collect_profile(indiv)

lst_blood   = []
lst_x_coord = []
lst_y_coord = []
lst_dob     = []
lst_age_yrs = []
for prof in all_profiles:
    lst_blood.append(prof[5])
    lst_x_coord.append(prof[4][0])
    lst_y_coord.append(prof[4][1])
    lst_dob.append(prof[-1])
    yrs = (date.today()-prof[-1]).days/365
    lst_age_yrs.append(yrs)
old_age = round((date.today()-min(lst_dob)).days/365, 2)
avg_age = round(mean(lst_age_yrs), 2)

def test_common_blood_type():
    common_blood_tup = common_blood_type(all_profiles)
    assert common_blood_tup[0] == mode(lst_blood),"Common blood group derived from named-tuple not matching"

def test_mean_current_loc():
    mean_loc_tup, elapsed = mean_current_loc(all_profiles)
    assert mean_loc_tup[0] == mean(lst_x_coord), "Mean location of X-Coordinate derived from named-tuple not matching"
    assert mean_loc_tup[1] == mean(lst_y_coord), "Mean location of Y-Coordinate derived from named-tuple not matching"

def test_oldest_person_age():
    oldest_age = oldest_person_age(all_profiles)
    assert oldest_age[0] == old_age, "Oldest age derived from named-tuple not matching"

def test_average_age():
    avg_age_nt = average_age(all_profiles)
    assert avg_age_nt[0] == avg_age, "Average age derived from named-tuple not matching"

all_profiles_d = {} #Creating an empty dictionary
for item in range(10_000):
    all_profiles_d[item] = generate.profile()
# Adding fake profiles generated into this dictionary

lst_blood_d   = []
lst_x_coord_d = []
lst_y_coord_d = []
lst_dob_d     = []
lst_age_yrs_d = []
for prof in all_profiles_d.values():
    lst_blood_d.append(prof['blood_group'])
    lst_x_coord_d.append(prof['current_location'][0])
    lst_y_coord_d.append(prof['current_location'][1])
    lst_dob_d.append(prof['birthdate'])
    yrs_d = (date.today()-prof['birthdate']).days/365
    lst_age_yrs_d.append(yrs_d)
old_age_d = round((date.today()-min(lst_dob_d)).days/365, 2)
avg_age_d = round(mean(lst_age_yrs_d), 2)

def test_common_blood_type_d():
    common_blood_tup = common_blood_type_d(all_profiles_d)
    assert common_blood_tup[0] == mode(lst_blood_d),"Common blood group derived from dictionary not matching"

def test_mean_current_loc_d():
    mean_loc_tup, elapsed = mean_current_loc_d(all_profiles_d)
    assert mean_loc_tup[0] == mean(lst_x_coord_d), "Mean location of X-Coordinate derived from dictionary not matching"
    assert mean_loc_tup[1] == mean(lst_y_coord_d), "Mean location of Y-Coordinate derived from dictionary not matching"

def test_oldest_person_age_d():
    oldest_age = oldest_person_age_d(all_profiles_d)
    assert oldest_age[0] == old_age_d, "Oldest age derived from dictionary not matching"

def test_average_age_d():
    avg_age_dt = average_age_d(all_profiles_d)
    assert avg_age_dt[0] == avg_age_d, "Average age derived from dictionary not matching"

# Prove that namedtuple is faster than dictionary
def test_compare_common_blood_type():
    common_blood_dict  = common_blood_type_d(all_profiles_d)
    common_blood_tuple = common_blood_type(all_profiles)
    assert common_blood_tuple[1] < common_blood_dict[1], 'Named tuple took more time to find common blood group'

def test_compare_mean_current_loc():
    mean_loc_dict, elapsed_d = mean_current_loc_d(all_profiles_d)
    mean_loc_tup, elapsed_t  = mean_current_loc(all_profiles)
    assert elapsed_t < elapsed_d, 'Named tuple took more time to find mean location'

def test_compare_oldest_person_age():
    oldest_age_dict  = oldest_person_age_d(all_profiles_d)
    oldest_age_tuple = oldest_person_age(all_profiles)
    assert oldest_age_tuple[1] < oldest_age_dict[1], 'Named tuple took more time to find oldest person age'

def test_compare_average_age():
    avg_age_dict  = average_age_d(all_profiles_d)
    avg_age_tuple = average_age(all_profiles)
    assert avg_age_tuple[1] < avg_age_dict[1], 'Named tuple took more time to find average age'
'''
Create fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). 
Assign a random weight to all the companies. Calculate and show what value the stock market started at, what was the highest value during 
the day, and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple. - 500  
(including 10 test cases)
'''
company      = namedtuple('company','name, symbol, open, high, close ,weight')
company_comb = namedtuple('company_comb', 'info')
symbol_set   = set()

for i in range(100):
     name    = generate.company()
     symbol  = name[0:3].upper() + random.choice(string.ascii_uppercase)
     while symbol in symbol_set:
         symbol = name[0:3].upper() + random.choice(string.ascii_uppercase)
     symbol_set.add(symbol)
     weight  = round(random.uniform(1,5), 2)
     open_   = round(random.uniform(100,1000), 2) * weight
     high_   = random.uniform(1, 1.4) * open_
     close_  = random.uniform(0.6, 1) * high_
     comp = company(name, symbol, open_, high_, close_, weight)
     if i == 0:
         top_100 = company_comb(comp)
     else:
         top_100 += company_comb(comp)

open_value, high_value, close_value = stock_market_valu(top_100)

def test_high_valu_ge_open_value():
    assert high_value >= open_value, "Error in high_value, high_value lesser than open_value"

def test_high_valu_ge_close_value():
    assert high_value >= close_value, "Error in high_value, high_value lesser than close_value"

def test_high_valu_within_upper_limits():
    high_factor = high_value/open_value
    assert high_factor <= 1.4, 'High Value of stock-market beyond expectations, someone manipulating market !'

def test_high_valu_above_upper_limits():
    high_factor = high_value/open_value
    with pytest.raises(AssertionError):
        assert high_factor > 1.4, 'High Value of stock-market beyond expectations, someone manipulating market !'

def test_close_valu_within_lower_limits():
    close_factor = close_value/high_value
    assert close_factor >= 0.6, 'Close Value of stock-market way low, someone manipulating market !'

def test_close_valu_below_lower_limits():
    close_factor = close_value / high_value
    with pytest.raises(AssertionError):
        assert close_factor < 0.6, 'Close Value of stock-market way low, someone manipulating market !'

def test_min_weight():
    assert min(list(map(lambda comp:comp[-1], top_100))) >= 1, 'Weightage assigned to 1 or more companies based on market cap on lower side'

def test_min_weight_fail():
    with pytest.raises(AssertionError):
        assert min(list(map(lambda comp:comp[-1], top_100))) < 1, 'Weightage less than 1'

def test_max_weight():
    assert max(list(map(lambda comp:comp[-1], top_100))) <=5, 'Weightage assigned to 1 or more companies based on market cap too high'

def test_max_weight_fail():
    with pytest.raises(AssertionError):
        assert max(list(map(lambda comp: comp[-1], top_100))) > 5, 'Weightage more than 5'

def test_duplicate_symbols():
    lst = list(map(lambda comp:comp[1], top_100))
    assert len(lst) == len(set(lst)), 'Duplicate symbols among companies listed !'

