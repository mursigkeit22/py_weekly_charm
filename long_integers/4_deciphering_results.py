import struct
import ctypes
import sys

# по адресу в памяти выводится следующая информация:
#
# - количество ссылок на объект(эта информация занимает 4 байта)
# - id типа объекта (8 байт)
# - к какому "блоку" принадлежит число  (1 - 2 * 30, 2 ** 30 - 2 ** 60, и т.д) (8 байт)
# - само число (от 4 байт, в зависимости от блока)  (base 2*30 numeral system)

#from https://repl.it/@arpitbbhayani/super-long-int?language=python3
# ("ob_refcnt", ctypes.c_long), l
# ("ob_type", ctypes.c_void_p), P?
# ("ob_size", ctypes.c_ulong), L
# ("ob_digit", ctypes.c_uint * 100) unsigned int I

# l:long;
# L:unsigned long;
# P:an integer type that is wide enough to hold a pointer.
# I:unsigned int;

# 'lPLI' = 4 + 8 + 8 + 4 = 24
# 'lPLII' = 4 + 8 + 8 + 4 +4= 28
# 'lPLIII' = 4 + 8 + 8 + 4 +4 + 4= 32
print(f"ID of integer type: {id(int)}")
print(sys.int_info)
print('==============')

obj = 0
print(f"Object: {obj}. Object size: {sys.getsizeof(obj)}")
print(ctypes.string_at(id(obj), 24))
print(struct.unpack('lPLI', ctypes.string_at(id(obj), 24)))
print('==============')
obj = 10
print(f"Object: {obj}. Object size: {sys.getsizeof(obj)}")
print(struct.unpack('lPLII', ctypes.string_at(id(obj), 28)))
print('==============')
obj = 2**30-1
print(f"Object: {obj}. Object size: {sys.getsizeof(obj)}")
print(struct.unpack('lPLII', ctypes.string_at(id(obj), 28)))
print('==============')
obj = 2**30
print(f"Object: {obj}. Object size: {sys.getsizeof(obj)}")
print(ctypes.string_at(id(obj), 32))
print(struct.unpack('lPLIII', ctypes.string_at(id(obj), 32)))
print('==============')
obj = 2**30 + 5783
print(f"Object: {obj}. Object size: {sys.getsizeof(obj)}")
print(struct.unpack('lPLIII', ctypes.string_at(id(obj), 32)))
print('==============')
obj = 2**60 + 75783
print(f"Object: {obj}. Object size: {sys.getsizeof(obj)}")
print(struct.unpack('lPLIIII', ctypes.string_at(id(obj), 36)))
print('==============')

