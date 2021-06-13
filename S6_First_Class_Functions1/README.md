# First Class Functions

## Notes

- Notebook : **S6_First_Class_Functions1_Notes**
- Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S6_First_Class_Functions1/S6_First_Class_Functions1_Notes.ipynb
#### Following topics are covered:
- **Default Values in functions**
    - How to make value population dynamic inside a function eg: Using time
    - Danger with using mutable items as default values eg: Using list
    - Building a cache eg: Using factorial
- **Docstrings and annotations**
    - help(func) -> Prints out both doc strings & annotations
    - func.__doc__ -> Gives doc strings
    - func.__annotations__ -> Gives annotations in dict format
- **lambda functions**
    - lambda [parameter list] : expression
        - my_func = ***lambda x, y : x + y***
        - my_func(1, 4) -> 5
        - my_func(-1, 1) -> 0
    - Using * args and ** kwargs with lambda
    - Lambda function used in **sorted** which fails in normal cases (eg: complex numbers)
        - Examples using list, dict and complex numbers
- **Functional Introspection**
    - dir(my_func) -> Will give all the attributes belonging to the function
    - my_func.__default__ 
    - my_func.__kwdefault__ -> Will give kwargs
    - inspect
- **Callable** - Those items that can be called with (). eg: my_func(), print()
- **Map, Filter, Zip, List Comprehension**
    - L1 = [1, 2, 3, 4, 5]
    - L2 = [10, 20, 30]
    - L3 = 100, 200, 300, 400
        - Map - ***list( map( lambda x, y, z: x+y+z, L1, L2, L3) )  -> [111, 222, 333]***
        - Filter - ***list( filter ( lambda x: x%3 == 0, range(25) ) ) -> [0,3,6,9,12,15,18,21,24]***
        - Zip - ***list( zip ( L1, L2, L3 ) ) -> [(1,10, 100), (2,20,200), (3,30,300)]***
        - List Comprehension - **[x+y for x, y in L1, L2 if (x+y)%2 == 0] -> [11]**
    
## Assignment

- Assignment is as below.

![Assignment](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S6_First_Class_Functions1/Assignment.jpg)

## Assignment Solution

- File that holds required functions : S6_deck_of_cards.py
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S6_First_Class_Functions1/S6_deck_of_cards.py
- Following functions are implemented:
- **create_deck_normal()**
    - Creating deck of 52 cards via normal function
- **Deck creation using list comprehension & zip**
    - sorted([val + '-' + suit for val, suit in zip(vals*4, suits*13)])
 - **winner()**
    - To determine the winner based in input of 2 players

## Testing
- All the above functions are tested using pytest.
- Testcase file : **test_S6_deck_of_cards.py** (Please note that that 'test_' need to be prefixed for Pytest to automatically identify that it is a testcase file).
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S6_First_Class_Functions1/test_S6_deck_of_cards.py
- Test case results are as shown below:
 
![Test_Results](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S6_First_Class_Functions1/pytest_snapshot.jpg)
