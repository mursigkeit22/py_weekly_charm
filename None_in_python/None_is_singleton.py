#Even though you try to create a new instance,
# you still get the existing None.
# You can prove that None and my_None are the same object by using id():
my_None = type(None)()  # Create a new instance
print(f'my_None is: {my_None}')
print(id(None))
print(id(my_None))

