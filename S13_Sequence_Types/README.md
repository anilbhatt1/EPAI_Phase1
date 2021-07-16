# Sequence Types

## Notes
- Notebook : **Sequence_Type_Notes.ipynb**
- Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S13_Sequence_Types/Sequence_Type_Notes.ipynb
#### Following topics are covered:
- **Sequence types are indexable**
- **All sequence types will be iterable**
- **All iterables are not sequence types eg: sets**
- **Can use 'in' with iterables**
- **Can use 'min' and 'max' with iterables**
- **Concatenation**
    - Can concatenate 2 sequences of same type eg: list + list
    - Can't use for iterables that are not sequence types eg: wont work for sets
- **How to convert a string to list**
- **How to convert a list to string using 'join'**
- **Using * operator for repetition eg: 'abc'*2 = 'abcabc'** - Wont work for iterables that are not sequence types
- **Finding position using index eg: s = "the school of ai of world" & s.index('o') -> 7**
- **Slicing**
    - Reversing string [::-1]
    - Selecting fixed elements alone from list eg : [0:5:2]
    - Selecting fixed elements alone from list in reverse order eg : [5:0:-2]
    - Inserting elements in a list in between - replacing the elements as well as without replacing the elements
- **list.append() -> [1, 2, 3, [4, 5, 6]] , Original list was [1,2,3]**
- **list.extend() -> [1, 2, 3, 4, 5, 6] , Original list was [1,2,3]**
    - extend will work only on iterables
- **How to delete an element from list**
    - pop
    - del
- **Shallow Copy vs Deep Copy**
- **Tuples are highly performant than lists - demonstration using dis**
- **Storage efficiency**
- **Slice type**
- **Building custom sequence types**
    - Usage of lru_cache & **staticmethod**
    - Usage of slice type
- **Inplace concatenation & repetition**
    - += and places at which it will work, it won't work & associated memory changes
- **Sorting sequences**
    - Output will always be a list

## Assignment(EPAI 3.0)

- Assignment is as below.

![Assignment](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S13_Sequence_Types/Assignment.png)

## Assignment Solution

- File that holds required functions for part 1: polygon.py
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S13_Sequence_Types/polygon.py
- Following functions are implemented:
- **__repr__(self)**
    - repr function for polygon class. Will give info on No: of edges(n), Circumradius(R).
- **__eq__()**
    - Checks whether a given polygon object is equal or not based on no:of edges and circumradius
- **__gt__**
    - Checks whether a given polygon object is greater than or not based on no:of edges
- **int_angle(self)**
    - This is a property.
    - Calculates int_angle -> (n−2) * 180 * n.
- **edge_len(self)**
    - This is a property.
    - Calculates s = 2 * R * sin(π/n)
- **apothem(self)**
    - This is a property.
    - Calculates a = R * cos(π * n)
- **area(self)**
    - This is a property.
    - Calculates area = 12 * n * s * a
- **perimeter(self)**
    - This is a property.
    - Calculates perimeter = n * s

- File that holds required functions for part 2: polygon_sequence.py
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S13_Sequence_Types/polygon_sequence.py
- Following functions are implemented:
- **__repr__(self)**
    - repr function for poly_seq class. Will give info on No: of edges(n) of largest polyon in the sequence and common Circumradius(R).
- **__len__()**
    - Returns length of polygon sequence
- **__getitem__(self, idx)**
    - getitem method that will help us to call the polygon sequences via index.
    - getitem based on the index it received, calls method '_calc_ratio' by supplying index+1 (to avoid 0 sides) & circumradius used while creating poly_seq class.
- **_calc_ratio(num_edges: int, c_radius: 'int or float')**
    - Returns area-perimeter ratio of the single polygon for given number of edges & circumradius.
    - This method is directly called in __getitem__() and indirectly called from max_efficient() methods.    
- **max_efficient(self)**
    - This is a property.
    - This method returns the Polygon with the highest area: perimeter ratio.
    - Calls _getitem__ for each edge starting from 0 till self.edges -1.
    - __getitem__ fetches area-perimeter ratio then by calling _calc_ratio.

- Draft Jupyter version where assignment was initially tried out can be found below:
https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S13_Sequence_Types/Sequence_Types_Assignment_Draft.ipynb

## Testing
- All the above functions are tested using pytest.
- Testcase file : **test_polygon_sequence.py** (Please note that that 'test_' need to be prefixed for Pytest to automatically identify that it is a testcase file).
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S13_Sequence_Types/test_polygon_sequence.py
- Test snapshot results as below:
![Test_Pass](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S13_Sequence_Types/Test_Passed_Snapshot_New.png)
