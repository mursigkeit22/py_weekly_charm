import sys

print(sys.version) # есть разница, 64бит или 32бит. На 32бит размеры меньше: инт - 14
# размер int: 0 занимает 24 байта, далее 28 байт, + 4 байт на каждый новый блок (2**30)
print(sys.int_info)


list_of_int_values = ['0', '1', '10', '257', '2**30-1', '2**30', '2**30+1', '2**60', ]
list_of_negative_int_values = ['-0', '-1', '-10', '-257', '-2**30+1', '-2**30', '-2**30-1', '-2**60',]

for integer in list_of_int_values:
    size = sys.getsizeof(eval(integer))
    print(f"Size of integer {integer} is {size} bytes.")

for integer in list_of_negative_int_values:
    size = sys.getsizeof(eval(integer))
    print(f"Size of integer {integer} is {size} bytes.")


