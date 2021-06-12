# Numeric Types

## Notes

- Notebook : **S5_Functional_Parameters_Notes.ipynb**
- Location : 
#### Following topics are covered:
- **Arguments**
    - Positional arguments
    - Keyword arguments
- **Unpacking**
    - Unpacking Tuple, set, dictionary
    - Use of dict.items() to fetch key/value pair as a tuple
- **Extended Unpacking using ' * ' and ' ** '**
    - Using * on LHS 
      - eg: l = [1, 2, 3, 4, 5, 6]
      - a, *b = l
    - Using * on RHS 
      - eg: l1 = [1, 2, 3]
      - s = 'anil'
      - l = [*l1, *s]
    - Cool trick to convert a string to list
    - Cool trick to eliminate duplicates
    - Using ** for dictionaries to combine key-value pairs
      - eg: d1 = {'key1': 1, 'key2': 2}
      -     d2 = {'key2': 3, 'key3': 4}  # key2 will be overwritten with final value i.e 'key2': 3
      -     d = {** d1, ** d2}
    - Nested unpacking
- **' * args'**
    - Returns Tuple
    - Cool trick to find avg using * args and short-circuting
- **Mandatory Keyword Arguments**
    - How to force user to enter a keyword argument
- **' ** kwargs'**
    - def fn(* args, ** kwargs) -> Can accept anything as long as positional arguments followed by keyword arguments are supplied
    - ' * '  indicates end of positional arguments
    - Named arguments can be given in any position after positional arguments
    
## Assignment

- Assignment is as below.

![Assignment](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S4_Numeric_Types_2/Assignment.jpg)

## Assignment Solution

- File that holds required functions : S5_time_it.py
- Github Location : 
- Following functions are implemented:
- **time_it()**
    - time_it(fn, *args, repetition=1, **kwargs)
    - Gives 2 output values 
        - 1) Output of corresponding function (fn) being called
        - 2) Time taken to execute the function as many times based on repetition supplied
- **myprint()**
    - myprint(*args, **kwargs)
    - Internally it accepts in below format 
    - '<values to be displayed', separator, end-of-line indicator
    - For this argument :1, 2, 3, sep='-', end= ' ***\n', result will be 
    - 1-2-3-***\n
 - **squared_power_list()**
    - squared_power_list(num, start, end)
    - if num = 2 and start = 0, end =5, result will be [1, 2, 4, 8, 16, 32]
 - **polygon_area()**
    - polygon_area(length, sides)
    - Returns area of polygons of sides 3 to 6 for given lengths
 - **temp_converter()**
    - temp_converter(temp, temp_given_in)
    - Converts given temperature 'temp' to celsius scale (c).
    - temp_given_in must be one among c, f or k where f denotes fahreinheat, k denotes kelvin
 - **speed_converter()**
    - speed_converter(speed, dist='km', time='hr')
    - Converts given speed 'speed' in km/hr to the desired units supplied via 'dist' and 'time'.
    - dist and time can be any of the below combinations:
        - dist : km/m/ft/yrd
        - time : ms/s/m/hr/day
        
## Testing
- All the above functions are tested using pytest.
- Testcase file : **test_S5_time_it.py** (Please note that that 'test_' need to be prefixed for Pytest to automatically identify that it is a testcase file).
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S4_Numeric_Types_2/test_S4_Qualean_Class.py
- Test case results are as shown below:
 
![Test_Results](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S4_Numeric_Types_2/Testcase_Pass.jpg)
