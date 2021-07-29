# Iterables and Iterators

## Notes
- Notebook : **Sequence_Type_Notes.ipynb**
- Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S14_Iterables_Iterators/Iterables_and_Iterators_Notes.ipynb
#### Following topics are covered:
- **List Comprehensions**
    - Nested list comprehensions
    - Nested loops using list comprehensions
    - List comprehensions behave like functions interms of scope
- **Iteration using next_ method**
- **Iterators**
    - Iterators are objects that implement the __iter__ and __next__ methods.
    - The __iter__ method of an iterator just returns itself.
    - Iterator **will get exhausted**.
- **Iterators and iterables**
    - An iterable is an object that can return an iterator (__iter__).    
    - How to solve exhaustion problem
    - Iterable **wont get exhausted**.
    - **iter()** function is used to request an iterator object from an iterable.
        - How to use **iter** on **lists**
        - How to use **iter** on **range**
- **Consuming iterators manually**
    - Usecase with cars.csv file
- **Cyclic Iterators**
    - Usecase to generate ['1N', '2S', '3W', '4E', '5N'...and so on] using zip, repetition and list comprehension.
    - Doing the same with a custom made cyclic iterator
    - Using **itertools.cycle** - Python's inbuilt cyclic iterator
- **Lazy Iterables**
    - Circle example where we reset radius & calculate and store area too each time when radius is changed
    - Circle example where we reset radius & calculate area only when c.area is called
    - Circle example where we reset radius & calculate area only when c.area is called & radius is changed. If radius is not changed, even when c.area is called, dont recalculate but fetch the c._area already stored and show it
    - Iterator example using factorial usecase - both finite and infinite sequence (Infinite customized from finite)
- **Iterators in file handling**
    - **TextIOWrapper** class
    - **next** method to fetch rows
    - **f.readline()** to fetch rows one-by-one
    - **f.readlines()** to fetch all the rows atonce to a list (memory overhead will be high)
    - Using **'for'** loop to print rows one-by-one
- **Sorting Iterables**
- **Iterating Callables, Delegating Iterators, Reversed Iteration, Reversing Sequences**

## Assignments(EPAI 3.0)

## Assignment-1 
- Assignment-1 is as below.

**Refactor the Polygons (sequence) type that was built in Sequence Types assignment, into an iterable. You'll need to implement both an iterable, and an iterator**

## Assignment-1 Solution

- File that holds required functions for part 1: Polygon.py
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S14_Iterables_Iterators/Polygon.py
- Following functions are implemented:
- **__count_vertices__(self)**
    - This is a property.
    - Will give no: of vertices which is essentially No: of edges(n)
- **__count_edges__(self)**
    - This is a property.
    - Will give No: of edges(n)
- **__circumradius__(self)**
    - This is a property.
    - Will give circumradius (R)
- **__repr__(self)**
    - repr function for polygon class. Will give info on No: of edges(n), Circumradius(R).
- **__eq__()**
    - Checks whether a given polygon object is equal or not based on no:of edges and circumradius
- **__gt__**
    - Checks whether a given polygon object is greater than or not based on no:of edges
- **interior_angle(self)**
    - This is a property.
    - Calculates int_angle -> (n−2) * 180 * n.
- **side_length(self)**
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

- File that holds required functions for part 2 (sequence): Polygons.py
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S14_Iterables_Iterators/Polygons.py
- Following functions are implemented:
- **__init__(self)**
    - Will store no: of edges in seqeunce (m), common circumradius(R)
    - Also generates polygon correspodning to the 'm' and 'R' and stores it in a list 'self._polygon' 
- **__repr__(self)**
    - repr function for poly_seq class. Will give info on No: of edges(n) of largest polyon in the sequence and common Circumradius(R).
- **__len__()**
    - Returns length of polygon sequence. This will be m-2 as sides 1 and 2 are not polygons.
- **__getitem__(self, idx)**
    - getitem method that will help us to call the polygon sequences via index.
    - It will fetch required polygon from self._polygon[idx] 
- **max_efficiency_polygon(self)**
    - This is a property.
    - This method returns the Polygon with the highest area: perimeter ratio.
    - Accesses self._polygon, calculates area:perimeter ratio for each polygon in list, sorts in descending order and returns first element (polygon with highest area:perimeter ratio)
- **__iter__(self)**
    - This is defined to make Polygons an iterable.
    - This calls the class **polyiterator**
- **__polyiterator__(self)**
    - This is a class defined to make Polygons an iterable.
    - **__init__(self, poly_obj)**
        - Essentially accepts the polygon sequence object from which it is called
        - Saves poly_obj in self._poly_obj.
        - Also maintains self._index
    - **__iter__(self)**
        - To maintain this as an iterator. Returns self.
    - **__next__(self)**
        - Returns sides, circumradius and area:perimeter ratio of polygons one by one by referring to the list **self._poly_obj._polygon**  
        - If self._index >= len(self._poly_obj) raises stopiteration. This avoids indefinite execution.

