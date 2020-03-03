import math       # math is a built-in module, so it doesn't matter that I created a math.py module in the same package:
# built-in module 'math' will be imported instead.

import sys

#Note that the Python interpreter first searches through the list of built-in modules,
# modules that are compiled directly into the Python interpreter.
# This list of built-in modules is installation-dependent and can be found in sys.builtin_module_names

# print(sys.builtin_module_names)

print("__init__.py from package_example: \n "
      "When a package is imported, Python runs all of the code in the package’s __init__.py file, if such a file exists. \n")
