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

- 