# main.py
# What is shown below is what happens when we import a module eg: import module1

import os.path
import types
import sys

module_name = 'module1'
module_file = 'module1_source.py'  # Please note that we are keeping module_name and module_file_names different. But, it is best practice to keep them both as same
module_path = '.'

module_rel_file_path = os.path.join(module_path, module_file)      # .\module1_source.py
module_abs_file_path = os.path.abspath(module_rel_file_path)       # C:\Users\anila\Desktop\AI\EPAI-Phase1\S11_Modules\Session_11\Example3\module1_source.py

print('module_rel_file_path:', module_rel_file_path)
print('module_abs_file_path:', module_abs_file_path)

# Opening and copying module1 code to source_code
# We have access to local file, so rel path will do. No need for abs path
with open(module_rel_file_path, 'r') as code_file:
    source_code = code_file.read()
    
#create a module object
mod = types.ModuleType(module_name)
#Copy the absolute file path to mod.__file__  so that main.py or any calling pgm can understand from where it can get the module1 file ie 'module1_source.py'
mod.__file__ = module_abs_file_path

#Add the newly created custom model 'mod' to sys.modules with name as 'module1'
sys.modules[module_name] = mod

#Compile the code. mode='exec' indicates that python code we are compiling is a multi-line code
code = compile(source_code, filename=module_abs_file_path, mode='exec')

#Execute the compiled code
exec(code, mod.__dict__)

#Call function inside the mod to see if it works. If everything thing is fine it should print 'module1 says hello'
mod.hello()
