# Named Tuples

## Notes

- Notebook : **Tuples_NamedTuples_Notes.ipynb**
- Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S10_NamedTuples_Modules/Tuples_NamedTuples_Notes.ipynb
#### Following topics are covered:
- **Dummy variables in tuples**
    - Can use only one  *_  in tuple unpacking
- **Importance of '__repr__' while defining classes**
- **Strings are immutable**
- **Tuples are immutable**
- **Enumerate**
    - Gives index & item while iterating
- **Named Tuples**
    - Overriding doc functions
    - Overriding **default** values in functions & named tuples
    - How to use a function to generate random namedtuple instances
    - How to use dictionary to create a namedtuple instance
    - How to check if something is **iterable or not**. eg:dict.values()
    - How to refer dynamically to fields in namedtuple like **d2.key_name** - Use **getattr(d2, key_name)**
- **Faker** to create fake data
- **How to use namedtuple to create another namedtuple**
    
## Assignment(EPAI 1.0/2.0/3.0)

- Assignment is as below.

![Assignment](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S10_NamedTuples_Modules/Assignment.png)

## Assignment Solution

- File that holds required functions : namedtuples.py
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S10_NamedTuples_Modules/namedtuples.py
- Following functions are implemented:
- **common_blood_type()**
    - This function will accept a named tuple.
    - Named tuple comprise of set of profiles of individuals.
    - Blood Group is one of the fields among the profile.
    - This function using a lambda function and mode will return the most common blood group among the profiles.
    - This function also returns the time it took to perform above operations.
- **mean_current_loc()**
    - This function will accept a named tuple.
    - Named tuple comprise of set of profiles of individuals.
    - Current location in terms of (x,y) coordinates is one of the fields among the profile.
    - This function using a lambda function and mean will return the mean location interms of (x,y) coordinates among the profiles.
    - This function also returns the time it took to perform above operations.
- **oldest_person_age()**
    - This function will accept a named tuple.
    - Named tuple comprise of set of profiles of individuals.
    - Date of birth in datetime format is one of the fields among the profile.
    - This function using a lambda function and min method will return the oldest DOB among the profiles.
    - Then this DOB will be subtracted from current date to find the age in days and then dividing by 365 will give us the oldest age in years.
    - This function also returns the time it took to perform above operations.
- **average_age()**
    - This function will accept a named tuple.
    - Named tuple comprise of set of profiles of individuals.
    - Date of birth in datetime format is one of the fields among the profile.
    - This function using a lambda function will subtract each DOB with current date, find the age in days, then divide it by 365 to give age in years, wrap it in a list and finally using mean will give us the average age in years.
     - This function also returns the time it took to perform above operations.
- **common_blood_type_d()**
    - This function will accept a dictionary.
    - Dictionary comprise of set of profiles of individuals.
    - Rest of the items are same as we have seen in common_blood_type() function
- **mean_current_loc_d()**
    - This function will accept a dictionary.
    - Dictionary comprise of set of profiles of individuals.
    - Rest of the items are same as we have seen in mean_current_loc() function
- **oldest_person_age_d()**
    - This function will accept a dictionary.
    - Dictionary comprise of set of profiles of individuals.
    - Rest of the items are same as we have seen in oldest_person_age() function
- **average_age_d()**
    - This function will accept a dictionary.
    - Dictionary comprise of set of profiles of individuals.
    - Rest of the items are same as we have seen in average_age() function
- **stock_market_valu()**
    - This function will accept a namedtuple.
    - Namedtuple will be having 'n' number on instances of companies in stock market.
    - Each company will be having following fields - 'name, symbol, open, high, close ,weight'
    - This function will sum of highest stock values, sum of values with which stocks opened and sum of values with which stocks closed out of the 'n' companies provided in named tuple.

- Draft Jupyter version where assignment was initially tried out can be found below:
https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S10_NamedTuples_Modules/Named_Tuples_Assignment_Draft.ipynb

## Testing
- All the above functions are tested using pytest.
- Testcase file : **test_namedtuples.py** (Please note that that 'test_' need to be prefixed for Pytest to automatically identify that it is a testcase file).
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S10_NamedTuples_Modules/test_namedtuples.py
- Test snapshot results as below:
![Test_Pass](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S10_NamedTuples_Modules/Test_Passed_Snapshot_New.png)
