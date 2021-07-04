# Decorators

## Notes

- Notebook : **Decorators_Notes**
- Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S9_Decorators/Decorators_Notes.ipynb
#### Following topics are covered:
- **Closures Recap**
- **Decorators**
- **Retaining original function doc strings using @wraps**
- **Stacking decorators**
- **Understanding decorators by creating 2 simple decorators and stacking them over a function**
- **Memoization**
    - Understanding difference between using class, closure and decorator approach
    - Making decorator that worked for fibonacci work for factorial also
- **lru_cache() - Inbuilt python memoization decorator**
    - Using maxsize to limit number of elements stored in memory
- **Parametrized decorators**
    - Decorator factory (enables @timed(15) kind of things)
    - How to make a class callable(**call** method)
    - Decorating a class
- **Monkey Patching**
    - Ability to add features to a class after the fact
- **HTMLizing**
- **Single Dispatch** - Inbuilt feature in Python that helps to add features to decorators
    
## Assignment(EPAI 1.0/2.0)

- Assignment corresponding to EPAI-1.0 is as below.

![Assignment](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S9_Decorators/EPA1_Assign.jpg)

## Assignment(EPAI 1.0/2.0) Solution

- File that holds required functions : Decorators_Assignment.py
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S9_Decorators/Decorators_Assignment.py
- Following functions are implemented:
- **odd_it()**
    - Decorator to ensure that function that it decorates runs only on odd seconds.
    - **fn_odd_secs()**
        - This is a simple function that simply passes. This is decorated in such a way that it is supposed to run only on odd seconds.
- **logger()**
    - Decorator that keeps log of time at which function that it decorates is invoked.
    - **add()**
        - This is a function that takes 2 variables var1 which is str and var2 which is int.
        - Function will return a string combining var1 and var2.
        - Function is decorated to keep a log of time at which it is invoked.
- **info()**
    - This function accepts an object that belongs to a class as argument and returns a log of info related to this object
    - Used along with decorator **dec_debug**
- **dec_debug()**
    - This decorator will decorate a class. Any object instantiated from the class can get a log info by calling obj.debug_info()
    - **class Country()**
        - Creates a class called country in such a way that object created is callable.
        - Also decorated by dec_debug so that obj.debug_info() can return the log details of the object.
- **authenticate()**
    - This decorator factory accepts a user_password.
    - Any function decorated with this decorator has to supply a password.
    - Function will be allowed to execute only if user supplied password matches with the system password set inside  'dec_authenticate'.
- **timed()**
    - Decorator to calculate average elapsed run time for a function.
    - Through 'reps' parameter this decorator has capability to execute the function 'reps' number of times.
- **dec_factory()**
    - Provides privilege access (has 4 parameters, based on privileges (high, mid, low, no), gives access to all 4, 3, 2 or 1 params).
- **decorator_factory()**
    - Based on the privilege_lvl with which a particular function is decorated, this decorator will give the list of access available to that particular function
    - 4 privilege levels are available for decoration - 'high', 'medium', 'low', 'no
- Draft Jupyter version where assignment was initially tried out can be found below:
https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S9_Decorators/Decorators_Assgn_Draft.ipynb

## Testing
- All the above functions are tested using pytest.
- Testcase file : **test_Decorators_Assignment.py** (Please note that that 'test_' need to be prefixed for Pytest to automatically identify that it is a testcase file).
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S9_Decorators/test_Decorators_Assignment.py

## Assignment(EPAI 3.0)

- Assignment corresponding to EPAI-3.0 is as below.

![Assignment](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S9_Decorators/EPA3_Assign.jpg)

## Assignment(EPAI 3.0) Solution

- File that holds required functions : session8.py
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S9_Decorators/session8.py
- Following functions are implemented:
- **odd_it()**
    - Decorator to ensure that function that it decorates runs only on odd seconds.
- **logger()**
    - Decorator that keeps log of time at which function that it decorates is invoked.
- **authenticate()**
    - This decorator factory accepts a user_password.
    - Any function decorated with this decorator has to supply a password.
    - Function will be allowed to execute only if user supplied password matches with the system password set inside  'dec_authenticate'.
- **timed()**
    - Decorator to calculate average elapsed run time for a function.
    - Through 'reps' parameter this decorator has capability to execute the function 'reps' number of times.
- **decorator_factory()**
    - Based on the privilege_lvl with which a particular function is decorated, this decorator will give the list of access available to that particular function
    - 4 privilege levels are available for decoration - 'high', 'medium', 'low', 'no

## Testing
- All the above functions are tested using pytest.
- Testcase file : **test_session8.py** (Please note that that 'test_' need to be prefixed for Pytest to automatically identify that it is a testcase file).
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S9_Decorators/test_session8.py