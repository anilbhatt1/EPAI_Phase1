# Modules

## Notes

- Notebook : **Modules_Notes.ipynb**
- Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S11_Modules/Modules_Notes.ipynb

#### Following topics are covered:

- When we create a function say **my_func()** it gets registered inside **globals()**
- **globals()** is a **dict** and we can refer the function as **globals()['my_func']** or execute my_func as **globals()['my_func'] ()**
- How **inbuilt functions** and **custom third party functions** gets fetched and stored
    - **inbuilt** eg: math fetched from **so** files
    - **custom** eg: fractions fetched from custom libraries like C:\\Users\\anila\\anaconda3\\lib\\fractions.py 
- **sys.modules()**
    - import math >> sys.modules >> globals
    - When we put something to sys.modules, it will go automatically to globals() as well
    - **But** we can use that module only if it is present in globals(). If we delete from globals(), we have to import again
    - For example : **del globals()['math']** will delete **math** only from **globals()**, **math** will remain in **sys.modules** but cant be used
- Getting more details of a module from **__spec__** eg: **math. __spec __**
    - Will give name of module, loader used, source location of module
- Creating own module via **types.ModuleType()**
    - We can add lambda functions, assign variables to methods of our custom made module via **__ dict __** key assignments
    - We can also copy over methods from other modules eg: math.sqrt can be copied over to be used in our custom made module
- **sys.prefix** : This gives path from where python is running
- **sys.path** : This **lists the library paths where python will search** for a module while importing it
- **How Python imports a module from file**
- **__ name __** will show as **main** when displayed from inside the file
- In **Session_11/Example3/main.py** we are doing what python does for us while importing a module (for understanding purpose)
    - Copies module code 
    - Creates module object say 'mod' using types.ModuleType
    - Copies absolute file path where module resides to mod. __file__ 
    - Adds newly created 'mod' to sys.modules
    - Compile the code
    - Exec the code
- How to check if an **imported module is part of a package** 
	- Source from which module is imported will be having **__ init__.py** in it like 'C:\\Users\\anila\\anaconda3\\lib\\collections\\__init__.py'
- Convert a variable string as a module using **importlib.import_module**
- **Loaders** 
    - When we import a module, python uses Loader to **find** that module from **sys.path** and to **load** it
    - **sys.meta_path** : Gives list of different type of loaders that python uses
- **importlib.util.find_spec** 
    - Helps to see the **spec** of a module **without importing it**
    - eg: importlib.util.find_spec('calendar')
- How to **import a module** present in a directory **outside present working directory**
    - Answer : Add the **directory location** of module to **sys.path**
- **Various type of imports**
    - Type 1 : **import math**
        - All methods under math will be available
        - Usage: math.sqrt(2)
        - 'math' will be present in globals() and sys.modules
    - Type 2 : **import numpy as np**
        - 'np' in globals(), 'numpy' in sys.modules
        - Usage: np.zeros(2)
    - Type 3 : **from cmath import polar**
        - Only 'polar' will be available. No other methods from cmath will be available.
        - Usage: polar(2+2j)
        - 'polar' will be present in globals(), 'cmath' in sys.modules
    - Type 4 : **from cmath import sin as c_sin** OR   **from math import sin as sin**
        - Helps to demarcate the functions (eg: complex sin vs normal sin)
        - Usage : c_sin(2+2j), sin(0)
        - 'c_sin' in globals(), 'sin' in globals()
    - Type 5 : **from fractions import** *
        - All methods from fractions will be available without prefix
        - Usage : Fraction(23)
        - 'Fraction' or 'methods present in fractions' will be there in globals(), 'fractions' in sys.modules
- **argparse**  Helps to run a python program from cmd supplying the arguments
	- parser = argparse.ArgumentParser(description=__doc__)
	- parser.add_argument
	- parser.parse_args()
	- Sample code to be given in cmd -> **python timing.py '[x**2 for x in range(10)]' -r 100**
	- Refer **C:\Users\anila\Desktop\AI\EPAI-Phase1\S11_Modules\Session_11\Main_Experiments** for code
- How to zip the python modules from a folder
    -  python -m zipfile -c app.zip module.py run.py timing.py
- How to list the contents of a zip file using python
    - python -m zipfile -l app.zip
