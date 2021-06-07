# Numeric Types

## Notes

- Notebook : **S4_Notes.ipynb**
- Location : https://nbviewer.jupyter.org/github/anilbhatt1/EPAI_1_Phase1/blob/main/S4_Numeric_Types_II/S4_Notes.ipynb.
- Following topics are covered:
    - isclose() both based on rel_tol and abs_tol
    - trunc()
    - floor()
    - ceil()
    - round()
    - Decimals
      - getcontext
      - Context manager 'decimal.localcontext()' and setting localcontexts to override 'rounding', 'prec' etc using it.
      - Getting size using sys.getsizeof()
      - Why we should use floats whenever possible instead of Decimal. Use Decimal only if extra precision is required
      - How to use **timeit()** to compare performance 
    - Complex Numbers
      - real & imag
      - cmath (Substitute of math for complex numbers)
    - Booleans
      - display using format with required decimal places
      - Fact : True is 1, false is 0
      - 5 Cool booelan tricks with examples
      - Familiarize strings
      - How OR evaluates a condition
      - How AND evaluates a condition
      - Using 'in' to evaluate conditions

## Assignment

- Assignment is as below.

![Assignment](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S4_Numeric_Types_2/Assignment.jpg)

## Assignment Solution

- File that defines class : **S4_Qualean_Class.py**  
- Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S4_Numeric_Types_2/S4_Qualean_Class.py
- Following functions were written to enable the Qualean Class. 

- **init**
  - This function accepts the user input which must be one among [-1, 0, 1].
  - This input is passed to **transform** function which will return a value that will be stored in self.q.
  - If user input is not the desired one, an exception is raised.
- **transform**
  - Used in tandom with **init** function.
  - Accepts user input from init function, generates a random value between -1 and 1.
  - Multiplies this random value with user input, rounds it to 10 decimal places and returns back value to init.
  - This value is stored as self.q in init.
- **str**
  - Overridden innate str function to return user input value *Qualean Number :{int(self.user_input)}* eg: Qualean Number :1
  - Prior to customization, str was returning memory location of object
  - Gets invoked when print() or str() is called. 
- **repr**
  - Overridden innate repr function to return user input value.
  - Initially it was displaying the location of the object.
  - Gets invoked when we try to display variable name eg: x
- **add**
  - Can add a number to an existing Qualean number (Q).
  - Number is infact added to self.q
  - Can be invoked as Q.__add__(x) where x is the user supplied value.
- **eq**
  - Can compare a Qualean number with a user supplied number to check if both of them are equal
  - Number is infact compared with self.q
  - Can be invoked as Q.__eq__(x)
- **float**
  - Returns the float value rounded upto 10 decimal places of a Qualean number
  - Value returned is float of self.q
  - Can be invoked as Q.__float__()
- **ge**
  - Can compare a Qualean number with a user supplied number to check if Q >= number
  - Number is infact compared with self.q
  - Can be invoked as Q.__ge__(x)
- **gt**
  - Can compare a Qualean number with a user supplied number to check if Q > number
  - Number is infact compared with self.q
  - Can be invoked as Q.__gt__(x)
- **invertsign**
  - Can invert the sign of a Qualean number.
  - Infact the sign of self.q is inverted.
  - Useful to find the square root of Qualean number if it comes as negative.
  - Can be invoked as Q.__invertsign__()
- **le**
  - Can compare a Qualean number with a user supplied number to check if Q <= number
  - Number is infact compared with self.q
  - Can be invoked as Q.__le__(x)
- **lt**
  - Can compare a Qualean number with a user supplied number to check if Q < number
  - Number is infact compared with self.q
  - Can be invoked as Q.__lt__(x)                                                                                  
- **mul**
  - Can multiply a number to an existing Qualean number (Q).
  - Number is infact multiplied with self.q
  - Can be invoked as Q.__mul__(x) where x is the user supplied value.
- **sqrt**
  - Can find the square root of a Qualean number.
  - Infact square root of self.q is found out and returned.
  - If self.q is -ve, then sign is inverted using **invertsign** and then square root is calculated.
  - Can be invoked as Q.__sqrt__()
- **bool**
  - Evaluates whether a Qualean number is 0 or not.
  - If it is 0 (can happen if user coice while defining Qualean class was supplied as 0), then False is returned.
  - Else True is returned.
  - Find its use in **and** & **or** functions.
  - Can be invoked as Q.__bool__().
- **getitem**
  - Returns self.q
- **and**
  - 'and' condition to compare two Qualean numbers say Q1 and Q2.
  - self.q of Q1 is compared with self.q of Q2.
  - Can be invoked as Q1.__and__(Q2)
- **or**
  - 'or' condition to compare two Qualean numbers say Q1 and Q2.
  - self.q of Q1 is compared with self.q of Q2.
  - Can be invoked as Q1.__or__(Q2)
  
## Testing
- All the above functions are tested using pytest.
- Testcase file : **test_S4_Qualean_Class.py** (Please note that that 'test_' need to be prefixed for Pytest to automatically identify that it is a testcase file).
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S4_Numeric_Types_2/test_S4_Qualean_Class.py
- Test case results are as shown below:
 
![Test_Results](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S4_Numeric_Types_2/Testcase_Pass.jpg)
