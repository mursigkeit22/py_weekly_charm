# Here, you can see None in the list of __builtins__ which is the dictionary
# the interpreter keeps for the builtins module.
# for el in dir(__builtins__):
#     print(el)


# None is a keyword, just like True and False.
# But because of this, you can’t reach None directly from __builtins__ as you could,
# for instance, ArithmeticError.
print(__builtins__.ArithmeticError)  # <class 'ArithmeticError'>
# print(__builtins__.True)  # SyntaxError: invalid syntax
# print(__builtins__.None)  # SyntaxError: invalid syntax

#  However, you can get it with a getattr() trick:

print(getattr(__builtins__, 'None'))
print(getattr(__builtins__, 'True'))
print(getattr(__builtins__, 'False'))

# Even though Python prints the word NoneType in many error messages,
# NoneType is not an identifier in Python.
# It’s not in builtins. You can only reach it with type(None).