# Packages

#### Following topics are covered:

- Packages are modules, but not all modules are packages
- file, path, package properties -> **Module vs Package**

![file_path_package](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S12_Packages/file_path_package.png)

- Package imports will fail if paths are not given correctly as shown below. 
- Here **import pack1** works without issues because we are executing import statement from directory which holds pack1. 
- But that is not the case when we execute **import pack1.pack1_1**. Hence it fails. 
- But when we give **import pack1.pack1_1** it realizes the path and accordingly imports successfully

![import_failure1](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S12_Packages/import_failure1.png)

- But importing as above wont help us to refer to any values directly because globals() only has pack1. We
can solve it by **import pack1.pack1_1 as pack1_1**

![value_failure1](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S12_Packages/value_failure1.png)

- Even if we import pack1_1 with a different name, **import pack1.pack1_1 as p1** it is the same object. We
can confirm this by checking the ids as shown below.

![same_id_diff_name](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S12_Packages/same_id_diff_name.png)

- But this approach is cumbersome. If we want to import module1_1a we have to give 
**import pack1.pack1_1.module1_1a**.

![cumbersome](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S12_Packages/cumbersome.png)

- We want **import pack1** to import entire modules for us. We can achieve this by editing **init.py inside
pack1** as follows.

![import_via_init](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S12_Packages/import_via_init.png)

- But this also comes with disadvantage. To get a value we have to use **pack1.pack1_1.module1_1a.values**. 
We can resolve this by using * as shown in below init.py file.

![import_all](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S12_Packages/import_all.png)

- But if we give as above, we will run into trouble incase directory names change. eg: **'common'** changes
to **'scripts'**, then entire import statements will start failing. We can resolve this by giving **relative 
path** as shown below.

![relative_path](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S12_Packages/relative_path.png)

- Let us say, we want to expose only certain functions and values via import. We can achieve that using
**all** as shown below

![all](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S12_Packages/all.png)

- We can also give combination of **all** from various subpackages in main init.py like below.
- Check **second_package_imports/package_imports/common/models** and **second_package_imports/package_imports/main.py** 
to understand the usage and convenience we can achieve through this.
    __all__ = (posts_pkg.__all__ +
            users_pkg.__all__) 
            
## Assignment(EPAI 1.0)

- Assignment is as below.

![Assignment](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S12_Packages/Assignment.png)

## Assignment Solution

- Files that holds required functions :
    - __init__.py (Inside 'calculator' folder)
        - Have import statements for cos, e, log, relu, sin, softmax, tan, tanh functions
        - Derivative functions are excluded by giving __all__ statement
        - These regular functions will get exposed if we give **import calculator**
    - derivatives.py (Inside 'calculator' folder)
        - Have import statements for derivatives of cos, e, log, relu, sin, softmax, tan, tanh 
        - Derivative functions can be used only if we give **import derivatives**
    - utils.py (Inside 'calculator' folder)
        - Have decorator **f_string_print** that will help to wrap the below functions
        - Purpose is to give a f print statement as output
        - All the regular functions and their derivatives are wrapped with decorator f_string_print
    - check_calculator.py (Inside 's12_Packages' folder)
        - Basic python file to do a quick check if imports are working correctly
        - Regular functions should become available via **import calculator**
        - Derivative functions must not work if we merely give **import calculator**
        - Derivative functions should become available once we give **import derivatives**
    - cos.py (Inside 'calculator' folder)
        - This calls cos, cos_der functions. 
        - Only cos will be exposed if we give **import calculator**
        - cos_der will get exposed only if we give **import derivatives**
    - e.py  (Inside 'calculator' folder)
        - This calls e, e_der functions. 
        - Only e will be exposed if we give **import calculator**
        - e_der will get exposed only if we give **import derivatives**
    - log.py (Inside 'calculator' folder)
        - This calls log, log_der functions. 
        - Only log will be exposed if we give **import calculator**
        - log_der will get exposed only if we give **import derivatives**
    - relu.py (Inside 'calculator' folder)
        - This calls relu, relu_der functions. 
        - Only relu will be exposed if we give **import calculator**
        - relu_der will get exposed only if we give **import derivatives**
    - sin.py (Inside 'calculator' folder)
        - This calls sin, sin_der functions. 
        - Only sin will be exposed if we give **import calculator**
        - sin_der will get exposed only if we give **import derivatives**    
    - softmax.py (Inside 'calculator' folder)
        - This calls softmax, softmax_der functions. 
        - Only softmax will be exposed if we give **import calculator**
        - softmax_der will get exposed only if we give **import derivatives**
    - tan.py (Inside 'calculator' folder)
        - This calls tan, tan_der functions. 
        - Only tan will be exposed if we give **import calculator**
        - tan_der will get exposed only if we give **import derivatives**    
    - tanh.py (Inside 'calculator' folder)
        - This calls tanh, tanh_der functions. 
        - Only tanh will be exposed if we give **import calculator**
        - tanh_der will get exposed only if we give **import derivatives**       
                 
- Github Locations : 
    - sin, cos, tan, tanh, e, log, softmax, relu, init, deriavtives and utils.py can be found in below location.
    - https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S12_Packages/calculator
    - https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S12_Packages/check_calculator.py

- Draft Jupyter version where assignment was initially tried out can be found below:
https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S12_Packages/Assignment_Draft.ipynb

## Testing
- All the above functions are tested using pytest.
- Testcase file : **test_calculator.py** (Please note that that 'test_' need to be prefixed for Pytest to automatically identify that it is a testcase file).
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S12_Packages/test_calculator.py
- Test snapshot results as below:
![Test_Pass](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S12_Packages/Test_Passed_Snapshot.png)


 


