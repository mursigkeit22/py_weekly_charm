cubes = (i ** 3 for i in range(5))     # generator
cubes_list = list(i ** 3 for i in range(10))
for i in range(5):
    print(next(cubes))

print('----------------')
for i in cubes:    # will print nothing cause the iterator is exhausted
    print(i)
print('----------------')
# print(next(cubes))    # StopIteration


