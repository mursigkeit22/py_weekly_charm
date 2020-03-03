import struct
import ctypes
import sys
# module struct performs conversions between Python values and C structs represented as Python bytes objects.
# struct.unpack(формат, строка) Разбирает строку в соответствие с данным форматов.
# Всегда возвращает кортеж, даже если строка содержит только один элемент.
# Строка должна содержать в точности то количество информации, как описано форматом.
# несколько возможных форматов:
# l:long;
# L:unsigned long;
# P:an integer type that is wide enough to hold a pointer.
# I:unsigned int;

obj = 1
size = sys.getsizeof(obj)
print(f"Object size: {size}")
print(ctypes.string_at(id(obj), size))
print(struct.unpack('lPLII', ctypes.string_at(id(obj), size)))
print('==============')
obj = 10000
size = sys.getsizeof(obj)
print(f"Object size: {size}")
print(ctypes.string_at(id(obj), size))
print(struct.unpack('lPLII', ctypes.string_at(id(obj), size)))
