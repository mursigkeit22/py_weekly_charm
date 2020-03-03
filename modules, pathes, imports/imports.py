# The only acceptable syntax for relative imports is from .[module] import name.
# All import forms not starting with . are interpreted as absolute imports.


import pkgutil
print(dir(pkgutil))     #After importing a module,
# use the dir() function to get a list of accessible names from the module.


# The function pkgutil.iter_modules (Python 2 and 3)
# can be used to get a list of all importable modules from a given path:
search_path = None  # set to None to see all modules importable from sys.path
# search_path = ['.']  # current dir
all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
for module in all_modules:
    print(module)
    pass
