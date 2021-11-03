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


 


