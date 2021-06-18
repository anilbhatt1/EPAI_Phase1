# Closures

## Notes

- Notebook : **S8_Closures_Notes**
- Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S8_Closures/S8_Closures_Notes.ipynb
#### Following topics are covered:
- **Built-in scope**
- **Global scope**
- **Local scope**
- **Non-local scope**
- **'global' keyword**
- **'nonlocal' keyword**
- **Closures**
    - How to check if a function is closure or not using **'fn.__ closure__'**, fn -> function name
- **Free Variables**
    - How to check free variables using **'fn.__ code__ .co_freevars'**, fn -> function name
- **How closures can replace classes. Explained with 'Averager' example**
- **How to call a object directly using __ call__ method (like fwd in Pytorch)**
- **Closure example to update a counter as & when a function is called**
    
## Assignment

- Assignment is as below.

![Assignment](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S8_Closures/Assignment.jpg)

## Assignment Solution

- File that holds required functions : S8_Closures_Assignment.py
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S8_Closures/S8_Closures_Assignment.py
- Following functions are implemented:
- **check_doc()**
    - Closure to check if a function has docstring having atleast 50 characters in it
- **next_fib()**
    -  Closure to generate the next fibonacci number
- **ctr_dict()**
    - Closure that will accept a function and a dictionary that hold the counter. Counter will be increased as and when the particular function is called.
- Draft Jupyter version where assignment was initially tried out can be found below:
https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S8_Closures/S8_Closures_Assgn_Try.ipynb

## Testing
- All the above functions are tested using pytest.
- Testcase file : **test_S8_Closures_Assignment.py** (Please note that that 'test_' need to be prefixed for Pytest to automatically identify that it is a testcase file).
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S8_Closures/test_S8_Closures_Assignment.py
- Test case results are as shown below:
 
![Test_Results](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S8_Closures/Pytest_Snapshot.jpg)