- Draft Jupyter version where assignment was initially tried out can be found below:
https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S14_Iterables_Iterators/Iterables_1_Assignment_Draft.ipynb

## Testing
- All the above functions are tested using pytest.
- Testcase file : **test_Polygons.py** (Please note that that 'test_' need to be prefixed for Pytest to automatically identify that it is a testcase file).
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S14_Iterables_Iterators/test_Polygons.py
- Test snapshot results as below:
![Test_Pass](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S14_Iterables_Iterators/Assignment1_Test_Passed_Snapshot.png)

## Assignment-2 
- Assignment-2 is as below.

    - Goal 1:
        - Refactor the `Polygon` class so that all the calculated properties are lazy properties, i.e. they should still be calculated properties, but they should not have to get recalculated more than once (since we made our `Polygon` class "immutable").
    - Goal 2:
        - Refactor the `Polygons` (sequence) type, into an **iterable**. Make sure also that the elements in the iterator are computed lazily - i.e. you can no longer use a list as an underlying storage mechanism for your polygons.You'll need to implement both an iterable and an iterator.
        
## Assignment-2 Solution

- File that holds required functions for part 1: Polygon2.py
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S14_Iterables_Iterators/Polygon2.py   
- Following functions are implemented:
- **__edge__(self)**
    - This is a property.
    - Will give No: of edges(n)
    - This can be set 
- **__radius__(self)**
    - This is a property.
    - Will give circumradius (R)
    - This can be set
- **__repr__(self)**
    - repr function for polygon class. Will give info on No: of edges(n), Circumradius(R).
- **__eq__()**
    - Checks whether a given polygon object is equal or not based on no:of edges and circumradius
- **__gt__**
    - Checks whether a given polygon object is greater than or not based on no:of edges
- **interior_angle(self)**
    - This is a property.
    - Calculates int_angle -> (n−2) * 180 * n.
    - Lazy calculation & stores value. Calculates only if 'n' changes, else provides from stored value.
- **side_length(self)**
    - This is a property.
    - Calculates s = 2 * R * sin(π/n)
    - Lazy calculation & stores value. Calculates only if 'n' or 'R' changes, else provides from stored value.
- **apothem(self)**
    - This is a property.
    - Calculates a = R * cos(π * n)
    - Lazy calculation & stores value. Calculates only if 'n' or 'R' changes, else provides from stored value.
- **area(self)**
    - This is a property.
    - Calculates area = 12 * n * s * a
    - Lazy calculation & stores value. Calculates only if 'n' or 'R' changes, else provides from stored value.    
- **perimeter(self)**
    - This is a property.
    - Calculates perimeter = n * s
    - Lazy calculation & stores value. Calculates only if 'n' or 'R' changes, else provides from stored value.
    
- File that holds required functions for part 2 (sequence): Polygons2.py
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S14_Iterables_Iterators/Polygons2.py
- Following functions are implemented:    
- **__init__(self)**
    - Will store no: of edges in seqeunce (m), common circumradius(R)
- **__repr__(self)**
    - repr function for poly_seq class. Will give info on No: of edges(n) of largest polyon in the sequence and common Circumradius(R).
- **__len__()**
    - Returns length of polygon sequence. This will be m-2 as sides 1 and 2 are not polygons.
- **max_efficiency_polygon(self)**
    - This is a property.
    - This method returns the Polygon with the highest area: perimeter ratio.
    - Lazy calculation. Calculates only if not present in storage. Calculates area:perimeter ratio for each polygon in list, sorts in descending order and returns first element (polygon with highest area:perimeter ratio)
- **__iter__(self)**
    - This is defined to make Polygons an iterable.
    - This calls the class **polyiterator**
- **__polyiterator__(self)**
    - This is a class defined to make Polygons an iterable.
    - **__init__(self, poly_obj)**
        - Essentially accepts the polygon sequence object from which it is called
        - Saves poly_obj in self._poly_obj.
        - Also maintains self._index
    - **__iter__(self)**
        - To maintain this as an iterator. Returns self.
    - **__next__(self)**
        - Returns sides, circumradius and area:perimeter ratio of polygons one by one by creating from **Polygon2** class on the fly  
        - If self._index > self._poly_obj._m raises stopiteration. This avoids indefinite execution.
        
- Draft Jupyter version where assignment was initially tried out can be found below:
https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S14_Iterables_Iterators/Iterables_2_Assignment_Draft.ipynb

## Testing
- All the above functions are tested using pytest.
- Testcase file : **test_Polygons2.py** (Please note that that 'test_' need to be prefixed for Pytest to automatically identify that it is a testcase file).
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S14_Iterables_Iterators/test_Polygons2.py
- Test snapshot results as below:
![Test_Pass](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S14_Iterables_Iterators/Assignment2_Test_Passed_Snapshot.png)        