- How to make an application using **__ main__.py**
    - python -m zipfile -c my-app  module1.py __ main__.py timing.py
    - python my-app

#### Also following topic is covered in test_convert_app.py
- **subprocess**
    - Using **subprocess.run()** to execute cmd commands
    - How to use **stdout=subprocess.PIPE** , **stderr=subprocess.PIPE** to display output of **subprocess.run()**    

## Assignment(EPAI 1.0)

- Assignment is as below.

![Assignment](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S11_Modules/Assignment.png)

## Assignment Solution

- Files that holds required functions :
    - __main__.py
        - main module 
        - This calls j2p.py, p2j.py, image_resize.py and image_crop.py based on convert option given
    - j2p.py  
        - This converts jpg/jpeg image or folder to png
        - Usage:
            - python convert_app.zip convert --convert_type j2p --image_name sample_jpg.jpg
            - python convert_app.zip convert --convert_type j2p --folder_name Sample_Images
    - p2j.py 
        - This converts png image or folder to jpg
        - Usage:
            - python convert_app.zip convert --convert_type p2j --image_name sample_png.png
            - python convert_app.zip convert --convert_type p2j --folder_name Sample_Images
    - image_resize.py
        - Following options are available
            - **res_p** : Resizes the image/folder for given percent (0 to 1). Upsizing not enabled.
                - Usage:
                    - python convert_app.zip resize --resize_type res_p --resize_percent 0.85 --image_name sample_png.png
                    - python convert_app.zip resize --resize_type res_p --resize_percent 0.85 --folder_name Sample_Images
            - **res_w** : Resizes the image/folder for given width. Height adjusted as per aspect ratio.
                - Usage:
                    - python convert_app.zip resize --resize_type res_w --resize_width 1064 --image_name sample_png.png
                    - python convert_app.zip resize --resize_type res_w --resize_width 1064 --folder_name Sample_Images
            - **res_h** : Resizes the image/folder for given height. Width adjusted as per aspect ratio.
                - Usage:
                    - python convert_app.zip resize --resize_type res_h --resize_height 100 --image_name sample_png.png
                    - python convert_app.zip resize --resize_type res_h --resize_height 100 --folder_name Sample_Images
    - image_crop.py
        - Following crop options are available
            - **crp_p** : Crops the image/folder for given percent (0 to 1).
                - Usage:
                    - python convert_app.zip crop --crop_type crp_p --crop_percent 0.5 --image_name sample_jpg.jpg
                    - python convert_app.zip crop --crop_type crp_p --crop_percent 0.5 --folder_name Sample_Images
            - **crp_px** : 
                - Crops the image/folder for given pixel values.
                - Square/rectangle crop can be done.
                - Pixel input should be in format -> left, upper, right, lower
                    - eg: for 1064 x 1064 to be square cropped to 224 x 224 we should give pixel values  as 420 420 644 644
                - Usage :
                    - python convert_app.zip crop --crop_type crp_p --crop_pixels 420 420 644 644 --image_name sample_jpg.jpg
                    - python convert_app.zip crop --crop_type crp_p --crop_pixels 420 420 644 644 --folder_name Sample_Images
    - convert_app.zip
        - Created via command **python -m zipfile -c convert_app.zip __ main__.py j2p.py p2j.py image_crop.py image_resize.py**
        - Invoked via command **python convert_app.zip resize --resize_type res_w --resize_width 1064 --folder_name Val_Images**
                 
- Github Locations : 
    - https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S11_Modules/__main__.py
    - https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S11_Modules/j2p.py
    - https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S11_Modules/p2j.py
    - https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S11_Modules/image_resize.py
    - https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S11_Modules/image_crop.py
    - https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S11_Modules/convert_app.zip

- Draft Jupyter version where assignment was initially tried out can be found below:
https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S11_Modules/Assignment_Draft.ipynb

## Testing
- All the above functions are tested using pytest.
- Testcase file : **test_convert_app.py** (Please note that that 'test_' need to be prefixed for Pytest to automatically identify that it is a testcase file).
- This py file also shows how **subprocess** can be used to **run()** python cmd commands
- Github Location : https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S11_Modules/test_convert_app.py
- Test snapshot results as below:
![Test_Pass](https://github.com/anilbhatt1/EPAI_Phase1/blob/master/S11_Modules/Test_Passed_Snapshot.png)
