import sys

import script_example2
import package_example

print(f"Running script_example.py. \n"
      f"It exists in the folder '...jupiter\py_weekly\modules, pathes, imports'. sys.path[0]: {sys.path[0]}\n")

# print(math.pi)   NameError: name 'math' is not defined
print(package_example.math.pi)
print('All of the objects defined in the module or the package’s __init__.py file are made available to the importer.')